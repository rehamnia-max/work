from rest_framework import generics
from work_app.models import Category
from work_app.serializers import CategorySerializer


class CategoryList(generics.ListCreateAPIView):

    serializer_class = CategorySerializer

    # queryset =

    def get_queryset(self):
        print('#' * 20)
        objs = Category.objects.all()
        return objs  #super().get_queryset()
