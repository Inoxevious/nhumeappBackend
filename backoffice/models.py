from django.db import models
from django.core.files import File
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from backoffice.UserManager import UserManager
from django.contrib.auth.hashers import get_hasher, identify_hasher
import uuid

class User(AbstractBaseUser, PermissionsMixin):

  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  customerId = models.CharField(max_length=100, null=True, blank=True,db_index=True)
  email = models.EmailField(unique=True,db_index=True)
  username = models.CharField(max_length=100, null=True, blank=True)
  facebookId = models.CharField(max_length=100, null=True, blank=True,db_index=True)
  android = models.BooleanField(blank=True, default=False)
  ios = models.NullBooleanField(blank=True, default=False, null=True)
  acceptPush = models.BooleanField(default=False)
  pushToken = models.CharField(max_length=100, null=True, blank=True,db_index=True)
  is_active = models.BooleanField(('active'), default=True)
  is_staff = models.BooleanField(('staff'), default=False)
  valid = models.BooleanField(default=True)
  isRider = models.BooleanField(default=True)
  objects = UserManager()
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  class Meta:
      verbose_name = ('User')
      verbose_name_plural = ('Users')


class File(models.Model):
    # file = models.FileField(blank=False, null=False)
    image = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
    car_id = models.CharField(max_length=100, null=True, blank=True)
    owner = models.CharField(max_length=100, null=True, blank=True)
    reg_number = models.CharField(max_length=100, null=True, blank=True)

    # def __str__(self):
    #     return self.reg_number
        
class PackageFile(models.Model):
    file =  models.FileField(blank=False, null=False)
    package_id = models.CharField(max_length=100, null=True, blank=True)
    owner = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.file.name
        
class Package(models.Model):

  Meters = 'Meters'
  Kilograms = 'Kilograms'
  Liters = 'Liters'
  Mililitres = "Mililitres"
  biddingOpen = 'biddingOpen'
  biddingClosed= 'biddingClosed'
  biddingSuspended= 'biddingSuspended'
  biddingReopened= 'biddingReopened'
  pickupPoint = 'pickupPoint'
  intransit = 'intransit'
  delivered = 'delivered'
  returning = 'returning'
  returned = 'returned'
  COURIER_CHOICES = [
        (pickupPoint,'pickupPoint'),
        (intransit,'intransit'),
        (delivered,'delivered'),
        (returning,'returning'),
        (returned,'returned'),
    ]
  BID_CHOICES = [
        (biddingOpen,'Bidding Open'),
        (biddingClosed,'Bidding Closed'),
        (biddingSuspended,'Bidding Suspended'),
        (biddingReopened,'Bidding Reopened'),
    ]
  MEASURE_CHOICES = [
        (Meters,'Meters'),
        (Kilograms,'Kilograms'),
        (Liters,'Liters'),
        (Mililitres,'Mililitres'),
    ]
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  packageOwner = models.CharField(max_length=100, null=True, blank=True)
  reference = models.CharField(max_length=100,db_index=True)
  quantity = models.CharField(max_length=100, null=True, blank=True)
  weight = models.CharField(max_length=100, null=True, blank=True)
  measure = models.CharField(max_length=100, null=True, blank=True, choices=MEASURE_CHOICES, default = Kilograms )
  qrCode = models.CharField(max_length=100, null=True, blank=True, db_index=True)
  picture = models.ImageField(upload_to="media/%Y/%m/%d",null=True, blank=True)
  available = models.BooleanField(default=True)
  biddingState  = models.CharField(max_length=100, null=True, blank=True, choices=BID_CHOICES, default = biddingOpen)
  courierState  = models.CharField(max_length=100, null=True, blank=True, choices=COURIER_CHOICES, default = pickupPoint)
  location = models.PointField(null=True, blank=True)
  pickupAddressCity = models.CharField(max_length=100, null=True, blank=True)
  pickupAddressResidence = models.CharField(max_length=100, null=True, blank=True)
  pickupAddressNeigbhourhood = models.CharField(max_length=100, null=True, blank=True)
  deliveryLocation = models.PointField(null=True, blank=True)
  deliveryAddressCity = models.CharField(max_length=100, null=True, blank=True)
  deliveryAddressNeigbhourhood = models.CharField(max_length=100, null=True, blank=True)
  deliveryAddressResidence = models.CharField(max_length=100, null=True, blank=True)
  isPrimary = models.BooleanField(default=True)

  class Meta:
      verbose_name = ('Package')
      verbose_name_plural = ('Packages')
  def __str__(self):
    return self.reference

        

class DeliveryAddressEntity(models.Model):
  packageID = models.ForeignKey(Package, default=uuid.uuid4, on_delete = models.CASCADE)
  deliveryAddress= models.CharField(max_length=100, null=True)
  isPrimary = models.BooleanField(default=True)
  postalCode= models.CharField(max_length=100, null=True, blank=True)
  street = models.CharField(max_length=100, null=True, blank=True)
  unitNumber= models.CharField(max_length=100, null=True, blank=True)



class TransactionLineItemEntity(models.Model):

  transactionLineItemId = models.CharField(max_length=100, null=True, blank=True)
  quantity = models.CharField(max_length=100, null=True, blank=True)
  serialNumber = models.CharField(max_length=100, null=True, blank=True)
  unitPrice = models.CharField(max_length=100, null=True, blank=True)
  subTotal = models.CharField(max_length=100, null=True, blank=True)
  menuItemEntity = models.CharField(max_length=100, null=True, blank=True)
  customisableItemId = models.CharField(max_length=100, null=True, blank=True)
  def __str__(self):
    return self.serialNumber

class PackageBids(models.Model):
  bidID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  packageOwner =  models.CharField(max_length=100, null=True, blank=True)
  packageID =  models.CharField(max_length=100, null=True, blank=True)
  bidderEmail = models.CharField(max_length=100, null=True, blank=True)
  bidPrice = models.CharField(max_length=100, null=True, blank=True)
  bidderPickupTime = models.CharField(max_length=100, null=True, blank=True)
  bidState = models.CharField(max_length=100, null=True, blank=True)
  def __str__(self):
    return self.bidderEmail

class AcceptedBids(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  bidID = models.CharField(max_length=100, null=True, blank=True)
  timeAccepted = models.TimeField(auto_now_add=True, null=True)

class Rides(models.Model):
  
  SUV = 'SUV'
  PICKUP = 'PICKUP'
  LORRY = 'LORRY'
  STATIONWAGON = 'STATIONWAGON'
  HATCHBACK = 'HATCHBACK'
  MINIVAN = 'MINIVAN'
  REFRIGERATORTRUCK = 'RefrigeratorTruck'
  SEDAN = 'SEDAN'
  RIDES_CHOICES = [
        (SUV, 'SUV'),
        (PICKUP, 'PICKUP'),
        (STATIONWAGON, 'STATION WAGON'),
        (HATCHBACK, 'HATCHBACK'),
        (MINIVAN, 'MINIVAN'),
        (REFRIGERATORTRUCK, 'RefrigeratorTruck'),
        (SEDAN, 'SEDAN'),
    ]
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  owner = models.CharField(max_length=100, null=True, blank=True)
  reg_number  = models.CharField(max_length=100, null=True, blank=True)
  maxWeight  = models.CharField(max_length=100, null=True, blank=True)
  file = models.FileField(blank=True, null=True)
  ride_category = models.CharField(max_length=100, null=True, blank=True, choices=RIDES_CHOICES, default = SUV )
  def __str__(self):
    return self.owner
  
class Driver(models.Model):
  One = 'One'
  Two = 'Two'
  Four = 'Four'
  Five = 'Five'
  LICENCE_CHOICES = [
          (One, 'One'),
          (Two, 'Two'),
          (Four, 'Four'),
          (Five, 'Five'),
      ]
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  owner = models.CharField(max_length=100, null=True, blank=True)
  license_number  = models.CharField(max_length=100, null=True, blank=True)
  years_experience  = models.CharField(max_length=100, null=True, blank=True)
  file = models.FileField(blank=True, null=True)
  license_class = models.CharField(max_length=100, null=True, blank=True, choices=LICENCE_CHOICES, default = Four )
  def __str__(self):
    return self.owner