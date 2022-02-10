from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)

    def __str__(self):
        return format(self.name)

class products(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    img=models.ImageField(upload_to='product')
    desc=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)

    def __str__(self):
        return format(self.name)
