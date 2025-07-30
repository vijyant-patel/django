from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'myzipapp'

urlpatterns = [
    # path('zips/', views.list_zips, name='list_zips'),
    path('upload/', views.upload_zip, name='upload_zip'),
    path('download/<int:pk>/', views.download_zip, name='download_zip'),

    path('zips/', views.ZipView.as_view(), name='list_zips'),

    path('login/', auth_views.LoginView.as_view(template_name="myzipapp/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='myzipapp:login'), name='logout'),
]
