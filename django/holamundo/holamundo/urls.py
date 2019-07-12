from django.urls import path,include
from rest_framework import routers
from holamundo.holamundoapp import urls as computadora_urls

from holamundo.holamundoapp import views

router = routers.DefaultRouter()
router.register("computadora",views.ComputadoraViewSet)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('',include(computadora_urls))
]
