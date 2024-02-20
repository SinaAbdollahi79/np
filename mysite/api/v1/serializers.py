from rest_framework import serializers

from post.models import posttest, Category



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']


class post_testserializers(serializers.ModelSerializer):
    category =CategorySerializer(many=True)
    #category = serializers.SlugRelatedField(many=True, slug_field='name',queryset=Category.objects.all())
    class Meta:
        model=posttest
        fields=['id', 'titel','published_date','updated_date','status','category']

    '''def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category']= CategorySerializer(instance.category).data
        return rep'''

