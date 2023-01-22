from rest_framework import generics
from work_app.models import Worker
from work_app.serializers import WorkerSerializer
from django.shortcuts import get_object_or_404


class WorkerList(generics.ListCreateAPIView):

    serializer_class = WorkerSerializer

    # queryset =

    def get_queryset(self):
        objs = Worker.objects.all()
        return objs  #super().get_queryset()


class WorkerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkerSerializer

    def get_object(self):
        return get_object_or_404(Worker, pk=self.kwargs["worker_id"])

    serializer_class = WorkerSerializer