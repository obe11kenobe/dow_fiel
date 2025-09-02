from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Data
from .forms import DataCreate

def index(request): # главная страница
    transfer = Data.objects.all()[:10] # обращаемся к модели Data через objects.all, [:10] делаем срез (берем только 10 записей)
    total = Data.objects.count() # считаем сколько всего записей, метод count делает запрос и выводит сколько всего записей
    return render (request, 'main/index.html', {
        'transfer': transfer,
        'total' : total
    })

def data_list(request): # список всех записей
    transfer_list = Data.objects.all() # обращаемся к модели Data через objects.all
    paginator = Paginator(transfer_list, 20) # создаем пагинатор, в скобках указываем список записей и количество записей на странице
    page = request.GET.get('page')
    transfer = paginator.get_page(page)
    return render(request, 'main/data_list.html', {'transfer': transfer})

def data_detail(request, pk): # детальная информация для записи
    transfer = get_object_or_404(Data, pk=pk)
    return render(request, 'main/data_detail.html', {'transfer': transfer})

def data_create(request): # создание новой записи
    if request.method == 'POST':
        form = DataCreate(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись успешно создана!')
        else:
            messages.error(request, 'Ошибка при создании записи!')
    else:
        form = DataCreate()
    return render(request, 'main/data_create.html', {'form': form})

def data_update(request, pk): # редактирование записи
    transfer = get_object_or_404(Data, pk=pk)
    if request.method == 'POST':
        form = DataCreate(request.POST, instance=transfer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Запись успешно обновлена!')
            return redirect('data_list')
        else:
            messages.error(request, 'Ошибка при редактировании записи!')
    else:
        form = DataCreate(instance=transfer)
    return render(request, 'main/data_update.html', {'form': form})

def data_delete(request, pk): # удаление записи
    transfer = get_object_or_404(Data, pk=pk)
    if request.method == 'POST':
        transfer.delete()
        messages.success(request, 'Запись успешно удалена!')
        return redirect('data_list')
    return render(request,'main/data_delete.html', {'transfer': transfer})







