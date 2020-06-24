from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('query_usuario', views.query_usuario, name='query_usuario'),
    path('query2', views.query2, name='query2')

]
