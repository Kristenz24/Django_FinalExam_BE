from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name          = models.CharField(max_length=100, blank=True, null=True)
    last_name           = models.CharField(max_length=100, blank=True, null=True)
    email               = models.EmailField(unique=True)
    password            = models.CharField(max_length=200)
    confirm_password    = models.CharField(max_length=200)
    username            = models.CharField(max_length=100)
    date_registered     = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
