from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [ 'id', 'title', 'body', 'created_at']
        # , 'update_at'