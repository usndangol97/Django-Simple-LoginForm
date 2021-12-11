from django.urls import path
from . import views

app_name="login_app"

urlpatterns = [
    #/home/
    path('register/', views.index, name='register'),
    path('login/', views.login_page, name='login')

]