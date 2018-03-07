from django.db import models

# Create your models here.
class Photo(models.Model):
	category_name = models.CharField(max_length=200)
	project_name = models.CharField(max_length=200)
	width = models.IntegerField(default=0)
	height = models.IntegerField(default=0)
	image = models.ImageField(null=False, blank=False, width_field='width', height_field='height')
	upload_time = models.DateTimeField(auto_now_add=True, auto_now=False)
	update_time = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return self.project_name

		class Meta:
			ordering = ['-upload_time']