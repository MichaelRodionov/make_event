from rest_framework import status, permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from core.models import User
from core.serializers import UserRegSerializer, UserAuthSerializer, UserListSerializer


# ----------------------------------------------------------------
# user views
class UserRegView(CreateAPIView):
    model = User
    serializer_class = UserRegSerializer


class UserAuthView(TokenObtainPairView):
    serializer_class = UserAuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        refresh = RefreshToken.for_user(serializer.validated_data['user'])
        return Response({
            'status': 'user_authenticated',
            'token': {
                'access': str(refresh.access_token)
            }
        }, status=status.HTTP_200_OK)


class UserListView(ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()
