
# Create your models here.
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#getting user object 
User =get_user_model()

class posttest(models.Model):
    titel = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    conted_view = models.IntegerField(default=0)
    category = models.ManyToManyField(Category)
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
    


