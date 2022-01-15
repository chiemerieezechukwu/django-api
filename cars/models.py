from django.db import models
from django.utils.translation import gettext_lazy as _


class Car(models.Model):
    CATEGORY_CHOICES = (
        ("ECONOMY", "ECONOMY"),
        ("BUSINESS", "BUSINESS"),
        ("FIRST CLASS", "FIRST CLASS"),
    )
    ENGINE_TYPE = (
        ("ELECTRIC", "ELECTRIC"),
        ("HYBRID", "HYBRID"),
        ("INTERNAL COMBUSTION ENGINE", "INTERNAL COMBUSTION ENGINE"),
    )
    reg_no = models.CharField(_("Registration number"), max_length=256)
    max_pax = models.CharField(_("Maximum number of passengers"), max_length=256)
    make_year = models.IntegerField(_("Year of manufacture"))
    manufacturer = models.CharField(_("Car manufacturer"), max_length=256)
    model = models.CharField(_("Car model"), max_length=256)
    category = models.CharField(_("Car category"), choices=CATEGORY_CHOICES, max_length=256)
    engine = models.CharField(_("Engine type"), choices=ENGINE_TYPE, max_length=256)
    car_type = models.CharField(_("Car Type"), max_length=256, blank=False)
