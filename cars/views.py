from cars.models import Car
from .serializers import CarSerializer
from rest_framework import viewsets


class CarViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing cars data.
    """

    queryset = Car.objects.all().order_by("id")
    serializer_class = CarSerializer
