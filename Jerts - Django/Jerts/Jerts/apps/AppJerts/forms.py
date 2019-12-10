from django import forms
from django.contrib.auth.models import User
from .models import Contacto
#from users.models import User

class RegisterForm(forms.Form):
	username = forms.CharField(required = True,min_length = 5, max_length=50,
								widget=forms.TextInput(attrs={
									'class': 'form-control',
									'id': 'username',
									'placeholder': 'Nombre Usuario'
									})
								)
	email = forms.EmailField(required = True, 
									widget=forms.EmailInput(attrs={
									'class': 'form-control',
									'id': 'email',
									'placeholder': 'ejemplo@jairogaleas.com'
									}))
	password = forms.CharField(required = True,
									widget=forms.PasswordInput(attrs={
									'class': 'form-control',
									'id': 'password'
									}))
	password2 = forms.CharField(label='Repetir Password',required = True,
									widget=forms.PasswordInput(attrs={
									'class': 'form-control',
									'id': 'password'
									}))
	def clean_username(self):
		username = self.cleaned_data.get('username')
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError('El Usuario ya se encuentra en uso')
		return username

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError('El Correo electronico ya se encuentra en uso')
		return email

	def clean(self):
		cleaned_data = super().clean()
		if cleaned_data.get('password2') != cleaned_data.get('password'):
			self.add_error('password2', 'El Pasword no coincide')

	def save(self):
		User.objects.create_user(
				self.clean
			)

class Contacto_Form(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = "__all__" 