from django.db import models
from django.contrib.auth.models import (
    AbstractUser,UserManager
)
import uuid
# Create your models here.
class UpdatedUserManager(UserManager):

    def _create_user(self, username, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """

        if not username:
            username = str(uuid.uuid4())
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(
            username=username, email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username,
                    email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            username, email, password, **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        username = None

        return self._create_user(
            username, email, password, **extra_fields
        )

class User(AbstractUser):
    full_name=models.CharField(max_length=250,null=True,blank=True)
    city= models.CharField(max_length=250,null=True,blank=True)
    state = models.CharField(max_length=250,null=True,blank=True)
    county = models.CharField(max_length=250,null=True,blank=True)
    vat_rate = models.DecimalField(max_digits=250, decimal_places=10,null=True,blank=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=1000)
    username = models.CharField(max_length=50, blank=True, null=True,)
    objects = UpdatedUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"
    

class Product(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=250,unique=True)
    retail_value = models.DecimalField(max_digits=250, decimal_places=10)
    screen_costs = models.DecimalField(max_digits=250, decimal_places=10)
    battery_costs = models.DecimalField(max_digits=250, decimal_places=10)
    screen_labor_costs: models.DecimalField(max_digits=250, decimal_places=10)
    battery_labor_costs=  models.DecimalField(max_digits=250, decimal_places=10) 
    memory_premium =models.DecimalField(max_digits=250, decimal_places=10)
    face_ID_Bdisc=  models.DecimalField(max_digits=250, decimal_places=10)
    touch_ID_Bdisc = models.DecimalField(max_digits=250, decimal_places=10)
    backcam_Bdisc = models.DecimalField(max_digits=250, decimal_places=10)
    margin = models.CharField(max_length=250,unique=True)



