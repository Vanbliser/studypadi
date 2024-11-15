from .models import Module, Submodule, Section, Topic, Question, Option, Quiz, Quiz_attempt


def create_question(
        module_id,
        submodule_id,
        section_id,
        topic_id,
        created_by,
        question_type,
        difficulty,
        question
):
    question = Question.objects.create(
        module_id,
        submodule_id,
        section_id,
        topic_id,
        created_by,
        question_type,
        difficulty,
        question
    )
