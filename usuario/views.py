from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView, UpdateView
from .forms import FormularioRegistroUsuario
from django.urls import reverse_lazy


class RegistroUsuario(SuccessMessageMixin, CreateView):
    form_class = FormularioRegistroUsuario
    template_name = "usuarios/registro.html"
    success_message = "Usuario creado correctamente. Por favor inicica sesion."
    success_url = reverse_lazy("login") 
    success_message = "Usuario creado correctamente. Por favor inicica sesion."

class LoginUsuario(LoginView):
    template_name = "usuarios/login.html"

class LogoutUsuario(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy("home")
