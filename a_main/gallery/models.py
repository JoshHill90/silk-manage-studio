from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from a_main.env.app_Logic.untility.quick_tools import DateFunction


class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return str(self.name)

class Image(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    portrait_format = models.CharField(max_length=50, default='square')
    private = models.BooleanField(default=False)
    client_id = models.ForeignKey('client.Client', null=True, blank=True, on_delete=models.SET_NULL)
    project_id = models.ForeignKey('client.Project', null=True, blank=True, on_delete=models.SET_NULL)
    image_link = models.URLField(blank=True, default=' ')
    cloudflare_id = models.CharField(max_length=255, blank=True)
    silk_id = models.CharField(max_length=50, default='CB01')

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("image-details", kwargs={"slug": self.cloudflare_id})
    
# settings note: /visble/site/random/lock
class Display(models.Model):
    name = models.CharField(max_length=255, unique=True)
    images = models.ManyToManyField(Image, blank=True, null=True, related_name='display_images')
    slug = AutoSlugField(populate_from='name')
    settings = models.CharField(max_length=4, default='0000')
    header_image = models.ForeignKey(Image,  null=True, blank=True, on_delete=models.SET_NULL, related_name='header_images')
    def __str__(self):
        return str(self.name)
    def get_absolute_url(self):
        return reverse("change-gal", kwargs={"slug": self.slug})
 
class DisplayKey(models.Model):
    key = models.CharField(max_length=32, unique=True)
    expire = models.DateField(default=str(DateFunction().number_to_days(90)))
    display = models.ForeignKey(Display, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.display) + ' | ' + str(self.expire) 