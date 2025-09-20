
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Package(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin_packages')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    image = models.ImageField(upload_to='packages/', null=True, blank=True)

    def __str__(self):
        return self.name
