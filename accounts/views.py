from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import View, CreateView


class HomeView(View):

    def get(self, request):
        return render(request, 'home/home.html')
    

class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login-view')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Usuário cadastrado com sucesso.')
        return response


class LoginView(View):

    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse_lazy('conversations-list-view'))
        return render(request, 'registration/login.html', {'form': form})


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('login-view')
