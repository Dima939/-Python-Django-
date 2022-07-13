from .forms import RegisterForm
from django.views import generic


class Register(generic.CreateView):
    form_class = RegisterForm
    success_url = 'accounts/login'
    template_name = 'register.html'
