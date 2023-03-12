from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, FormView

from form import UserLoginForm,UserRegisterForm

# Create your views here.


class LoginView(FormView):
    template_name = 'signUpPatient.html'
    form_class = UserLoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        name  = data['name']
        email = data['email']
        password = data['password']
        user = authenticate(username=name,email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponseRedirect(reverse('error'))
        return HttpResponseRedirect(reverse('error'))

class UserRegisterView(CreateView):
    template_name = 'sign_up.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')


class DoctorLoginView(FormView):
    template_name = 'loginDoctor.html'
    form_class = UserLoginForm

    def form_valid(self, form):
        data = form.cleaned_data
        name  = data['name']
        email = data['email']
        password = data['password']
        user = authenticate(username=name,email=email, password=password)
        if user is not None:
            if user.is_active:
                login(self.request, user)
                return redirect('index')
            else:
                return HttpResponseRedirect(reverse('error'))
        return HttpResponseRedirect(reverse('error'))

class DoctorRegisterView(CreateView):
    template_name = 'signUpDoctor.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('index')
