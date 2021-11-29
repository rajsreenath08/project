from django.urls import path
from . import views
app_name= 'app12'
urlpatterns=[
    path('',views.index),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('update/<int:id>',views.update,name='update'),
    path('change_password/<int:id>',views.change_password,name='change_password'),
    path('logout',views.logout,name='logout'),
]