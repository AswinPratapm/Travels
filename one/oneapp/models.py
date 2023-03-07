from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    city=models.TextField(max_length=250)

    def __str__(self):
        return self.name

class team(models.Model):
    pic=models.ImageField(upload_to='profile')
    name=models.CharField(max_length=200)
    role=models.TextField()

    def __str__(self):
        return self.name
