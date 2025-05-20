from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Car, Client, Contract, Manager, Sku
from .forms import ClientForm, ContractForm


# Главная страница
def home(request):
    return render(request, 'index.html')


# Список автомобилей
class CarListView(ListView):
    model = Car
    template_name = 'cars_list.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.filter(count__gt=0)


# Детали автомобиля
class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'


# Список менеджеров
class ManagerListView(ListView):
    model = Manager
    template_name = 'managers_list.html'
    context_object_name = 'managers'
    queryset = Manager.objects.all().order_by('-sold_cars')


# Список договоров
class ContractListView(ListView):
    model = Contract
    template_name = 'contracts_list.html'
    context_object_name = 'contracts'
    queryset = Contract.objects.all().order_by('-date')


# Создание клиента
class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('home')


# Оформление договора
def create_contract(request, sku_id):
    sku = get_object_or_404(Sku, pk=sku_id)

    if request.method == 'POST':
        form = ContractForm(request.POST)
        if form.is_valid():
            # Получаем или создаем клиента
            client, created = Client.objects.get_or_create(
                email=form.cleaned_data['email'],
                defaults={
                    'name': form.cleaned_data['name'],
                    'phone': form.cleaned_data['phone']
                }
            )

            # Создаем договор
            contract = Contract(
                client=client,
                manager=Manager.objects.order_by('?').first(),  # случайный менеджер
                sku=sku,
                payment_method=form.cleaned_data['payment_method'],
                date=timezone.now()
            )
            contract.save()

            # Уменьшаем количество доступных авто
            car = sku.car
            car.count -= 1
            car.save()

            # Увеличиваем счетчик продаж менеджера
            contract.manager.sold_cars += 1
            contract.manager.save()

            return redirect('contracts_list')
    else:
        initial_data = {}
        if request.user.is_authenticated and hasattr(request.user, 'client'):
            initial_data = {
                'name': request.user.client.name,
                'phone': request.user.client.phone,
                'email': request.user.client.email
            }
        form = ContractForm(initial=initial_data)

    return render(request, 'create_contract.html', {
        'form': form,
        'sku': sku
    })