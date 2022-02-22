from urllib.request import urlopen
from django.db import models
from django.template.defaultfilters import truncatechars
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile


class Prints(models.Model):
    key = models.CharField(verbose_name="Prints Unique Key", max_length=200)
    author = models.CharField(verbose_name="Автор", max_length=150,)
    details = models.TextField(verbose_name="Подробности", null=True, blank=True)
    blueprint = models.TextField(verbose_name="Строка чертежа", null=True, blank=True)
    image = models.ImageField(verbose_name="Изображение чертежа", upload_to="images", null=True, blank=True)
    created_at = models.CharField(verbose_name="Дата создания", max_length=200)
    updated_at = models.CharField(verbose_name="Обновлено в", max_length=200)
    favorites = models.CharField(verbose_name="Избранное", max_length=10)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Чертеж"
        verbose_name_plural = "Чертежи"

    def get_image_from_url(self, url):
        img_tmp = NamedTemporaryFile(delete=True)
        with urlopen(url) as uo:
            assert uo.status == 200
            img_tmp.write(uo.read())
            # img_tmp.flush()
        # img = File()
        self.image.save(img_tmp.name, img_tmp)

    @property
    def short_details(self):
        return truncatechars(self.details or '', 40)

    @property
    def short_blueprint(self):
        return truncatechars(self.blueprint, 40)

    def __str__(self):
        return f"{self.author}:{self.favorites}"
