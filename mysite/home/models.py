from django.db import models
from django.urls import reverse

class Ssh(models.Model):
    ssh_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    pub_date = models.DateField()
    

    # class Meta:
    #     verbose_name = _("Ssh")
    #     verbose_name_plural = _("Sshs")

    def __str__(self):
        return self.ssh_name

    def get_absolute_url(self):
        return reverse("Ssh_detail", kwargs={"pk": self.pk})

