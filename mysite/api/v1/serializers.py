from rest_framework import serializers
from django.contrib.auth import get_user_model
from post.models import posttest, Category


User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "email"]


class post_testserializers(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    author = AuthorSerializer()

    # author = serializers.SlugRelatedField(slug_field='email',queryset=User.objects.all())
    # category = serializers.SlugRelatedField(many=True, slug_field='name',queryset=Category.objects.all())
    class Meta:
        model = posttest
        # depth=1
        fields = [
            "id",
            "titel",
            "author",
            "content",
            "published_date",
            "updated_date",
            "status",
            "category",
        ]

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        user = self.context.get("request").user

        if not user.is_authenticated:
            rep.pop("category")
        return rep
