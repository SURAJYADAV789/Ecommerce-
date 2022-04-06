
from django.contrib.auth.models import Group
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.
GENDER_CHOICES = [('Male','Male'),('Female','Female'),('Others','Others')]

class MyUserManager(BaseUserManager):
    
    def _create_user(self,contact,password,**extrafields):
        
        if not contact:
            raise ValueError('Mobile Number is required')
        user = self.model(contact=contact,password=password,**extrafields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # def create_user(self,contact,password,**extrafields):
        
    #     extrafields.setdefault('is_superuser',False)
    #     extrafields.setdefault('role','user')
        
    #     user = self._create_user(contact,password,**extrafields)
    #     return user
    
    # def create_superuser(self,contact,password,**extrafields):
        
    #     extrafields.setdefault('is_superuser',True)
    #     extrafields.setdefault('role','superuser')
        
    #     user = self._create_user(contact,password,**extrafields)
    #     return user

class MyUser(AbstractBaseUser):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    contact=models.BigIntegerField(unique=True)
    email=models.EmailField(unique=True)
    groups=models.ManyToManyField(Group)
    address=models.TextField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    objects=MyUserManager()
    
    USERNAME_FIELD='contact'


    REQUIRED_FIELDS=[]


    
    