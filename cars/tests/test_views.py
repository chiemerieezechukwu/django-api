import factory
import pytest
from .factories import CarFactory
from django.test import TransactionTestCase
from django.urls import reverse
from core.utils.reverse_with_query_string import reverse_querystring
from ..models import Car


@pytest.fixture
def inject_fixtures(request, car_factory):
    request.cls.car_factory = car_factory


@pytest.mark.usefixtures("inject_fixtures")
class TestCarAPI(TransactionTestCase):
    reset_sequences = True

    def setUp(self):
        self.car_factory.create()

    def tearDown(self):
        Car.objects.all().delete()

    def test_create_car(self):
        car_dict = factory.build(dict, FACTORY_CLASS=CarFactory)
        res = self.client.post(reverse("car-list"), car_dict)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(Car.objects.count(), 2)

    def test_delete_car(self):
        print(Car.objects.all())
        res = self.client.delete(reverse("car-detail", kwargs={"pk": 1}))
        self.assertEqual(res.status_code, 204)
        self.assertEqual(Car.objects.count(), 0)

    def test_update_car_in_place(self):
        new_car_type = "Car Type MODIFIED"
        res = self.client.patch(
            reverse("car-detail", kwargs={"pk": 1}),
            {"car_type": new_car_type},
            content_type="application/json",
        )
        self.assertEqual(res.json()["car_type"], new_car_type)
        self.assertEqual(res.status_code, 200)

    def test_serializer_not_return_fields_by_default(self):
        all_fields = (
            "url",
            "id",
            "reg_no",
            "max_pax",
            "make_year",
            "manufacturer",
            "model",
            "car_type",
            "category",
            "engine",
        )
        excluded_fields_by_default = ("category", "engine")
        included_fields_by_default = tuple(set(all_fields) - set(excluded_fields_by_default))
        res = self.client.get(reverse("car-detail", kwargs={"pk": 1}))
        self.assertTrue(all(x not in res.json() for x in excluded_fields_by_default))
        self.assertTrue(all(x in res.json() for x in included_fields_by_default))

        res_with_extra_fields = self.client.get(
            reverse_querystring("car-detail", kwargs={"pk": 1}, query_kwargs={"include": "category"})
        )

        self.assertTrue("category" in res_with_extra_fields.json())

        res_with_extra_fields = self.client.get(
            reverse_querystring("car-detail", kwargs={"pk": 1}, query_kwargs={"include": "engine"})
        )

        self.assertTrue("engine" in res_with_extra_fields.json())

        res_with_extra_fields = self.client.get(
            reverse_querystring("car-detail", kwargs={"pk": 1}, query_kwargs={"include": ["engine", "category"]})
        )
        self.assertTrue(all(x in res_with_extra_fields.json() for x in excluded_fields_by_default))
        self.assertTrue(all(x in res_with_extra_fields.json() for x in all_fields))
