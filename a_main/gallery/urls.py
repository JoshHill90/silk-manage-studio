from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    
    path('o-panel/change/<slug:gal>/<slug:subgal>/', views.manage_gallery, name='change-gal'),
    
    path('o-panel/image-upload', views.image_upload, name='image-upload'),
    path('image/process/', views.image_process, name='image-process'),
    path('image/form/<slug:data_packet>', views.image_form, name='image-form'),
    path('image/all/', views.all_image_list, name='image-details'),
    path('image/upload/api', views.upload_token_endpoint, name='image-token'),
    path('image/create/api', views.create_image_endpoint, name='image-token2'),
    path('image/delete/api', views.delete_image_endpoint, name='image-token3'),
    
    path('image/clear-gal/api/<slug:gal>/', views.clear_gallery_endpoint, name='gal-clear-endpoint'),
    path('image/load-gal/api/<slug:gal>/', views.load_more_enpoint, name='load-gal-endpoint'),
]