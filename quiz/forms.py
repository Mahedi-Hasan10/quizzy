from django import forms
from .models import UserReviewModel

class UserReviewForm(forms.ModelForm):
    RATING =(
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
    )
    user =forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control my-2','readonly': 'readonly'}))
    details = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control mt-3 d-block'}))
    class Meta:
        model = UserReviewModel
        fields = "__all__"
        