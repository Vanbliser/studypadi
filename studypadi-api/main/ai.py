from openai import OpenAI
from django.conf import settings

api_key = getattr(settings, 'OPENAI_KEY')


def get_completion(text, num_of_questions=50, level="Undergradute", temperature=0.7):

    prompt = f"""
Read the following text and generate {num_of_questions} multiple-choice questions with exactly 4 options each. 
One option must be the correct answer. Set difficulty (EAS/MED/HRD) based on {level} level. Format your response as a JSON array with this exact structure: 
[
    {{
        "question": "question text",
        "difficulty" "EAS/MED/HRD",
        "options": [
            {{"text": "option 1", "is_answer": true/false}},
            {{"text": "option 2", "is_answer": true/false}},
            {{"text": "option 3", "is_answer": true/false}},
            {{"text": "option 4", "is_answer": true/false}}
        ]
    }},
    {{
        "question": "question text",
        "difficulty" "EAS/MED/HRD",
        "options": [
            {{"text": "option 1", "is_answer": true/false}},
            {{"text": "option 2", "is_answer": true/false}},
            {{"text": "option 3", "is_answer": true/false}},
            {{"text": "option 4", "is_answer": true/false}}
        ]
    }}
]

Text: {text}
"""
    return OpenAI(
        api_key=api_key
    ).chat.completions.create(
                                model="gpt-4o-mini",
                                messages=[
                                    {"role": "system", "content": """You are an educated teacher that is so good at generating \
questions from a provided text with accurate options."""},
                                    {"role": "user", "content": prompt}
                                ],
                                temperature=temperature
    ).choices[0].message.content.strip()
