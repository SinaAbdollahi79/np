
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class posttest(models.Model):
    titel = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    conted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return "{} - {}".format(self.titel, self.id)
    
    def get_absolute_url(self):
        return reverse('blog:blog-single', kwargs={'pid': self.id})