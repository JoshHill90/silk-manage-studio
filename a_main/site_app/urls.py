from django.contrib import admin
from django.urls import path
from .views import *
from . import views

urlpatterns = [   
    path('error/<int:status>/<slug:error_message>', views.error_logger, name='issue-backend'),     
    
    path('panel', views.o_main, name='o_panel'),
    path('panel/binder', views.o_binder, name='binder'),
    path('panel/marketing', views.marketing, name='marketing'),
    path('', views.o_gallery, name='o-gallery'),
    
    path('panel/settings/documents', views.document_settings, name='o-documents'),

]