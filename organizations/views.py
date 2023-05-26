from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from organizations.models import Organization
from organizations.serializers import OrgCreateSerializer


# ----------------------------------------------------------------
# organization view
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
