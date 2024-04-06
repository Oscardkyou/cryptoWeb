from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
   return HttpResponse("Страница приложения Cats")


def categories(request, dog_id):
   return HttpResponse(f"<h1>Сатья по категориям</h1><p>id: {dog_id}</p>")


def categories_by_slug(request, dog_slug):
   if request.POST: #можно поулчать GET и POST
      print(request.POST)
   return HttpResponse(f"<h1>Сатья по категориям</h1><p>slug: {dog_slug}</p>")


def archive(request, year):
   if year > 2023: #добавил int для переопрделения
      uri = reverse('dogs', args=('sport',))
      return HttpResponseRedirect(uri)#'/', permanent=True
   return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
   return HttpResponseNotFound("<h1>Страница не надйена</h1>")



