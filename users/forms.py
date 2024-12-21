from . import models
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = [
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2'
        ]


class UpdateUserForm(CreateUserForm):
    def clean_username(self):
        return self.cleaned_data.get('username')