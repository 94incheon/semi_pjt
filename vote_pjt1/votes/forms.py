from django import forms
from .models import Vote, Comment

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['title', 'issue_a', 'issue_b']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['pick', 'content']
