from django.contrib import admin
from .models import Photo
from .models import Logo

# Register your models here.
class Photo_Admin(admin.ModelAdmin):
	list_display = ['category_name', 'project_name']

	class Meta:
		model = Photo

class Logo_Admin(admin.ModelAdmin):
	list_display = ['logo_name', 'create_time', 'update_time']

	class Meta:
		model = Logo

admin.site.register(Photo, Photo_Admin)
admin.site.register(Logo, Logo_Admin)