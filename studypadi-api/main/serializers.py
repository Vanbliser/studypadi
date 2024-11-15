from rest_framework import serializers
from .models import Module, Submodule, Section, Topic, Question, Quiz, Quiz_attempt, Response, Option
from account.models import User


class ModuleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Module
        fields = ['id', 'title', 'description']
        extra_kwargs = {
            'title': {'required': True},
            'description': {'required': True},
        }
    
    def validate(self, attrs):
        # check for additional fields
        allowed_fields = set(self.fields.keys())
        for initial_data in self.initial_data:
            extra_fields = set(initial_data.keys()) - allowed_fields
            if extra_fields:
                raise serializers.ValidationError("Bad request. Unknown field(s).")
        return attrs

class SubmoduleSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    description = serializers.CharField()
    module_id = serializers.IntegerField()

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
        for initial_data in self.initial_data:
            extra_fields = set(initial_data.keys()) - allowed_fields
            if extra_fields:
                raise serializers.ValidationError("Bad request. Unknown field(s).")
        print(attrs)
        return attrs
    
class SectionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    description = serializers.CharField()
    submodule_id = serializers.IntegerField()

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
        for initial_data in self.initial_data:
            extra_fields = set(initial_data.keys()) - allowed_fields
            if extra_fields:
                raise serializers.ValidationError("Bad request. Unknown field(s).")
        return attrs

class TopicSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField()
    description = serializers.CharField()
    section_id = serializers.IntegerField()

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
        for initial_data in self.initial_data:
            extra_fields = set(initial_data.keys()) - allowed_fields
            if extra_fields:
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
            return attrs
        else:
            raise serializers.ValidationError("Invalid options JSON")

class CreateQuestionSerializer(serializers.Serializer):
    module_id = serializers.IntegerField()
    submodule_id = serializers.IntegerField()
    section_id = serializers.IntegerField()
    topic_id = serializers.IntegerField()
    difficulty = serializers.CharField(max_length=3)
    question = serializers.CharField()
    options = OptionSerializer(many=True, write_only=True)

    class Meta:
        fields = ['module_id', 'submodule_id', 'section_id', 'topic_id', 'difficulty', 'question', 'options']
        extra_kwargs = {
            'question': {'required': True},
            'options': {'required': True}
        }

    def validate(self, attrs):

        module_id = attrs.get('module_id', None)
        submodule_id = attrs.get('submodule_id', None)
        section_id = attrs.get('section_id', None)
        topic_id = attrs.get('topic_id', None)
        difficulty = attrs.get('difficulty', None)
        question = attrs.get('question', None)
        
        module = Module.objects.filter(id=module_id).first()
        submodule = Submodule.objects.filter(id=submodule_id).first()
        section = Section.objects.filter(id=section_id).first()
        topic = Topic.objects.filter(id=topic_id).first()
        if difficulty not in ['EAS', 'HRD', 'MED']:
            difficulty = "EAS"

        if question == "":
            raise serializers.ValidationError("Bad request. empty question")
        
        return_data = dict()
        if module:
            return_data['module'] = module.title
        if submodule:
            return_data['submodule'] = submodule.title
        if section:
            return_data['section'] = section.title
        if topic:
            return_data['topic'] = topic.title
        return_data['difficulty'] = difficulty
        return_data['question'] = question

        print('return data', return_data)

        data = {
            'module_id': module,
            'submodule_id': submodule,
            'section_id': section,
            'topic_id': topic,
            'difficulty': difficulty,
            'question': question,
            'options': attrs.get('options'),
            'return': return_data
        }
        cleaned_data = {k: v for k, v in data.items() if v is not None}
        return cleaned_data
    
    def to_representation(self, instance):
        """
        Override to include options in the response
        """
        representation = super().to_representation(instance)
        representation['options'] = OptionSerializer(
            Option.objects.filter(question=instance),
            many=True
        ).data
        return representation

class CreateQuestionListSerializer(serializers.ListSerializer):
    child = CreateQuestionSerializer()

class GenerateQuizSerializer(serializers.Serializer):

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
        pass

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
        pass

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
        pass

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
        pass

class SubmitMaterialSerializer(serializers.Serializer):

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
        pass
