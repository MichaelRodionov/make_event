from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.pagination import LimitOffsetPagination

from events.models import Event
from events.serializers import EventCreateSerializer, EventSerializer


# ----------------------------------------------------------------
# event views
class EventCreateView(CreateAPIView):
    """
    View to handle POST request to create event entity

    Attrs:
        - model: Event model
        - permission_classes: defines permissions for this APIView
        - serializer_class: defines serializer class for this APIView
    """
    model = Event
    serializer_class = EventCreateSerializer
    permission_classes: list = [permissions.IsAuthenticated]


class EventRetrieveView(RetrieveAPIView):
    """
    View to handle GET request to get one event

    Attrs:
        - queryset: defines queryset for event
        - serializer_class: defines serializer class for this APIView
        - permission_classes: defines permissions for this APIView
    """
    queryset: QuerySet = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes: list = [permissions.IsAuthenticated]


class EventListView(ListAPIView):
    """
    View to handle GET request to get list of event entities

    Attrs:
        - queryset: defines queryset for event
        - serializer_class: defines serializer class for this APIView
        - permission_classes: defines permissions for this APIView
        - pagination_class: defines pagination type for this APIView
        - filterset_fields: defines collection of fields to filter
        - filter_backends: defines collection of filtering options for this APIView
        - ordering_fields: defines collection of ordering options for this APIView
        - search_fields: defines collection of search options for this APIView
    """
    queryset: QuerySet = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes: list = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination
    filterset_fields: list = ['title', 'date']
    filter_backends: tuple = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    ordering_fields: list = ['date']
    search_fields: list = ['title']
