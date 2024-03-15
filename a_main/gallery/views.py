from typing import Any
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse 
from django.conf import settings
from .models import Image, Display, Tag, DisplayKey
from client.models import Project
from django.core.paginator import Paginator
from a_main.env.app_Logic.photo_layer import col3_col6_col3
from a_main.env.app_Logic.untility.quick_tools import ViewExtendedFunctions, DateFunction, ViewQueryHelper
from a_main.env.cloudflare_API.CFAPI import APICall, Encode_Metadata
from a_main.env.cloudflare_API.CFR2API import CloudflareR2API
from logs.logging_config import logging
from a_main.env.app_Logic.KeyPass import SETTINGS_KEYS
import json
from django.utils.text import slugify
import zlib
import secrets
from rest_framework.response import Response
from .serializers import ImageSerializer
r2_api_call = CloudflareR2API()
cf_api_call= APICall()
vef = ViewExtendedFunctions()
encodeM = Encode_Metadata()
date_functions = DateFunction()
vqh = ViewQueryHelper()

#-----------------------------------------------------------------------------------------------------------#
#
# functions
#
#-----------------------------------------------------------------------------------------------------------#
def append_cloundflare_id(cf_id, image_id):

	update_image_record = Image.objects.get(id=image_id)
	
	image_url = 'https://imagedelivery.net/4_y5kVkw2ENjgzV454LjcQ/' + cf_id +'/display'
	update_image_record.image_link = image_url
	update_image_record.save()

#-------------------------------------------------------------------------------------------------------#
# gallery views site, project and client
#-------------------------------------------------------------------------------------------------------#

def manage_gallery(request, slug):
	# The gallery management section empowers users to curate the content for various galleries, 
	# including the home page and header images for each gallery. 
	
	try:
		all_images = Image.objects.all().distinct()
		display = Display.objects.get(slug=slug)
		current_images = display.images.all()

		print()
		
		filter_set = vqh.image_query(request, all_images, display)
		
		image_p = Paginator(filter_set.all(), 21)
		last_page = image_p.num_pages
		page = request.GET.get('page')
		image_sets = image_p.get_page(page)

		# Post request section for functions called on the front
		if request.method == 'POST':
			
			# request to update the images of the current gallery
			# the images will only add images that are selected
			if 'update' in request.POST.values():
				# creats blank image list and sets all images in the galllery to none
				image_listed = set()
				# creates keypair values for selected images
				for image_value, image_key in zip(request.POST.values(),  request.POST.keys()):
					if 'checkbox' in image_key:
						image_listed.add(image_value)
				# filter and update selected values
				
				selected_images = all_images.filter(id__in=image_listed)
				display.images.add(*selected_images)
				

				return redirect('change-gal', display.slug)

			# remove function: will only remove items selected
			elif 'remove' in request.POST.values():
				#print('remove')
				# creats blank image list and sets all images in the galllery to none
				image_listed = set()

				for image_value, image_key in zip(request.POST.values(),  request.POST.keys()):
					if 'checkbox' in image_key:
						print(image_key)
						image_listed.add(image_value)
		
				# filter for selected values
				selected_images = all_images.filter(id__in=image_listed)
				for image_index in range(len(selected_images)):
					display.images.remove(selected_images[image_index])

				return redirect('change-gal', display.slug)
			
			# make image header for the gallery
			elif 'header' in request.POST.keys():

				header_image_id = request.POST.get('header')
				print(header_image_id)
				header_image = all_images.get(id=header_image_id)
				display.header_image = header_image
				display.save()

				return redirect('change-gal', display.slug)

		return render(request, 'o_panel/gallery/change-gallery.html', {
			'current_list': current_images,
			'gal': slug,
			'display': display,
			'image_sets':image_sets,
			'last_page':last_page
		})
  
	except Exception as e:
		logging.error("Gallery Control Error: %s", str(e))
		slugified_error_message = slugify(str(e))
		return redirect('issue-backend', status=500, error_message=slugified_error_message)
#-------------------------------------------------------------------------------------------------------#
# Image views
#-------------------------------------------------------------------------------------------------------#
# gallery view for all images
def all_image_list(request):
	all_images = Image.objects.all().distinct()
	template_name = 'o_panel/images/image-details.html'
	
	filter_set = vqh.image_query(request, all_images, '0')
	
	image_p = Paginator(filter_set.all(), 21)
	last_page = image_p.num_pages
	page = request.GET.get('page')
	image_sets = image_p.get_page(page)

 
	return render(request, template_name, {'image_sets':image_sets, 'last_page': last_page})

# endpoint for loading more gallery images
def load_more_enpoint(request, slug):
	print('load more ', slug)
	image_in_display = []
	
	all_images = Image.objects.all().distinct().only('id', 'project_id', 'title', 'image_link')
	if slug == 'None':
		display_object = Display.objects.all()
		image_in_display = []

	else:
		display_object = Display.objects.get(slug=slug)
		for img_id in display_object.images.all():
			image_in_display.append(img_id.id)
			print(img_id)

	filter_set = vqh.image_query(request, all_images, display_object)

	# Pagenate date and get the next page set
	image_p = Paginator(filter_set.all(), 21)
	next_image_set = []
	next_p = json.load(request)['next_p'] 
	next_page = int(next_p)
	next_set = list(image_p.page(next_page).object_list.values())
	# manual serilizer... I know, I promis it's faster
	for image_info in next_set:
		get_info = all_images.get(id=image_info['id'])
		image_id = str(get_info.id)
		image_project = str(get_info.project_id.name)
		image_title = str(get_info.title)
		image_link = str(get_info.image_link)

		next_image_set.append({
			'id':image_id,
			'project':image_project, 
			'title':image_title, 
			'image_link':image_link
			})
  
	return HttpResponse(json.dumps({"imgObj": next_image_set, 'displaySet': image_in_display}))

# endpoint for clearing selected gallery images
def clear_gallery_endpoint(request, slug):
	display_object = Display.objects.get(slug=slug)
	
	if request.method == 'GET':
		display_object.header_image = None
		display_object.images.clear()
		display_object.save()

		reps = json.dumps({'sucess': 'sucess'})
		return HttpResponse(reps)

def create_display_endpoint(request):
	
	
	if request.method == 'POST':
		try:
			json_data = json.loads(request.body)
			name = json_data.get('name')

			display_object = Display.objects.create(name=name)
			display_object.save()

			return HttpResponse({'success':'sucess'})
		except ValueError as e:
			logging.error("Client Invite Error: %s", str((e)))
			slugified_error_message = slugify(str(e))
			return HttpResponse({'issue-backend':f'issue-backend {e}'}, status=500, error_message=slugified_error_message)

#-------------------------------------------------------------------------------------------------------#
# Image upload views
#-------------------------------------------------------------------------------------------------------#

def image_upload(request):
	
	return render(request, 'o_panel/images/image_upload.html')

def image_form(request, data_packet):
	
	compressed_data = bytes.fromhex(data_packet)
	decompressed_data = zlib.decompress(compressed_data)
	list_data = decompressed_data.decode().split()
	if not list_data:
		return redirect('issue-backend', status='400', error_message='image-failed-upload')
	tags_object = Tag.objects.all()
	display_objects = Display.objects.all()
	project_objects = Project.objects.all()

	return render(request, 'o_panel/images/image-create.html',
		{
			'display_objects': display_objects,
			'tags_object':tags_object,
			'project_objects':project_objects,
			'list_data': list_data
	})

#-------------------------------------------------------------------------------------------------------#
# Image API endpoints
#-------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------#
# image processing endpoints
#-------------------------------------------------------------------------------------------------------#

def upload_token_endpoint(request):
	data_packet = []
	cfId_slug = ''
	if request.method == 'POST':
		try:
			for cf_object in json.load(request)['data'] :
				
				slug_id =' ' + str(cf_object)
				cfId_slug = cfId_slug + slug_id
			compressed_data = zlib.compress(cfId_slug.encode())
			data_packet = compressed_data.hex()
			
			image_form_url = reverse('image-form', args=[data_packet])
			return HttpResponse(json.dumps(image_form_url))

		except ValueError as e:
			logging.error("error creating token in the upload process: %s", str((e)))
			slugified_error_message = slugify(str(e))
			return HttpResponse(json.dumps({'status':500, 'error_message':slugified_error_message}))
	
	elif request.method == 'GET':
		try:
			post_data = []
			cloudflare_token = cf_api_call.get_batch_token()
			if 'error' not in cloudflare_token:
				cloudflare_token = str(cloudflare_token)
				front_end_url = 'https://batch.imagedelivery.net/images/v1'

				post_data.append({'cf_token':cloudflare_token,'cf_url': front_end_url})

			else:
				e = cloudflare_token
				logging.error("error creating token in the upload process: %s", str((e)))
				slugified_error_message = slugify(str(e))
				return redirect('issue-backend', status=500, error_message=slugified_error_message)
		
			return JsonResponse(post_data, safe=False)

		except ValueError as e:
			logging.error("Client Invite Error: %s", str((e)))
			slugified_error_message = slugify(str(e))
			return HttpResponse(json.dumps({'status':500, 'error_message':slugified_error_message}))

	else:
		return JsonResponse({'error': 'Invalid request method'})

def create_image_endpoint(request):
	
	if request.method == 'POST':
		try:
			formData = json.load(request)
			datalist = formData.get('data')
			datalist[0].get('title')
			set_project = datalist[1].get('project')
			set_title = datalist[0].get('title')
			cfId_set = datalist[2].get('cf_id')
			project_instance = Project.objects.get(id=set_project)
			slected_client = project_instance.client_id
			
			imgobj_list = []

			for cf_id in cfId_set:
				#print('upload')
				image_url = f'https://imagedelivery.net/4_y5kVkw2ENjgzV454LjcQ/{cf_id}/display'
				imgobj = Image(
					title=str(set_title) + ' -' + str(cf_id[(len(cf_id) - 5): -1]),
					client_id=slected_client,
					project_id=project_instance,
					image_link=image_url,
					cloudflare_id=cf_id,
				)

				imgobj_list.append(imgobj)
			
			new_images = Image.objects.bulk_create(imgobj_list)
			
			image1Set = ImageSerializer(new_images, many=True)
			image_data = {'image1Set':image1Set.data }

			return HttpResponse(json.dumps(image_data))
		except ValueError as e:
			logging.error("Client Invite Error: %s", str((e)))
			slugified_error_message = slugify(str(e))
			return HttpResponse(json.dumps({'status':500, 'error_message':slugified_error_message}))

	else:
		return JsonResponse({'error': 'Invalid request method'})

def tags_image_endpoint(request):
	if request.method == 'POST':
		try:
			request_data = json.loads(request.body)
			image_data= request_data.get('imageList')
			new_images = image_data.get('image1Set')
			
			set_tags = request_data.get('tags')
			tag_list = []
			image_list = []
			for images in new_images:
				print(images)
				image_list.append(images.get('cloudflare_id'))

			image_objects = Image.objects.filter(client_id__in=image_list)
			for tag in set_tags:
				tags_object = Tag.objects.get_or_create(name=tag)
				tag_list.append(tags_object)
			tags = Tag.objects.filter(name__in=tag_list)
			for image in image_objects:
				image.tag.add(*tags)
   
			return HttpResponse({'success':'success'})

		except ValueError as e:
			logging.error("Client Invite Error: %s", str((e)))
			slugified_error_message = slugify(str(e))
			return HttpResponse(json.dumps({'status':500, 'error_message':slugified_error_message}))

	else:
		return JsonResponse({'error': 'Invalid request method'})

def gallery_image_endpoint(request):
	if request.method == 'POST':
		try:
			request_data = json.loads(request.body)
			image_data = request_data.get('imageList')
			new_images = image_data.get('image1Set')
			image_query = []
			for images in new_images:
				image_query.append(images.get('cloudflare_id'))
			image_objects = Image.objects.filter(cloudflare_id__in=image_query)
			image_list = []
			for images in image_objects:
				print(images)
				image_list.append(images.id)
			set_display = request_data.get('displays')
			#print(new_images, set_display)
			
			for display in set_display:
				display_instance =  Display.objects.get(id=display)
				display_instance.images.add(*image_list)

			return HttpResponse({'success':'success'})

		except ValueError as e:
			logging.error("Client Invite Error: %s", str((e)))
			slugified_error_message = slugify(str(e))
			return HttpResponse(json.dumps({'status':500, 'error_message':slugified_error_message}))

	else:
		return JsonResponse({'error': 'Invalid request method'})

#  Gallery functions
def delete_image_endpoint(request):
	cf_id_chain = []
	
	try:
		formData = json.load(request)
		datalist = formData.get('data')
		deletedImages = Image.objects.filter(id__in=datalist).only('cloudflare_id', 'id')
  
		for cf_id in deletedImages:
			#print(cf_id)
			cf_id_chain.append(cf_id.cloudflare_id)
		deletedImages.delete()
		data = {
	  		'cf_id_chain':datalist,
		}
  
		post_data = json.dumps(data)
		r2_api_call.upload_r2_object(post_data, f'delete-task-list/object{str(date_functions.date_time_now())}')

		return JsonResponse('success', safe=False)
	
	except ValueError as e:
		logging.error("Client Invite Error: %s", str((e)))
		slugified_error_message = slugify(str(e))
		return redirect('issue-backend', status=500, error_message=slugified_error_message)

def display_settings_endpoint(request, slug):
	settings_value = lambda setting: 0 if setting == False else(1) 
	
	if request.method == 'PUT':
		current_display = Display.objects.get(slug=slug)
		settings = json.loads(request.body)
		settings_update = (
	  		str(settings_value(settings.get('visiable'))) + 
			str(settings_value(settings.get('site'))) + 
			str(settings_value(settings.get('random'))) + 
			str(settings_value(settings.get('lock'))) 
   		)
		current_display.settings = settings_update
		current_display.save()

	return HttpResponse({'success':'success'})

def display_delete_endpoint(request, slug):
	if request.method == 'DELETE':
		current_display = Display.objects.get(slug=slug)
		current_display.delete()
	return HttpResponse({'success':'success'})

def display_share_endpoint(request, slug):
	if request.method == 'POST':

		byte_string = int(json.loads(request.body))
		expire = str(DateFunction().number_to_days(byte_string))
		current_display = Display.objects.get(slug=slug)
		new_key = secrets.token_hex(16)
		DisplayKey.objects.create(
			key=new_key,
			expire=expire,
			display=current_display
		)
	base_site = str(SETTINGS_KEYS.SHARE_GALLERY)
	full_url = base_site + f'?gallery=${new_key}'
	return HttpResponse(json.dumps({'url':full_url}))