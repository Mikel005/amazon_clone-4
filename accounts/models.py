from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # prevent clash with default user
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # prevent clash
        blank=True
    )
    
    def __str__(self):
        return self.username
    
    
    

