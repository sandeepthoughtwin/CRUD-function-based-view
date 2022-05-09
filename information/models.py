from django.db import models




# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=20)
    roll_num = models.IntegerField()
    email = models.EmailField()
    mobile = models.IntegerField()

    def __str__(self):
      return self.name