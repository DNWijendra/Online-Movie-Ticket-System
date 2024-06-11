from.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class New_User_Form(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class New_Movie_Form(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
