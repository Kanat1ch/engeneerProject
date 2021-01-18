from django.urls import path
from .views import cars, filter_by_transmissions, filter_by_class
from rest_framework import routers
from .api import TransmissionsViewSet, MarksViewSet, RanksViewSet, CarsViewSet


router = routers.DefaultRouter()

router.register('api/transmissions', TransmissionsViewSet, 'transmissions')
router.register('api/marks', MarksViewSet, 'marks')
router.register('api/ranks', RanksViewSet, 'ranks')
router.register('api/сars', CarsViewSet, 'сars')

urlpatterns = router.urls

urlpatterns = [
    path('', cars, name='cars'),
    path('transmission/<int:transmission_id>/', filter_by_transmissions, name='filter_by_transmissions'),
    path('class/<int:class_id>/', filter_by_class, name='filter_by_class'),
]