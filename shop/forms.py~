from django import forms
from shop.models import Profile, Sweet
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('vk_page', 'timezone')

class SweetBuyForm(forms.Form):
	price1 = forms.IntegerField(label='Сколько вы хотите купить штук?', min_value = 0, initial=1)
	price2 = forms.IntegerField(label='Сколько вы хотите купить на вес? (В граммах, минимум 100)', min_value=100, required=False)
	
class ContactForm(forms.Form):
	subject = forms.CharField(max_length = 100)
	sender = forms.EmailField()
	message = forms.CharField(widget = forms.Textarea(attrs = {'class': 'form-control'}))
	copy = forms.BooleanField(required = False)
		
	
        

