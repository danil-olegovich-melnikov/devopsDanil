from django.http import HttpRequest
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User


def hello(request: HttpRequest) -> HttpResponse:
    users = User.objects.all()
    return render(request, "index.html", {"users": users})