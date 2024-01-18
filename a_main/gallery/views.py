from typing import Any
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect 
from django.urls import reverse 
from django.conf import settings
from .models import Image, Dispaly, Tag
from client.models import Project
from django.core.paginator import Paginator
from a_main.env.app_Logic.photo_layer import col3_col6_col3
from a_main.env.app_Logic.untility.quick_tools import ViewExtendedFunctions, DateFunction, ViewQueryHelper
from a_main.env.cloudflare_API.CFAPI import APICall, Encode_Metadata
from a_main.env.cloudflare_API.CFR2API import CloudflareR2API
from logs.logging_config import logging
import json
from django.utils.text import slugify
import zlib
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

def manage_gallery(request, gal):
	# The gallery management section empowers users to curate the content for various galleries, 
	# including the home page and header images for each gallery. 
	
	try:
		all_images = Image.objects.all().distinct()
		display = Dispaly.objects.filter(gal)
		
		#subgal_instance = display.get(id=subgal)
		#gall_instance = display.get(id=gal)
		current_gallery = display.image_set.all()
		
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
				#print('update')
				# creats blank image list and sets all images in the galllery to none
				image_listed = set()
				# creates keypair values for selected images
				for image_value, image_key in zip(request.POST.values(),  request.POST.keys()):
					if 'checkbox' in image_key:
						image_listed.add(image_value)
				# filter and update selected values
				
				selected_images = all_images.filter(id__in=image_listed)
				display.update(image=None)
				

				return redirect('change-gal', display)

			# remove function: will only remove items selected
			elif 'remove' in request.POST.values():
				#print('remove')
				# creats blank image list and sets all images in the galllery to none
				image_listed = set()

				for image_value, image_key in zip(request.POST.values(),  request.POST.keys()):
					if 'checkbox' in image_key:
						image_listed.add(image_value)
		
				# filter for selected values
				selected_images = all_images.filter(id__in=image_listed)
				
				for image in selected_images:
					image.display.remove(subgal_instance)

				return redirect('change-gal', display)
			
			# make image header for the gallery
			elif 'header' in request.POST.keys():

				header_image_id = request.POST.get('header')
				#print(header_image_id)
				header_image = all_images.filter(id=header_image_id)
				current_header = gall_instance.image_set.filter(display=gal)
				for image in current_header:
					image.display.remove(gal)
		
				header_image.get().display.add(gall_instance)
				return redirect('change-gal', gal=gal, subgal=subgal)

		return render(request, 'o_panel/gallery/change-gallery.html', {
			'current_list': get_gallery,
			'gal': gal,
			'subgal':subgal,
			'image_sets':image_sets,
			'gal_name':gall_instance,
			'subgal_name':subgal_instance,
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

# endpoint for clearing selected gallery images
def load_more_enpoint(request, gal, subgal):
	print('load')
	
	all_images = Image.objects.all().distinct().only('id', 'project_id', 'title', 'display', 'image_link')
	filter_set = vqh.image_query(request, all_images, subgal)
	display = Dispaly.objects.all()
	subgal_instance = None

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
		display_list = get_info.display.values()

		image_display = str(0)
		if display_list and subgal != '0':
     
			subgal_instance = display.get(id=subgal)
   
			for display_id in display_list:

				if display_id['id'] == subgal_instance.id:
					image_display = subgal
     
		next_image_set.append({
			'id':image_id,
			'project':image_project, 
			'title':image_title, 
			'display':image_display,
			'image_link':image_link
			})
  
	return HttpResponse(json.dumps(next_image_set))

# endpoint for clearing selected gallery images
def clear_gallery_endpoint(request, gal, subgal):
	display_object = Dispaly.objects.all()
	subgal_instance = display_object.get(id=subgal)
	
	if request.method == 'GET':
		img_list = []
		gal_images = Image.objects.filter(display=subgal_instance).distinct().only('id', 'display')
		for index in range(len(gal_images)):
			img_list.append(str(gal_images[index].id))

		reps = json.dumps({'imgList': img_list})
		return HttpResponse(reps)
			
	if request.method == 'POST':
		body_unicode = request.body.decode('utf-8')
		body = json.loads(body_unicode)
		img_id = body.get('id')
		
		gal_instance = display_object.get(id=gal)
		gal_image = Image.objects.get(id=img_id)
		gal_image.display.remove(subgal_instance)
		gal_image.display.remove(gal_instance)
		resp = json.dumps({'success':'success'})
		
		return HttpResponse(resp)
	
def image_upload(request):
	
	return render(request, 'o_panel/images/image_upload.html')
#-------------------------------------------------------------------------------------------------------#
# Image upload views
#-------------------------------------------------------------------------------------------------------#

def image_process(request):
	data_packet = []
	cfId_slug = ''
	if request.method == 'POST':
		for cf_object in json.load(request)['data'] :
			
			slug_id =' ' + str(cf_object)
			cfId_slug = cfId_slug + slug_id
		compressed_data = zlib.compress(cfId_slug.encode())
		data_packet = compressed_data.hex()
		
		image_form_url = reverse('image-form', args=[data_packet])
		return JsonResponse(str(image_form_url), safe=False)

	return JsonResponse({'error': 'Invalid request method'})

def image_form(request, data_packet):
	
	compressed_data = bytes.fromhex(data_packet)
	decompressed_data = zlib.decompress(compressed_data)
	list_data = decompressed_data.decode().split()
	if not list_data:
		return redirect('issue-backend', status='400', error_message='image-failed-upload')
	tags_object = Tag.objects.all()
	display_objects = Dispaly.objects.all()
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

def upload_token_endpoint(request):
	if request.method == 'GET':
		post_data = []
		cloudflare_token = cf_api_call.get_batch_token()
		if 'error' not in cloudflare_token:
			cloudflare_token = str(cloudflare_token)
			front_end_url = 'https://batch.imagedelivery.net/images/v1'

			post_data.append({'cf_token':cloudflare_token,'cf_url': front_end_url})

		else:
			e = cloudflare_token
			logging.error("Client Invite Error: %s", str((e)))
			slugified_error_message = slugify(str(e))
			return redirect('issue-backend', status=500, error_message=slugified_error_message)
	
		return JsonResponse(post_data, safe=False)

				
def delete_image_endpoint(request):
	cf_id_chain = []
	print('check-0')
	try:
		formData = json.load(request)
		datalist = formData.get('data')
		deletedImages = Image.objects.filter(id__in=datalist).only('cloudflare_id', 'id')
  
		for cf_id in deletedImages:
			print(cf_id)
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
	
	
		

 
def create_image_endpoint(request):
	tags_object = Tag.objects.all()
	display_object = Dispaly.objects.all()

	formData = json.load(request)
	datalist = formData.get('data')
	datalist[0].get('title')
	
	set_tags = datalist[1].get('tag') 
	set_display = datalist[3].get('display')
	set_project = datalist[2].get('project')
	set_title = datalist[0].get('title')
	cfId_set = datalist[4].get('cf_id')
	project_instance = Project.objects.get(id=set_project)
	slected_client = project_instance.client_id
	
	imgobj_id = []

	for cf_id in cfId_set:
		print('upload')
		image_url = f'https://imagedelivery.net/4_y5kVkw2ENjgzV454LjcQ/{cf_id}/display'
		imgobj = Image(
			title=str(set_title) + '-' + str(cf_id),
			client_id=slected_client,
			project_id=project_instance,
			image_link=image_url,
			cloudflare_id=cf_id,
		)
		imgobj_id.append(imgobj)
	
	new_images = Image.objects.bulk_create(imgobj_id)
	image_list = Image.objects.filter(title__in=new_images)
 
	for images in image_list:

		for tags in set_tags:
			tag_instance = tags_object.filter(name=tags)
			if tag_instance:
					tag_instance = tags_object.get(name=tags)
			else:
				tag_instance = tags_object.create(name=tags)
				tag_instance.save()
    
			images.tag.add(tag_instance.id)

		for display in set_display:
			display_instance = display_object.get(id=display)
			images.display.add(display_instance.id)

	return JsonResponse('success', safe=False)