from django.shortcuts import render, HttpResponse
from .models import Photo
from .models import Logo

# Create your views here.
def home(request):
	portifolio_query = Photo.objects.all()
	logo_query = Logo.objects.all()[:1].get()
	content = {
		'photos':portifolio_query,
		'logos' : logo_query
	}
	context = {
		'logos' : logo_query
	}
	return render(request, 'portifolio.html', content)
	return render(request, 'index.html', context)