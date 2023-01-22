from rest_framework import generics
from work_app.models import Category
from work_app.serializers import CategorySerializer
from django.shortcuts import get_object_or_404


class CategoryList(generics.ListCreateAPIView):

    serializer_class = CategorySerializer

    # queryset =

    def get_queryset(self):
        objs = Category.objects.all()
        return objs  #super().get_queryset()


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):

    def get_object(self):
        return get_object_or_404(Category, pk=self.kwargs["category_id"])

    serializer_class = CategorySerializer
