from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
	return HttpResponse('<h2>Welcome website home pages.</h2>')