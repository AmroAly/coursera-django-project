from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission, Enrollment

# <HINT> Register QuestionInline and ChoiceInline classes here
class QuestionInline(admin.StackedInline):
    model = Question

class ChoiceInline(admin.StackedInline):
    model = Choice


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ('lesson_id', 'question_text')
    list_filter = ['lesson_id']
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['choice_content', 'is_correct']
    list_filter = ['question_id']
    search_fields = ['choice_content']


class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


# <HINT> Register Question and Choice models here
admin.site.register(Question)
admin.site.register(Submission)
admin.site.register(Enrollment)
admin.site.register(Choice)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
