from django.db import models
from taggit.managers import TaggableManager
from django.utils.timezone import now


class Anime(models.Model):
    title = models.CharField("Название", max_length=50, default="Ничего нет")
    episode = models.CharField('Эпизод', max_length=20, default="0")
    image = models.ImageField("Картинка", upload_to="img/")
    description = models.TextField("Описание")
    date_out = models.DateField("Дата выхода")
    date_time = models.DateTimeField("Дата и время", default=now)
    tags = TaggableManager()
    published = models.BooleanField('Статус', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Аниме"
        verbose_name_plural = "Аниме"
