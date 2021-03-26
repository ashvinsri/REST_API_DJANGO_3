from django.db import models

class Student(models.Model):
    clas=models.CharField(max_length=264)
    name=models.CharField(max_length=264)
    city=models.CharField(max_length=264)

    def __str__(self):
        return self.clas
