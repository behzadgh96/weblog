from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,JsonResponse
from django.views import generic

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins



from .models import Post,Comment
from .serializers import PostSerializer

#def methods with templates:

"""def index(request):
    return HttpResponse("<h1>welcome to my weblog</h1>")

def post_list(request):
    
    posts = Post.objects.all()
    context = {'posts':posts}
    return render (request,'post-templates/post-list.html', context=context)

def post_detail(request,post_id):
    
 try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return HttpResponseNotFound('<h1 style="font-family:arial;"><center>Sorry! Page Not Found</center></h1>')    
    
    comments = Comment.objects.filter(post=post)
    context = {'post':post,'comments':comments}
    return render (request,'post-templates/post-detail.html',context=context) """

#class methods with templates:

"""class PostList(generic.ListView):
    
    queryset = Post.objects.all()
    template_name = 'post-templates/post-list.html'
    context_object_name = 'posts'


class PostDetail(generic.DetailView):
    
    def get_context_data(self, **kwargs):
        context = super(PostDetail,self).get_context_data()
        context['comments'] = Comment.objects.filter(post=kwargs['object'].pk)
        return context
    
    model = Post
    template_name = 'post-templates/post-detail.html'"""


#api_views:

"""@api_view(['GET'])
def index(request):
    return Response('hello everyone we bach with rest frameworks!!!')"""

"""@api_view(['GET'])
def index(request):
    data = {"name":"behzad gholampoor",
    "age":26,}
    return Response(data,status=status.HTTP_404_NOT_FOUND)"""


#api_views_with_serializers(json-files):

"""@api_view(['get'])
def index(request):
    try:
        p = Post.objects.get(pk=2)
    except Post.DoesNotExist:
        return Response("Sorry! Page not found ")
    s = PostSerializer(p)        
    return Response(s.data)"""


"""@api_view(['GET','POST'])
def post_list(request, format=None):

    if request.method == 'GET':
        p = Post.objects.all()
        s = PostSerializer(p, many=True)
        return Response(s.data)

    elif request.method == 'POST':
        s = PostSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def post_detail(request,pk,format=None):
    try:
        p = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        s = PostSerializer(p)
        return Response(s.data)

    elif request.method == 'PUT':
        s = PostSerializer(p,data=request.data)            
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)    

    elif request.method == 'DELETE':
        p.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)"""

#API:class base views:

class post_list_view(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class post_detail_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer                

        






    

    
    
                            
       




    
    

        



