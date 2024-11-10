from django.urls import path
from .views import ModulesView, SubmodulesView, SectionView, TopicView, UserView, UserRevisionTestView, UserPrefilledQuizView, UserRealtimeQuizView, QuizView, GenerateQuizView, SaveQuizView, SubmitQuizView, CreateQuizView, CreateQuestionView, SubmitMaterialView


urlpatterns = [
    path('modules/', ModulesView.as_view(), name='modules'),
    path('submodules/', SubmodulesView.as_view(), name='submodules'),
    path('sections/', SectionView.as_view(), name='sections'),
    path('topics/', TopicView.as_view(), name='topics'),
    path('user/', UserView.as_view(), name='user'),
    path('user/revision-test/', UserRevisionTestView.as_view(), name='revision-test'),
    path('user/prefilled-quiz/', UserPrefilledQuizView.as_view(), name='prefilled-quiz'),
    path('user/realtime-quiz/', UserRealtimeQuizView.as_view(), name='realtime-quiz'),
    path('quiz/', QuizView.as_view(), name='quiz'),
    path('quiz/generate/', GenerateQuizView.as_view(), name='generate-quiz'),
    path('quiz/save/', SaveQuizView.as_view(), name='save-quiz'),
    path('quiz/submit/', SubmitQuizView.as_view(), name='quiz'),
    path('quiz/create/', CreateQuizView.as_view(), name='create-quiz'),
    path('question/create/', CreateQuestionView.as_view(), name='create-question'),
    path('submit-material/', SubmitMaterialView.as_view(), name='submit-material'),
]