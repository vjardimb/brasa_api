from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    age= models.PositiveBigIntegerField()
    email = models.EmailField(unique=True)
    password=models.CharField(max_length=200)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'age']

    objects = UserManager()

    def __str__(self):
        return self.email

'''class User(AbstractUser):
    #django ja tem fist_name, last_name, email e password
  username= None
    age= models.PositiveBigIntegerField()
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    #campos que eu quero na minha database
    REQUIRED_FIELDS = ['first_name', 'last_name', 'age','username'] 
    USERNAME_FIELD = 'email'

    def create_superuser(self, email, password, **extra_fields):
        user=self._create_user(email, password, **extra_fields)
        user.save(using=self._db)
        return user
'''

   

