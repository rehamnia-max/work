from django.db import models
from work_app.models import Worker, Category
class Work(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='works/')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
   
   
    def __str__(self):
        return str(self.id)
