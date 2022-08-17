from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

app_name="basic_app"

urlpatterns = [
    path('', views.SchoolListView.as_view(),name='list'),
    # path('', views.SchoolListView.as_view(),name=),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(),name='detail'),
    url(r'^create/$', views.SchoolCreateView.as_view(),name='create'),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
    # url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='delete'),

]
