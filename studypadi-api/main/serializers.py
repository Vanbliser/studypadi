from rest_framework import serializers
from .models import Module, Submodule, Section, Topic, Question, Quiz, Quiz_attempt, Response, Option
from account.models import User

def check(superset, subset):
    for key in superset:
        if key not in subset:
            return True
    return False 

class ModuleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Module
        fields = ['id', 'title', 'description']
    
    def validate(self, attrs):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        if isinstance(self.initial_data, list):
            for initial_data in self.initial_data:
                if check(initial_data, allowed_fields):
                    raise serializers.ValidationError("Bad request. Unknown field(s).")
        else:
            if self.check(self.initial_data, allowed_fields):
                raise serializers.ValidationError("Bad request. Unknown field(s).")
        return attrs

class SubmoduleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    module_id = serializers.PrimaryKeyRelatedField(queryset=Module.objects.all())

    class Meta:
        model = Submodule
        fields = ['id', 'module_id', 'title', 'description']
        extra_kwargs = {
            'module_id': {'required': True},
            'title': {'required': True},
            'description': {'required': True},
        }
    
    def validate(self, attrs):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        if isinstance(self.initial_data, list):
            for initial_data in self.initial_data:
                if check(initial_data, allowed_fields):
                    raise serializers.ValidationError("Bad request. Unknown field(s).")
        else:
            if self.check(self.initial_data, allowed_fields):
                raise serializers.ValidationError("Bad request. Unknown field(s).")
        return attrs

class SectionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    submodule_id = serializers.PrimaryKeyRelatedField(queryset=Submodule.objects.all())

    class Meta:
        model = Section
        fields = ['id', 'submodule_id', 'title', 'description']
        extra_kwargs = {
            'submodule_id': {'required': True},
            'title': {'required': True},
            'description': {'required': True},
        }
    
    def validate(self, attrs):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        if isinstance(self.initial_data, list):
            for initial_data in self.initial_data:
                if check(initial_data, allowed_fields):
                    raise serializers.ValidationError("Bad request. Unknown field(s).")
        else:
            if self.check(self.initial_data, allowed_fields):
                raise serializers.ValidationError("Bad request. Unknown field(s).")
        return attrs

class TopicSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    section_id = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all())

    class Meta:
        model = Topic
        fields = ['id', 'section_id', 'title', 'description']
        extra_kwargs = {
            'section_id': {'required': True},
            'title': {'required': True},
            'description': {'required': True},
        }
    
    def validate(self, attrs):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        if isinstance(self.initial_data, list):
            for initial_data in self.initial_data:
                if check(initial_data, allowed_fields):
                    raise serializers.ValidationError("Bad request. Unknown field(s).")
        else:
            if self.check(self.initial_data, allowed_fields):
                raise serializers.ValidationError("Bad request. Unknown field(s).")
        return attrs

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['option', 'is_answer']
        extra_kwargs = {
            'option': {'required': True},
            'is_answer': {'required': True}
        }
    def validate(self, attrs):
        if isinstance(attrs['is_answer'], bool) or attrs['option'] != "":
            # check for additional fields
            allowed_fields = set(self.fields.keys())
            if isinstance(self.initial_data, list):
                for initial_data in self.initial_data:
                    if check(initial_data, allowed_fields):
                        raise serializers.ValidationError("Bad request. Unknown field(s).")
            else:
                if self.check(self.initial_data, allowed_fields):
                    raise serializers.ValidationError("Bad request. Unknown field(s).")
            return attrs
        else:
            raise serializers.ValidationError("Invalid options JSON")
        
class CreateQuestionSerializer(serializers.ModelSerializer):
    module_id = serializers.PrimaryKeyRelatedField(queryset=Module.objects.all(), required=False)
    submodule_id = serializers.PrimaryKeyRelatedField(queryset=Submodule.objects.all(), required=False)
    section_id = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all(), required=False)
    topic_id = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all(), required=False)
    difficulty = serializers.ChoiceField(choices=[
        ('EAS', 'Easy'),
        ('MED', 'Medium'),
        ('HRD', 'Hard'),
    ], required=False)
    question = serializers.CharField()
    options = OptionSerializer(many=True, write_only=True)
    question_type = serializers.ChoiceField(choices=[
        ('EDQ', 'Educator created question'),
        ('PAQ', 'Question from question bank created by superadmin'),
        ('AIG', 'Generative AI question'),
    ], required=False, read_only=True)

    class Meta:
        model = Question
        fields = ['module_id', 'submodule_id', 'section_id', 'topic_id', 'question_type', 'difficulty', 'question', 'options']
        extra_kwargs = {
            'question': {'required': True},
            'options': {'required': True}
        }

    def validate(self, attrs):
        question = attrs.get('question', None)
        if not question:
            raise serializers.ValidationError("Bad request. empty question")
        
        user = self.context.get('user')
        if user.user_role == 'EDU':
            attrs['question_type'] = 'EDQ'
        if user.user_role == 'SUP':
            attrs['question_type'] = 'PAQ'
        if user.user_role == 'AIG':
            attrs['question_type'] = 'AIG'

        # check for additional fields
        allowed_fields = set(self.fields.keys())
        if isinstance(self.initial_data, list):
            for initial_data in self.initial_data:
                if check(initial_data, allowed_fields):
                    raise serializers.ValidationError("Bad request. Unknown field(s).")
        else:
            if self.check(self.initial_data, allowed_fields):
                raise serializers.ValidationError("Bad request. Unknown field(s).")

        return attrs

class CreateQuestionListSerializer(serializers.ListSerializer):
    child = CreateQuestionSerializer()

class GenerateQuizSerializer(serializers.Serializer):
    name = serializers.CharField()
    module_id = serializers.PrimaryKeyRelatedField(queryset=Module.objects.all(), required=False)
    submodule_id = serializers.PrimaryKeyRelatedField(queryset=Submodule.objects.all(), required=False)
    section_id = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all(), required=False)
    topic_id = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all(), required=False)
    num_of_questions = serializers.IntegerField()
    question_type = serializers.ChoiceField(choices=[
        ('AIG', 'AI Generated quiz'),
        ('EDQ', 'Educator quiz'),
        ('PAQ', 'Past question quiz'),
        ('AIE', 'AI Generated and Educator quiz'),
        ('AIP', 'AI Generated and Past question quiz'),
        ('ALL', 'All type')
    ])
    difficulty = serializers.ChoiceField(choices=[
        ('EAS', 'Easy'),
        ('MED', 'Medium'),
        ('HRD', 'Hard'),
        ('EAM', 'Easy AND Medium'),
        ('EAH', 'Easy AND Hard'),
        ('EMD', 'Easy AND Medium AND Hard')
    ])
    algorithm = serializers.ChoiceField(choices=[
        ('RAD', 'Random'),
        ('MOF', 'Most failed'),
        ('LEA', 'Least attempted')
    ])

    class Meta:
        fields = ['name', 'module_id', 'submodule_id', 'section_id', 'topic_id', 'num_of_questions', 'question_type', 'difficulty', 'algorithm']
        extra_kwargs = {
            'name': {'required': True},
            'num_of_question': {'required': True},
            'question_type': {'required': True},
            'difficulty': {'required': True},
            'algorithm': {'required': True}
        }
    
    def validate(self, attrs):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        if isinstance(self.initial_data, list):
            for initial_data in self.initial_data:
                if check(initial_data, allowed_fields):
                    raise serializers.ValidationError("Bad request. Unknown field(s).")
        else:
            if self.check(self.initial_data, allowed_fields):
                raise serializers.ValidationError("Bad request. Unknown field(s).")
        return attrs

class SubmitMaterialSerializer(serializers.Serializer):

    text = serializers.CharField()
    name = serializers.CharField()
    num_of_questions = serializers.IntegerField()

    class Meta:
        fields = ['name', 'text', 'num_of_questions']
        extra_kwargs = {
            'name': {'required': True},
            'text': {'required': True},
            'num_of_questions': {'required': True}
        }
    
    def validate(self, attrs):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        if isinstance(self.initial_data, list):
            for initial_data in self.initial_data:
                if check(initial_data, allowed_fields):
                    raise serializers.ValidationError("Bad request. Unknown field(s).")
        else:
            if self.check(self.initial_data, allowed_fields):
                raise serializers.ValidationError("Bad request. Unknown field(s).")
        return attrs

class SaveQuizSerializer(serializers.Serializer):

    class Meta:
        fields = ['email', 'first_name', 'last_name', 'password', 'confirm_password']
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'required': True},
            'confirm_password': {'required': True},
        }
    
    def validate(self, attrs):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        if isinstance(self.initial_data, list):
            for initial_data in self.initial_data:
                if check(initial_data, allowed_fields):
                    raise serializers.ValidationError("Bad request. Unknown field(s).")
        else:
            if self.check(self.initial_data, allowed_fields):
                raise serializers.ValidationError("Bad request. Unknown field(s).")

class SubmitQuizSerializer(serializers.Serializer):

    class Meta:
        fields = ['email', 'first_name', 'last_name', 'password', 'confirm_password']
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'required': True},
            'confirm_password': {'required': True},
        }
    
    def validate(self, attrs):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        if isinstance(self.initial_data, list):
            for initial_data in self.initial_data:
                if check(initial_data, allowed_fields):
                    raise serializers.ValidationError("Bad request. Unknown field(s).")
        else:
            if self.check(self.initial_data, allowed_fields):
                raise serializers.ValidationError("Bad request. Unknown field(s).")

class CreateQuizSerializer(serializers.Serializer):

    class Meta:
        fields = ['email', 'first_name', 'last_name', 'password', 'confirm_password']
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'required': True},
            'confirm_password': {'required': True},
        }
    
    def validate(self, attrs):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        if isinstance(self.initial_data, list):
            for initial_data in self.initial_data:
                if check(initial_data, allowed_fields):
                    raise serializers.ValidationError("Bad request. Unknown field(s).")
        else:
            if self.check(self.initial_data, allowed_fields):
                raise serializers.ValidationError("Bad request. Unknown field(s).")
