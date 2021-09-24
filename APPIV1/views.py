from django.views import generic
from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from APPIV1.serializers import *
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework import status
from .serializers import ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
#from .permissions import IsLoggedInUserOrAdmin, IsAdminUser, IsCustomerUser, IsOwner
from app.models import *
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
import random
import string
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .pagination import *
from django.core.paginator import Paginator
from .permissions import IsOwner
from rest_framework.generics import *
from rest_framework.pagination import PageNumberPagination # Any other type works as well
from rest_framework import status
from rest_framework.exceptions import NotFound as NotFoundError
from rest_framework.views import APIView

from rest_framework.pagination import PageNumberPagination






class CustomPaginator(PageNumberPagination):
    page_size = 10 # Number of objects to return in one page

    def generate_response(self, query_set, serializer_obj, request):
        try:
            page_data = self.paginate_queryset(query_set, request)
        except NotFoundError:
            return Response({"error": "No results found for the requested page"}, status=status.HTTP_400_BAD_REQUEST)

        serialized_page = serializer_obj(page_data, many=True)
        return self.get_paginated_response(serialized_page.data)


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


'''
class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = ()


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validate_data
        _, token = AuthToken.objects.create(user)
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": token
        })
'''


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({
            'login': super(LoginAPI, self).post(request, format=None).data,
            "user": UserDetailsSerializer(user, context=self.get_serializer_context()).data,
            })

# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user



@api_view(['GET'])
@permission_classes([IsAuthenticated, IsOwner])
def UserDetails(request):
    #user = get_object_or_404(User,  pk=request.user.id)
    user = request.user
    #all_transfered = InstantInvestment.objects.filter(investor=request.user.id, done=True).aggregate(Sum('transferable'))['transferable__sum']
    #all_conversion = InstantInvestment.objects.filter(investor=request.user.id, done=True).aggregate(Sum('conversion'))['conversion__sum']
    #profile = Investor.objects.filter(user=user).first()
    


    if request.method == 'GET':
        #serializer = UserDetailsSerializer(user)
        return Response({
        #'total_transfered': all_transfered if all_transfered else 0, 
        #'total_conversion': all_conversion if all_conversion else 0, 
        #'profile': profile.passport.url, 
        'user': UserDetailsSerializer(user).data})




class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







        
@api_view(['GET'])
def CategoryNews(request):
    category = Category.objects.all()
   
    
    if request.method == 'GET':
        
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)






class AllNewsList(ListAPIView):
    search_fields = ['title', 'content']
    filter_backends = (filters.SearchFilter,)
    pagination_class = LargeResultsSetPagination
    serializer_class = NewsDetailSerializer
    queryset = NewsDetails.objects.all()
    


   

@api_view(['GET',])
#@permission_classes([IsAuthenticated])
def AllNewsDetails(APIView):
    
   

    def get(self, request, *args, **kwargs):
        news = get_object_or_404(NewsDetails, pk=kwargs['pk'])
        serializer = NewsDetails(news)
        return Response(serializer.data)


@api_view(['GET'])
def AllNewsByID(request, pk):
    news  = get_object_or_404(NewsDetails, pk=pk)
    if request.method == 'GET':
        serializer = NewsDetailSerializer(news)
        return Response(serializer.data) 



@api_view(['GET'])
def AllNewsByCategory(request, category):
    category = get_object_or_404(Category, name=category)
    if request.method == 'GET':
        news = NewsDetails.objects.filter(category=category)
        serializer = NewsDetailSerializer(news, many=True)
        return Response(serializer.data) 






@api_view(['GET'])
#@permission_classes([AllowAny,])
def AllNewsByMedia(request, site):
    
    site = get_object_or_404(Site, name=site)
    if request.method == 'GET':
        if site:
            #paginator = PageNumberPagination()
            #paginator.page_size = 10
            pagination_class = api_settings.DEFAULT_PAGINATION_CLASS
            paginator = pagination_class()
            news = NewsDetails.objects.filter(site=site)
            result_page = paginator.paginate_queryset(news, request)
            serializer = NewsDetailSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({},status=status.HTTP_200_OK)




@api_view(['GET'])
def NewsSite(request):
    
    if request.method == 'GET':
        site = Site.objects.all()
        serializer = SiteSerializer(site, many=True)
        return Response(serializer.data)





@api_view(['GET', 'POST'])
#@permission_classes([IsAuthenticated])
def AllCommentListAPIView(request, pk):
    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    news = get_object_or_404(NewsDetails, id=pk)
   
    
    allnews = NewsComment.objects.filter(news=news.id)
    
    
    
    if request.method == 'GET':
       
        serializer = NewsCommentSerializer(allnews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        user = User.objects.filter(pk=request.user.id).first()
      
        print(user)

        
        data = request.data
        if isinstance(data, list):
            serializer = NewsCommentSerializer(data=request.data, many=True)
        else:
            serializer = NewsCommentSerializer(data=request.data)



        #user = Order.objects.create(user=orderuser, ref_code=create_ref_code())
        #serializer = NewsCommentSerializer(data=request.data)
        if serializer.is_valid():
            newscomment = NewsComment.save(user=user.id, news=news.id)
            return HttpResponse("Comment Was Created Successful", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CommentDetail(RetrieveUpdateDestroyAPIView):
    #queryset = NewsComment.objects.all()
    serializer_class = NewsCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwner]
    


    
    

class AddAuthor(ListCreateAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
   


