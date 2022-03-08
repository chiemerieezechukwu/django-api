from rest_framework.permissions import SAFE_METHODS
from rest_framework import serializers
from .models import Car


class DynamicHyperlinkedModelSerializer(serializers.HyperlinkedModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def get_field_names(self, declared_fields, info):
        field_names = super().get_field_names(declared_fields, info)
        maybe_fields = self.Meta.maybe_fields if hasattr(self.Meta, "maybe_fields") else ()

        assert set(maybe_fields).issubset(set(field_names)), "%s are declared in `maybe_fields` but not `fields`" % (
            set(maybe_fields) - set(field_names)
        )

        # don't exclude any fields for create or update actions
        if self.request_method not in SAFE_METHODS:
            maybe_fields = ()

        if self.fields_from_query:
            # Drop any fields that are not specified in the `fields` argument.
            maybe_fields = tuple(set(maybe_fields) - set(self.fields_from_query))

        excluded_field_names = set(maybe_fields)
        field_names = tuple(x for x in field_names if x not in excluded_field_names)
        return field_names

    def __init__(self, *args, **kwargs):
        self.request_method = kwargs["context"]["request"].method
        self.fields_from_query = kwargs["context"]["request"].query_params.getlist("include")

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)


class CarSerializer(DynamicHyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = (
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

        """
        These custom fields control which fields are not shown by default.
        They will be returned if the request explicitly requests them

        Example:
        GET /cars/1/?include=category&include=engine
        """
        maybe_fields = (
            "category",
            "engine",
        )
