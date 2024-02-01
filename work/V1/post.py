from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from work.models import Post
from work.serializers import PostSerializer


# bu foydalanuvchini o'zi uchun

class PostViewOne(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset().filter(user_id=self.request.user.id)
        return queryset

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
        serializer = self.serializer_class(data=data, instance=self.get_object(), partial=True)
        serializer.is_valid(raise_exception=True, )
        result = serializer.save()
        return Response(result.format())

    def delete(self, request, pk):
        try:
            obj = self.get_object()
        except Exception as e:
            return Response({"error": "Post topilmadi."})
        obj.delete()
        return Response({"natija": "bajarildi"})


class PostView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                return Response(Post.objcts.get(pk=pk).first().format())
            except:
                return Response({"error": "Bunday post mavjud emas"})
        posts = Post.objects.all().order_by("-pk")
        return Response([x.format() for x in posts])
