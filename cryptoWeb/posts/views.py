from django.shortcuts import render
from .models import Posts

# Create your views here.
def post_view(request):
   posts = Posts.objects.all()
   context = {'title': 'Добрый Вечер!', 'posts': posts}

   return render(request, 'index10.html', context)
