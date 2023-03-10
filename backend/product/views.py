from rest_framework import generics


from .models import Product
from .serializers import ProductSerializer



class ProductCreateAPIView(generics.CreateAPIView): # post method

    queryset = Product.objects.all()
    serializer_class = ProductSerializer



product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView): # get method
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk' primary key

product_detail_view = ProductDetailAPIView.as_view()


