from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets


from .models import Category, Card
from .serializers import CategorySerializer, CardSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def get_queryset(self):
        """ Filter cards """
        queryset = Card.objects.filter(status=Card.STATUS_NEW).order_by('-id')
        category_id = self.request.query_params.get('category_id')
        if category_id is not None:
            # queryset = queryset.filter(category=category_id)
            # return queryset[:1]

            queryset.filter(category=category_id)
        # queryset[0]
        return queryset
