from django.urls import path, include
from core.views import portafolioList, portafolioDetail
from rest_framework import routers
from core import views
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('project/', portafolioList.as_view(), name="projectList"),
    path('project/<int:pk>/', portafolioDetail.as_view() , name="projectDetail"),
    path('', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view())
]