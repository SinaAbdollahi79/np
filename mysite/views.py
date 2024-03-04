from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


class PostTest(APIView):
    def get(self, request):
        return Response("hello world")


@api_view()
def post_test(request):
    return Response({"name": "test"})
