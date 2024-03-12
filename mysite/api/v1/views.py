from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .serializers import post_testserializers, CategorySerializer
from post.models import posttest, Category
from .permissions import IsOwnerOrReadOnly
from .paginations import StandardResultsSetPagination


"""@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly ])
def post_test(request):
    posts = posttest.objects.filter(status=True)
    if request.method == 'GET':
        serializer=post_testserializers(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=post_testserializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)"""


"""@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly ])
def post_deateil(request,id):
    posts = get_object_or_404(posttest,pk=id,status=True)
    if request.method == 'GET':
        serializer = post_testserializers(posts)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer=post_testserializers(posts, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method =='DELETE':
        posts.delete()
        return Response({'deteail':'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)
        """


"""class postlist(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = post_testserializers
    def get(self, request):
        posts = posttest.objects.filter(status=True)
        serializer=post_testserializers(posts, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer=post_testserializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)"""


"""class PostList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = post_testserializers
    queryset = posttest.objects.filter(status=True)"""


"""class singelpost(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = post_testserializers
    
    def get_object(self,id):
        post = get_object_or_404(posttest,pk=id,status=True)
        return post

    def get(self,request, id):
        post = self.get_object(id)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self,request, id):
        post = self.get_object(id)
        serializer=post_testserializers(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request, id):
        post = self.get_object(id)
        post.delete()
        return Response({'deteail':'item removed successfully'}, status=status.HTTP_204_NO_CONTENT)"""

"""class SingelPost(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = post_testserializers
    queryset = posttest.objects.filter(status=True)"""


class PostModelView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = post_testserializers
    queryset = posttest.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "author"]
    search_fields = ["titel"]
    ordering_fields = ["author__email", "published_date"]
    pagination_class = StandardResultsSetPagination


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
