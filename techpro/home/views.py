from django.shortcuts import render, HttpResponse
from .models import Photo

# Create your views here.
def home(request):
	queryset = Photo.objects.all()
	content = {
		'photos':queryset
	}
	return render(request, 'index.html', content)