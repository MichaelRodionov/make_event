from drf_spectacular.utils import extend_schema
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from organizations.models import Organization
from organizations.serializers import OrgCreateSerializer


# ----------------------------------------------------------------
# organization view
@extend_schema(tags=['Organization'])
class OrgCreateView(CreateAPIView):
    """
    View to handle POST request to create organization entity

    Attrs:
        - model: Organization model
        - serializer_class: defines serializer class for this APIView
        - permission_classes: defines permissions for this APIView
    """
    model = Organization
    serializer_class = OrgCreateSerializer
    permission_classes: list = [permissions.IsAuthenticated]

    @extend_schema(
        description="Create new organization instance",
        summary="Create organization",
    )
    def post(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        return super().post(request, *args, **kwargs)
