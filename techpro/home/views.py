from django.shortcuts import render, HttpResponse
from .models import Photo
from .models import Logo
from .models import Header

# Create your views here.
def home(request):
	portifolio_query = Photo.objects.all()
	logo_query = Logo.objects.all()[:1].get()
	header_query = Header.objects.all()

	content = {
		'photos':portifolio_query
	}
	context = {
		'logos' : logo_query,
		'headers' : header_query
	}
	return render(request, 'portifolio.html', content)
	return render(request, 'index.html', context)