from django.contrib.auth.models import User
from django.db import models
from product.models import Product
from user.models import CustomerUser

class Message(models.Model):
    room = models.ForeignKey(Product, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    content = models.TextField()
    img = models.ImageField(upload_to='images',default=None,null=True)
    date_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.content