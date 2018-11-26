from django.db import models
from django.urls import reverse
from genres.models import Genre

class Good(models.Model):
  name = models.CharField(max_length = 50, unique = False, db_index = True, verbose_name = "Название")
  genre = models.ForeignKey(Genre, null = True, blank = True, on_delete = models.SET_NULL, verbose_name = "Жанр")
  contacts = models.CharField(max_length = 50, unique = False, db_index = True, verbose_name = "Контакты")
  author = models.CharField(max_length = 50, unique = False, db_index = True, verbose_name = "Автор")
  description = models.TextField(verbose_name = "Краткое описание")
  price = models.FloatField(db_index = True, verbose_name = "Цена, руб.")
  image = models.ImageField(upload_to = "goods/list", verbose_name = "Основное изображение")
  def save(self, *args, **kwargs):
    try:
      this_record = Good.objects.get(pk = self.pk)
      if this_record.image != self.image:
        this_record.image.delete(save = False)
    except:
      pass
    super(Good, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
    self.image.delete(save = False)
    super(Good, self).delete(*args, **kwargs)

  def get_absolute_url(self):
    return reverse("goods_detail", kwargs = {"pk": self.pk})

  class Meta:
    verbose_name = "товар"
    verbose_name_plural = "товары"

class GoodImage(models.Model):
  good = models.ForeignKey(Good, on_delete = models.CASCADE)
  image = models.ImageField(upload_to = "goods/detail", verbose_name = "Дополнительное изображение")
  def save(self, *args, **kwargs):
    try:
      this_record = GoodImage.objects.get(pk = self.pk)
      if this_record.image != self.image:
        this_record.image.delete(save = False)
    except:
      pass
    super(GoodImage, self).save(*args, **kwargs)

  def delete(self, *args, **kwargs):
    self.image.delete(save = False)
    super(GoodImage, self).delete(*args, **kwargs)

  class Meta:
    verbose_name = "изображение к товару"
    verbose_name_plural = "изображения к товару"
