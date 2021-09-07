from bees.forms import BeeForm
from django.shortcuts import render,redirect
from .models import Bee
from .forms import BeeForm
# Create your views here.

def index(request):
    bees = Bee.objects.all()
    context = {
        'bees':bees,
    }
    return render(request,'bees/index.html',context)

def create(request):
    if request.method=='POST':
        form = BeeForm(request.POST)
        if form.is_valid():
            bee = form.save()
            return redirect('bees:detail',bee.pk)
    else:
        form = BeeForm()
    context = {
        'form':form,
    }
    return render(request,'bees/create.html',context)

def update(request,pk):
    bee = Bee.objects.get(pk=pk)
    if request.method == 'POST':
        form = BeeForm(request.POST, instance=bee)
        if form.is_valid():
            bee = form.save()
            return redirect('bees:detail',bee.pk)
    else:
        form = BeeForm(instance=bee)
    context={
        'form':form,
        'bee':bee,
    }
    return render(request,'bees/update.html',context)

def detail(request,pk):
    bee = Bee.objects.get(pk=pk)
    context={
        'bee': bee,
    }
    return render(request,'bees/detail.html',context)

def kill(request,pk):
    bee = Bee.objects.get(pk=pk)
    if request.method == 'POST':
        bee.delete()
        return redirect('bees:index')
    return redirect('bees:detail',bee.pk)