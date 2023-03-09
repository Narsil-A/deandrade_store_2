from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data) # send the data and verify if match with the requirements of the ProductSerializer.
    if serializer.is_valid(raise_exception=True):  # validation for the front
        print(serializer.data)

        return Response(serializer.data)
    return Response({"invalid":"not good data"}, status=400)