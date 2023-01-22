from django.urls import path
from work_app import views
from django.conf import settings
# from django.templatetags.static import static
from django.conf.urls.static import static

urlpatterns = [
    path('categories/', view=views.CategoryList.as_view(), name="category-list"),
    path('categories/<int:category_id>/', view=views.CategoryDetail.as_view(), name="category-detail"),
    path('workers/', view=views.WorkerList.as_view(), name="category-list"),
    path('workers/<int:worker_id>/', view=views.WorkerDetail.as_view(), name="worker-detail"),
    path('works/', view=views.WorkList.as_view(), name="category-list"),
    path('works/<int:work_id>/', view=views.WorkDetail.as_view(), name="work-detail"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
