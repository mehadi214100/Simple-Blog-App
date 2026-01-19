from .models import Category,Author,Post
from django import forms

class categoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class authorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

class postForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"