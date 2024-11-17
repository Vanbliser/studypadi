from django.urls import path
from .views import ModulesView, SubmodulesView, SectionView, TopicView, UserView, QuestionView, UserQuizView, UserPrefilledQuizView, UserRealtimeQuizView, UserRevisionTestQuizView, QuizView, QuizQuestionsView, GenerateQuizView, SaveQuizView, SubmitQuizView, CreateQuizView, CreateQuestionView, SubmitMaterialView, UserQuizResponseView


urlpatterns = [
    path('modules/', ModulesView.as_view(), name='modules'),
    path('submodules/', SubmodulesView.as_view(), name='submodules'),
    path('sections/', SectionView.as_view(), name='sections'),
    path('topics/', TopicView.as_view(), name='topics'),
    path('user/', UserView.as_view(), name='user'),
    path('user/quiz/', UserQuizView.as_view(), name='quiz'),
    path('user/quiz/prefilled/', UserPrefilledQuizView.as_view(), name='prefilled-quiz'),
    path('user/quiz/realtime/', UserRealtimeQuizView.as_view(), name='realtime-quiz'),
    path('user/quiz/revision-test/', UserRevisionTestQuizView.as_view(), name='revision-test-quiz'),
    path('quiz/', QuizView.as_view(), name='quiz'),
    path('quiz/question/', QuizQuestionsView.as_view(), name='quiz-question'),
    path('question/create/', CreateQuestionView.as_view(), name='create-question'),
    path('quiz/generate/', GenerateQuizView.as_view(), name='generate-quiz'),
    path('submit-material/', SubmitMaterialView.as_view(), name='submit-material'),
    path('question/', QuestionView.as_view(), name='question'),
    path('user/quiz/response/', UserQuizResponseView.as_view(), name='quiz-response'),
    path('quiz/save/', SaveQuizView.as_view(), name='save-quiz'),
    path('quiz/submit/', SubmitQuizView.as_view(), name='submit-quiz'),
    path('quiz/create/', CreateQuizView.as_view(), name='create-quiz'),
]