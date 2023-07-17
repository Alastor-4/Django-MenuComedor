from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, CreateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import RegisterForm, LoginForm, VerificationForm
from .functions import code_generator
from .models import User

class LoginUserView(FormView):
    template_name = 'auth/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:home-menu')
    
    def form_valid(self, form):
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        login(self.request, user)
        return super(LoginUserView, self).form_valid(form)

class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('auth_app:auth-login'))

class UserRegisterView(CreateView):
    template_name = "auth/register.html"
    form_class = RegisterForm

    def form_valid(self, form):
        # llamar a la función para generar código
        codigo = code_generator()

        usuario = User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password'],
            codregistro=codigo
        )

        # enviar el código al email del usuario
        asunto = "Confirmación de email"
        mensaje = "Codigo de verificación: " + codigo
        email_remitente = "comedorucf@gmail.com"
        emails = [form.cleaned_data['email'],]

        send_mail(asunto, mensaje, email_remitente, emails,)

        return HttpResponseRedirect(reverse('auth_app:auth-verification', kwargs={'id_user': usuario.id}))

class CodeVerificationView(FormView):
    template_name = 'auth/verification.html'
    form_class = VerificationForm
    success_url = reverse_lazy('auth_app:auth-login')
    
    def get_form_kwargs(self):
        kwargs = super(CodeVerificationView, self).get_form_kwargs()
        kwargs.update({'id_user' : self.kwargs['id_user']})
        return kwargs
    
    def form_valid(self, form):
        User.objects.filter(id=self.kwargs['id_user']).update(is_active=True)
        return super(CodeVerificationView, self).form_valid(form)