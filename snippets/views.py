from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer

from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
# Create your views here.

from django.contrib.auth.models import User


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetListAPIView(ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# GenericAPIView
class SnippetListGenericView(ListModelMixin, CreateModelMixin, GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)



class SnippetDetailGenericView(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(self, request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)



# APIView based views
class SnippetListView(APIView):

    def get(self, request):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid() == True:
            serializer.save()
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class SnippetDetailView(APIView):

    def get(self, request, pk):
        try:
            snippet = Snippet.objects.get(id=pk)
        except Snippet.DoesNotExist as err:
            return Response({"message": str(err)}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SnippetSerializer(data=snippet)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def put(self, request, pk):
        try:
            snippet = Snippet.objects.get(id=pk)
        except Snippet.DoesNotExist as err:
            return Response({"message": str(err)}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        try:
            snippet = Snippet.objects.get(id=pk)
        except Snippet.DoesNotExist as err:
            return Response({"message": str(err)}, status=status.HTTP_404_NOT_FOUND)
        
        deleted_snippet = snippet.delete()
        serializer = SnippetSerializer(data=deleted_snippet)
        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)





# function based views, legacy code
@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(data={"message": "Item not found"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(data={"message": "Item not found"}, status=status.HTTP_204_NO_CONTENT)

