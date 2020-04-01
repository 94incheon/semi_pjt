from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # add 주의
    updated_at = models.DateTimeField(auto_now=True)
    