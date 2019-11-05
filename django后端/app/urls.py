from app import views
from django.conf.urls import url

urlpatterns = [
    url(r'^login', views.login),
    url(r'^pyq', views.pyq),
    url(r'^review', views.review),
]