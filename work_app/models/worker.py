from django.db import models
from django.utils import timezone
# from work_app.serializers import WorkSerializer


class Worker(models.Model):
    username = models.CharField(max_length=30)
    birth_date = models.DateField(max_length=30)
    phone = models.CharField(max_length=15)
    avatar = models.ImageField(blank=True, null=True, upload_to='avatars/')
    created_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    # works = WorkSerializer(source="work", read_only=True)


    def __str__(self):
        return str(self.id)
