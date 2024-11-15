from django.core.paginator import Paginator
from django.db.models import Q
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from account.models import User
from django.db import transaction
from .models import Module, Submodule, Section, Topic, Question, Option, Quiz, Quiz_attempt, Response as ResponseModel
from .serializers import ModuleSerializer, SubmoduleSerializer, SectionSerializer, TopicSerializer, CreateQuestionListSerializer, GenerateQuizSerializer, SaveQuizSerializer, SubmitQuizSerializer, CreateQuizSerializer, SubmitMaterialSerializer

# Create your views here.

class ModulesView(GenericAPIView):
    permission_classes = [IsAuthenticated]

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
        data = list(page_obj.object_list.values('id', 'title', 'description'))
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

    def post(self, request):
        serializer = ModuleSerializer(data=request.data, context={'request': request}, many=True)

        if not isinstance(request.data, list):
            return Response({"detail": "Request data must be a list"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(email=request.user)
        if user.user_role not in ['SUP', 'AID', 'EDU']:
            return Response({'message': "You don't have permission to create or update"}, status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            instances = []
            for data in serializer.validated_data:
                id = data.get('id', None)
                if id:
                    module = Module.objects.filter(id=int(id)).first()
                    if module:
                        for attr, value in data.items():
                            setattr(module, attr, value)
                        module.save()
                        instances.append(module)
                    else:
                        module = Module.objects.create(title=data['title'], description=data['description'], created_by=user)
                        instances.append(module)
                else:
                    module = Module.objects.create(title=data['title'], description=data['description'], created_by=user)
                    instances.append(module)

            # Serialize the results
            response_serializer = ModuleSerializer(instances, many=True)
            return Response(response_serializer.data, status=status.HTTP_200_OK)
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubmodulesView(GenericAPIView):
    permission_classes = [IsAuthenticated]

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
        data = list(page_obj.object_list.values('id', 'title', 'description', 'module_id'))
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

    def post(self, request):
        serializer = SubmoduleSerializer(data=request.data, context={'request': request}, many=True)

        if not isinstance(request.data, list):
            return Response({"detail": "Request data must be a list"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(email=request.user)
        if user.user_role not in ['SUP', 'AID', 'EDU']:
            return Response({'message': "You don't have permission to create or update"}, status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            instances = []
            for data in serializer.validated_data:
                args = {}
                id = data.get('id', None)
                module_id = data.get('module_id', None)
                module = Module.objects.filter(id=module_id).first()
                if module:
                    args['module_id'] = module
                    data['module_id'] = module
                else:
                    del data['module_id']
                if id:
                    submodule = Submodule.objects.filter(id=int(id)).first()
                    if submodule:
                        for attr, value in data.items():
                            setattr(submodule, attr, value)
                        submodule.save()
                        instances.append({
                            "id": submodule.id,
                            "module_id": submodule.module_id.id,
                            "title": submodule.title,
                            "description": submodule.description
                        })
                    else:
                        submodule = Submodule.objects.create(title=data['title'], description=data['description'], created_by=user, **args)
                        instances.append({
                            "id": submodule.id,
                            "module_id": submodule.module_id.id,
                            "title": submodule.title,
                            "description": submodule.description
                        })
                else:
                    submodule = Submodule.objects.create(title=data['title'], description=data['description'], created_by=user, **args)
                    instances.append({
                        "id": submodule.id,
                        "module_id": submodule.module_id.id,
                        "title": submodule.title,
                        "description": submodule.description
                    })
            return Response(instances, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SectionView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    
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
        data = list(page_obj.object_list.values('id', 'title', 'description', 'submodule_id'))
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

    def post(self, request):
        serializer = SectionSerializer(data=request.data, context={'request': request}, many=True)

        if not isinstance(request.data, list):
            return Response({"detail": "Request data must be a list"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(email=request.user)
        if user.user_role not in ['SUP', 'AID', 'EDU']:
            return Response({'message': "You don't have permission to create or update"}, status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            instances = []
            for data in serializer.validated_data:
                args = {}
                id = data.get('id', None)
                submodule_id = data.get('submodule_id', None)
                submodule = Submodule.objects.filter(id=submodule_id).first()
                if submodule:
                    args['submodule_id'] = submodule
                    data['submodule_id'] = submodule
                else:
                    del data['submodule_id']
                if id:
                    section = Section.objects.filter(id=int(id)).first()
                    if section:
                        for attr, value in data.items():
                            setattr(section, attr, value)
                        section.save()
                        instances.append({
                            "id": section.id,
                            "submodule_id": section.submodule_id.id,
                            "title": section.title,
                            "description": section.description
                        })
                    else:
                        section = Section.objects.create(title=data['title'], description=data['description'], created_by=user, **args)
                        instances.append({
                            "id": section.id,
                            "submodule_id": section.submodule_id.id,
                            "title": section.title,
                            "description": section.description
                        })
                else:
                    section = Section.objects.create(title=data['title'], description=data['description'], created_by=user, **args)
                    instances.append({
                        "id": section.id,
                        "module_id": section.submodule_id.id,
                        "title": section.title,
                        "description": section.description
                    })
            return Response(instances, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TopicView(GenericAPIView):
    permission_classes = [IsAuthenticated]

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
        data = list(page_obj.object_list.values('id', 'title', 'description', 'section_id'))
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

    def post(self, request):
        serializer = TopicSerializer(data=request.data, context={'request': request}, many=True)

        if not isinstance(request.data, list):
            return Response({"detail": "Request data must be a list"}, status=status.HTTP_400_BAD_REQUEST)
        user = User.objects.get(email=request.user)
        if user.user_role not in ['SUP', 'AID', 'EDU']:
            return Response({'message': "You don't have permission to create or update"}, status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            instances = []
            for data in serializer.validated_data:
                args = {}
                id = data.get('id', None)
                section_id = data.get('section_id', None)
                section = Section.objects.filter(id=section_id).first()
                if section:
                    args['section_id'] = section
                    data['section_id'] = section
                else:
                    del data['section_id']
                if id:
                    topic = Topic.objects.filter(id=int(id)).first()
                    if topic:
                        for attr, value in data.items():
                            setattr(topic, attr, value)
                        topic.save()
                        instances.append({
                            "id": topic.id,
                            "section_id": topic.section_id.id,
                            "title": topic.title,
                            "description": topic.description
                        })
                    else:
                        topic = Topic.objects.create(title=data['title'], description=data['description'], created_by=user, **args)
                        instances.append({
                            "id": topic.id,
                            "section_id": topic.section_id.id,
                            "title": topic.title,
                            "description": topic.description
                        })
                else:
                    topic = Topic.objects.create(title=data['title'], description=data['description'], created_by=user, **args)
                    instances.append({
                        "id": topic.id,
                        "section_id": topic.section_id.id,
                        "title": topic.title,
                        "description": topic.description
                    })
            return Response(instances, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
                        'quiz_id': quiz.id,
                        'module_title': quiz.module_id.title,
                        'submodule_title': quiz.submodule_id.title,
                        'section_title': quiz.section_id.title,
                        'topic_title': quiz.topic_id.title,
                        'num_of_questions': quiz.num_of_questions,
                        'created_at': quiz.created_at,
                        'created_by': f"{quiz.created_by.first_name} {quiz.created_by.last_name}"
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
        
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            email = request.user
            try:
                user =  User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({'message': 'User not found. Please register'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                if user.user_role not in ['EDU', 'SUP', 'AIG']:
                    return Response({'message': 'Unauthorised request'}, status=status.HTTP_401_UNAUTHORIZED)
            
            try:
                with transaction.atomic():
                    questions = []
                    for question_data in serializer.validated_data:
                        # Extract options data
                        options_data = question_data.pop('options')

                        # Extract return data
                        return_data = question_data.pop('return')

                        if user.user_role == 'EDU':
                            question_data['question_type'] = 'EDQ'
                            return_data['question_type'] = 'EDQ'
                        if user.user_role == 'SUP':
                            question_data['question_type'] = 'PAQ'
                            return_data['question_type'] = 'PAQ'
                        if user.user_role == 'AIG':
                            question_data['question_type'] = 'AIG'
                            return_data['question_type'] = 'AIG'

                        print('validated data', question_data)
                        # Create question
                        question = Question.objects.create(**question_data)
                        
                        # Create options for this question
                        Option.objects.bulk_create([
                            Option(
                                question_id=question,
                                option=option_data['option'],
                                is_answer=option_data['is_answer']
                            )
                            for option_data in options_data
                        ])
                        
                        questions.append(return_data)
                    return Response(questions, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionView(GenericAPIView):
    pass

class UserQuizResponseView(GenericAPIView):
    pass

class GenerateQuizView(GenericAPIView):
    pass

class SaveQuizView(GenericAPIView):
    pass

class SubmitQuizView(GenericAPIView):
    pass

class CreateQuizView(GenericAPIView):
    pass

class SubmitMaterialView(GenericAPIView):
    pass
