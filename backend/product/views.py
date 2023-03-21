from rest_framework import authentication, generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .authentication import TokenAuthentication

from .models import Product
from .permissions import IsStaffEditorPermission
from .serializers import ProductSerializer, CategorySerializer




class ProductListCreateAPIView(generics.ListCreateAPIView): 
    """
    CreateAPIView and ListCreateAPIView are slightly different
    ListCreateAPIView: Used for read-write endpoints to represent a collection of model instances
                       Provides get and post method handlers
                       Extends: GenericAPIView, ListModelMixin, CreateModelMixin
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        TokenAuthentication
    ]
    # 
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]

    def perform_create(self, serializer):
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description') or None
        
        if description is None:
            description = name
        serializer.save(description=description)
        

product_list_create_view = ProductListCreateAPIView.as_view()
class ProductDetailAPIView(generics.RetrieveAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

product_detail_view = ProductDetailAPIView.as_view()

"""
class ProductListAPIView(generics.ListAPIView): # get method
    
    # not gonna use this method 
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' primary key

product_list_view = ProductListAPIView.as_view() """ 



class ProductUpdateAPIView(generics.UpdateAPIView):

    """
    UPDATE  method 
    Used for update-only endpoints for a single model instance.
    Provides put and patch method handlers.
    Extends: GenericAPIView, UpdateModelMixin
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.description:
            instance.description = instance.name
           

product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
    """
    Used for delete-only endpoints for a single model instance.

    Provides a delete method handler.

    Extends: GenericAPIView, DestroyModelMixin
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()
# Function based view for create and retrive data
@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method 

    if method == "GET":
        if pk is not None:
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        # list view
        queryset = Product.objects.all() 
        data = ProductSerializer(queryset, many=True).data
        return Response(data)

    if method == "POST":
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            name = serializer.validated_data.get('name')
            description = serializer.validated_data.get('description') or None
            if description is None:
                description = name
            serializer.save(description=description)
            return Response(serializer.data)
        return Response({"invalid": "not good data"}, status=400)