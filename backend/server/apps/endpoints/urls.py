from django.urls import path,include
from apps.endpoints.models import Endpoints
from apps.endpoints.views import EndpointViewset, MLAlgorithmViewset, MLAlgorithmStatusViewset, MLRequestViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register('endpoints',EndpointViewset,basename='endpoints')
router.register('mlalgorithm',MLAlgorithmViewset,basename='MLAlgorithm')
router.register('mlalgorithmstatus',MLAlgorithmStatusViewset,basename='MLAlgorithmStatus')
router.register('mlrequest',MLRequestViewset,basename='MLRequest')

urlpatterns = [
    path('api/v1/',include(router.urls)),
]