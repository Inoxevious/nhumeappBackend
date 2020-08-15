from django.db import models
# from django.contrib.auth.models import User
from django.core.files import File
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from backoffice.UserManager import UserManager
from backoffice.models import User
from django.contrib.auth.hashers import get_hasher, identify_hasher
import uuid

# Create your models here.
import uuid

class TargetMarketCategory(models.Model):
  name =  models.CharField(max_length=255)
  description = models.TextField(null=True ,blank=True)
  class Meta:
    verbose_name_plural = "target_markets_catories"

  def __str__(self):
      return self.name
class TargetMarket(models.Model):
  name =  models.CharField(max_length=255)
  target_categorie = models.ForeignKey(TargetMarketCategory, default=uuid.uuid4, on_delete = models.CASCADE)
  description = models.TextField(null=True ,blank=True)
  class Meta:
    verbose_name_plural = "target_markets"

  def __str__(self):
      return self.name

class Vendor(models.Model):
  user = models.ForeignKey(User, default=uuid.uuid4, on_delete = models.CASCADE)
  nameCompany =  models.CharField(max_length=255)
  nameTrading =  models.CharField(max_length=255)
  description = models.TextField(null=True ,blank=True)
  location = models.PointField(null=True, blank=True)
  phoneSales = models.CharField(max_length=100, null=True, blank=True)
  phoneCustomerQueries = models.CharField(max_length=100, null=True, blank=True)
  emailSales = models.CharField(max_length=100, null=True, blank=True)
  emilCustomerQueries = models.CharField(max_length=100, null=True, blank=True)
  mainAddressCity = models.CharField(max_length=100, null=True, blank=True)
  mainAddressResidence = models.CharField(max_length=100, null=True, blank=True)
  mainAddressNeigbhourhood = models.CharField(max_length=100, null=True, blank=True)
  zimraVendorID = models.CharField(max_length=100, null=True, blank=True)
  taxClearance = models.FileField(null=True ,blank=True, upload_to='media/vendor_images')
  logoImage = models.ImageField(null=True ,blank=True, upload_to='media/vendor_images')
  time_update = models.DateTimeField()

  class Meta:
    verbose_name_plural = "vendors"

  def __str__(self):
      return self.nameCompany

class Catergory(models.Model):
  name =  models.CharField(max_length=255)
  image = models.ImageField(null=True ,blank=True, upload_to='media/vendor_images')
  time_update = models.DateTimeField()
  description = models.TextField(null=True ,blank=True)
  class Meta:
    verbose_name_plural = "categories"

  def __str__(self):
      return self.name

class Brand(models.Model):
  vendor_id = models.ForeignKey(Vendor, default=uuid.uuid4, on_delete = models.CASCADE)
  unqueSellingPoint = models.TextField(null=True ,blank=True)
  targetMarket = models.ManyToManyField(TargetMarket)
  name =  models.CharField(max_length=255)
  image = models.ImageField(null=True ,blank=True, upload_to='media/vendor_images')
  time_update = models.DateTimeField()
  description = models.TextField(null=True ,blank=True)
  class Meta:
    verbose_name_plural = "brands"

  def __str__(self):
      return self.name


class Product(models.Model):
    # vendor_id =  models.OneToOneField(User, on_delete=models.CASCADE)
    id  = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True ,blank=True)
    targetMarket = models.ManyToManyField(TargetMarket)
    unit_price = models.TextField(null=True ,blank=True)
    old_price = models.TextField(null=True ,blank=True)
    image = models.ImageField(null=True ,blank=True, upload_to='media/vendor_images')
    time = models.DateTimeField()
    time_update = models.DateTimeField()
    visibility = models.IntegerField(null=True ,blank=True)
    shop_categorie = models.ForeignKey(Catergory, null=True, on_delete = models.CASCADE)
    quantity = models.IntegerField(null=True ,blank=True)
    order_limits = models.IntegerField(null=True ,blank=True)
    unit_measurement = models.TextField(null=True ,blank=True)
    in_slider = models.IntegerField(null=True ,blank=True)
    url = models.URLField(null=True ,blank=True)
    virtual_products = models.IntegerField(null=True ,blank=True)
    brand = models.ForeignKey(Brand,null=True, on_delete = models.CASCADE)
    position = models.IntegerField(null=True ,blank=True)


    class Meta:
      verbose_name_plural = "products"

    def __str__(self):
        return self.name


