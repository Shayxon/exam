from rest_framework import serializers
from .models import Category, Product
from django.utils.text import slugify

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'slug']
        read_only_fields = ['slug']

    def create(self, validated_data):
        name = validated_data.get('name')
        slug = slugify(name)
        category = Category.objects.create(name=name, slug=slug)
        return category
    
    def update(self, instance, validated_data):
        name = validated_data.get('name')
        if name:
            slug = slugify(name)
            validated_data['slug'] = slug
        return super().update(instance, validated_data)
    
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description', 'price', 'available']

    def create(self, validated_data):
        name = validated_data.get('name')
        slug = slugify(name)
        category = Category.objects.create(name=name, slug=slug)
        return category
    
    def update(self, instance, validated_data):
        name = validated_data.get('name')
        if name:
            slug = slugify(name)
            validated_data['slug'] = slug
        return super().update(instance, validated_data)    