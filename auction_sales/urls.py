from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register('items', views.ItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', views.SignUpView.as_view(), name='signup'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
