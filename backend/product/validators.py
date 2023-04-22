from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

# def validate_name(value):
#     qs = Product.objects.filter(name__iexact=value)
#     if qs.exists():
#        raise serializers.ValidationError(f"{value} is already a product name.")
#     return value



def validate_title(self, value):
   request = self.context.get('request')
   user = request.user
   qs = Product.objects.filter(user=user, title__iexact=value)
   if qs.exists():
      raise serializers.ValidationError(f"{value} is already a product name.")
   return value

