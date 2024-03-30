from django.shortcuts import render

# Create your views here.
def index_view(request):
   context = {'title': 'Главная страница'}
   return render(request, 'index.html', context=context)


def index_view2(request):
   context = {'title': 'Другая страница'}
   return render(request, 'index2.html', context)

