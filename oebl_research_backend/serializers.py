from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from typing import List as ListType

from .models import ListEntry, List
from oebl_irs_workflow.serializers import EditorSerializer

gndType = ListType[str]

class ListSerializer(serializers.ModelSerializer):
    editor = EditorSerializer()

    class Meta:
        model = List
        fields = "__all__"

class ListSerializerLimited(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = ["id", "title", "editor"]


class ListEntrySerializer(serializers.ModelSerializer):
    gnd = serializers.SerializerMethodField(method_name="get_gnd")
    firstName = serializers.CharField(source="person.first_name")
    lastName = serializers.CharField(source="person.name")
    list = ListSerializerLimited()

    def get_gnd(self, object) -> gndType:
        if object.person.uris is not None:
            res = []
            for uri in object.person.uris:
                if "d-nb.info" in uri:
                    res.append(uri.split("/")[-2])
            return res
        return []

    class Meta:
        model = ListEntry
        fields = [
            "id",
            "gnd",
            "list",
            "firstName",
            "lastName",
            "columns_user",
            "columns_scrape",
        ]


