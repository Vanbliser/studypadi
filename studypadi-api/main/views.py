from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from account.models import User
from django.db import transaction
from .models import Module, Submodule, Section, Topic, Question, Option, Quiz, Quiz_attempt, get_ai_gen_user, Response as ResponseModel
from .serializers import ModuleSerializer, SubmoduleSerializer, SectionSerializer, TopicSerializer, CreateQuestionListSerializer, GenerateQuizSerializer, SaveQuizSerializer, SubmitQuizSerializer, CreateQuizSerializer, SubmitMaterialSerializer
import random
from .ai import get_completion
import json
import re

# Create your views here.

class ModulesView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = ModuleSerializer

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
        serializer = self.serializer_class(instance=page_obj.object_list, many=True)
        return Response(
            {
                "size": size,
                "page": page,
                "total_pages": paginator.num_pages,
                "total_items": paginator.count,
                "results": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        user = User.objects.get(email=request.user)
        if user.user_role not in ['SUP', 'AID', 'EDU']:
            return Response({'message': "You don't have permission to create or update"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        if not isinstance(request.data, list):
            return Response({'message': 'List of objects required.'})
        errors = []
        returned_data = []
        combined = []
        for data in request.data:
            try:
                id = int(data.get("id"))
            except:
                errors.append({'error': f'Invalid {data.get("id")} id'})
                combined.append({'error': f'Invalid {data.get("id")} id'})
            else:
                try:
                    module = Module.objects.get(id=id)
                except Module.DoesNotExist:
                    errors.append({"error": f"ID {id} does not exist"})
                    combined.append({"error": f"ID {id} does not exist"})
                else:
                    serializer = self.serializer_class(instance=module, data=data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        returned_data.append(serializer.data)
                        combined.append(serializer.data)
                    else:
                        errors.append(serializer.errors)
                        combined.append(serializer.errors)
        if errors and returned_data:
            return Response(combined, status=status.HTTP_207_MULTI_STATUS)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(returned_data, status=status.HTTP_200_OK)

class SubmodulesView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SubmoduleSerializer

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
        serializer = self.serializer_class(many=True, instance=page_obj.object_list)
        return Response(
            {
                "size": size,
                "page": page,
                "total_pages": paginator.num_pages,
                "total_items": paginator.count,
                "results": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        user = User.objects.get(email=request.user)
        if user.user_role not in ['SUP', 'AID', 'EDU']:
            return Response({'message': "You don't have permission to create or update"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        if not isinstance(request.data, list):
            return Response({'message': 'List of objects required.'})
        errors = []
        returned_data = []
        combined = []
        for data in request.data:
            try:
                id = int(data.get("id"))
            except:
                errors.append({'error': f'Invalid {data.get("id")} id'})
                combined.append({'error': f'Invalid {data.get("id")} id'})
            else:
                try:
                    module = Submodule.objects.get(id=id)
                except Submodule.DoesNotExist:
                    errors.append({"error": f"ID {id} does not exist"})
                    combined.append({"error": f"ID {id} does not exist"})
                else:
                    serializer = self.serializer_class(instance=module, data=data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        returned_data.append(serializer.data)
                        combined.append(serializer.data)
                    else:
                        errors.append(serializer.errors)
                        combined.append(serializer.errors)
        if errors and returned_data:
            return Response(combined, status=status.HTTP_207_MULTI_STATUS)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(returned_data, status=status.HTTP_200_OK)

class SectionView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SectionSerializer
    
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
        serializer = self.serializer_class(many=True, instance=page_obj.object_list)
        return Response(
            {
                "size": size,
                "page": page,
                "total_pages": paginator.num_pages,
                "total_items": paginator.count,
                "results": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        user = User.objects.get(email=request.user)
        if user.user_role not in ['SUP', 'AID', 'EDU']:
            return Response({'message': "You don't have permission to create or update"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        if not isinstance(request.data, list):
            return Response({'message': 'List of objects required.'})
        errors = []
        returned_data = []
        combined = []
        for data in request.data:
            try:
                id = int(data.get("id"))
            except:
                errors.append({'error': f'Invalid {data.get("id")} id'})
                combined.append({'error': f'Invalid {data.get("id")} id'})
            else:
                try:
                    module = Section.objects.get(id=id)
                except Section.DoesNotExist:
                    errors.append({"error": f"ID {id} does not exist"})
                    combined.append({"error": f"ID {id} does not exist"})
                else:
                    serializer = self.serializer_class(instance=module, data=data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        returned_data.append(serializer.data)
                        combined.append(serializer.data)
                    else:
                        errors.append(serializer.errors)
                        combined.append(serializer.errors)
        if errors and returned_data:
            return Response(combined, status=status.HTTP_207_MULTI_STATUS)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(returned_data, status=status.HTTP_200_OK)

class TopicView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TopicSerializer

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
        serializer = self.serializer_class(many=True, instance=page_obj.object_list)
        return Response(
            {
                "size": size,
                "page": page,
                "total_pages": paginator.num_pages,
                "total_items": paginator.count,
                "results": serializer.data
            },
            status=status.HTTP_200_OK
        )

    def post(self, request):
        user = User.objects.get(email=request.user)
        if user.user_role not in ['SUP', 'AID', 'EDU']:
            return Response({'message': "You don't have permission to create or update"}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.serializer_class(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request):
        if not isinstance(request.data, list):
            return Response({'message': 'List of objects required.'})
        errors = []
        returned_data = []
        combined = []
        for data in request.data:
            try:
                id = int(data.get("id"))
            except:
                errors.append({'error': f'Invalid {data.get("id")} id'})
                combined.append({'error': f'Invalid {data.get("id")} id'})
            else:
                try:
                    module = Topic.objects.get(id=id)
                except Topic.DoesNotExist:
                    errors.append({"error": f"ID {id} does not exist"})
                    combined.append({"error": f"ID {id} does not exist"})
                else:
                    serializer = self.serializer_class(instance=module, data=data, partial=True)
                    if serializer.is_valid():
                        serializer.save()
                        returned_data.append(serializer.data)
                        combined.append(serializer.data)
                    else:
                        errors.append(serializer.errors)
                        combined.append(serializer.errors)
        if errors and returned_data:
            return Response(combined, status=status.HTTP_207_MULTI_STATUS)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(returned_data, status=status.HTTP_200_OK)

class UserView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        email = request.user
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': "User not found! Please register again"}, status=status.HTTP_404_NOT_FOUND)
        data = {
            'id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
        }
        return Response(data=data, status=status.HTTP_200_OK)

class UserQuizView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        email = request.user
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': "User not found! Please register again"}, status=status.HTTP_404_NOT_FOUND)

        size = request.GET.get('size', 5)
        page = request.GET.get('page', 1)
        try:
            size = int(size)
            page = int(page)
        except ValueError:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        quiz_id = request.GET.get('quizid', None)
        if quiz_id:
            queryset = Quiz_attempt.objects.filter(taken_by=user, quiz_id=quiz_id)
        else:
            queryset = Quiz_attempt.objects.filter(taken_by=user)

        paginator = Paginator(queryset, size)
        if page > paginator.num_pages or page < 1:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        page_obj = paginator.page(page)
        data = list(page_obj.object_list.values('quiz_id', 'score', 'status', 'time_taken'))
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
        
class UserPrefilledQuizView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        email = request.user
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': "User not found! Please register again"}, status=status.HTTP_404_NOT_FOUND)

        size = request.GET.get('size', 5)
        page = request.GET.get('page', 1)
        try:
            size = int(size)
            page = int(page)
        except ValueError:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        quiz_id = request.GET.get('quizid', None)
        if quiz_id:
            queryset = Quiz_attempt.objects.filter(taken_by=user, quiz_id=quiz_id, quiz_id__created_by__user_role='EDU')
        else:
            queryset = Quiz_attempt.objects.filter(taken_by=user, quiz_id__created_by__user_role='EDU')

        paginator = Paginator(queryset, size)
        if page > paginator.num_pages or page < 1:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        page_obj = paginator.page(page)
        data = list(page_obj.object_list.values('quiz_id', 'score', 'status', 'time_taken'))
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

class UserRealtimeQuizView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        email = request.user
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': "User not found! Please register again"}, status=status.HTTP_404_NOT_FOUND)

        size = request.GET.get('size', 5)
        page = request.GET.get('page', 1)
        try:
            size = int(size)
            page = int(page)
        except ValueError:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        quiz_id = request.GET.get('quizid', None)
        if quiz_id:
            queryset = Quiz_attempt.objects.filter(taken_by=user, quiz_id=quiz_id, quiz_id__created_by__user_role='SUP')
        else:
            queryset = Quiz_attempt.objects.filter(taken_by=user, quiz_id__created_by__user_role='SUP')

        paginator = Paginator(queryset, size)
        if page > paginator.num_pages or page < 1:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        page_obj = paginator.page(page)
        data = list(page_obj.object_list.values('quiz_id', 'score', 'status', 'time_taken'))
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

class UserRevisionTestQuizView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        email = request.user
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': "User not found! Please register again"}, status=status.HTTP_404_NOT_FOUND)

        size = request.GET.get('size', 5)
        page = request.GET.get('page', 1)
        try:
            size = int(size)
            page = int(page)
        except ValueError:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        quiz_id = request.GET.get('quizid', None)
        if quiz_id:
            queryset = Quiz_attempt.objects.filter(taken_by=user, quiz_id=quiz_id, quiz_id__created_by__user_role='AIG')
        else:
            queryset = Quiz_attempt.objects.filter(taken_by=user, quiz_id__created_by__user_role='AIG')

        paginator = Paginator(queryset, size)
        if page > paginator.num_pages or page < 1:
            return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
        
        page_obj = paginator.page(page)
        data = list(page_obj.object_list.values('quiz_id', 'score', 'status', 'time_taken'))
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
    
class QuizView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        moduleid = request.GET.get('moduleid', 0)
        submoduleid = request.GET.get('submoduleid', 0)
        sectionid = request.GET.get('sectionid', 0)
        topicid = request.GET.get('topicid', 0)
        educatorid = request.GET.get('educatorid', 0)
        quizid = request.GET.get('quizid', 0)
        educatorname = request.GET.get('educatorname', None)
        quizname = request.GET.get('quizname', None)
        search = request.GET.get('search', None)
        size = request.GET.get('size', 5)
        page = request.GET.get('page', 1)
        try:
            moduleid = int(moduleid)
            submoduleid = int(submoduleid)
            sectionid = int(sectionid)
            topicid = int(topicid)
            educatorid = int(educatorid)
            quizid = int(quizid)
            size = int(size)
            page = int(page)
        except ValueError:
            return Response({'message': 'Invalid query parameters. Number expected.'}, status=status.HTTP_400_BAD_REQUEST)

        if quizid:
            try:
                quiz = Quiz.objects.get(id=quizid)
            except Quiz.DoesNotExist:
                return Response({'message': 'Not found for quizid value'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response(
                    {
                        'quizid': quiz.id,
                        'name': quiz.name,
                        'module': getattr(quiz.module_id, 'title', None),
                        'submodule': getattr(quiz.submodule_id, 'title', None),
                        'section': getattr(quiz.section_id, 'title', None),
                        'topic': getattr(quiz.topic_id, 'title', None),
                        'number_of_questions': quiz.num_of_questions,
                        'created_at': quiz.created_at,
                    },
                    status=status.HTTP_200_OK
                )
        if educatorid:
            try:
                educator = User.objects.get(id=educatorid)
            except User.DoesNotExist:
                pass
            else:
                if topicid:
                    queryset = Quiz.objects.filter(topic_id=topicid, created_by=educator)
                elif sectionid:
                    queryset = Quiz.objects.filter(section_id=sectionid, created_by=educator)
                elif submoduleid:
                    queryset = Quiz.objects.filter(submodule_id=submoduleid, created_by=educator)
                elif moduleid:
                    queryset = Quiz.objects.filter(module_id=moduleid, created_by=educator)
                else:
                    queryset = Quiz.objects.filter(created_by=educator)
        else:
            if topicid:
                queryset = Quiz.objects.filter(topic_id=topicid)
            elif sectionid:
                queryset = Quiz.objects.filter(section_id=sectionid)
            elif submoduleid:
                queryset = Quiz.objects.filter(submodule_id=submoduleid)
            elif moduleid:
                queryset = Quiz.objects.filter(module_id=moduleid)
            elif quizname and educatorname and search:
                queryset = Quiz.objects.filter(
                    Q(name__icontains=quizname) |
                    Q(created_by__first_name__icontains=educatorname) |
                    Q(created_by__last_name__icontains=educatorname) |
                    Q(name__icontains=search) |
                    Q(created_by__first_name__icontains=search) |
                    Q(created_by__last_name__icontains=search)
                )
            elif quizname and educatorname:
                queryset = Quiz.objects.filter(
                    Q(name__icontains=quizname) |
                    Q(created_by__first_name__icontains=educatorname) |
                    Q(created_by__last_name__icontains=educatorname)
                )
            elif quizname and search:
                queryset = Quiz.objects.filter(
                    Q(name__icontains=quizname) |
                    Q(name__icontains=search) |
                    Q(created_by__first_name__icontains=search) |
                    Q(created_by__last_name__icontains=search)
                )
            elif search and educatorname:
                queryset = Quiz.objects.filter(
                    Q(created_by__first_name__icontains=educatorname) |
                    Q(created_by__last_name__icontains=educatorname) |
                    Q(name__icontains=search) |
                    Q(created_by__first_name__icontains=search) |
                    Q(created_by__last_name__icontains=search)
                )
            elif quizname:
                queryset = Quiz.objects.filter(name__icontains=quizname)
            elif educatorname:
                queryset = Quiz.objects.filter(
                    Q(created_by__first_name__icontains=educatorname) |
                    Q(created_by__last_name__icontains=educatorname)
                )
            elif search:
                queryset = Quiz.objects.filter(
                    Q(name__icontains=search) |
                    Q(created_by__first_name__icontains=search) |
                    Q(created_by__last_name__icontains=search)
                )
            else:
                queryset = Quiz.objects.all()

            paginator = Paginator(queryset, size)
            if page > paginator.num_pages or page < 1:
                return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
            
            page_obj = paginator.page(page)
            data = list(page_obj.object_list.values(
                'id',
                'name',
                'module_id__title',
                'submodule_id__title',
                'section_id__title',
                'topic_id__title',
                'num_of_questions',
                'created_at'
            ))
            key_mapping = {
                'id': 'quizid',
                'module_id__title': 'module',
                'submodule_id__title': 'submodule',
                'section_id__title': 'section',
                'topic_id__title': 'topic',
                'num_of_questions': 'number_of_questions'
            }
            data = [
                {key_mapping.get(k, k): v for k, v in item.items()}
                for item in data
            ]
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

class QuizQuestionsView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):

        quizid = request.GET.get('quizid', 0)
        if quizid:
            try:
                quizid = int(quizid)
            except ValueError:
                return Response({'message': 'Invalid query parameters. Number expected.'}, status=status.HTTP_400_BAD_REQUEST)

            try:
                quiz = Quiz.objects.get(id=quizid)
            except Quiz.DoesNotExist:
                return Response({'message': 'Quiz not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                result = []
                questions = quiz.questions.prefetch_related('option_set').all()
                for question in questions:
                    options = [{'id': option.id, 'option': option.option, 'is_answer': option.is_answer} for option in question.option_set.all()]
                    result.append(
                        {
                            'question_id': question.id,
                            'question': question.question,
                            'option': options
                        }
                    )
                data = {
                    'id': quiz.id,
                    'name': quiz.name,
                    'module': getattr(quiz.module_id, 'title', None),
                    'submodule': getattr(quiz.submodule_id, 'title', None),
                    'section': getattr(quiz.section_id, 'title', None),
                    'topic': getattr(quiz.topic_id, 'title', None),
                    'number_of_questions': quiz.num_of_questions,
                    'created_at': quiz.created_at,
                    'created_by': f"{quiz.created_by.first_name} {quiz.created_by.last_name}",
                    'questions': result
                }
                return Response(data=data, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid quiz id.'}, status=status.HTTP_400_BAD_REQUEST)

class CreateQuestionView(GenericAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = CreateQuestionListSerializer

    def post(self, request):
        data = request.data

        if not isinstance(data, list):
            return Response({'error': 'Expected a list of questions'}, status=status.HTTP_400_BAD_REQUEST)
        
        user =  User.objects.get(email=request.user)
        serializer = self.serializer_class(data=data, context={'user': user})
        if serializer.is_valid(raise_exception=True):
            print('serializer.data', serializer.data)
            print('serializer.validated_data', serializer.validated_data)
            if user.user_role not in ['EDU', 'SUP', 'AIG']:
                return Response({'message': 'Unauthorised request'}, status=status.HTTP_401_UNAUTHORIZED)
            
            try:
                with transaction.atomic():
                    questions = []
                    for question_data in serializer.validated_data:
                        options_data = question_data.pop('options')
                        question = Question.objects.create(**question_data)
                        Option.objects.bulk_create([
                            Option(
                                question_id=question,
                                option=option_data['option'],
                                is_answer=option_data['is_answer']
                            )
                            for option_data in options_data
                        ])
                        response = {
                            'id': question.id,
                            'module': getattr(question.module_id, 'title', None),
                            'submodule': getattr(question.submodule_id, 'title', None),
                            'section': getattr(question.section_id, 'title', None),
                            'topic': getattr(question.topic_id, 'title', None),
                            'difficulty': question.difficulty,
                            'question_type': question.question_type,
                            'question': question.question
                        }
                        cleaned_data = {k: v for k, v in response.items() if v is not None}
                        questions.append(cleaned_data)
                    print(questions)
                    return Response(questions, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GenerateQuizView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = GenerateQuizSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):

            email = request.user
            try:
                user =  User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'message': 'User not found. Please register'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            validated_data = serializer.validated_data
            name = validated_data.get("name")
            module_id = validated_data.get("module_id")
            submodule_id = validated_data.get("submodule_id")
            section_id = validated_data.get("section_id")
            topic_id = validated_data.get("topic_id")
            question_type = validated_data.get("question_type")
            difficulty = validated_data.get("difficulty")
            algorithm = validated_data.get("algorithm")
            num_of_questions = validated_data.get("num_of_questions")

            # Build base filter
            question_filter = Q()
            if topic_id:
                question_filter &= Q(topic_id=topic_id)
            elif section_id:
                question_filter &= Q(section_id=section_id)
            elif submodule_id:
                question_filter &= Q(submodule_id=submodule_id)
            elif module_id:
                question_filter &= Q(module_id=module_id)

            # Handle difficulty filter
            if difficulty == "EAS":
                question_filter &= Q(difficulty="EAS")
            elif difficulty == "MED":
                question_filter &= Q(difficulty="MED")
            elif difficulty == "HRD":
                question_filter &= Q(difficulty="HRD")
            elif difficulty == "EAM":
                question_filter &= Q(difficulty__in=["EAS", "MED"])
            elif difficulty == "EAH":
                question_filter &= Q(difficulty__in=["EAS", "HRD"])
            elif difficulty == "EMD":
                question_filter &= Q(difficulty__in=["EAS", "MED", "HRD"])

            # Handle question type filter
            if question_type == "AIG":
                question_filter &= Q(created_by__user_role="AIG")
            elif question_type == "EDQ":
                question_filter &= Q(created_by__user_role="EDU")
            elif question_type == "PAQ":
                question_filter &= Q(created_by__user_role="SUP")
            elif question_type == "AIE":
                question_filter &= Q(created_by__user_role__in=["AIG", "EDU"])
            elif question_type == "AIP":
                question_filter &= Q(created_by__user_role__in=["AIG", "SUP"])

            # Fetch questions based on algorithm
            if algorithm == "RAD":
                questions = list(Question.objects.filter(question_filter))
                random.shuffle(questions)
                questions = questions[:num_of_questions]

            elif algorithm == "MOF":
                failed_questions = Response.objects.filter(
                    quiz_attempt__taken_by=user,
                    chosen_option__is_answer=False
                ).values_list("question_id", flat=True)
                questions = list(Question.objects.filter(id__in=failed_questions).filter(question_filter))
                questions = questions[:num_of_questions]

            elif algorithm == "LEA":
                attempted_questions = Response.objects.filter(
                    quiz_attempt__taken_by=user
                ).values_list("question_id", flat=True)
                questions = list(Question.objects.exclude(id__in=attempted_questions).filter(question_filter))
                questions = questions[:num_of_questions]

            # Handle case where no questions are generated
            if not questions:
                return Response({"detail": "No questions available for the provided criteria."}, status=status.HTTP_404_NOT_FOUND)

            # Create quiz and attach questions
            num = len(questions)
            args = {
                'name': name,
                'module_id': module_id,
                'submodule_id': submodule_id,
                'section_id': section_id,
                'topic_id': topic_id,
                'num_of_questions': num
            }
            cleaned_args = {key: value for key, value in args.items() if value is not None}
            quiz = Quiz.objects.create(**cleaned_args)
            quiz.questions.set(questions)

            # Prepare response data
            quiz_data = {
                "id": quiz.id,
                "name": quiz.name,
                "num_of_questions": num
            }
            return Response(quiz_data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubmitMaterialView(GenericAPIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = SubmitMaterialSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            validated_data = serializer.validated_data
            name = validated_data.get("name", "AI Gen")
            text = validated_data.get("text")
            num_of_questions = validated_data.get("num_of_questions")
            response = get_completion(text=text, num_of_questions=num_of_questions)
            response = re.search(r'\[.*?(?:\[.*?\].*?)*\]', response, re.DOTALL).group(0)
            print(response)
            # Parse the JSON response
            try:
                questions_data = json.loads(response)
            except json.JSONDecodeError:
                return Response({"error": f"""Failed to parse question from the LLM response."""}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            with transaction.atomic():
                # Create a Quiz instance
                quiz = Quiz.objects.create(
                    name=name,
                    num_of_questions=len(questions_data),
                    created_by=get_ai_gen_user()
                )

                # Create Question and Option instances
                for question_data in questions_data:
                    question_text = question_data.get("question")
                    options = question_data.get("options", [])
                    difficulty = question_data.get("difficulty")
                    if difficulty not in ["EAS", "MED", "HRD"]:
                        difficulty = "EAS"

                    # Create the Question instance
                    question = Question.objects.create(
                        question=question_text,
                        created_by=get_ai_gen_user(),
                        question_type="AIG",
                        difficulty=difficulty
                    )
                    quiz.questions.add(question)

                    # Create Option instances
                    for option_data in options:
                        Option.objects.create(
                            question_id=question,
                            option=option_data["text"],
                            is_answer=option_data["is_answer"]
                        )
                data = {
                    "id": quiz.id,
                    "name": quiz.name,
                    "num_of_questions": quiz.num_of_questions
                }

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        id = request.GET.get('id')
        if id:
            try:
                question = Question.objects.get(id=int(id))
            except Question.DoesNotExist:
                return Response({'message': 'Qustion with id not found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                data = {
                    'id': question.id,
                    'module': getattr(question.module_id, 'title', None),
                    'submodule': getattr(question.submodule_id, 'title', None),
                    'section': getattr(question.section_id, 'title', None),
                    'topic': getattr(question.topic_id, 'title', None),
                    'question_type': question.question_type,
                    'difficulty': question.difficulty,
                    'question': question.question
                }
                return Response(data, status=status.HTTP_200_OK)
        else:
            size = request.GET.get('size', 5)
            page = request.GET.get('page', 1)
            try:
                size = int(size)
                page = int(page)
            except ValueError:
                return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
            
            queryset = Question.objects.all()
            paginator = Paginator(queryset, size)
            if page > paginator.num_pages or page < 1:
                return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)
            
            page_obj = paginator.page(page)

            data = list(page_obj.object_list.values(
                'id',
                'module_id__title',
                'submodule_id__title',
                'section_id__title',
                'topic_id__title',
                'question_type',
                'difficulty',
                'question'
            ))
            key_mapping = {
                'module_id__title': 'module',
                'submodule_id__title': 'submodule',
                'section_id__title': 'section',
                'topic_id__title': 'topic',
            }
            data = [
                {key_mapping.get(k, k): v for k, v in item.items()}
                for item in data
            ]
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

class UserQuizResponseView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Get query parameters
        quiz_id = request.GET.get('quizid')
        user = request.user
        size = int(request.GET.get('size', 5))
        page = int(request.GET.get('page', 1))

        try:
            if quiz_id:
                # Fetch the specific `Quiz_attempt`
                attempt = Quiz_attempt.objects.filter(taken_by=user, quiz_id=quiz_id).prefetch_related('response_set__chosen_option', 'quiz_id__questions__option_set').first()
                if not attempt:
                    return Response({'message': 'Quiz attempt not found'}, status=status.HTTP_404_NOT_FOUND)

                # Map questions to responses
                question_to_response = {res.question_id.id: res for res in attempt.response_set.all()}
                questions = attempt.quiz_id.questions.prefetch_related('option_set').all()

                # Serialize the `Quiz_attempt` and its associated `Response` objects
                quiz_attempt_data = {
                    "quiz_id": attempt.quiz_id.id,
                    "score": attempt.score,
                    "status": attempt.status,
                    "time_taken": attempt.time_taken,
                    "responses": [
                        {
                            "question_id": ques.id,
                            "question": ques.question,
                            "option_1_id": opt[0].id if len(opt) > 0 else None,
                            "option_1": opt[0].option if len(opt) > 0 else None,
                            "option_2_id": opt[1].id if len(opt) > 1 else None,
                            "option_2": opt[1].option if len(opt) > 1 else None,
                            "option_3_id": opt[2].id if len(opt) > 2 else None,
                            "option_3": opt[2].option if len(opt) > 2 else None,
                            "option_4_id": opt[3].id if len(opt) > 3 else None,
                            "option_4": opt[3].option if len(opt) > 3 else None,
                            "chosen_option_id": question_to_response.get(ques.id).chosen_option.id if ques.id in question_to_response else None
                        }
                        for ques in questions
                        for opt in [list(ques.option_set.all())]  # Fetch options only once per question
                    ]
                }
                return Response(quiz_attempt_data, status=status.HTTP_200_OK)

            else:
                # Fetch all `Quiz_attempt` objects for the user
                queryset = Quiz_attempt.objects.filter(taken_by=user).prefetch_related('response_set__chosen_option', 'quiz_id__questions__option_set')

                # Apply pagination
                paginator = Paginator(queryset, size)
                if page > paginator.num_pages or page < 1:
                    return Response({'message': 'Invalid query parameters'}, status=status.HTTP_400_BAD_REQUEST)

                page_obj = paginator.page(page)

                # Serialize data
                results = []
                for attempt in page_obj.object_list:
                    question_to_response = {res.question_id.id: res for res in attempt.response_set.all()}
                    questions = attempt.quiz_id.questions.prefetch_related('option_set').all()

                    quiz_attempt_data = {
                        "quiz_id": attempt.quiz_id.id,
                        "score": attempt.score,
                        "status": attempt.status,
                        "time_taken": attempt.time_taken,
                        "responses": [
                            {
                                "question_id": ques.id,
                                "question": ques.question,
                                "option_1_id": opt[0].id if len(opt) > 0 else None,
                                "option_1": opt[0].option if len(opt) > 0 else None,
                                "option_2_id": opt[1].id if len(opt) > 1 else None,
                                "option_2": opt[1].option if len(opt) > 1 else None,
                                "option_3_id": opt[2].id if len(opt) > 2 else None,
                                "option_3": opt[2].option if len(opt) > 2 else None,
                                "option_4_id": opt[3].id if len(opt) > 3 else None,
                                "option_4": opt[3].option if len(opt) > 3 else None,
                                "chosen_option_id": question_to_response.get(ques.id).chosen_option.id if ques.id in question_to_response else None
                            }
                            for ques in questions
                            for opt in [list(ques.option_set.all())]
                        ]
                    }
                    results.append(quiz_attempt_data)

                # Response data
                response_data = {
                    "size": size,
                    "page": page,
                    "total_pages": paginator.num_pages,
                    "total_items": paginator.count,
                    "results": results,
                }
                return Response(response_data, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SaveQuizView(GenericAPIView):
    pass

class SubmitQuizView(GenericAPIView):
    pass

class CreateQuizView(GenericAPIView):
    pass
