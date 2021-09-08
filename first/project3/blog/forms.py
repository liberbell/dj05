from django import forms
from django.db import models
from django.db.models import fields
from .models import Comment

class CommentCreateForms(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["name", "text"]
