from django.urls import path

from .views import master
from .views import detail

urlpatterns = [
    path('', master.as_view(), name="master"),
    path(r'(?P<pk>\d+)$', detail.as_view(), name='detail')
]