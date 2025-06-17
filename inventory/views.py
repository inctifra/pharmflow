from django.shortcuts import render, redirect, get_object_or_404
from .models import Drug, Stock
from .forms import DrugForm, StockForm, DispenseForm

def index(request):
    stocks = Stock.objects.select_related('drug').all()
    return render(request, 'inventory/index.html', {'stocks': stocks})

def add_drug(request):
    if request.method == 'POST':
        form = DrugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DrugForm()
    return render(request, 'inventory/form.html', {'form': form, 'title': 'Add Drug'})

def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StockForm()
    return render(request, 'inventory/form.html', {'form': form, 'title': 'Add Stock'})

def delete_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    stock.delete()
    return redirect('index')

def edit_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StockForm(instance=stock)
    return render(request, 'inventory/form.html', {'form': form, 'title': 'Edit Stock'})

def dispense_drug(request):
    if request.method == 'POST':
        form = DispenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DispenseForm()
    return render(request, 'inventory/form.html', {'form': form, 'title': 'Dispense Drug'})


def drug_detail_view(request, slug, pk):
    drug = get_object_or_404(Drug, slug=slug, pk=pk)
    context = {
        "drug": drug,
        "stocks": drug.stocks()
    }
    return render(request, "drug/index.html", context)