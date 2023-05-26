from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from core.models import User
from core.serializers import UserRegSerializer, UserAuthSerializer


# ----------------------------------------------------------------
# user views
class UserRegView(CreateAPIView):
    """
    View to handle registration

    Attrs:
        - serializer_class: defines serializer class for this APIView
    """
    serializer_class = UserRegSerializer


class UserAuthView(TokenObtainPairView):
    """
    View to handle authentication

    Attrs:
        - serializer_class: defines serializer class for this APIView
    """
    serializer_class = UserAuthSerializer

    def post(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        """
        Method to redefine post logic

        Params:
            - request: HttpRequest
            - args: positional arguments
            - kwargs: named (keyword) arguments

        Returns:
            - Response: Successful authentication

        Raises:
            - AuthenticationFailed (in case of invalid username or password)
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh = RefreshToken.for_user(serializer.validated_data['user'])
        return Response({
            'status': 'user_authenticated',
            'token': {
                'access': str(refresh.access_token)
            }
        }, status=status.HTTP_200_OK)
