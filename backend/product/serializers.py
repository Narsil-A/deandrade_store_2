from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Category, Product


"""
Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes

"""
class ProductSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Product
        fields = (
            'url',
            "pk",
            "name",
            "description",
            "price", 
        )

    def get_url(self, obj):
        # return f"/api/v2/product-v2/{obj.pk}/"
        request = self.context.get('request') # self.request
        if request is None:
            return None
        return reverse("Product-detail", kwargs={"pk":obj.pk}, request=request)

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