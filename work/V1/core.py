from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from work.models import Profile, Experience, Post, User
from work.serializers import ProfileSerializer, PostSerializer, ExperienceSerializer


class ProfileView(GenericAPIView):
    permission_classes = AllowAny,
    serializer_class = ProfileSerializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                return Response(Profile.objects.get(pk=pk).format())
            except:
                return Response({"error": "Qo'ysangchi bunaq user yoq "})

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()
        return Response(profile.format())

    def put(self, request, pk, *args, **kwargs):
        data = request.data
        root = Profile.objects.filter(pk=pk).first()
        if not root:
            return Response({"error": "bunaqa profile mavjud emas"})
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()
        return Response(profile.format())

    def delete(self, request, pk):
        try:
            Profile.objects.get(pk=pk).delete()
            return Response({"natija": "uchirildi"})
        except:
            return Response({"natija": "Bunaqa profile mavjud emas "})


class ExperienceView(GenericAPIView):
    permission_classes = AllowAny,
    serializer_class = ExperienceSerializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                return Response(Experience.objects.get(pk=pk).format())
            except:
                return Response({"error": "Bunaqa experience mavjud emas"})

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        profile = serializer.save()
        return Response(profile.format())

    def put(self, request, pk, *args, **kwargs):
        data = request.data
        root = Experience.objects.filter(pk=pk).first()
        if not root:
            return Response({"error": "bunaqa experince yoq"})
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True)
        experince = serializer.save()
        return Response(experince.format())

    def delete(self, request, pk):
        try:
            Experience.objects.get(pk=pk).delete()
            return Response({"natija": "bajarildi"})
        except:
            return Response({"error": "aldama jigar"})


class PostView(GenericAPIView):
    permission_classes = AllowAny,  # IsAuthenticated
    serializer_class = PostSerializer

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                return Response(Post.objcts.get(pk=pk).first().format())
            except:
                return Response({"error": "Bunday post mavjud emas"})
        posts = Post.objects.all().order_by("-pk")
        return Response([x.format() for x in posts])

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        post = serializer.save()
        return Response(post.format())

    def put(self, request, pk, *args, **kwargs):
        data = request.data
        root = Post.objects.filter(pk=pk).first()
        if not root:
            return Response({"error": "Bunday post mavjud emas !"})
        serializer = self.serializer_class(data=data, instance=root, partial=True)
        serializer.is_valid(raise_exception=True, )
        result = serializer.save()
        return Response(result.format())

    def delete(self, request, pk):
        try:
            Post.objects.get(pk=pk).delete()
            return Response({"natija": "bajarildi"})
        except:
            return Response({"error": " bunaqasi yo uxlama !"})

    def perfrom_update(self, serializer):
        result = serializer.save()
        if result.user != self.request.user:
            raise permissions.PermissionDonied("Siz bu postni o'zgartira olmaysiz")
