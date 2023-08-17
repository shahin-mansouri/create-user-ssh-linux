from django.shortcuts import render, redirect
from django .urls import reverse
from django.views.generic import TemplateView
# from django.contrib.auth.decorators import login_required
from .models import Ssh
from .forms import CreateSshForm
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
    try:
        do_it = change_user_passwd(username, password)
    except TypeError:
        return redirect(reverse('home'))
    if not do_it:
        context = dict()
        context["sshs"] = sorted(Ssh.objects.all(), key=lambda x: x.ssh_name)
        context['success'] = 'Unchanged password. Try again!'
        context['pk'] = False
        return render(request, './home/home.html', context)

    ssh.password = password
    ssh.pub_date = exp
    ssh.save()
    context = dict()
    context["sshs"] = sorted(Ssh.objects.all(), key=lambda x: x.ssh_name)
    context['success'] = f'Successfully. Password of {username} changed.'
    context['pk'] = False
    return render(request, './home/home.html', context)


# useing screen for keep running service. dont forget
# screen -r for see running

from django.contrib import messages 


def create(request):
    context = dict()
    context['form'] = CreateSshForm()
    context["sshs"] = sorted(Ssh.objects.all(), key=lambda x: x.ssh_name)
    if request.method == 'POST':
        form = CreateSshForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['ssh_name']
            password = form.cleaned_data['password']
            pub_date = form.cleaned_data['pub_date']
            if username in map(lambda x: x.ssh_name, Ssh.objects.all()):
                context['errors'] = f'{username} there exist!'
                return render(request, './home/create_ssh.html', context)
            
            os.system(f"echo {password} | adduser --gecos \"\" {username}")
            os.system(f"usermod -s usr/sbin/nologin {username}")
            change_user_passwd(username, password)
            newUser = Ssh()
            newUser.ssh_name = username
            newUser.password = password
            newUser.pub_date = pub_date
            newUser.save()
            return render(request, './home/home.html', {'success': f'{username} has been successfully created',
                                                        'sshs': sorted(Ssh.objects.all(), key=lambda x: x.ssh_name)})
        else:
            context['errors'] = form.errors.as_text
            return render(request, './home/create_ssh.html', context)
    return render(request, './home/create_ssh.html', context)
