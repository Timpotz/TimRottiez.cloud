from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pup
from .models import AvailablePuppy
from .models import GalleryImage

admin.site.register(Pup)
admin.site.register(AvailablePuppy)
admin.site.register(GalleryImage)
