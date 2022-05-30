from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(verbose_name="Название сайта", max_length=10)
    logo = models.ImageField(verbose_name="Логотип сайта",blank=True,upload_to='images/')
    keywords = models.CharField(verbose_name="Ключевые слова для поиска сайта",max_length=255)
    description = models.CharField(verbose_name="Описание сайта",max_length=255)
    address = models.CharField(verbose_name="Адрес сайта",blank=True,max_length=100)
    phone = models.CharField(verbose_name="телефон",blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    facebook = models.CharField(help_text="ссылка на facebook", blank=True,max_length=50)
    instagram = models.CharField(help_text="ссылка на instagram", blank=True,max_length=50)
    twitter = models.CharField(help_text="ссылка на twitter", blank=True,max_length=50)
    telegram = models.CharField(help_text="ссылка на telegram", blank=True, max_length=50)

    def __str__(self):
        return f"ID: {self.id} ||||| {self.title}"
    
    class Meta:
        verbose_name_plural = "Основные настройки сайта"
