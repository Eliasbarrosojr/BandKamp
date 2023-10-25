from .models import Album
from .serializers import AlbumSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics


class AlbumView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    """ def get_queryset(self):
        if self.request.user.is_superuser:
            return Album.objects.all()

        return Album.objects.filter(user=self.request.user) """

    def perform_create(self, serializer):   
        return serializer.save(user=self.request.user)