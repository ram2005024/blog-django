from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=("username","email","password1","password2")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name,field in self.fields.items():
            if field_name=='password1':
                placeholder='Password'
            elif field_name=='password2':
                placeholder='Confirm'
            else:
                placeholder=field_name
            field.widget.attrs.update({
                'class':'w-sm ring ring-gray-100 text-gray-400 p-2 pl-12 transition-all eas-in duration-200 rounded-lg focus:ring-indigo-400 outline-none',
                'placeholder':f'{placeholder.capitalize()}'
            })
class LoginForm(AuthenticationForm):
    error_messages={
        'invalid_login':'Please enter valid username and password',
        'inactive':'This account is inactive'

    }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name,field in self.fields.items():
            field.widget.attrs.update({
                'placeholder':f'Enter {field_name}',
                'class':'w-sm ring ring-gray-100 text-gray-400 p-2 pl-12 transition-all eas-in duration-200 rounded-lg focus:ring-indigo-400 outline-none'
            })
    

    