from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
  return render(request, 'rango/index.html', context=context_dict)

def about(request):
  return HttpResponse("<a href='/rango'>Rango says here is the about page.</a>")
