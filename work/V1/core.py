from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from work.models import Profile, Experience, Post, User
from work.serializers import ProfileSerializer, PostSerializer, ExperienceSerializer




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
        user = User.objects.filter(email=data['email'])
        if not user:
            return Response({
                "error": " User mavjud emas "
            })
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



