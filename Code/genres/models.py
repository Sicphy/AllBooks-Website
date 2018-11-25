from django.db import models

class Genre(models.Model):
  name = models.CharField(max_length = 30, db_index = True, unique = True, verbose_name = "Название")
  def __str__(self):
    return self.name

  class Meta:
    ordering = ["name"]
    verbose_name = "жанр"
    verbose_name_plural = "жанры"
