from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	greeting = "Hello World!"
	return render(request, 'scpyladies/index.html', locals())
