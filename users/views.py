from rest_framework.generics import *
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import *


class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user