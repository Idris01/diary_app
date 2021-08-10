from django.db import models

# Create your models here.
class Diary(models.Model):
    title=models.CharField(max_length=50, blank=False)
    content=models.CharField(max_length=200, blank=False)
    created_on=models.DateTimeField(auto_now=True)
    last_update=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

