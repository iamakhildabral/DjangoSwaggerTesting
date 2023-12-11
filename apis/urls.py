from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apis import views


router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router.urls))
]
