# apps/blog/forms.py

# Django modules
from django import forms

# My modules
from blog.models import BlogPost

# Create your model forms here.


class BlogPostModelForm(forms.ModelForm):
    tag = forms.CharField()
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'cover_image',
            'content',
            'category',
            'tag',
        ]

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['title'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['content'].widget.attrs.update({'class':'form-control'})
    #     self.fields['category'].widget.attrs.update({'class':'form-control'})
    #     self.fields['tag'].widget.attrs.update({'class':'form-control'})