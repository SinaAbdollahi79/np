from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import post_testserializers
from post.models import posttest



@api_view(['GET', 'POST'])
def post_test(request):
    if request.method == 'GET':
        post=posttest.objects.filter(status=1)
        serializer=post_testserializers(post, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=post_testserializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)