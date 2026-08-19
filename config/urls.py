from django.contrib import admin
from django.urls import path,include,re_path
from rest_framework.routers import DefaultRouter
from main.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router=DefaultRouter()

router.register('actors',ActorModelViewSet,basename='actor')
router.register('movie',MovieModelViewSet,basename='movie')
router.register('price',PriseModelViewSet,basename='sub')
router.register('review',ReviewModelViewSet,basename='review')


schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="My API documentation",
        contact=openapi.Contact(email="admin@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    re_path(
        r'^swagger/$',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),

    re_path(
        r'^redoc/$',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),
    # path('actors/', ActorsAPIView.as_view()),
    # path('movies/', MoviesAPIView.as_view()),
    # path('price/',PriseView.as_view()),
    # path('actor-details/<int:id>/',ActorDetailsView.as_view()),
    # path('movie-details/<int:id>/',MovieDetailsView.as_view()),
    # path('price-details/<int:id>/',PriceDetailsView.as_view()),
]
