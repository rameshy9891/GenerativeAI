from rest_framework import serializers
from .model import Post, Comment

class PostSerializer(serializers.modelSerializer):

    class Meta:  
        model= Post
        fields = ['id','username','caption','likes']

        class  CommentSerializer(serializers.ModelSerializer):

            class Meta:
                 model = Comment
                 fields= ['text']