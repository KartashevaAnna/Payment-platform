from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'handler/index.html'
    title = 'Payment handler'
    context = {
        'title': title,
        'text': 'Welcome to our platform!'
               }
    return render(request, template, context)


def personal_page(request):
    return HttpResponse('Personal page')


def transactions(request):
    template = 'handler/transactions.html'
    title = "Transactions"
    context = {
        'title': title,
        'text': 'Here are your transactions'
    }
    return render(request, template, context)
