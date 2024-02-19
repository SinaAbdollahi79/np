from rest_framework import serializers

from post.models import posttest

class post_testserializers(serializers.ModelSerializer):
    class Meta:
        model=posttest
        fields=['id', 'titel','published_date','updated_date','status']
