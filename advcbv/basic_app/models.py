from django.db import models
# from django.core.urlresolvers import reverse
# Create your models here.
from django.urls import reverse

class School(models.Model):
    name=models.CharField(max_length=256)
    principal=models.CharField(max_length=256)
    location=models.CharField(max_length=256)

    def __str__(self):      # this is string representation of model in case we want to print it out
        return self.name

    def get_absolute_url(self):
        return reverse('basic_app:detail',kwargs={'pk':self.pk})



class Studend(models.Model):
    name=models.CharField(max_length=256)
    age=models.PositiveIntegerField()
    school=models.ForeignKey(School, related_name='students', on_delete=models.CASCADE,)     # it will inherit School name from School folder

    def __str__(self):
        return self.name
