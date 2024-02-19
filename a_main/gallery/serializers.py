from gallery.models import Image
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['title', 'image_link','client_id', 'project_id', 'cloudflare_id']
