from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# from django.contrib.auth.decorators import login_required
from .models import Ssh
import os


# @login_required
# def home(request):
#     # This view will only be accessible to logged in users.
#     return render(request, './home/home.html')

class HomeView(TemplateView):
    template_name = './home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sshs"] = sorted(Ssh.objects.all(), key=lambda x: x.ssh_name)
        try:
            context['pk'] = True
            ssh = Ssh.objects.get(pk=kwargs['pk'])
            context["ssh"] = ssh
            context['id'] = ssh
        except KeyError:
            context['pk'] = False
 
        return context
    

def change_user_passwd(username, password):
    import subprocess, crypt, random
    login = username
    
    ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    salt = ''.join(random.choice(ALPHABET) for i in range(8))
    shadow_password = crypt.crypt(password,'$1$'+salt+'$')
    r = subprocess.call(('usermod', '-p', shadow_password, login))

    if r != 0:
        print('Error changing password for ' + login)
        return False
    return True



def change(request, pk):
    password = request.POST.get('password')
    exp      = request.POST.get('exp')
    ssh      = Ssh.objects.get(pk=pk)
    username = ssh.ssh_name
    do_it = change_user_passwd(username, password)
    if not do_it:
        context = dict()
        context["sshs"] = sorted(Ssh.objects.all(), key=lambda x: x.ssh_name)
        context['success'] = 'unchanged password. Try again!'
        context['pk'] = False
        return render(request, './home/home.html', context)

    ssh.password = password
    ssh.pub_date = exp
    ssh.save()
    context = dict()
    context["sshs"] = sorted(Ssh.objects.all(), key=lambda x: x.ssh_name)
    context['success'] = f'successfully. Password of {username} changed!'
    context['pk'] = False
    return render(request, './home/home.html', context)


# useing screen for keep running service. dont forget
# screen -r for see running
