from rest_framework import serializers

from vehicles.models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class BrandSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ('id', 'name')


class BrandSerializer(serializers.ModelSerializer):
    series = BrandSeriesSerializer(many=True, read_only=True)
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Brand
        fields = ('id', 'name', 'description', 'founding_date', 'country', 'series')
