from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import Group, User
from django.views import View
from django.core.cache import cache
from app_shops.models import History, Shops
from app_users.forms import RegisterForm, TopUpYourBalancetForm, AboutMeUserForm
from app_users.models import Profile


class AnotherLoginView(LoginView):
    template_name = 'users/login.html'


class AnotherLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = '/'


def another_register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})


def account_view(request, user_id):
    profile = Profile.objects.get(user_id=user_id)
    history_cache_key = 'history:{}'.format(profile)
    history = History.objects.filter(user_id=user_id)
    for product in history:
            print(product.date_of_purchase)
    cache.get_or_set(history_cache_key, history, 30*30)
    shops = Shops.objects.first()
    top_up_your_balancet_form = TopUpYourBalancetForm()
    return render(request, 'users/account.html', {'profile': profile,
                                                  'user_id': user_id,
                                                  'history': history,
                                                  'marketplace': shops,
                                                  'top_up_your_balancet_form': top_up_your_balancet_form
                                                  }
                  )


def top_up_your_balancet_view(request, user_id):
    if request.method == 'POST':
        form = TopUpYourBalancetForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.get(user_id=user_id)
            amount_of_money = form.cleaned_data.get('amount_of_money')
            profile.balance = profile.balance + amount_of_money
            profile.save(update_fields=['balance'])
            return HttpResponseRedirect(f'/users/{user_id}')


