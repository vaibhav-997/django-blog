from rest_framework import serializers
from .models import Blog, Comments
from django.contrib.auth.models import User


# auth
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=150)
    
    def validate(self, user_data):
        if User.objects.filter(username=user_data['username']):
            raise serializers.ValidationError("Username already taken ! Please enter a different username")
        
        if User.objects.filter(username=user_data['email']):
            raise serializers.ValidationError("Email already exists")
        
        return user_data
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        
        return user
    
    


    
# blog 
class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['id', 'user','title' , 'description', 'image']
        

# comments
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'user','comment', 'blog']