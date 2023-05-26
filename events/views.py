from django.db.models import QuerySet
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import permissions, filters
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.request import Request
from rest_framework.response import Response

from events.models import Event
from events.serializers import EventCreateSerializer, EventSerializer


# ----------------------------------------------------------------
# event views
@extend_schema(tags=['Event'])
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

    @extend_schema(
        description="Create new event instance",
        summary="Create event",
    )
    def post(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().post(request, *args, **kwargs)


@extend_schema(tags=['Event'])
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

    @extend_schema(
        description="Get one event",
        summary="Retrieve event",
    )
    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().get(request, *args, **kwargs)


@extend_schema(tags=['Event'])
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
    filterset_fields: list = ['date']
    filter_backends: tuple = (
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    )
    ordering_fields: list = ['date']
    search_fields: list = ['title']

    @extend_schema(
        description="Get list of events",
        summary="Events list",
    )
    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().get(request, *args, **kwargs)
