from django.contrib import admin
from .models import Ssh

@admin.register(Ssh)
class SshAdmin(admin.ModelAdmin):
    list_display = ['ssh_name', 'password', 'pub_date']

