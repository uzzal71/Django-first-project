from django.contrib import admin
from .models import Photo

# Register your models here.
class Photo_Admin(admin.ModelAdmin):
	list_display = ['category_name', 'project_name']

	class Meta:
		model = Photo

admin.site.register(Photo, Photo_Admin)