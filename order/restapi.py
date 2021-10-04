from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Post


class RestApiViewSet(ModelViewSet):
    def display_post(self, request):
        response_data = {"name": "Anup Kumar", "address": "Bangalore"}
        print("response_data", response_data)
        # Skipping the exception handling to make it simple for now
        return Response(response_data, status=200)
