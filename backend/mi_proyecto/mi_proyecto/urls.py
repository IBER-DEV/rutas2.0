from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from routes.views import ConductorViewSet, BusViewSet, RutaViewSet, ParadaViewSet, ViajeViewSet
from tracking.views import BusLocationViewSet
from users.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'conductores', ConductorViewSet)
router.register(r'buses', BusViewSet)
router.register(r'rutas', RutaViewSet)
router.register(r'paradas', ParadaViewSet)
router.register(r'viajes', ViajeViewSet)
router.register(r'locations', BusLocationViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
