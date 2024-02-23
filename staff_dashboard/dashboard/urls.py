from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_staff', views.add_staff, name='add_staff'),
    path('delete_staff', views.delete_staff, name='delete_staff')
    path('edit_staff', views.edit_staff, name='edit_staff'),
    path('update_staff', views.update_staff, name='update_staff'),
]