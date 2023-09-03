from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control mb-4'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-4'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-4'}))
    
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','readonly': 'readonly'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control mb-4'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-4'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-4'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # jodi user er account thake 
        if self.instance:
            try:
                user_account = self.instance
            except User.DoesNotExist:
                user_account = None

            if user_account:
                self.fields['first_name'].initial = user_account.first_name
                self.fields['last_name'].initial = user_account.last_name
                self.fields['email'].initial = user_account.email
        
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_account, created = User.objects.get_or_create(user=user) # jodi account thake taile seta jabe user_account ar jodi account na thake taile create hobe ar seta created er moddhe jabe
            user_account.first_name = self.cleaned_data['first_name']
            user_account.last_name = self.cleaned_data['last_name']
            user_account.email = self.cleaned_data['email']
            user_account.save()
        return user