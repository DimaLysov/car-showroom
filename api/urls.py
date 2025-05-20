from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cars/', views.CarListView.as_view(), name='cars_list'),
    path('cars/<int:pk>/', views.CarDetailView.as_view(), name='car_detail'),
    path('managers/', views.ManagerListView.as_view(), name='managers_list'),
    path('contracts/', views.ContractListView.as_view(), name='contracts_list'),
    path('client/create/', views.ClientCreateView.as_view(), name='create_client'),
    path('contract/create/<int:sku_id>/', views.create_contract, name='create_contract'),
]