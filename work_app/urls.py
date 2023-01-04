from django.urls import path
from work_app import views

urlpatterns = [
    path('categories/',
         view=views.CategoryList.as_view(),
         name="category-list")
]
