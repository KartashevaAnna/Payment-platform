from django.http import HttpResponse


def index(request):
    return HttpResponse('Landing page')


def personal_page(request):
    return HttpResponse('Personal page')
