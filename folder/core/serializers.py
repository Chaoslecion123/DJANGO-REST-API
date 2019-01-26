from core.models import portafolio
from rest_framework import serializers
from django.contrib.auth.models import User


class portafolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = portafolio
        fields = ('id','title','description','langs')



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','password')
        extra_kwargs = {'password': {'write_only':True, 'required':True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user