#Main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('batallas/', views.batallas, name='batallas'),
    path('batalla/<int:id>/', views.detalle_batalla, name='detalle_batalla'),
    path('batalla/nueva/', views.nueva_batalla, name='nueva_batalla'),
    path('batalla/editar/<int:id>/', views.editar_batalla, name='editar_batalla'),
    path('batalla/eliminar/<int:id>/', views.eliminar_batalla, name='eliminar_batalla'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('about/', views.about, name='about'),
]