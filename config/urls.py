from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from main.views import *
from rest_framework.authtoken.views import obtain_auth_token


router=DefaultRouter()

router.register('actors',ActorModelViewSet,basename='actor')
router.register('movie',MovieModelViewSet,basename='movie')
router.register('price',PriseModelViewSet,basename='sub')
router.register('review',ReviewModelViewSet,basename='review')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/token/', obtain_auth_token),
    # path('actors/', ActorsAPIView.as_view()),
    # path('movies/', MoviesAPIView.as_view()),
    # path('price/',PriseView.as_view()),
    # path('actor-details/<int:id>/',ActorDetailsView.as_view()),
    # path('movie-details/<int:id>/',MovieDetailsView.as_view()),
    # path('price-details/<int:id>/',PriceDetailsView.as_view()),
]
