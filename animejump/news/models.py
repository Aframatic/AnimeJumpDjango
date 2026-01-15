from django.db import models
from django.utils.timezone import now


class News(models.Model):
    title = models.CharField("Название", max_length=50)
    image = models.ImageField("Картинка", upload_to="img/")
    description = models.CharField("Описание", max_length=500)
    full_text = models.TextField("Полная статья")
    date_out = models.DateField("Дата выхода", default=now)
    date_time = models.DateTimeField("Дата и время", default=now)
    published = models.BooleanField('Статус', default=False)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return f'/news/{self.id}'

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
