from django.db import models
from django.contrib.auth import get_user_model



class Duck(models.Model):
    title = models.CharField(max_length=255)   
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title