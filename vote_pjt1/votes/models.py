from django.db import models
from django.conf import settings

# Create your models here.
class Vote(models.Model):
    title = models.CharField(max_length=100)
    issue_a = models.CharField(max_length=500)
    issue_b = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Comment(models.Model):
    AGREE = 'Agree'
    DISAGREE = 'Disagree'
    PICK_CHOICES = (
        (AGREE, 'Agree'),
        (DISAGREE, 'Disagree')
    )
    pick = models.CharField(max_length=10, choices=PICK_CHOICES, default=AGREE)
    content = models.CharField(max_length=200)
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
