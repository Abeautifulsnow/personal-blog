from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Blog


class BlogForm(forms.Form):
    title = forms.CharField(required=True)
    content = forms.CharField(widget=CKEditorWidget(config_name='default'))