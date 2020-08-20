from backoffice.models import *
from rest_framework import serializers
# from .models import File

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = '__all__'

        def get_distance(self, obj):
            return obj.distance_to_user.km

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('image','car_id','owner','reg_number')


class AcceptedBidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedBids
        fields = '__all__'


class PackageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageFile
        fields = "__all__"

class RidesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rides
        fields = '__all__' 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' 

class PackageBidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageBids
        fields = '__all__'
        # ('packageOwner','packageID','bidderEmail','bidPrice','bidderPickupTime')  
