from django.urls import path

from printpagge import views

urlpatterns = [
    path('',views.hai,name='hai')]
