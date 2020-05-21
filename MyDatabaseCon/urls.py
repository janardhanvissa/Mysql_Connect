
from django.urls import path
from . import views

urlpatterns = [

	path('', views.hello),
	path('MyDatabaseCon/ece/', views.ece),
	path('MyDatabaseCon/cse/', views.cse),
	path('MyDatabaseCon/eee/', views.eee),
]
