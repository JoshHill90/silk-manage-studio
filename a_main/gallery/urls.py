from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    
    path('o-panel/change/<slug:slug>/', views.manage_gallery, name='change-gal'),
    
    path('o-panel/image-upload', views.image_upload, name='image-upload'),

    path('image/form/<slug:data_packet>', views.image_form, name='image-form'),
    path('image/all/', views.all_image_list, name='image-details'),
    path('api/v1/image/upload/', views.upload_token_endpoint, name='image-token'),
    path('api/v1/image/create/', views.create_image_endpoint, name='create-image-endpoint'),
    path('api/v1/image/create/tags', views.tags_image_endpoint, name='create-image-tags-endpoint'),
    path('api/v1/image/create/gallery', views.gallery_image_endpoint, name='create-image-gallery-endpoint'),
    path('api/v1/image/delete/', views.delete_image_endpoint, name='image-token3'),
    
    path('api/v1/gallery/clear-gal/<slug:slug>/', views.clear_gallery_endpoint, name='gal-clear-endpoint'),
    path('api/v1/gallery/load-gal/<slug:slug>/', views.load_more_enpoint, name='load-gal-endpoint'),
    path('api/v1/create/', views.create_display_endpoint, name='create-display-endpoint'),
    path('api/v1/<slug:slug>/settings/', views.display_settings_endpoint, name='settings-display-endpoint'),
    path('api/v1/<slug:slug>/delete/', views.display_delete_endpoint, name='delete-display-endpoint'),
    path('api/v1/<slug:slug>/share/', views.display_share_endpoint, name='share-display-endpoint'),
]