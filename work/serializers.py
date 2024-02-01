from rest_framework import serializers

from work.models import  Post, Friend, Experience, PostImgs


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = "__all__"


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class PostImgsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImgs
        fields = "__all__"

