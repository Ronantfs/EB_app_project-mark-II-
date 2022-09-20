import django_filters
from .models import Question


class QuestionFilter(django_filters.FilterSet):

    class Meta: 
        model = Question
        fields = {"name":['icontains'],
            "source":['contains'],
            "section":['exact'],
            "AS_only": ['exact'],
            "question_progress": ['lt', 'gt'],
            }


''' 
class Add_to_ExamFilter(django_filters.FilterSet):

    class Meta: 
        model = Question
        fields = {"name":['icontains'],
            "source":['contains'],
            "section":['exact'],
            "AS_only": ['exact'],
            "question_progress": ['lt', 'gt'],
            }

'''