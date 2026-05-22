from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# Custom user manager to handle user creation and superuser creation
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None): # Method to create a regular user (regular user does not have admin privileges)
        if not email:
            raise ValueError('User must have an email address')
        
        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email), # Normalize the email address by lowercasing the domain part
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, first_name, last_name, email, username, password): # Method to create a superuser (superuser has admin privileges)
        user=self.create_user(
            email = self.normalize_email(email),
            username = username,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_active = True
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Custom user model that extends AbstractBaseUser to define the fields and behavior of the user in our application
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100,unique=True)
    phone_number = models.CharField(max_length=50)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'  # Use email as the unique identifier for authentication
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] # Fields that are required when creating a superuser

    objects = MyAccountManager() # Specify the custom user manager for this model

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):  # Check if the user has a specific permission
        return self.is_admin

    def has_module_perms(self, add_lable): # check if the user has permissions to view the app 'add_lable'
        return True

