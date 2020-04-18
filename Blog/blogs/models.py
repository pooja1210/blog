from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class blog(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=100, blank=False)
    desc = models.TextField(max_length=100, blank=False)
    image = models.ImageField(blank=True, upload_to='images')
    pub_date = models.DateField(auto_now=True)
    