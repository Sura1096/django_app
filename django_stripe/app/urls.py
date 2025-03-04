from django.urls import path

from .views import buy_item, item_detail

urlpatterns = [
    path('item/<int:id>/', item_detail, name='item_detail'),
    path('buy/<int:id>/', buy_item, name='buy_item'),
]