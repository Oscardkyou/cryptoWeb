from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.template.defaultfilters import slugify

# Create your views here.
#menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

menu = [{'title': "О сайте", 'url_name':'about'},
        {'title': "Добавить статью", 'url_name':'addpage'},
        {'title': "Обратная связь", 'url_name':'contact'},
        {'title': "Войти", 'url_name': 'login'},
]

data_db = [
   {
       'id': 1,
       'title': 'Биткойн',
       'content': '''<h1>Биткойн</h1> (англ. Bitcoin) - это первая и самая известная криптовалюта, созданная под псевдонимом Сатоши Накамото в 2008 году. Биткойн использует децентрализованную технологию блокчейн для обеспечения безопасности и прозрачности транзакций.
       Биткойн позволяет пользователям отправлять и получать деньги напрямую друг от друга без участия посредников, таких как банки или правительственные организации. Это делает его популярным среди тех, кто ценит конфиденциальность и независимость от централизованных властей.
       В последние годы биткойн привлекает внимание как инвестиционный актив, так как его цена значительно выросла, и многие инвесторы видят его как средство сохранения капитала или спекулятивный актив.''',
       'is_published': True
   },
   {
       'id': 2,
       'title': 'Эфириум',
       'content': 'Описание Эфириума и его применений',
       'is_published': False
   },
   {
       'id': 3,
       'title': 'Рипл',
       'content': 'Описание Рипла и его технологии блокчейн',
       'is_published': True
   },
]

cats_db = [
   {'id': 1, 'name': 'Биткойн'},
   {'id': 2, 'name': 'Эфириум'},
   {'id': 3, 'name': 'Рипл'},
]

#class MyClass:
#   def __init__(self, a, b):
#      self.a = a
#      self.b = b


def index(request):
   #t = render_to_string('cats/index.html')
   data = { 'title': 'главная страница123?',
            'main_tittle': 'title',
            'menu': menu,
            'posts': data_db,
         }
   return render(request, 'cats/index.html', context=data)


def about(request):
   return render(request, 'cats/about.html', { 'title': 'О сайте', 'menu': menu })


def show_post(request, post_id):
   return HttpResponse(f"Отображение статьи с id={post_id}")


def addpage(request):
   return HttpResponse("Добавление статьи")


def contact(request):
   return HttpResponse("Обратная связь")


def login(request):
   return HttpResponse("Авторизация")


def show_category(request, cat_id):
   return index(request)


def page_not_found(request, exception):
   return HttpResponseNotFound("<h1>Страница не надйена</h1>")



#def categories(request, dog_id):
#   return HttpResponse(f"<h1>Сатья по категориям</h1><p>id: {dog_id}</p>")
#
#
#def categories_by_slug(request, dog_slug):
#   if request.POST: #можно поулчать GET и POST
#      print(request.POST)
#   return HttpResponse(f"<h1>Сатья по категориям</h1><p>slug: {dog_slug}</p>")
#
#
#def archive(request, year):
#   if year > 2023: #добавил int для переопрделения
#      uri = reverse('dogs', args=('sport',))
#      return HttpResponseRedirect(uri)#'/', permanent=True
#   return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")






