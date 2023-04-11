from rest_framework import serializers
from .models import Category, Card


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class CardSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', read_only=True) # related HasOne
    # directors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True) # related ManyToMany

    class Meta:
        model = Card
        exclude = ['created_at', 'updated_at']
    # fields = '__all__'
