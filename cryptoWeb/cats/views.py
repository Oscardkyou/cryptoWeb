from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
   return HttpResponse("Страница приложения Cats")


def categories(request, dog_id):
   return HttpResponse(f"<h1>Сатья по категориям</h1><p>id: {dog_id}</p>")


def categories_by_slug(request, dog_slug):
   return HttpResponse(f"<h1>Сатья по категориям</h1><p>slug: {dog_slug}</p>")


def acrhive(request, year):
   return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")