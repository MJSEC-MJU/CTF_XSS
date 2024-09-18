from django.shortcuts import render, redirect
from django.urls import reverse
def redirect_based_on_login(request):
    if request.user.is_authenticated:
        return redirect(reverse('board:post_list'))
    else:
        return redirect(reverse('user:login'))