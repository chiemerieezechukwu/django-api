import random
from fake import faker
import factory
from factory import fuzzy  # noqa
from ..models import Car


class CarFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Car
        exclude = ("vehicle_object",)

    vehicle_object = factory.LazyAttribute(lambda _: faker.vehicle_object())
    reg_no = factory.LazyAttribute(lambda _: faker.license_plate())
    max_pax = factory.LazyAttribute(lambda _: random.randint(2, 6))
    make_year = factory.LazyAttribute(lambda self: self.vehicle_object["Year"])
    manufacturer = factory.LazyAttribute(lambda self: self.vehicle_object["Make"])
    model = factory.LazyAttribute(lambda self: self.vehicle_object["Model"])
    car_type = factory.LazyAttribute(lambda self: self.vehicle_object["Category"])
    category = factory.fuzzy.FuzzyChoice(Car.CATEGORY_CHOICES)
    engine = factory.fuzzy.FuzzyChoice(Car.ENGINE_TYPE)
