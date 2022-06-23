from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from item.serializers import ItemSerializer

# Create your views here.

class ItemView(APIView):

    def get(self, request):
        item = request

        serializer = ItemSerializer(item).data

        return Response(serializer, status=status.HTTP_200_OK)

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass
