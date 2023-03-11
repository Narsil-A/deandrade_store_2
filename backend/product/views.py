from django.http import Http404

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer



class ProductCreateAPIView(generics.CreateAPIView): # post method create product objects
    
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        name = serializer.validated_data.get('name')
        description = serializer.validated_data.get('description') or None
        if description is None:
            description = name
        serializer.save(description=description)
        # send a Django signal

product_create_view = ProductCreateAPIView.as_view()
class ProductDetailAPIView(generics.RetrieveAPIView): # get method
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' primary key

product_detail_view = ProductDetailAPIView.as_view()
class CategoryDetailAPIView(generics.CreateAPIView):

    def perform_create(self, serializer):
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data) 



