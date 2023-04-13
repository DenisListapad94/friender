from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import *
import datetime

# friends = {
#     "Max": [34, "max@mail.ru"],
#     "Grigory": [32, "grigory@mail.ru"],
#     "Anna": [29, "anna@mail.ru"],
#     'Pedro': [21, "pedro@mail.ru"],
#     'Kate': [32, "kate@mail.ru"]
# }
# establishments = ['Butter bro', 'Terra', 'Golden Cafe', 'Pancakes', 'Depo']


# функция представления (вьюшка)

def main_page(request):
    return render(request, 'main.html')


def place_arrangments(request):
    context = {
        "establishments": Establishments.objects.all(),
    }
    return render(request, 'establishments.html', context=context)

def all_friends(request):
    context = {
        # "friends": Users.objects.filter(age__gte=28).order_by('name')[:100],
        # "friends": Users.objects.filter(name = 'Suzan')[:100],
        "friends": Users.objects.filter(sex='f').order_by('-age')[:100],
        # "friends": Users.objects.filter(age__gte=28).order_by('-sex')[:100],
    }
    return render(request, "friends.html", context=context)

def static_url(request):
    return render(request, "static_example.html")


