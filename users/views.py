from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib import messages
from . import models
from . import forms
from django.views.generic import (
    CreateView, UpdateView
)
from . import mixins



class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'form.html'
    model = models.User
    form_class = forms.CreateUserForm
    success_url = reverse_lazy('login')
    success_message = _('User registered successfully')
    extra_context = {
        'head': _('Sign-up'),
        'button_text': _('Register'),
    }


class UserUpdateView(mixins.CheckSelfUserMixin,
                     SuccessMessageMixin, UpdateView):
    model = models.User
    form_class = forms.UpdateUserForm
    template_name = 'form.html'
    success_url = reverse_lazy('users_index')
    success_message = _('User successfully changed')
    extra_context = {
        'head': _('Change user'),
        'button_text': _('Change'),
    }

