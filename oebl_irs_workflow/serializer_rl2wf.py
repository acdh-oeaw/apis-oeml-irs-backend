from rest_framework import serializers

from oebl_research_backend.tasks import move_research_lemmas_to_workflow
from .models import Issue


class ResearchLemma2WorkflowLemmaSerializer(serializers.Serializer):
    issue = serializers.PrimaryKeyRelatedField(
        queryset=Issue.objects.all(), required=False
    )
    lemmas = serializers.ListField(child=serializers.IntegerField(), required=True)

    def create(self, validated_data, editor):
        issue = validated_data["issue"] if "issue" in validated_data.keys() else None
        res = move_research_lemmas_to_workflow.delay(
            editor.pk, self.validated_data["lemmas"], issue=issue
        )
        return {"success": res.id}