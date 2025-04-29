from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Edition
from .forms import EditionForm

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
    form_class = EditionForm
    model = Edition

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class EditionUpdate(LoginRequiredMixin, UpdateView):
    form_class = EditionForm
    model = Edition
    
class EditionDelete(LoginRequiredMixin, DeleteView):
    model = Edition
    success_url = '/editions/'