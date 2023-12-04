from rest_framework.routers import DefaultRouter
from back.views import *


router = DefaultRouter()


# router.register(r'usuario', UsuarioViewSet, basename="usuario")



urlpatterns = router.urls