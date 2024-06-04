from django.db import models


# Create your models here.
class Logins(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_created=True,auto_now_add=True)
