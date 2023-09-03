from rest_framework.routers import DefaultRouter
from .views import TODOViewSet
from django.urls import include, path

router = DefaultRouter()
router.register('app', TODOViewSet)

# urlpatterns = [
#     path('', include(router.urls))
# ]

urlpatterns = router.urls