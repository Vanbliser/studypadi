from django.core.paginator import Paginator
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from account.models import User
from .models import Module, Submodule, Section, Topic, Question, Option, Quiz, Quiz_attempt, Response as ResponseModel
from .serializers import UserSerializer, CreateQuestionSerializer, GenerateQuizSerializer, SaveQuizSerializer, SubmitQuizSerializer, CreateQuizSerializer, SubmitMaterialSerializer

# Create your views here.

class ModulesView(GenericAPIView):
    
    def get(self, request):
        size = request.GET.get('size', 5)
        page = request.GET.get('page', 1)
        try:
            size = int(size)
            page = int(page)
        except ValueError:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Module.objects.all()
        paginator = Paginator(queryset, size)
        if page > paginator.num_pages or page < 1:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        page_obj = paginator.page(page)
        data = list(page_obj.object_list.values())
        return Response(
            {
                "size": size,
                "page": page,
                "total_pages": paginator.num_pages,
                "total_items": paginator.count,
                "results": data
            },
            status=status.HTTP_200_OK
        )

class SubmodulesView(GenericAPIView):
    
    def get(self, request):
        size = request.GET.get('size', 5)
        page = request.GET.get('page', 1)
        try:
            size = int(size)
            page = int(page)
        except ValueError:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Submodule.objects.all()
        paginator = Paginator(queryset, size)
        if page > paginator.num_pages or page < 1:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        page_obj = paginator.page(page)
        data = list(page_obj.object_list.values())
        return Response(
            {
                "size": size,
                "page": page,
                "total_pages": paginator.num_pages,
                "total_items": paginator.count,
                "results": data
            },
            status=status.HTTP_200_OK
        )

class SectionView(GenericAPIView):
    
    def get(self, request):
        size = request.GET.get('size', 5)
        page = request.GET.get('page', 1)
        try:
            size = int(size)
            page = int(page)
        except ValueError:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Section.objects.all()
        paginator = Paginator(queryset, size)
        if page > paginator.num_pages or page < 1:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        page_obj = paginator.page(page)
        data = list(page_obj.object_list.values())
        return Response(
            {
                "size": size,
                "page": page,
                "total_pages": paginator.num_pages,
                "total_items": paginator.count,
                "results": data
            },
            status=status.HTTP_200_OK
        )

class TopicView(GenericAPIView):
    
    def get(self, request):
        size = request.GET.get('size', 5)
        page = request.GET.get('page', 1)
        try:
            size = int(size)
            page = int(page)
        except ValueError:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Topic.objects.all()
        paginator = Paginator(queryset, size)
        if page > paginator.num_pages or page < 1:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        page_obj = paginator.page(page)
        data = list(page_obj.object_list.values())
        return Response(
            {
                "size": size,
                "page": page,
                "total_pages": paginator.num_pages,
                "total_items": paginator.count,
                "results": data
            },
            status=status.HTTP_200_OK
        )

class UserView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        email = request.user
        user = user = User.objects.get(email=email)
        if user:
            data = {
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            }
            return Response(data=data, status=status.HTTP_200_OK)
        return Response({'message': "Internal error! User not found! Please register again"})

class UserRevisionTestView(GenericAPIView):
    pass

class UserPrefilledQuizView(GenericAPIView):
    pass

class UserRealtimeQuizView(GenericAPIView):
    pass

class QuizView(GenericAPIView):
    pass

class GenerateQuizView(GenericAPIView):
    pass

class SaveQuizView(GenericAPIView):
    pass

class SubmitQuizView(GenericAPIView):
    pass

class CreateQuizView(GenericAPIView):
    pass

class CreateQuestionView(GenericAPIView):
    pass

class SubmitMaterialView(GenericAPIView):
    pass
