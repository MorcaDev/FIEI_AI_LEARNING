from django.contrib import admin
from .models import *

class Hobby_Admin(admin.ModelAdmin):

    pass

class LearningStyle_Admin(admin.ModelAdmin):

    pass

class School_Admin(admin.ModelAdmin):

    pass

class Subject_Admin(admin.ModelAdmin):

    pass

class Student_Admin(admin.ModelAdmin):

    pass

class StudentHobby_Admin(admin.ModelAdmin):

    pass

class StudentSubject_Admin(admin.ModelAdmin):

    pass

class Lesson_Admin(admin.ModelAdmin):

    pass

class Content_Admin(admin.ModelAdmin):

    pass

class TypeQuestion_Admin(admin.ModelAdmin):

    pass

class TemplateAssessment_Admin(admin.ModelAdmin):
    
    pass

class AdaptedRecommendation_Admin(admin.ModelAdmin):
    
    pass

class AdaptedActivity_Admin(admin.ModelAdmin):
    
    pass

class AdaptedQuestion_Admin(admin.ModelAdmin):
    
    pass

class AdaptedSummary_Admin(admin.ModelAdmin):
    
    pass

admin.site.register(Hobby, Hobby_Admin)
admin.site.register(LearningStyle, LearningStyle_Admin)
admin.site.register(School, School_Admin)
admin.site.register(Subject, Subject_Admin)
admin.site.register(Student, Student_Admin)
admin.site.register(StudentHobby, StudentHobby_Admin)
admin.site.register(StudentSubject, StudentSubject_Admin)
admin.site.register(Lesson, Lesson_Admin)
admin.site.register(Content, Content_Admin)
admin.site.register(TypeQuestion, TypeQuestion_Admin)
admin.site.register(TemplateAssessment, TemplateAssessment_Admin)
admin.site.register(AdaptedRecommendation, AdaptedRecommendation_Admin)
admin.site.register(AdaptedActivity, AdaptedActivity_Admin)
admin.site.register(AdaptedQuestion, AdaptedQuestion_Admin)
admin.site.register(AdaptedSummary, AdaptedSummary_Admin)
