from django.db import models

# Create your models here.
class Order(models.Model):
    fio_customer = models.CharField(max_length=100)
    computer_model = models.CharField(max_length=100)
