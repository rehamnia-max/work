from rest_framework import generics
from work_app.models import Work
from work_app.serializers import WorkSerializer
from django.shortcuts import get_object_or_404


class WorkList(generics.ListCreateAPIView):

    serializer_class = WorkSerializer

    # queryset =

    def get_queryset(self):
        objs = Work.objects.all()
        return objs  #super().get_queryset()


class WorkDetail(generics.RetrieveUpdateDestroyAPIView):

    def get_object(self):
        return get_object_or_404(Work, pk=self.kwargs["work_id"])

    serializer_class = WorkSerializer