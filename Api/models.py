from django.db import models
from django.contrib.auth import get_user_model

# enlace al User de Django
User = get_user_model()

# ────────────────────────────
# Hobby
# ────────────────────────────
class Hobby(models.Model):

    name        = models.CharField(null=False,max_length=100)
    description = models.TextField(null=False)

    def __str__(self):
        return self.name


# ────────────────────────────
# Learning Style
# ────────────────────────────
class LearningStyle(models.Model):

    name        = models.CharField(null=False,max_length=100)
    description = models.TextField(null=False,blank=False)

    def __str__(self):
        return self.name
    

# ────────────────────────────
# School
# ────────────────────────────
class School(models.Model):

    name        = models.CharField(null=False,max_length=120)
    description = models.TextField(null=False,blank=False)

    def __str__(self):
        return self.name


# ────────────────────────────
# Subject
# ────────────────────────────
class Subject(models.Model):

    name        = models.CharField(null=False,max_length=120)
    description = models.TextField(null=False,blank=False)

    school      = models.ForeignKey(School, on_delete=models.CASCADE)
    year        = models.PositiveSmallIntegerField(null=False, blank=False)
    ciclo       = models.PositiveSmallIntegerField(null=False, blank=False)
    image       = models.TextField(null=False,blank=False)

    def __str__(self):
        return self.name


# ────────────────────────────
# Student  
# ────────────────────────────
class Student(models.Model):

    code             = models.CharField(null=False,max_length=10, primary_key=True)
    user             = models.OneToOneField(User, on_delete=models.CASCADE)

    career           = models.ForeignKey(School, on_delete=models.CASCADE)
    year             = models.PositiveSmallIntegerField(null=False, blank=False)
    cycle            = models.PositiveSmallIntegerField(null=False, blank=False)

    learning_style   = models.ForeignKey(LearningStyle, on_delete=models.CASCADE, null=True, blank=True)
    hobbies          = models.ManyToManyField(Hobby, through="StudentHobby", related_name="student")
    enrollments      = models.ManyToManyField(Subject, through="StudentSubject", related_name="student")

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.code})"

# ────────────────────────────
# Student–Hobby (tabla puente)
# ────────────────────────────
class StudentHobby(models.Model):

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    hobby   = models.ForeignKey(Hobby,   on_delete=models.CASCADE)

    class Meta:
        unique_together = ("student", "hobby")
        verbose_name    = "Student Hobby"


# ────────────────────────────
# Student-Subject (tabla puente)
# ────────────────────────────
class StudentSubject(models.Model):

    grade      = models.FloatField(default=0.0)
    student    = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject    = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("student", "subject")
        verbose_name    = "Student Subject"


# ────────────────────────────
# Lesson  
# ────────────────────────────
class Lesson(models.Model):

    title       = models.CharField(null=False,max_length=120)
    description = models.TextField(null=False,blank=False)
    goal        = models.CharField(null=False,max_length=255, blank=False)
    expectation = models.CharField(null=False,max_length=255, blank=False, default="-")

    subject     = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


# ────────────────────────────
# Content
# ────────────────────────────
class Content(models.Model):

    title    = models.CharField(null=False,max_length=200)
    format   = models.CharField(null=False,max_length=50)          # e.g. pdf, video…
    location = models.TextField(null=False,blank=False)        # URL o path

    related_class = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - .{self.format}'


# ────────────────────────────
# TypeQuestion 
# ────────────────────────────
class TypeQuestion(models.Model):

    description = models.CharField(null=False,max_length=150)

    def __str__(self):
        return self.description


# ────────────────────────────
# TemplateAssessment
# ────────────────────────────
class TemplateAssessment(models.Model):

    number_questions = models.PositiveSmallIntegerField()
    max_grade        = models.FloatField(default=20.0)

    type_questions   = models.ForeignKey(TypeQuestion, on_delete=models.PROTECT)


# ────────────────────────────
# AdaptedSummary
# ────────────────────────────
class AdaptedSummary(models.Model):

    title       = models.CharField(null=False,max_length=200)
    content     = models.TextField(null=False)

    student     = models.ForeignKey(Student, on_delete=models.CASCADE)
    related_class = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    completed   = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=False)
    image       = models.ImageField(upload_to="Recomendation/",height_field=None,width_field=None,max_length=100, null=True )


# ────────────────────────────
# AdaptedRecommendation
# ────────────────────────────
class AdaptedRecommendation(models.Model):

    title       = models.CharField(null=False,max_length=200)
    content     = models.TextField(null=False)

    student     = models.ForeignKey(Student, on_delete=models.CASCADE)
    related_class = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    completed   = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=False)
    image       = models.ImageField(upload_to="Recomendation/",height_field=None,width_field=None,max_length=100, null=True )

# ────────────────────────────
# AdaptedActivity
# ────────────────────────────
class AdaptedActivity(models.Model):

    title       = models.CharField(null=False,max_length=200)
    content     = models.TextField(null=False,)

    student     = models.ForeignKey(Student, on_delete=models.CASCADE)
    related_class = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    completed   = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=False) 
    image       = models.ImageField(upload_to="Recomendation/",height_field=None,width_field=None,max_length=100, null=True )


# ────────────────────────────
# AdaptedQuestion
# ────────────────────────────
class AdaptedQuestion(models.Model):

    question    = models.TextField(null=False,)
    options     = models.TextField(null=True)
    answer      = models.TextField(null=True,blank=True)
    status      = models.BooleanField(default=False)

    student     = models.ForeignKey(Student, on_delete=models.CASCADE)
    related_class = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    template    = models.ForeignKey(TemplateAssessment, on_delete=models.CASCADE, null=True)

    completed   = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=False) 