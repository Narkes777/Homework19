from django.shortcuts import render, get_object_or_404
from .models import Car

# Create your views here.

def model_list(request):
    models = Car.objects.all()
    return render(request, 'model_list.html', {'models': models})

def model_detail(request, pk):
    model = get_object_or_404(Car, pk=pk)
    return render(request, 'model_detail.html', {'model': model})
