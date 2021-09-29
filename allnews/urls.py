"""allnews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions



from django.contrib import admin
from django.urls import path, include, re_path
from app.views import *
from APPIV1.views import *
from knox import views as knox_views



schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    #path('', include('web.urls')),
    #path(r'swagger-docs/', schema_view),
    

    path('admin/', admin.site.urls),



    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('sport/<str:punch>/<str:sport>/', PunchSport, name='index'),
    path('news/<str:punch>/<str:news>/', PunchNews, name='index'),
    path('metro/<str:punch>/<str:metro>/', PunchMetro, name='index'),
    path('politics/<str:punch>/<str:politics>/', PunchPolitics, name='index'),
    path('business/<str:punch>/<str:business>/', PunchBusiness, name='index'),
    path('editorial/<str:punch>/<str:editorial>/', PunchEditorial, name='index'),
    path('columns/<str:punch>/<str:columns>/', PunchColumns, name='index'),
    path('opinion/<str:punch>/<str:opinion>/', PunchOpinion, name='index'),

    path('sport/<str:premium>/<str:sport>', PremiumSport, name='index'),
    path('top_news/<str:premium>/<str:top_news>', PremiumTopNews, name='index'),
    path('headline/<str:premium>/<str:headline>', PremiumHeadline, name='index'),
    path('fashion/<str:premium>/<str:fashion>', PremiumFashion, name='index'),
    path('health/<str:premium>/<str:health>', PremiumHealth, name='index'),





    #path('api/', include('APPIV1.urls'))

    path('api/category/', CategoryNews, name='allcategory'),
    


    path('api/news/', AllNewsList.as_view(), name='all_news'),

    
   

    path('api/allnewsbycategory/<str:category>', AllNewsByCategory, name='category_news'),
    path('api/newsbymedia/<str:site>', AllNewsByMedia, name='site_news'),


    

    path('api/site/', NewsSite, name='Site'),
    

    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginView.as_view(), name='login'),

    #path('api/userlogin/', LoginAPI.as_view(), name='user-login'),
    path('api/userdetail/', UserDetails, name='user-detail'),


    
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

    
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='reset_password')),
    path('api/user/', UserAPI.as_view(), name='user'),


    path('api/allcomment/<int:pk>/', AllCommentListAPIView, name='comment_by_news'),

    path('api/addnewscomment/<int:pk>', CommentDetail.as_view(), name='add_comment_news'),


    
    path('api/newsbyid/<int:pk>', AllNewsByID, name='news-details-id'),

    path('api/addauthor/', AddAuthor.as_view(), name='add-author'),

 

 

  


   




    

 
    
]
