from django.views import View
from django.views.generic import DetailView, CreateView

from clone_a_gram.models import Photo


class PhotoDetailsView(DetailView):
    model = Photo


class PhotoCreateView(CreateView):
    model = Photo
    succes_url = ''
    fields = "__all__"
