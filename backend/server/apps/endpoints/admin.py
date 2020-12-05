from django.contrib import admin
from apps.endpoints.models import Endpoints,MLAlgorithm,MLAlgorithmStatus
# Register your models here.

admin.site.register(Endpoints)
admin.site.register(MLAlgorithm)
admin.site.register(MLAlgorithmStatus)


