from django.contrib import admin
from rest_framework.routers import DefaultRouter

from django.urls import include, path

from api.views import MailingViewSet, ClientViewSet, MessageViewSet


router = DefaultRouter()
router.register('mailing', MailingViewSet)
router.register('clients', ClientViewSet)
router.register('messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] 