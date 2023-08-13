from django.shortcuts import render, redirect
from django.views.generic import TemplateView
# from django.contrib.auth.decorators import login_required
from .models import Ssh


# @login_required
# def home(request):
#     # This view will only be accessible to logged in users.
#     return render(request, './home/home.html')

class HomeView(TemplateView):
    template_name = './home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sshs"] = Ssh.objects.all()
        try:
            context['pk'] = True
            ssh = Ssh.objects.get(pk=kwargs['pk'])
            context["ssh"] = ssh
            context['id'] = ssh
        except KeyError:
            context['pk'] = False
 
        return context
    

def change(request, pk):
    password = request.POST.get('password')
    exp      = request.POST.get('exp')
    ssh      = Ssh.objects.get(pk=pk)
    ssh.password = password
    ssh.pub_date = exp
    ssh.save()

    context = dict()
    context["sshs"] = Ssh.objects.all()
    context['success'] = 'successfully Changes!'
    context['pk'] = False

    return render(request, './home/home.html', context)



