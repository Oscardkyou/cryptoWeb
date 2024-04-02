from django.db import models

# Create your models here.
class Posts(models.Model):
   title = models.CharField(max_length=100, verbose_name="Заголовок")
   create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
   update_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
   text = models.TextField(verbose_name="Текст")


   class Meta:
      verbose_name = "Пост"
      verbose_name_plural = "Посты"


   def __str__(self) -> str:
      return f"Пост: {self.title}"
















