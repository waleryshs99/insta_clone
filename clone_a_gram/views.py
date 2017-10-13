from django.contrib.auth.models import User
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView

from clone_a_gram.models import Photo


class PhotoDetailsView(DetailView):
    model = Photo


class PhotoCreateView(CreateView):
    model = Photo
    succes_url = ''
    fields = "__all__"


class UserDetailsView(DetailView):
    model = User


class UserModifyView(UpdateView):
    model = User
    success_url = ''
    fields = '__all__'
