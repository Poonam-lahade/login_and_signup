from django.shortcuts import render

# Create your views here.
# authentication/views.py

from . import forms


def login_page(request):
    form = forms.LoginForm()
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'authentication/login.html', context={'form': form})