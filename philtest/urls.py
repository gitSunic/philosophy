from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'login/', views.login, name="login"),
	url(r'logout/', views.logout, name="logout"),
	url(r'add/', views.add, name="add"),
]