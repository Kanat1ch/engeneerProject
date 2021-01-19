from django.urls import path
from .views import bicycles
from rest_framework import routers
from .api import MarksViewSet, TypeViewSet, WheelsViewSet, BslesViewSet


router = routers.DefaultRouter()

router.register('api/mark', MarksViewSet, 'mark')
router.register('api/type', TypeViewSet, 'type')
router.register('api/wheels', WheelsViewSet, 'wheels')
router.register('api/bsles', BslesViewSet, 'bsles')


urlpatterns = router.urls


urlpatterns = [
    path('', bicycles, name='bicycles')
]