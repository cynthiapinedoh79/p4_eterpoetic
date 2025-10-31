from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """Form for creating and editing comments.
    """
    
    class Meta:
        model = Comment
        fields = ('body',)
