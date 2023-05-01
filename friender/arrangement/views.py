from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import *
from .forms import *
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

        "friends": Users.objects.all().prefetch_related("hobbies_set", "userrating_set")
        # "friends": Users.objects.filter(age__gte=28).order_by('name')[:100],
        # "friends": Users.objects.filter(name = 'Suzan')[:100],
        # "friends": Users.objects.filter(sex='f').order_by('-age')[:100],
        # "friends": Users.objects.filter(age__gte=28).order_by('-sex')[:100],
    }
    return render(request, "friends.html", context=context)


def static_url(request):
    return render(request, "static_example.html")


def user_rating(request):
    context = {
        "ratings": UserRating.objects.all().select_related('user')
    }
    return render(request, "userrating.html", context=context)


def user_form_rating(request, **kwargs):
    user_id = int(kwargs['id'])
    context = {}
    if request.method == "POST":
        form = RatingUserForm(request.POST)
        context["form"] = form
        if form.is_valid():
            UserRating.objects.create(
                user_id=user_id,
                rating=request.POST['rating'],
                description=request.POST['description']
            )
            return redirect("friends")
    else:
        form = RatingUserForm()
        context["form"] = form
    # context = {
    #     # "user": Users.objects.get(id=user_id)
    #     "form" : form
    # }
    return render(request, "user_form_rating.html", context=context)

def create_user(request):
    context = {}
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        context["form"] = form
        if form.is_valid():
            form.save()
            return redirect("friends")
    else:
        form = CreateUserForm()
        context["form"] = form
    # context = {
    #     # "user": Users.objects.get(id=user_id)
    #     "form" : form
    # }
    return render(request, "create_user_form.html", context=context)