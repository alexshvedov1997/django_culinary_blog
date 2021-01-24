from django import forms
from .models import Comment, CulinaryPost

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class CulinaryPostForm(forms.ModelForm):
    class Meta:
        model = CulinaryPost
        fields = ('title','slug','body', 'culinary_category', 'photo' )

class SearchForm(forms.Form):
    query = forms.CharField()