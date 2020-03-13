from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from rest_framework import viewsets

from .serializers import TutorialSerializer
from .models import Tutorial
# Create your views here.


class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all().order_by('tutorial_title')
    serializer_class = TutorialSerializer


def homepage(request):
    return render(request=request,
                  template_name='main/home.html',
                  context={"tutorials": Tutorial.objects.all})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("main:homepage")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="main/register.html",
                          context={"form": form})

    form = UserCreationForm
    return render(request=request,
                  template_name="main/register.html",
                  context={"form": form})
