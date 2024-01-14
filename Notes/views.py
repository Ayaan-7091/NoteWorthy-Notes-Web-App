from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Note

from django.views.generic import CreateView,UpdateView,DeleteView,ListView

from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.views import LoginView,LogoutView

from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class LoginInterfaceView(LoginView):
    template_name = 'login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'logout.html'

class SignupView(CreateView):
    template_name='signup.html'
    form_class = UserCreationForm
    success_url = "/"

class NotesCreateView(LoginRequiredMixin,CreateView):
    login_url="/"
    model = Note
    fields = ['title','content']
    success_url="/notes/"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())       
    

class NotesUpdateView(LoginRequiredMixin,UpdateView):
    login_url="/"

    model = Note
    fields = ['title','content']
    success_url="/notes/"

class NotesDeleteView(LoginRequiredMixin,DeleteView):
    login_url="/"

    model = Note
    success_url="/notes/"
    template_name = "Notes/note_delete.html"

class NotesListView(LoginRequiredMixin,ListView):
    model = Note
    template_name="notes.html"
    context_object_name="note"

    def get_queryset(self) :
        return self.request.user.notes.all()



def home(request): 
    return render(request,'home.html',{})




@login_required(login_url='/')
def details(request,pk):
    note = Note.objects.get(pk=pk)

    return render(request,'details.html',{'note': note})