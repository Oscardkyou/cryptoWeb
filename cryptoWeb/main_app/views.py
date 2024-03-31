from django.shortcuts import render

# Create your views here.
def index_view(request):
   context = {'title': 'Главная страница'}
   return render(request, 'index.html', context=context)


def index_view2(request):
   context = {'title': 'Другая страница'}
   return render(request, 'index2.html', context)


def index_view3(request):
   context = {'title': 'Наследуем старницу'}
   return render(request, 'index3.html', context)


def index_view4(request):
   context = {'title': 'Наследуем страницу2'}
   return render(request, 'index4.html', context)
