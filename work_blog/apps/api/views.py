from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from django.contrib.auth.models import User
from .serializers import UserSerializer, TagSerializer, BlogTypeSerializer, BlogSerializer
from .permissions import IsAdminUserOrReadOnly
from blog.models import BlogType, Tag, Blog


class UserListSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class BlogTypeListSet(viewsets.ModelViewSet):
    queryset = BlogType.objects.all()
    serializer_class = BlogTypeSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class TagListSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly,)


class BlogListSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = (DjangoModelPermissionsOrAnonReadOnly, IsAdminUserOrReadOnly)

    # 将blog和用户关联起来
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)