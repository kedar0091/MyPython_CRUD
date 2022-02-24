from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_emp/',views.add_data),
    path('get_emp/',views.get_data),
    path('getAll_emp/',views.getall_data),
    path('update_emp/',views.update_data),
    path('delete_emp/',views.delete_data),
    path('login/',views.login)
]