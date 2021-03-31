from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import auth, messages
from .forms import LoginForm


@login_required
def home(request):
    return render(request, "core/main.html")


def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            f = LoginForm(request.POST)
            if f.is_valid():
                # user = User.objects.filter(email=f.cleaned_data['email'])
                user = get_user_model()
                user = user.objects.filter(email=f.cleaned_data['email'])
                if user:
                    user = auth.authenticate(
                        username=user[0].email,
                        password=f.cleaned_data['password'],
                    )
                    if user:
                        auth.login(request, user)
                        return redirect(request.GET.get('next') or 'home')

                messages.add_message(request, messages.INFO, 'Invalid email/password.')
                return render(request, 'core/login.html', {'form': f})
        else:
            f = LoginForm()

    return render(request, 'core/login.html', {'form': f})


def logout(request):
    auth.logout(request)
    return redirect('login')
