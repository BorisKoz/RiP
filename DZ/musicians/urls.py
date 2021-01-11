from django.urls import path

from . import views

urlpatterns = [
    path('', views.master.as_view(), name='master'),
    path('?key=<slug:slug>/', views.detail1, name='songs_list'),
    path('report/', views.report, name='report'),
    path('graph-data/', views.graph_chart, name='graph-data')
    ]
