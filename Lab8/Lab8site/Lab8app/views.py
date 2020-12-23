from django.shortcuts import render
from django.http import HttpResponse, request
from django.views import generic


from .models import Song
class master(generic.ListView):
    template_name = 'Lab8app/master.html'
    context_object_name = 'Songs'
    allow_empty = True
    def get_queryset(self):
        return Song.objects.all()

class detail(generic.DetailView):
    model = Song
    template_name = 'Lab8app/detail.html'



# Create your views here.
