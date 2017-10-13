 from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.generic.edit import FormView, CreateView, UpdateView, DeleteView
from .models import Photo, Comment, Like


class PhotoDetailsView(DetailView):
    model = Photo


class PhotoCreateView(CreateView):
    model = Photo
    succes_url = ''
    fields = "__all__"

class MainView(FormView):
    
    template_name = 'insta_clone.html'
    form_class = ContactForm
     
      
class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'insta_clone.html/login', {'form':form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data[ 'password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('U {} R Logged in'.format(user.username))
            else:
                return HttpResponse('Incorrect login data')
            
class UserCreateView(CreateView):
    model = User
    form_class = CreateView
    success_url = 'insta_clone/login.html'
    

class UserDetailsView(DetailView):
    model = User


class UserModifyView(UpdateView):
    model = User
    success_url = ''
    fields = '__all__'
