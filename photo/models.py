from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    img = models.ImageField(verbose_name='Photo', upload_to='images/')
    title = models.CharField(verbose_name='Photo Title', max_length=50)
    desc = models.TextField(verbose_name='Photo Descriprion', blank=True, null=True)
    people = models.CharField(verbose_name='People on photo', max_length=255, blank=True, null=True)
    loacation = models.CharField(verbose_name='Location of the photo', max_length=255, blank=True, null=True)
    tags = models.CharField(verbose_name='Photo Search Tags', max_length=100, blank=True, null=True)
    cr_dt = models.DateTimeField(verbose_name='Photo Created Date', auto_now_add=True)

    user = models.ForeignKey(User, verbose_name='Created By User', on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title