from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from . import models
from . import forms
from django.views.generic import (
    CreateView, UpdateView, DetailView
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
    success_url = reverse_lazy('index')
    success_message = _('User successfully changed')
    extra_context = {
        'head': _('Change user'),
        'button_text': _('Change'),
    }

class UsersDetailView(mixins.CheckSelfUserMixin, DetailView):
    template_name = 'users/users_detail.html'
    model = models.User