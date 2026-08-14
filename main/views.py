from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import Actor
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from .FilterSet import ReviewFilter
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class ActorPagination(PageNumberPagination):
    page_size = 2


class ActorModelViewSet(ModelViewSet):

    queryset=Actor.objects.all()
    serializer_class=ActorSerializer

    pagination_class=ActorPagination

    filter_backends=[filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend]
    search_fields=['name']
    ordering_fields=['name','birth_date']
    filterset_fields=['country','gender']

    authentication_classes = [TokenAuthentication] 
    permission_classes = [IsAuthenticated]



class ReviewModelViewSet(ModelViewSet):

    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    filter_backends=[filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend]

    search_fields=['user.name']
    ordering_fields=['rate','created_at']
    filterset_fields=['user','movie']
    filterset_class=ReviewFilter




class MovieModelViewSet(ModelViewSet):

    queryset=Movie.objects.all()
    serializer_class=MovieSerializer


class PriseModelViewSet(ModelViewSet):

    queryset=Subscription.objects.all()
    serializer_class=SubSerializer


# class ActorsAPIView(APIView):
#     def get(self, request):
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ActorSerializer(data=request.data)
#         if serializer.is_valid():
#             Actor.objects.create(
#                 name=serializer.validated_data['name'],
#                 country=serializer.validated_data['country'],
#                 gender=serializer.validated_data['gender'],
#                 birth_date=serializer.validated_data['birth_date'],
#             )

#             response = {
#                 "message": "Actor created successfully!",
#                 "data": serializer.data,
#             }

#             return Response(response, status=HTTP_201_CREATED)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    

# class ActorDetailsView(APIView):
#     def get(self,request,id):
#         actor=Actor.objects.get(id=id)
#         serializer=ActorSerializer(actor)

#         return Response(serializer.data)
    
#     def put(self,request,id):
#         actor=Actor.objects.get(id=id)
#         serializer=ActorSerializer(actor,data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 {
#                     'message':'put succes!',
#                     'data':serializer.data
#                 }
#             )
#         return Response(serializer.error_messages,status=400)
    
#     def patch(self,request,id):
#         actor=Actor.objects.get(id=id)
#         serializer=ActorSerializer(actor,data=request.data,partial=True)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 {
#                     'message':'patch succes!',
#                     'data':serializer.data
#                 }
#                 )
#         return Response(serializer.error_messages,status=400)


# class MoviesAPIView(APIView):
#     def get(self, request):
#         serializer = MovieSerializer(Movie.objects.all(), many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             response = {
#                 "message": "Movie created successfully!",
#             }
#             return Response(response, status=HTTP_201_CREATED)
#         return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# class MovieDetailsView(APIView):
#     def get(self,request,id):
#         movie=Movie.objects.get(id=id)
#         serializer=MovieSerializer(movie)

#         return Response(serializer.data)
    
#     def put(self,request,id):
#         movie=Movie.objects.get(id=id)
#         serializer=MovieSerializer(movie,data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 {
#                     'message':'put succes!',
#                     'data':serializer.data
#                 }
#             )
#         return Response(serializer.error_messages,status=400)
    
#     def patch(self,request,id):
#         movi=Movie.objects.get(id=id)
#         serializer=ActorSerializer(movi,data=request.data,partial=True)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 {
#                     'message':'patch succes!',
#                     'data':serializer.data
#                 }
#                 )
#         return Response(serializer.error_messages,status=400)


# class PriseView(APIView):
#     def get(self,request):
#         serializer=SubSerializer(Subscription.objects.all(),many=True)
#         return Response(serializer.data)
    
#     def post(self,request):
#         serializer=SubSerializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=201)
#         return Response(serializer.errors,status=400)


# class PriceDetailsView(APIView):
#     def get(self,request,id):
#         price=Subscription.objects.get(id=id)
#         serializer=SubSerializer(price)

#         return Response(serializer.data)
    
#     def put(self,request,id):
#         price=Subscription.objects.get(id=id)
#         serializer=SubSerializer(price,data=request.data)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 {
#                     'message':'put succes!',
#                     'data':serializer.data
#                 }
#             )
#         return Response(serializer.error_messages,status=400)
    
#     def patch(self,request,id):
#         price=Subscription.objects.get(id=id)
#         serializer=SubSerializer(price,data=request.data,partial=True)

#         if serializer.is_valid():
#             serializer.save()

#             return Response(
#                 {
#                     'message':'patch succes!',
#                     'data':serializer.data
#                 }
#                 )
#         return Response(serializer.error_messages,status=400)

