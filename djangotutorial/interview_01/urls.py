from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ShopViewSet
app_name = 'interview_01'

router = DefaultRouter()
router.register('shops', ShopViewSet)

urlpatterns = [
    path('', views.Home, name='Home'),
    path('add/', views.AddShop, name='AddShop'),
    path('edit/<int:shop_id>/', views.EditShop, name='EditShop'),
    path('delete/<int:shop_id>/', views.DeleteShop, name='DeleteShop'),
    path('api/', include(router.urls)),

]