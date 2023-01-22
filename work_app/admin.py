from django.contrib import admin
from work_app.models import Worker, Category, Work

# Register your models here.
admin.site.register(Worker)
admin.site.register(Work)
admin.site.register(Category)
