from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import settings 



# models

class Usuario(AbstractUser):
    imagen = models.ImageField(null=True, blank=True, upload_to='usuario', default='usuario/user-default.png' )
    
    
    def get_absolute_url(self):
        return reverse('index')





    
