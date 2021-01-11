from django.shortcuts import render

# Create your views here.
from django.urls import path
from django.views import generic
from django.http import HttpResponse, JsonResponse
from .models import Musician, Song


class master(generic.ListView):
    template_name = 'musicians/Musician_list.html'
    context_object_name = 'musicians'
    allow_empty = True

    def get_queryset(self):
        return Musician.objects.all()




def detail1(request, slug):
    filt = request.GET.get('key')
    s_list = Song.objects.filter(Musician_key=slug)
    context = {'songs' : s_list}
    return render(request, 'musicians/Songs_list.html', context)

def report(request):
    rep_list = Musician.objects.all()
    Songs_by_auth = Song.objects.all()
    context = {'musicians': rep_list, 'songs' : Songs_by_auth}
    return render(request, 'musicians/report.html', context)

from django.db.models import Count
def graph_chart(request):
    labels = []
    data = []
    queryset = Musician.objects.values('Musician_name').annotate(Song_count=Count('song'))
    for entry in queryset:
        labels.append(entry['Musician_name'])
        data.append(entry['Song_count'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
