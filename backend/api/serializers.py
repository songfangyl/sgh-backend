from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Car, CarImage


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class CarImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ["id", "car", "image"]


class CarSerializer(serializers.ModelSerializer):
    images = CarImageSerializer(many=True, read_only=True)
    upload_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )
    class Meta:
        model = Car
        fields = ["id", "make", "model", "year", "listing_price", "sold_price", "cost", "mileage", "color", "plate_number", "status", "images", "upload_images"]
        extra_kwargs = {
            "id": {"read_only": True},
        }

    def create(self, validated_data):
        uploaded_images = validated_data.pop("upload_images")
        car = Car.objects.create(**validated_data)
        for image in uploaded_images:
            CarImage.objects.create(car=car, image=image)
        return car


