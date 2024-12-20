from django.db import models
from account.models import User
from django.contrib.auth.hashers import make_password
from django.conf import settings


ai_gen_password = getattr(settings, 'AIGEN')

def get_super_user():
    return User.objects.filter(is_superuser=True, user_role="SUP").values_list('id', flat=True).first()

def get_ai_gen_user():
    user = User.objects.filter(user_role="AIG", is_verified=True, is_active=True).first()

    if not user:
        # Create a new user if none exist
        user = User.objects.create(
            email = 'aigen@email.com',
            first_name = 'ai',
            last_name = 'gen',
            is_verified = True,
            is_superuser = False,
            user_role = 'AIG',
            password = make_password(ai_gen_password)
        )
    return user

# Create your models here.

class Module(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=get_super_user)
    class Meta:
        ordering = ['-created_at']

class Submodule(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    module_id = models.ForeignKey(Module, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=get_super_user)
    class Meta:
        ordering = ['-created_at']

class Section(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    submodule_id = models.ForeignKey(Submodule, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=get_super_user)
    class Meta:
        ordering = ['-created_at']

class Topic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    section_id = models.ForeignKey(Section, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=get_super_user)
    class Meta:
        ordering = ['-created_at']

class Question(models.Model):
    difficulties = [
        ("EAS", "Easy"),
        ("MED", "Medium"),
        ("HRD", "Hard")
    ]
    question_types = [
        ('AIG', 'AI Generated'),
        ('EDQ', 'Educator'),
        ('PAQ', 'Past question')
    ]
    module_id = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    submodule_id = models.ForeignKey(Submodule, on_delete=models.SET_NULL, null=True)
    section_id = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    topic_id = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=get_super_user)
    question_type = models.CharField(max_length=3, choices=question_types)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    difficulty = models.CharField(max_length=3, default="EAS", choices=difficulties)
    question = models.TextField()
    class Meta:
        ordering = ['-created_at']

class Option(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    is_answer = models.BooleanField(default=False)
    option = models.TextField()

class Quiz(models.Model):
    name = models.CharField(max_length=255)
    module_id = models.ForeignKey(Module, on_delete=models.SET_NULL, null=True)
    submodule_id = models.ForeignKey(Submodule, on_delete=models.SET_NULL, null=True)
    section_id = models.ForeignKey(Section, on_delete=models.SET_NULL, null=True)
    topic_id = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    num_of_questions = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=get_super_user)
    questions = models.ManyToManyField(Question)
    class Meta:
        ordering = ['-created_at']
                                                 
class Quiz_attempt(models.Model):
    statuses = [
        ('FIN', 'Completed'),
        ('STA', 'Not started'),
        ('MID', 'Not completed')
    ]
    quiz_id = models.ForeignKey(Quiz, on_delete=models.PROTECT)
    taken_by = models.ForeignKey(User, on_delete=models.PROTECT)
    score = models.IntegerField()
    status = models.CharField(max_length=3, choices=statuses, default="MID")
    time_taken = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-time_taken"]

class Response(models.Model):
    quiz_attempt = models.ForeignKey(Quiz_attempt, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.PROTECT)
    chosen_option = models.ForeignKey(Option, on_delete=models.PROTECT, null=True)
