from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Category, Product

"""
Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes

"""
class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
            view_name='product-detail',
            lookup_field='pk'
    )
    class Meta:

        model = Product
        fields = (
            "category",
            "url",
            "pk",
            "name",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            "date_added",
        )

# class CategorySerializer(serializers.ModelSerializer):

#     products = ProductSerializer(serializers.PrimaryKeyRelatedField(
#     many=True, queryset=Product.objects.all())
# )
#     class Meta:

#         model = Category
#         fields = [
#             "name",
#             "slug",
#             "products"
#             ]

#     def create(self, validated_data):
#         products_data = validated_data.pop('products')
#         category = Category.objects.create(**validated_data)
#         Product.objects.create(category=category, **products_data)
#         return category

#     def to_representation(self, category):
#         representation = super(CategorySerializer, self).to_representation(category)
#         representation['products'] = ProductSerializer(category.product_set.all(), many=True).data
#         return representation

 # bug = Cannot set both 'fields' and 'exclude' options on serializer CategorySerializer.

class CategorySerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True, required=False)

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "slug",
            "get_absolute_url",
            "products",
        )

