from django.shortcuts import render,redirect
from .forms import SignUpForm
from . import models


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    else:
        form = SignUpForm()
    return render(request, 'singup.html', {'form': form})
