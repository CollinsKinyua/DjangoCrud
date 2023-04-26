from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=37, blank=False, null=False)
    email = models.EmailField(max_length=47, blank=False, null=False)
    age = models.IntegerField()
    gender = models.CharField(max_length=37, blank=False, null=False)


def __str__(self):
    return self.name
