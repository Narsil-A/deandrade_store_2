from django.http import Http404

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Product
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
