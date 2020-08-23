# *coding: utf-8*
from backoffice.models import User, Package
# from django.contrib.gis.db.models.functions import Distance 
from api.serializers import *
from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework_gis.filters import DistanceToPointFilter
from django.contrib.gis.measure import D, Distance
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status , generics , mixins
from django.contrib.gis.db.models import PointField
from django.db.models.functions import Cast
from django.http import JsonResponse
from django.contrib.auth import backends, get_user_model
from django.db.models import Q

from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import FileSerializer, PackageFileSerializer
from rest_framework.parsers import FileUploadParser

class FileUploadView(APIView):
    parser_class = (FileUploadParser,)
    
    def post(self, request, *args, **kwargs):
      
      file_serializer = RidesSerializer(data=request.data)

      if file_serializer.is_valid():
          file_serializer.save()
          return Response(file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PackgesFileUploadView(APIView):
    parser_class = (FileUploadParser,)
    
    def post(self, request, *args, **kwargs):
      
      package_file_serializer = PackageFileSerializer(data=request.data)

      if package_file_serializer.is_valid():
          package_file_serializer.save()
          return Response(package_file_serializer.data, status=status.HTTP_201_CREATED)
      else:
          return Response(package_file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RidesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rides
        fields = ('id','owner','reg_number','ride_category','maxWeight','file')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

class AcceptedBidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedBids
        fields = '__all__'
class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'
@api_view(['GET', 'POST'])
def driver_list(request):
    print('CURRENT REQUEST', request)
    if request.method == 'GET':
        drivers = Driver.objects.all()
        serializer = DriverSerializer(drivers, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DriverSerializer(data=request.data)
        print('Serilizer', request.data)
        if serializer.is_valid():
            owner = request.data.get('owner')
            license_number = request.data.get('license_number')
            print('this p0aCKAgte ownr', owner, license_number)
            ride = Driver.objects.filter(owner__contains = str(owner), license_number__contains = str(license_number) )
            if(ride):
                picture = request.query_params.get('picture')
                if(picture):
                    driver = Driver.objects.filter(owner__contains = str(owner), 
                    license_number__contains = str(license_number)).update(
                        picture = picture
                    )
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                # driver_id = driver.id

            else:
                new_driver = serializer.save()
                print("New driver OnBect", new_driver.id)
                
                if(request.query_params.get('file')):
                    picture = request.query_params.get('picture')
                    driver = Driver.objects.get(id = str(new_driver.id)).update(
                        picture = picture
                    )
                return Response(new_driver.id, status=status.HTTP_201_CREATED)


            
            # packageOwner = request.query_params.get('packageOwner')
            # print('this p0aCKAgte ownr', packageOwner)
            # package = Package.objects.filter(packageOwner__contains = str(packageOwner))
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def driver_detail(request, pk):
    try:
        driver = Driver.objects.get(pk=pk)
    except Driver.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = DriverSerializer(driver, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = DriverSerializer(driver, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
           
    elif request.method == 'DELETE':
        driver.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])

def ride_list(request):
    print('CURRENT REQUEST', request)
    parser_class = (FileUploadParser,)
    if request.method == 'GET':
        rides = Rides.objects.all()
        serializer = RidesSerializer(rides, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        parser_class = (FileUploadParser,)
        serializer = RidesSerializer(data=request.data)
        print('Serilizer', request.data)
        if serializer.is_valid():
            owner = request.data.get('owner')
            reg_number = request.data.get('reg_number')
            print('this p0aCKAgte ownr', owner, reg_number)
            ride = Rides.objects.filter(owner__contains = str(owner), reg_number__contains = str(owner) )
            if(ride):
                file = request.FILES['file']
                if(file):
                    ride = Rides.objects.filter(owner__contains = str(owner), 
                    reg_number__contains = str(owner)).update(
                        file = file
                    )
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                # ride_id = ride.id

            else:
                new_packge = serializer.save()
                print("New Ride OnBect", new_packge.id)
                
                if(request.query_params.get('file')):
                    file = request.query_params.get('file')
                    ride = Rides.objects.get(id = str(new_packge.id)).update(
                        file = file
                    )
                return Response(new_packge.id, status=status.HTTP_201_CREATED)


            
            # packageOwner = request.query_params.get('packageOwner')
            # print('this p0aCKAgte ownr', packageOwner)
            # package = Package.objects.filter(packageOwner__contains = str(packageOwner))
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def ride_detail(request, pk):
    try:
        product = Rides.objects.get(pk=pk)
    except Rides.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = RidesSerializer(ride, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = RidesSerializer(ride, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
           
    elif request.method == 'DELETE':
        ride.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

        def get_distance(self, obj):
            return obj.distance_to_user.km
@api_view(['GET', 'POST'])
def getdriver(request):
    print('CURRENT REQUEST', request)
    if request.method == 'GET':
        packages = Package.objects.all()
        serializer = PackageSerializer(packages, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PackageSerializer(data=request.data)
        print('Serilizer', request.data)
        if serializer.is_valid():
            new_packge = serializer.save()
            packageOwner = request.query_params.get('packageOwner')
            print('this p0aCKAgte ownr', packageOwner)
            package = Package.objects.filter(packageOwner__contains = str(packageOwner))
            print("New PACKAGE OnBect", new_packge.id)
            return Response(new_packge.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getride(request):
    print('CURRENT REQUEST', request)
    reg_number = request.query_params.get('reg_number')
    try:
        ride = Rides.objects.filter(reg_number__iexact = str(reg_number))
    except Rides.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)
    if request.method == 'GET':
        ride = ''
        # packages = Package.objects.all()
        reg_number = request.query_params.get('reg_number')
        # serializer = PackageSerializer(packages, context={'request': request}, many=True)
        rides = Rides.objects.filter(reg_number__iexact = str(reg_number))
        print("Ride e", ride)
        for r in rides:
            ride = r.reg_number
        serializer = RidesSerializer(ride, context={'request': request}, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def packagecreate_list(request):
    print('CURRENT REQUEST', request)
    if request.method == 'GET':
        packages = Package.objects.all()
        serializer = PackageSerializer(packages, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PackageSerializer(data=request.data)
        print('Serilizer', request.data)
        if serializer.is_valid():
            new_packge = serializer.save()
            packageOwner = request.query_params.get('packageOwner')
            print('this p0aCKAgte ownr', packageOwner)
            package = Package.objects.filter(packageOwner__contains = str(packageOwner))
            print("New PACKAGE OnBect", new_packge.id)
            return Response(new_packge.id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def userpackages(request):
    packageOwner = request.query_params.get('packageOwner')
    print('this p0aCKAgte ownr', packageOwner)
    try:
        package = Package.objects.filter(packageOwner__contains = str(packageOwner))
    except Package.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        
        return JsonResponse(package, safe=False)
        # return Response(response)
    
@api_view(['GET', 'PUT', 'DELETE'])
def carimages(request):
    car_id = request.query_params.get('car_id')
    print('this p0aCKAgte ownr', car_id)
    try:
        ride = File.objects.filter(car_id__contains = str(car_id))
    except File.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = FileSerializer(ride, context={'request': request})
        return Response(serializer.data)
        
        # return Response(response)
class retrievePackageImagesView(generics.ListAPIView):
    """
            get:
                Search or get bids
    """
    queryset = PackageFile.objects.all()
    serializer_class = PackageFileSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('package_id', )

    def get_queryset(self):
            package_id = self.request.query_params.get('package_id')
            queryset = PackageFile.objects.filter(package_id__contains = str(package_id))
            print('owner bids', queryset)
            
            return queryset
class retrieveCarImagesView(generics.ListAPIView):
    """
            get:
                Search or get bids
    """
    queryset = File.objects.all()
    serializer_class = FileSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('car_id', )

    def get_queryset(self):
            owner = self.request.query_params.get('owner')
            car_id = self.request.query_params.get('car_id')
            # packageID = self.request.query_params.get('packageID')
            queryset = File.objects.filter(owner__contains = str(owner), car_id__contains = str(car_id))
            print('package images', queryset)
            
            return queryset

@api_view(['GET', 'PUT', 'DELETE'])
def packageimages(request):
    owner = request.query_params.get('owner')
    reg_number = request.query_params.get('reg_number')
    print('this p0aCKAgte ownr', owner)
    try:
        package = PackageFile.objects.filter(owner__contains = str(owner), reg_number__contains = str(reg_number))
    except PackageFile.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        
        return JsonResponse(package, safe=False)
        # return Response(response)
    



@api_view(['GET', 'PUT', 'DELETE'])
def package_detail(request, pk):
    try:
        package = Package.objects.get(id=pk)
    except Package.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = PackageSerializer(package, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PackageSerializer(package, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
           
    elif request.method == 'DELETE':
        package.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RetrievePrimaryDeliveryAddressView(generics.ListAPIView):
    """
            get:
                Search or get users
    """
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('package_user', 'deliveryAddress')

class retrievePackageByReferenceView(generics.ListAPIView):
    """
            get:
                Search or get users
    """
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('packageOwner', 'reference', 'id')

class PackageListView(generics.ListAPIView):
    
    """
            get:
                Get list of Packages
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    """
    distance_filter_field = 'pickupLocation'
    filter_backends = (DistanceToPointFilter,)
    distance_filter_convert_meters = True
    """
    def get_queryset(self):
            latitude = self.request.query_params.get('latitude', None)
            longitude = self.request.query_params.get('longitude', None)
            max_distance = self.request.query_params.get('max_distance', None)
            if latitude and longitude:
                point_of_user = Point(float(longitude), float(latitude), srid=4326)
                # Here we're actually doing the query, notice we're using the Distance class fom gis.measure
                queryset =Package.objects.filter(
                    location__distance_lte=(
                        point_of_user,
                        Distance(km=float(max_distance))
                    )
                )
                # .annotate( geom=Cast('location', PointField())).filter(geom__within=point_of_user)
            else:
                queryset =Package.objects.all()
            return queryset
   
    
        
class retrieveUserByEmailView(generics.ListAPIView):
    """
            get:
                Search or get users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('email', 'username', 'id', 'password')
    def get_queryset(self):
            email = self.request.query_params.get('email')
            password = self.request.query_params.get('password')
            queryset = User.objects.filter(email__contains = email)
            print('usr found', queryset)
            
            return queryset

class retrievePackageByEmailView(generics.ListAPIView):
    """
            get:
                Search or get packages
    """
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('packageOwner', )

    def get_queryset(self):
            packageOwner = self.request.query_params.get('packageOwner')
            queryset = Package.objects.filter(packageOwner__contains = str(packageOwner))
            print('packageOwner Package', queryset)

            return queryset

class retrieveRideByEmailView(generics.ListAPIView):
    """
            get:
                Search or get ride
    """
    queryset = Rides.objects.all()
    serializer_class = RidesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('owner', )

    def get_queryset(self):
            owner = self.request.query_params.get('owner')
            queryset = Rides.objects.filter(owner__contains = str(owner))
            print('owner ride', queryset)
            
            return queryset
class retrieveDriverByEmailView(generics.ListAPIView):
    """
            get:
                Search or get ride
    """
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('owner', )

    def get_queryset(self):
            owner = self.request.query_params.get('owner')
            queryset = Driver.objects.filter(owner__contains = str(owner))
            print('owner ride', queryset)
            
            return queryset

class retrieveRideByRegNumberView(generics.ListAPIView):
    """
            get:
                Search or get ride
    """
    queryset = Rides.objects.all()
    serializer_class = RidesSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('reg_number', )

    def get_queryset(self):
            reg_number = self.request.query_params.get('reg_number')
            queryset = Rides.objects.filter(reg_number__contains = str(reg_number))
            print('reg_number ride', queryset)
            
            return queryset



class UserListView(generics.ListAPIView):
    """
            get:
                Search or get users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('email', 'username')

class UserListCreateView(generics.ListCreateAPIView):
    """
            create:
                add users
            get:
                Search or get users
                You can search using:
                    :param email
                    :param username
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('email', 'username','password', '')



class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
            get:
                get a specific user
            delete:
                Remove an existing user.
            patch:
                Update one or more fields on an existing user.
            put:
                Update a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET', 'POST'])
def usercreate_list(request):
    print('CURRENT REQUEST', request)
    if request.method == 'GET':
        email = request.query_params.get('email')
        print("qury paaraams email", email)
        
        user = User.objects.filter(email=email)
        serializer = UserSerializer(user, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        print('Serilizer', request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
           
    elif request.method == 'DELETE':
        ride.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def createpaymentintent(request):
    if request.method == "POST":
        amount =  request.data["amount"]
        stripe.api_key = "pk_test_51GslFEGN6hwQCl2kYrHGNohCYqg8P4mmTWl8a7CS8tz9jaREYCLKSxvkuZjFg7bgWa0CYsiLfuonhpBj5BtrdRsB00hNez14LZ"
        intent = stripe.PaymentIntent.create(
            amount=int(amount),
            currency='eur',
        )
        return JsonResponse(intent, safe=False)
    else:
        return HttpResponse(status=501)

class PackageBidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageBids
        fields = '__all__'
        # ('packageOwner','packageID','bidderEmail','bidPrice','bidderPickupTime')  

@api_view(['GET', 'POST'])
def packagebids_list(request):
    print('CURRENT REQUEST', request)
    if request.method == 'GET':
        packagebids = PackageBids.objects.all()
        serializer = PackageBidsSerializer(packagebids, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PackageBidsSerializer(data=request.data)
        print('Serilizer', request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def packagebid_detail(request, pk):
    try:
        packagebid = PackageBids.objects.get(pk=pk)
    except PackageBids.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = PackageBidsSerializer(packagebid, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PackageBidsSerializer(packagebid, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
           
    elif request.method == 'DELETE':
        ride.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class retrievePackageBidsView(generics.ListAPIView):
    """
            get:
                Search or get bids
    """
    queryset = PackageBids.objects.all()
    serializer_class = PackageBidsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('packageID', )

    def get_queryset(self):
            packageID = self.request.query_params.get('packageID')
            queryset = PackageBids.objects.filter(packageID__contains = str(packageID))
            print('owner bids', queryset)
            
            return queryset


class UsrView(generics.ListAPIView):
    """
            get:
                Search or get bids
    """
    queryset = AcceptedBids.objects.all()
    serializer_class = AcceptedBidsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('bidID' )

    def get_queryset(self):
            packageID = self.request.query_params.get('bidID')
            queryset = AcceptedBids.objects.filter(bidID__contains = str(bidID))
            print('owner bids', queryset)
            
            return queryset


@api_view(['GET', 'POST'])
def acceptedbids_list(request):
    print('CURRENT REQUEST', request)
    if request.method == 'GET':
        acceptedbids = AcceptedBids.objects.all()
        serializer = AcceptedBidsSerializer(acceptedbids, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print('packageID', request.data.get('packageID'))
        packageState = Package.objects.filter(
            id__contains=request.data.get('packageID')
        ).update(
              currentState  = 'biddingClosed',
              courierState  = 'pickupPoit'
        )
        print('bidID', request.data.get('bidID'))
        bidState = PackageBids.objects.filter(
            bidID__contains=request.data.get('bidID')
        ).update(
              bidState  = 'accepted'
        )
        serializer = AcceptedBidsSerializer(data=request.data)
        print('Serilizer', request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def acceptedbid_detail(request, pk):
    try:
        bid = AcceptedBids.objects.get(pk=pk)
    except AcceptedBids.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = AcceptedBidsSerializer(acceptedbid, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AcceptedBidsSerializer(acceptedbid, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
           
    elif request.method == 'DELETE':
        ride.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class retrieveAcceptedBidsView(generics.ListAPIView):
    """
            get:
                Search or get bids
    """
    queryset = AcceptedBids.objects.all()
    serializer_class = AcceptedBidsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('bidID' )

    def get_queryset(self):
            packageID = self.request.query_params.get('bidID')
            queryset = AcceptedBids.objects.filter(bidID__contains = str(bidID))
            print('owner bids', queryset)
            
            return queryset

@api_view(['GET', 'POST'])
def revokedbids_list(request):
    print('CURRENT REQUEST', request)
    if request.method == 'GET':
        revokedbids = AcceptedBids.objects.all()
        serializer = AcceptedBidsSerializer(revokedbids, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print('packageID', request.data.get('packageID'))
        packageState = Package.objects.filter(
            id__contains=request.data.get('packageID')
        ).update(
              currentState  = 'biddingOpen',
              courierState  = 'pickupPoit'
        )
        print('bidID', request.data.get('bidID'))
        bidState = PackageBids.objects.filter(
            bidID__contains=request.data.get('bidID')
        ).update(
              bidState  = 'revoked'
        )
        serializer = AcceptedBidsSerializer(data=request.data)
        print('Serilizer', request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def packageupload_list(request):
    print('CURRENT REQUEST', request)
    if request.method == 'GET':
        ride = File.objects.all()
        serializer = FileSerializer(ride, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        print('car_id', request.data.get('car_id'))
        ride = Rides.objects.filter(
            id__contains=request.data.get('car_id')
        ).update(
              file  = request.data.get('file')
              
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def appdata(request):
    if request.method == 'GET':
        ride = File.objects.all()
        serializer = FileSerializer(ride, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def revokedbid_detail(request, pk):
    try:
        bid = AcceptedBids.objects.get(pk=pk)
    except AcceptedBids.DoesNotExist:
        return Response(status=status.HTTP_400_NOT_FOUND)

    if request.method == 'GET':
        serializer = AcceptedBidsSerializer(revokedbid, context={'request': request})
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AcceptedBidsSerializer(revokedbid, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
           
    elif request.method == 'DELETE':
        ride.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class retrieveRevokedBidsView(generics.ListAPIView):
    """
            get:
                Search or get bids
    """
    queryset = AcceptedBids.objects.all()
    serializer_class = AcceptedBidsSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('bidID','bidState' )

    def get_queryset(self):
            packageID = self.request.query_params.get('bidID')
            queryset = AcceptedBids.objects.filter(bidID__contains = str(bidID),
            bidState__contains = 'revoked'
            )
            print('owner bids', queryset)
            
            return queryset

class AppVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppVersion
        fields = '__all__'

class appDataView(generics.ListAPIView):
    """
            get:
                Search or get app
    """
    queryset = AppVersion.objects.all()
    serializer_class = AppVersionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('version_name','app_expire_date' )

    def get_queryset(self):
            queryset = AppVersion.objects.all()
            
            return queryset