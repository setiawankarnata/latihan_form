from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        user_name = request.POST['username']
        print(user_name)
        return HttpResponse("Masuk ke index.")
    return render(request, 'explore/index.html', {'nilai': 3})


def validate_index(request):
    if request.method == "POST":
        user_name = request.POST['username']
        print(f"{user_name} - dari validate_index")
    return HttpResponse("Masuk ke validate_index")


def cek_param(request, ctr):
    if request.method == "POST":
        user_name = request.POST['username']
        print(f"{user_name} - dari cek_param with {ctr}")
    return HttpResponse("Masuk ke cek_param")
