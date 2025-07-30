from django.shortcuts import render, redirect, get_object_or_404
from .models import Shop
from django.contrib.auth.decorators import login_required
from .forms import ShopForm
from rest_framework import viewsets
from .serializers import ShopSerializer
app_name = "interview_01"

@login_required
def Home(request):
    shops = Shop.objects.all()
    return render(request, 'interview_01/home.html', {'shops': shops})

@login_required
def AddShop(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('interview_01:Home')
    else:
        form = ShopForm()
    return render(request, 'interview_01/addShop.html', {'form':form})

@login_required
def EditShop(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('interview_01:Home')
    else:
        form = ShopForm(instance=shop)
    return render(request, 'interview_01/addShop.html', {'form':form})

@login_required
def DeleteShop(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    shop.delete()
    return redirect('interview_01:Home')

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


