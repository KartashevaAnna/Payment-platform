from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'handler/index.html'
    return render(request, template)


def personal_page(request):
    return HttpResponse('Personal page')
