from django.db import models

class Student(models.Model):
    name = models.CharFilds(max_lenght=20)
