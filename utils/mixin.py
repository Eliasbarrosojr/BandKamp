from rest_framework.views import Request, Response, status
from django.shortcuts import get_object_or_404



class ListModelMixin:
    def list(self, request: Request) -> Response:
        queryset = self.queryset.all()

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data, status.HTTP_200_OK)

class CreateModelMixin:
    def create(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class RetrieveModelMixin:
    def get(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        user_field = kwargs.get(self.user_field)
        obj = get_object_or_404(self.queryset, pk=user_field)
        serializer = self.serializer_class(obj)

        return Response(serializer.data, status.HTTP_200_OK)

class UpdateModelMixin:
    def update(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        user_field = kwargs.get(self.user_field)
        obj = get_object_or_404(self.queryset, pk=user_field)
        serializer = self.serializer_class(obj, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)


class DestroyModelMixin:
    def delete(self, request: Request, *args: tuple, **kwargs: dict) -> Response:
        user_field = kwargs.get(self.user_field)
        obj = get_object_or_404(self.queryset, pk=user_field)
        obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


