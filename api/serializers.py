from backoffice.models import *
from rest_framework import serializers
# from .models import File

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"




class PackageFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageFile
        fields = "__all__"