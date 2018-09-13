from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserView)
router.register('roles', views.RoleView)
router.register('lead_sources', views.LeadSourceView)

urlpatterns = [
    path('', include(router.urls))
]
