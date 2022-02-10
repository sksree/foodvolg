from django.db import models
from productapp.models import *
# Create your models here.
class cartlist(models.Model):
    cart_id=models.CharField(max_length=25,unique=True)
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return format(self.cart_id)


class items(models.Model):
    prodt = models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quen=models.IntegerField()

    def __str__(self):
        return format(self.prodt)