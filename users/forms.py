from . import models
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import CaptchaField


class CreateUserForm(UserCreationForm):
    captcha = CaptchaField()
    class Meta:
        model = models.User
        fields = [
            'first_name', 'last_name', 'email',
            'username', 'phone', 'address',
            'password1', 'password2'
        ]
    

class UpdateUserForm(CreateUserForm):
    def clean_username(self):
        return self.cleaned_data.get('username')