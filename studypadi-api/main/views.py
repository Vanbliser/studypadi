from django.core.paginator import Paginator
from django.db.models import Q
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
        try:
            user = user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'message': "User not found! Please register again"}, status=status.HTTP_404_NOT_FOUND)
        data = {
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
            user = user = User.objects.get(email=email)
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
            user = user = User.objects.get(email=email)
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
            user = user = User.objects.get(email=email)
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
            user = user = User.objects.get(email=email)
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
    
class UserQuizResponseView(GenericAPIView):
    pass

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
                pass
            else:
                return Response(
                    {
                        'quiz_id': quiz.id,
                        'module_title': quiz.module_id__title,
                        'submodule_title': quiz.submodule_id__title,
                        'section_title': quiz.section_id__title,
                        'topic_title': quiz.topic_id__title,
                        'num_of_questions': quiz.num_of_questions,
                        'created_at': quiz.created_at,
                        'created_by': f"{quiz.created_by__first_name} {quiz.created_by__last_name}"
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
            'module_id__title',
            'submodule_id__title',
            'section_id__title',
            'topic_id__title',
            'num_of_questions',
            'created_at',
            'created_by'
        ))
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
                    result.append(
                        {
                            'question': question.question,
                            'option': list(question.option_set.all())
                        }
                    )
                data = {
                    'name': quiz.name,
                    'module': quiz.module_id__title,
                    'submodule': quiz.submodule_id__title,
                    'section': quiz.section_id__title,
                    'topic': quiz.topic_id__title,
                    'number_of_questions': quiz.num_of_questions,
                    'created_at': quiz.created_at,
                    'created_by': f"{quiz.created_by__first_name} {quiz.created_by__last_name}",
                    'questions': result
                }
                return Response(data=data, status=status.HTTP_200_OK)
        return Response({'message': 'Invalid quiz id.'}, status=status.HTTP_400_BAD_REQUEST)

class GenerateQuizView(GenericAPIView):
    pass

class SaveQuizView(GenericAPIView):
    pass

class SubmitQuizView(GenericAPIView):
    pass

class CreateQuizView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        pass

class CreateQuestionView(GenericAPIView):
    pass

class SubmitMaterialView(GenericAPIView):
    pass
