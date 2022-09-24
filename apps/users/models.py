from django.db import models
from django.db.models.signals import post_save
from simple_history.models import HistoricalRecords
# Create your models here.
from apps.base.models import BaseModel
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
#import stripe

MEMBERSHIP_CHOICES = (
    ("Enterprice","ent"),
    ("Professional","pro"),
    ("Free","free"),
)

class UserManager(BaseUserManager):
    def _create_user(self, username, email, name,last_name, password, is_staff, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_staff = is_staff,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, False, False, **extra_fields)

    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    name = models.CharField('Nombres', max_length = 255, blank = True, null = True)
    last_name = models.CharField('Apellidos', max_length = 255, blank = True, null = True)
    image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255, null=True, blank = True)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    historical = HistoricalRecords()
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["username",'name','last_name']

    def __str__(self):
        return f'{self.email} {self.name} {self.last_name}'

class Membership(BaseModel):
    slug = models.SlugField()
    membership_type = models.CharField("Tipo de membresia",max_length = 30,choices=MEMBERSHIP_CHOICES,default="Free")
    price = models.IntegerField(default=0)
    runway_plan_id =  models.CharField('Pasarela de pago membresia', max_length = 40)

    historical = HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        verbose_name = "Membership"
        verbose_name_plural = "Memberships"


    def __str__(self):
        return f'{self.membership_type}'

    
class Subscription(BaseModel):
    count_sub = models.PositiveSmallIntegerField(default=1)
    count_sub_total = models.PositiveSmallIntegerField(default=1)
    proof_of_payment =  models.TextField("Comprobante de pago",blank=False,null=False, unique=True)
    expiration_date= models.DateTimeField(blank=False)

    membership = models.ForeignKey(Membership,on_delete=models.CASCADE)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    


    historical = HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta: 
        verbose_name = "Subscription"
        verbose_name_plural = "Subscriptions"


    def __str__(self):
        return f'{self.proof_of_payment}, {self.expiration_date}'


    



