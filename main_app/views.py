from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Edition

def home(request):
    return render(request, 'home.html')

class SignIn(LoginView):
    template_name = 'main_app/signin.html'

def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('edition_index')
        else:
            error_message = 'Invalid sign up please try again'
    form = UserCreationForm()
    context = {'form':form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def about(request):
    return render(request, 'about.html')

class EditionsList(LoginRequiredMixin, ListView):
    model = Edition
    def get_queryset(self):
        return Edition.objects.filter(user=self.request.user)
    

class  EditionDetail(LoginRequiredMixin, DetailView):
    model = Edition

class EditionCreate(LoginRequiredMixin, CreateView):
    model = Edition
    fields = ['edition_name', 'year', 'edition_size', 'paper_size', 'plate_size', 'technique', 'margin_upper', 'margin_lower', 'margin_sides', 'available_prints', 'status', 'edition_type']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)