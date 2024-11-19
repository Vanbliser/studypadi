from rest_framework import serializers
from .models import Module, Submodule, Section, Topic, Question, Quiz, Quiz_attempt, Response, Option
from account.models import User

def check(superset, subset):
    for key, value in superset.items():
        if key not in subset:
            return{
                'k': key,
                'v': value
            }
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
            if check(self.initial_data, allowed_fields):
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
            if check(self.initial_data, allowed_fields):
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
            if check(self.initial_data, allowed_fields):
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
            if check(self.initial_data, allowed_fields):
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

    def to_internal_value(self, data):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        if isinstance(data, list):
            for initial_data in data:
                if k := check(initial_data, allowed_fields):
                    raise serializers.ValidationError(f"Bad request. Unknown {{{k['k']}: {k['v']}}} field.")
        else:
            if k := check(data, allowed_fields):
                raise serializers.ValidationError(f"Bad request. Unknown {{{k['k']}: {k['v']}}}  field.")
        return super().to_internal_value(data)
    
    def validate(self, attrs):
        if isinstance(attrs['is_answer'], bool) or attrs['option'] != "":
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
    options = OptionSerializer(many=True)
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
        
        if self.context and self.context.get('user'):
            user = self.context.get('user')
            if user.user_role == 'EDU':
                attrs['question_type'] = 'EDQ'
            if user.user_role == 'SUP':
                attrs['question_type'] = 'PAQ'
            if user.user_role == 'AIG':
                attrs['question_type'] = 'AIG'

        if hasattr(self, 'initial_data'):
            # check for additional fields
            allowed_fields = set(self.fields.keys())
            if isinstance(self.initial_data, list):
                for initial_data in self.initial_data:
                    if check(initial_data, allowed_fields):
                        raise serializers.ValidationError("Bad request. Unknown field(s).")
            else:
                if check(self.initial_data, allowed_fields):
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
            if check(self.initial_data, allowed_fields):
                raise serializers.ValidationError("Bad request. Unknown field(s).")
        return attrs

class SubmitMaterialSerializer(serializers.Serializer):

    text = serializers.CharField()
    name = serializers.CharField()
    num_of_questions = serializers.IntegerField()
    level = serializers.ChoiceField(choices=[
        ('High School', 'High School'),
        ('Undergradute', 'Undergradute'),
        ('Postgradute', 'Postgradute')
    ])

    class Meta:
        fields = ['name', 'text', 'num_of_questions', 'level']
        extra_kwargs = {
            'name': {'required': True},
            'text': {'required': True},
            'num_of_questions': {'required': True},
            'level': {'required': True}
        }
    
    def validate(self, attrs):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        if isinstance(self.initial_data, list):
            for initial_data in self.initial_data:
                if check(initial_data, allowed_fields):
                    raise serializers.ValidationError("Bad request. Unknown field(s).")
        else:
            if check(self.initial_data, allowed_fields):
                raise serializers.ValidationError("Bad request. Unknown field(s).")
        return attrs

class ResponseSerializer(serializers.ModelSerializer):
    quiz_attempt_id = serializers.IntegerField(required=False)
    question_id = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all())
    chosen_option = serializers.PrimaryKeyRelatedField(queryset=Option.objects.all(), allow_null=True)

    class Meta:
        model = Response
        fields = ["quiz_attempt_id", "question_id", "chosen_option"]

class QuizSerializer(serializers.ModelSerializer):
    quiz_attempt_id = serializers.PrimaryKeyRelatedField(queryset=Quiz_attempt.objects.prefetch_related('response_set'), required=False)
    quiz_id = serializers.PrimaryKeyRelatedField(queryset=Quiz.objects.all())
    responses = ResponseSerializer(many=True)

    class Meta:
        model= Quiz_attempt
        fields = ['quiz_attempt_id', 'quiz_id', 'responses']
        extra_kwargs = {
            'quiz_id': {'required': True},
            'responses': {'required': True},
        }
    
    def validate(self, attrs):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        if isinstance(self.initial_data, list):
            for initial_data in self.initial_data:
                if check(initial_data, allowed_fields):
                    raise serializers.ValidationError("Bad request. Unknown field(s).")
        else:
            if check(self.initial_data, allowed_fields):
                raise serializers.ValidationError("Bad request. Unknown field(s).")
        
        quiz_id = attrs["quiz_id"]
        responses = attrs["responses"]

        # Check for duplicate responses
        question_ids = {response['question_id'] for response in responses}
        if len(question_ids) != len(responses):
            raise serializers.ValidationError("Duplicate question_id found in responses.")
        
        # Invalid quiz and response combination
        questions = quiz_id.questions.prefetch_related('option_set').all()
        for response in responses:
            v = False
            for question in questions:
                if response.get('question_id') == question:
                    v = True
                    if r := response.get('chosen_option'):
                        if r in question.option_set.all():
                            break
                        else:
                            raise serializers.ValidationError("Bad request. Invalid quiz and response combination")
            if not v:
                raise serializers.ValidationError("Bad request. Invalid quiz and response combination")

        return attrs

class CreateQuizSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    module_id = serializers.PrimaryKeyRelatedField(queryset=Module.objects.all(), required=False)
    submodule_id = serializers.PrimaryKeyRelatedField(queryset=Submodule.objects.all(), required=False)
    section_id = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all(), required=False)
    topic_id = serializers.PrimaryKeyRelatedField(queryset=Topic.objects.all(), required=False)
    questions = CreateQuestionSerializer(many=True)

    class Meta:
        model= Quiz
        fields = ['id', 'name', 'module_id', 'submodule_id', 'section_id', 'topic_id', 'questions']
        extra_kwargs = {
            'name': {'required': True},
            'questions': {'required': True},
        }
    
    def validate(self, attrs):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        if isinstance(self.initial_data, list):
            for initial_data in self.initial_data:
                if check(initial_data, allowed_fields):
                    raise serializers.ValidationError("Bad request. Unknown field(s).")
        else:
            if check(self.initial_data, allowed_fields):
                raise serializers.ValidationError("Bad request. Unknown field(s).")
        
        return attrs
