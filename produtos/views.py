from django.shortcuts import render
from django.views.generic import DetailView


def detail(request):
    return render(request, 'produtos/detail.html')
