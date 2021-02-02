from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes

from .models import ListEntry, List
from oebl_irs_workflow.serializers import EditorSerializer


class ListEntrySerializer(serializers.ModelSerializer):
    gnd = serializers.SerializerMethodField(method_name="get_gnd")
    firstName = serializers.CharField(source="person.first_name")
    lastName = serializers.CharField(source="person.name")
    list = serializers.SerializerMethodField(method_name="get_list")

    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_list(self, object):
        res = {"id": object.list_id, "title": object.list.title}
        return res

    @extend_schema_field(OpenApiTypes.OBJECT)
    def get_gnd(self, object):
        if object.person.uris is not None:
            res = []
            for uri in object.person.uris:
                if "d-nb.info" in uri:
                    res.append(uri)
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


class ListSerializer(serializers.ModelSerializer):
    editor = EditorSerializer()

    class Meta:
        model = List
        fields = "__all__"
