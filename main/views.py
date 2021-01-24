from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. This is a homepage.")

def vacancies(request):
    return render(request, 'labsite/vacancies.html', {})
