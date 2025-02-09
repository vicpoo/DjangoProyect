from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('batallas/', views.batallas, name='batallas'),
    path('batalla/<int:id>/', views.detalle_batalla, name='detalle_batalla'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
]