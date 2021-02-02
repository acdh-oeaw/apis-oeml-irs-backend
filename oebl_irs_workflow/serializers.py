from django.contrib.auth.models import User
from typing import Dict, Tuple, List
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.utils import inline_serializer
from rest_framework import serializers
from .models import (
    Author,
    Editor,
    Issue,
    IssueLemma,
    LemmaStatus,
    Lemma,
    LemmaNote,
    LemmaLabel,
)


Array = List[int]


class UserDetailSerializer(serializers.ModelSerializer):
    userId = serializers.IntegerField(source="pk")
    role = serializers.SerializerMethodField(method_name="get_role")

    def get_role(self, object):
        if object.is_superuser:
            return "admin"
        elif "ChefredakteurIn" in [x.name for x in object.groups.all()]:
            return "ChefredakteurIn"
        else:
            return object.__class__.__name__

    class Meta:
        model = User
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    userId = serializers.IntegerField(source="pk")
    name = serializers.SerializerMethodField(method_name="get_name")

    def get_name(self, object):
        if object.last_name is not None:
            return f"{object.last_name}, {object.first_name}"
        else:
            return object.username

    class Meta:
        model = User
        fields = ["userId", "email", "name"]


class AuthorSerializer(UserSerializer):
    class Meta:
        model = Author
        fields = ["userId", "email", "name", "address"]


class EditorSerializer(UserSerializer):
    class Meta:
        model = Editor
        fields = ["userId", "email", "name"]


class LemmaSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source="first_name")
    lastName = serializers.CharField(source="name")
    dateOfBirth = serializers.SerializerMethodField("get_date_of_birth")
    dateOfDeath = serializers.SerializerMethodField("get_date_of_death")

    @extend_schema_field(OpenApiTypes.STR)
    def get_date_of_birth(self, obj):
        if obj.start_date is not None:
            return obj.start_date.isoformat()
        else:
            return obj.start_date_written

    @extend_schema_field(OpenApiTypes.STR)
    def get_date_of_death(self, obj):
        if obj.end_date is not None:
            return obj.end_date.isoformat()
        else:
            return obj.end_date_written

    class Meta:
        model = Lemma
        fields = ["firstName", "lastName", "dateOfBirth", "dateOfDeath", "info"]


class LemmaStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LemmaStatus
        fields = "__all__"


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"


class LemmaNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = LemmaNote
        fields = "__all__"


class LemmaLabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = LemmaLabel
        fields = "__all__"


class IssueLemmaSerializerOpenApi(serializers.ModelSerializer):
    issue = IssueSerializer()
    lemma = LemmaSerializer()
    author = AuthorSerializer()
    editor = EditorSerializer()
    status = LemmaStatusSerializer()

    class Meta:
        model = IssueLemma
        exclude = ["serialization"]


class IssueLemmaSerializer(serializers.ModelSerializer):
    notes = serializers.SerializerMethodField(method_name="get_notes")
    serialization = serializers.SerializerMethodField(method_name="get_serialization")

    @extend_schema_field(IssueLemmaSerializerOpenApi(many=True))
    def get_serialization(self, object):
        return object.serialization

    def get_notes(self, object) -> Array:
        res = LemmaNote.objects.filter(lemma=object.lemma)
        return list(res.values_list("pk", flat=True))

    class Meta:
        model = IssueLemma
        fields = "__all__"
        read_only_fields = ["serialization"]