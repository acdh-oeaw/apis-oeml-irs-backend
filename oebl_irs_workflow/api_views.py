from rest_framework.response import Response
from rest_framework import filters, viewsets, renderers
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Author,
    Issue,
    IssueLemma,
    LemmaStatus,
    LemmaNote,
    Lemma,
    LemmaLabel,
    Editor,
)
from .serializers import (
    UserDetailSerializer,
    AuthorSerializer,
    EditorSerializer,
    IssueSerializer,
    IssueLemmaSerializer,
    LemmaStatusSerializer,
    LemmaNoteSerializer,
    LemmaSerializer,
    LemmaLabelSerializer,
)


class UserProfileViewset(viewsets.ViewSet):
    """Viewset to show UserProfile of current User"""

    def list(self, request):
        user = UserDetailSerializer(request.user)
        return Response(user.data)


class AuthorViewset(viewsets.ReadOnlyModelViewSet):
    """Viewset to retrieve Author objects"""

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_fields = ["username"]
    permission_classes = [IsAuthenticated]


class EditorViewset(viewsets.ReadOnlyModelViewSet):
    """Viewset to retrieve Editor objects"""

    queryset = Editor.objects.all()
    serializer_class = EditorSerializer
    filterset_fields = ["username"]
    permission_classes = [IsAuthenticated]


class IssueViewset(viewsets.ModelViewSet):

    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    filter_fields = ["name", "pubDate"]
    permission_classes = [IsAuthenticated]


class IssueLemmaViewset(viewsets.ModelViewSet):

    queryset = IssueLemma.objects.all()
    serializer_class = IssueLemmaSerializer
    filter_fields = ["lemma", "issue", "author", "editor"]
    permission_classes = [IsAuthenticated]


class LemmaViewset(viewsets.ReadOnlyModelViewSet):

    queryset = Lemma.objects.all()
    serializer_class = LemmaSerializer
    permission_classes = [IsAuthenticated]


class LemmaNoteViewset(viewsets.ModelViewSet):

    queryset = LemmaNote.objects.all()
    serializer_class = LemmaNoteSerializer
    filter_fields = ["lemma"]
    permission_classes = [IsAuthenticated]


class LemmaStatusViewset(viewsets.ModelViewSet):

    queryset = LemmaStatus.objects.all()
    serializer_class = LemmaStatusSerializer
    filter_fields = ["issuelemma", "issue"]
    permission_classes = [IsAuthenticated]


class LemmaLabelViewset(viewsets.ModelViewSet):

    queryset = LemmaLabel.objects.all()
    serializer_class = LemmaLabelSerializer
    filter_fields = ["issuelemma"]
    permission_classes = [IsAuthenticated]