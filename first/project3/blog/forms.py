from django import forms
from django.db import models
from django.db.models import fields
from .models import Comment

class CommentCreateForms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Comment
        fields = ["name", "text"]
