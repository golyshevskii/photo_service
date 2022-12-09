from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    img = models.ImageField()
    title = models.CharField(verbose_name='Photo Title', max_length=50)
    desc = models.TextField(verbose_name='Photo Descriprion', blank=True, null=True)
    cr_dt = models.DateTimeField(verbose_name='Photo Created Date', auto_now_add=True)

    user = models.ForeignKey(User, verbose_name='By User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title