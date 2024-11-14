from rest_framework import serializers
from .models import Module, Submodule, Section, Topic, Question, Quiz, Quiz_attempt, Response, Option
from account.models import User

class CreateQuestionSerializer(serializers.Serializer):

    class Meta:
        fields = ['module_id', 'submodule_id', 'section_id', 'topic_id', 'difficulty', 'question']
        extra_kwargs = {
            'question': {'required': True}
        }
    
    def validate(self, attrs):
        allowed_fields = set(self.fields.keys())

        # Check for any additional fields
        # extra_fields = set(self.initial_data.keys()) - allowed_fields
        # if extra_fields:
        #     raise serializers.ValidationError("Bad request. Unknown field(s).")
        # try:
        #     question = attrs.get('question')
        # except:
        #     raise serializers.ValidationError("Invalid JSON")
        module_id = int(attrs.get('module_id', 0))
        submodule_id = int(attrs.get('submodule_id', 0))
        section_id = int(attrs.get('section_id', 0))
        topic_id = int(attrs.get('topic_id', 0))
        difficulty = attrs.get('difficulty', None)
        if not Module.objects.filter(id=module_id).exists():
            module_id = None
        if not Submodule.objects.filter(id=submodule_id).exists():
            submodule_id = None
        if not Section.objects.filter(id=section_id).exists():
            section_id = None
        if not Topic.objects.filter(id=topic_id).exists():
            topic_id = None
        if difficulty not in ['EAS', 'HRD', 'MED']:
            difficulty = "EAS"
        if attrs.get('question') == "":
            raise serializers.ValidationError("Bad request. empty question")
        
        data = {
            'module_id': module_id,
            'submodule_id': submodule_id,
            'section_id': section_id,
            'topic_id': topic_id,
            'difficulty': difficulty,
            'question': attrs.get('question')
        }
        cleaned_data = {key: value for key, value in data.items() if value not in (0, None)}

        print(cleaned_data)
        return cleaned_data

class CreateQuestionsSerializer(serializers.ListSerializer):
    print('validating')
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
