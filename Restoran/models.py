from django.db import models
from django.urls import reverse


class Menu(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    photo = models.ImageField(upload_to='image/')
    price = models.TextField()
    menu = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self, id):
    #     return reverse('Index', kwargs={'id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=90, db_index=True)

    def __str__(self):
        return self.name

