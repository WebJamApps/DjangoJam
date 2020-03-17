from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from rest_framework import viewsets
from datatableview.views import DatatableView
from .serializers import TutorialSerializer
from .models import Tutorial
from .forms import PostForm
# Create your views here.


class ZeroConfigurationDatatableView(DatatableView):
    model = Tutorial


class TutorialViewSet(viewsets.ModelViewSet):
    queryset = Tutorial.objects.all().order_by('tutorial_title')
    serializer_class = TutorialSerializer


def tutorial_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/table', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'main/tutorial_edit.html', {'form': form})


def tutorial_edit(request, pk):
    post = get_object_or_404(Tutorial, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/table', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'main/tutorial_edit.html', {'form': form})


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
