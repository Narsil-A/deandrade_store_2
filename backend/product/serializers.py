from rest_framework import serializers
from .models import Category, Product

"""
Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes

"""
class ProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = Product
        fields = ( 
            "name",
            "description",
            "price", 
        )
        
class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)
    
    class Meta:
        
        model = Category
        fields = ( 
            "id",
            "name",
            "get_absolute_url",
            "products",
        )