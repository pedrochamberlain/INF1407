from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, "index.html")


def register_new_account(request):
    if(request.method == 'POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            context = {
                'form': form
            }
            return render(request, 'register.html', context)
    else:
        form = UserCreationForm()
        context = {
            'form': form
        }
        return render(request, 'register.html', context)
