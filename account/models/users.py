from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin



# Create your models here.
class MyUserManager(BaseUserManager):

    #create user model 
    def create_user(self,email,password,**extra_fields ):
        #creat user with email and password
        if not email:
            raise ValueError('please enter an email address')
        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
        

    def create_superuser(self, email,password, **extra_fields ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_verified", True)


        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, password, **extra_fields)
        
 

class User(AbstractBaseUser, PermissionsMixin):
    # castum user model for project 
    email = models.EmailField(max_length=50,unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    is_superuser= models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    first_name = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"

    objects = MyUserManager()

    def __self__(self):
        return self.email
    