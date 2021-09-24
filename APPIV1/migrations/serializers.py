from rest_framework import serializers
from app.models import *
from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={
                                     "input_type":   "password"})
    #password2 = serializers.CharField(
    #    style={"input_type": "password"}, write_only=True, label="Confirm password")


    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    
class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ('name', 'logo') 



class NewsDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    site = SiteSerializer(read_only=True)
    #user = serializers.ReadOnlyField(source='owner.username')
    comment = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    many = True

    class Meta:
        model = NewsDetails
        fields = ('id', 'title', 'content', 'image_url', 'url', 'category', 'author',  'site', 'uploaded', 'comment', 'get_comment' ) 

    def get_coment_count(self, obj):
        return obj.comment.count()



class NewsCommentSerializer(serializers.ModelSerializer):

    


    user = serializers.ReadOnlyField(source='user.username')
    news = serializers.ReadOnlyField(source='news.title')
    many = True


   
    
    class Meta:
        model = NewsComment
        fields = "__all__"

        #read_only_fields = ('user', ) 





