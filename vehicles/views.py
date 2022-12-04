from rest_framework import viewsets

from vehicles.models import Brand
from vehicles.serializers import BrandSerializer


class BrandAPIView(viewsets.ReadOnlyModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
