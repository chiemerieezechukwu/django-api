from faker import Faker
from faker_vehicle import VehicleProvider


faker = Faker(["pl_PL"])
faker.add_provider(VehicleProvider)
