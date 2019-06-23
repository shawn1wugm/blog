from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls.base import reverse

# Create your views here.

def main(request):
    '''
    Show 'Hello world!' in the main page
    '''
    context = {'like':'templates 很棒  需要多練習'}
    return render(request, 'main/main.html', context)
def about(request):
    '''
    Show 'about' in the main page
    '''
    return render(request, 'main/about.html') 

def admin_required(func):
    def auth(request, *args, **kwargs):
        if not request.user.is_superuser:
            messages.error(request, '請以管理者身份登入')
            return redirect(reverse('account:login') + '?next=' + request.get_full_path())
        return func(request, *args, **kwargs)
    return auth

