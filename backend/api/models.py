from django.db import models

# Create your models here.
class product(models.Model):
    title=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=20,decimal_places=3)
    details=models.TextField(max_length=300,null=True)