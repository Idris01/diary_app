from django.db import models
from django.contrib.auth.models import AbstractUser
from .utility import generate_key

# Create your models here.
class User(AbstractUser):
    key=models.CharField(max_length=8, default=generate_key(),primary_key=True)


class Diary(models.Model):
    title=models.CharField(max_length=50, blank=False)
    content=models.CharField(max_length=200, blank=False)
    created_on=models.DateTimeField(auto_now=True)
    last_update=models.DateTimeField(auto_now_add=True)
    diary_key=models.ForeignKey(User,to_field='key',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

