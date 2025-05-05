from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Edition, Note, Ink, Paper
from .forms import EditionForm, NoteForm
from cloudinary.uploader import destroy

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
        editions = Edition.objects.filter(user=self.request.user)
        return editions.exclude(status = 'a')

@login_required
def archive_list(request):
    editions = Edition.objects.filter(user=request.user)
    archive = editions.filter(status='a')
    return render(request, 'editions/archive_list.html', {
        'archive' : archive
    })

class  EditionDetail(LoginRequiredMixin, DetailView):
    model = Edition

    def get_context_data(self, **kwargs):
        edition = self.get_object()
        inks_available = Ink.objects.exclude(id__in = edition.ink.all().values_list('id'))
        paper_available = Paper.objects.exclude(id__in = edition.paper.all(). values_list('id'))
        context = super().get_context_data(**kwargs)
        context['ink_list'] = inks_available
        context['paper_list'] = paper_available
        return context

class EditionCreate(LoginRequiredMixin, CreateView):
    form_class = EditionForm
    model = Edition

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class EditionUpdate(LoginRequiredMixin, UpdateView):
    form_class = EditionForm
    model = Edition

    def form_valid(self, form):
        current_image = Edition.objects.get(id=self.get_object().pk).image
        new_image = self.request.FILES.get('image')

        if current_image and new_image:
            public_id = current_image.public_id
            destroy(public_id)
        return super().form_valid(form)
    
    
class EditionDelete(LoginRequiredMixin, DeleteView):
    model = Edition
    success_url = '/editions/'

class NoteCreate(LoginRequiredMixin, CreateView):
    form_class = NoteForm
    model = Note

    def form_valid(self, form):
        new_note = form.save(commit=False)
        new_note.edition_id = self.kwargs['edition_id']
        new_note.save()
        return redirect('edition_detail', self.kwargs['edition_id'])

class NoteDelete(LoginRequiredMixin, DeleteView):
    model = Note

    def get_success_url(self):
        current_edition = self.get_object().edition.id

        if current_edition:
            return  reverse('edition_detail', kwargs={'pk':current_edition})
        else:
            return redirect('edition_index')

class NoteUpdate(LoginRequiredMixin, UpdateView):
    form_class = NoteForm
    model = Note

    def get_object(self, queryset = None):
        return Note.objects.get(pk = self.kwargs['pk'])

class InkList(LoginRequiredMixin, ListView):
    model = Ink

    def get_queryset(self):
        return Ink.objects.filter(user=self.request.user)

class InkCreate(LoginRequiredMixin, CreateView):
    model = Ink
    fields = ['ink_name', 'ink_color', 'ink_type', 'ink_based', 'ink_qty']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class InkDelete(LoginRequiredMixin, DeleteView):
    model = Ink
    success_url = '/inks/'

class InkUpdate(LoginRequiredMixin, UpdateView):
    model = Ink
    fields = ['ink_name', 'ink_color', 'ink_type', 'ink_based', 'ink_qty']

@login_required
def associate_ink(request, edition_id, ink_id):
    Edition.objects.get(id=edition_id).ink.add(ink_id)
    return redirect('edition_detail', edition_id)
    
@login_required
def remove_ink(request, edition_id, ink_id):
    Edition.objects.get(id=edition_id).ink.remove(ink_id)
    return redirect('edition_detail', edition_id)

class PaperList(LoginRequiredMixin, ListView):
    model = Paper

    def get_queryset(self):
        return Paper.objects.filter(user=self.request.user)

class PaperCreate(LoginRequiredMixin, CreateView):
    model = Paper
    fields = ['paper_name', 'paper_color', 'paper_size', 'paper_weight', 'paper_qty']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class PaperDelete(LoginRequiredMixin, DeleteView):
    model = Paper
    success_url = '/papers/'

class PaperUpdate(LoginRequiredMixin, UpdateView):
    model = Paper
    fields = ['paper_name', 'paper_color', 'paper_size', 'paper_weight', 'paper_qty']

@login_required
def associate_paper(request, edition_id, paper_id):
    Edition.objects.get(id=edition_id).paper.add(paper_id)
    return redirect('edition_detail', edition_id)

@login_required
def remove_paper(request, edition_id, paper_id):
    Edition.objects.get(id=edition_id).paper.remove(paper_id)
    return redirect('edition_detail', edition_id)