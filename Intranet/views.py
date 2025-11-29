from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.http.response import HttpResponse
from Api.models import *
from google import genai
from pydantic import BaseModel
from django.utils import timezone
import json
from decouple import config

# class for geminy purposes
class Formater(BaseModel):
    summary : str
    recommendation : str
    activity : str
    ingredients: list[str]

# Create your views here.
@login_required
@require_http_methods(["GET","POST"])
def search(request):

    all_subjects = Subject.objects.all()
    all_subjects = [subject for subject in all_subjects]
    return render(request,"search.html",{"subjects":all_subjects})

@login_required
@require_http_methods(["GET","POST"])
def profile(request):

    current_user = request.user
    current_student = Student.objects.get(user=request.user)
    current_school = School.objects.get(name=current_student.career)
    current_learningstyle = LearningStyle.objects.get(name=current_student.learning_style)

    all_info = {
        "username":current_user.username,
        "fullname": f'{current_user.first_name} {current_user.last_name}',
        "email": current_user.email,
        "studentcode": current_student.code,
        "grade": f'{current_student.year}° (cycle {current_student.cycle})',
        "school": current_school.name,
        "schooldescription" : current_school.description,
        "learningstyle": current_learningstyle.name,
        "learningstyledescription" : current_learningstyle.description,
        "hobbies": [hobbies.hobby for hobbies in StudentHobby.objects.filter(student=current_student.pk)]
    }

    return render(request,"profile.html",{"studentuser":all_info})

@login_required
@require_http_methods(["GET","POST"])
def subject(request, code):

    current_student = Student.objects.get(user=request.user)
    current_subject = Subject.objects.get(pk=code)
    all_lessons     = Lesson.objects.filter(subject=current_subject)
    subjectcontent = {
        "pk":current_subject.pk,
        "name":current_subject.name,
        "description" : current_subject.description,
        "year":current_subject.year,
        "cycle":current_subject.ciclo,
        "image":current_subject.image,
        "lessons": all_lessons,
    }

    is_enrolled = StudentSubject.objects.filter(student= current_student, subject = current_subject).exists()
    if  is_enrolled:

        return render(request, "subject-enrolled.html",context={"subject":subjectcontent})
    
    return render(request, "subject-no-enrolled.html",context={"subject":subjectcontent})

@login_required
@require_http_methods(["GET","POST"])
def enroll_subject(request,code):

    current_student = Student.objects.get(user=request.user)
    current_subject = Subject.objects.get(pk=code)
    StudentSubject.objects.create(student=current_student,subject=current_subject).save()

    return redirect("subject",code=code)

@login_required
@require_http_methods(["GET","POST"])
def lesson(request, code):

    # lesson
    print("ERROR 01")
    current_lesson = Lesson.objects.get(pk=code)

    # content
    print("ERROR 02")
    current_content = Content.objects.get(related_class=current_lesson)

    # subject
    print("ERROR 03")
    current_subject = Subject.objects.get(pk=current_lesson.subject.pk)

    # student
    print("ERROR 04")
    current_student = Student.objects.get(user = request.user)
    student_career = current_student.career.name
    student_cycle = current_student.cycle
    student_year = current_student.year
    learning_style = current_student.learning_style.name

    # adapted
    print("ERROR 05")
    current_summary = AdaptedSummary.objects.filter(related_class=current_lesson, student= current_student)
    current_recommendation = AdaptedRecommendation.objects.filter(related_class=current_lesson, student= current_student)
    current_activity = AdaptedActivity.objects.filter(related_class=current_lesson, student= current_student)
    current_test = AdaptedQuestion.objects.filter(student=current_student,related_class=current_lesson) 

    # Hobbies
    print("ERROR 06")
    list_hobbies = StudentHobby.objects.filter(student=current_student)
    list_hobbies = [Hobby.objects.get(pk=hobby.hobby.pk).name for hobby in list_hobbies]

    # create info with AI
    print("ERROR 07")
    existensing = [current_summary.exists(), current_recommendation.exists(),current_activity.exists(),current_test.exists()]
    if not all(existensing):

        student_data = f"""Datos del estudiante:
            - Carrera: {student_career}
            - Año: {student_year}, Ciclo: {student_cycle}
            - Hobbies: {list_hobbies}
        """
        academic_data = f"""Datos académicos:
            - Curso: {current_subject.name}
            - Lección: {current_lesson.title}
            - Descripción de la lección: {current_lesson.description}
        """
        prompts = {
            "Visual": f"""
                Eres una IA educativa experta en aprendizaje VISUAL.  
                Usa el perfil del estudiante y la lección dada para generar:

                1. **Mapa mental (Markmap)** con resumen del tema (`#` título, `##` subtemas, `-` ideas).
                2. **Mapa mental (Markmap)** con recomendaciones según sus intereses.
                3. **Actividad visual breve** para reforzar el tema .Usa etiquetas html para esta sección.
                4. **Tres preguntas** con tres opciones y respuesta correcta.

                Datos del estudiante:
                {student_data}

                Datos académicos:
                {academic_data}

                Devuelve exclusivamente el siguiente JSON:
                {{
                "summary": "Mapa mental en formato Markmap.",
                "recommendation": "Mapa mental en formato Markmap.",
                "activity": "Actividad visual breve.",
                "questions": [
                    {{"text": "Pregunta 1", "type": "Respuesta Única", "options": ["A) Texto opción A", "B) Texto opción B", "C) Texto opción C"], "answer": "Texto opción A"}},
                    {{"text": "Pregunta 2", "type": "Respuesta Única", "options": ["A) Texto opción A", "B) Texto opción B", "C) Texto opción C"], "answer": "Texto opción A"}},
                    {{"text": "Pregunta 3", "type": "Respuesta Única", "options": ["A) Texto opción A", "B) Texto opción B", "C) Texto opción C"], "answer": "Texto opción A"}}
                ]
                }}
            """,
            "Auditivo": f"""
                Eres una IA educativa experta en aprendizaje AUDITIVO.  
                Usa el perfil del estudiante y la lección dada para generar:

                1. **Guion narrativo** (voz o podcast) con el resumen del tema (explicación clara y secuencial).
                2. **Guion narrativo** (voz o podcast) con recomendaciones personalizadas según sus intereses.
                3. **Actividad auditiva breve** (voz o podcast), como escuchar y repetir, o describir lo aprendido oralmente.
                4. **Tres preguntas** con tres opciones y respuesta correcta (estilo de comprensión auditiva).

                Datos del estudiante:
                {student_data}

                Datos académicos:
                {academic_data}

                Devuelve exclusivamente el siguiente JSON:
                {{
                "summary": "Guion narrativo del resumen.",
                "recommendation": "Guion narrativo de recomendaciones.",
                "activity": "Actividad auditiva breve.",
                "questions": [
                    {{"text": "Pregunta 1", "type": "Respuesta Única", "options": ["A) Texto opción A", "B) Texto opción B", "C) Texto opción C"], "answer": "Texto opción A"}},
                    {{"text": "Pregunta 2", "type": "Respuesta Única", "options": ["A) Texto opción A", "B) Texto opción B", "C) Texto opción C"], "answer": "Texto opción A"}},
                    {{"text": "Pregunta 3", "type": "Respuesta Única", "options": ["A) Texto opción A", "B) Texto opción B", "C) Texto opción C"], "answer": "Texto opción A"}}
                ]
                }}
            """,
            "Kinestésico":f"""
                Eres una IA educativa experta en aprendizaje KINESTÉSICO.  
                Usa el perfil del estudiante y la lección dada para generar:

                1. **Resumen práctico** del tema con énfasis en acciones, ejemplos y simulaciones. Usa etiquetas html para esta sección.
                2. **Recomendaciones prácticas** adaptadas a sus intereses (aprender haciendo). Usa etiquetas html para esta sección.
                3. **Actividad física o interactiva** que permita aplicar lo aprendido (experimento, simulación o movimiento). Usa etiquetas html para esta sección. Usa etiquetas html para esta sección.
                4. **Tres preguntas** con tres opciones y respuesta correcta (enfocadas en aplicación práctica).

                Datos del estudiante:
                {student_data}

                Datos académicos:
                {academic_data}

                Devuelve exclusivamente el siguiente JSON:
                {{
                "summary": "Resumen práctico con ejemplos.",
                "recommendation": "Recomendaciones prácticas.",
                "activity": "Actividad kinestésica o simulación.",
                "questions": [
                    {{"text": "Pregunta 1", "type": "Respuesta Única", "options": ["A) Texto opción A", "B) Texto opción B", "C) Texto opción C"], "answer": "Texto opción A"}},
                    {{"text": "Pregunta 2", "type": "Respuesta Única", "options": ["A) Texto opción A", "B) Texto opción B", "C) Texto opción C"], "answer": "Texto opción A"}},
                    {{"text": "Pregunta 3", "type": "Respuesta Única", "options": ["A) Texto opción A", "B) Texto opción B", "C) Texto opción C"], "answer": "Texto opción A"}}
                ]
                }}
            """,
            "Lectura": f"""
                Eres una IA educativa experta en aprendizaje por LECTURA.  
                Usa el perfil del estudiante y la lección dada para generar:

                1. **Resumen textual estructurado** (párrafos y listas) que sintetice el tema. Usa etiquetas html para esta sección.
                2. **Recomendaciones escritas** basadas en sus intereses (libros, artículos, apuntes). Usa etiquetas html para esta sección.
                3. **Actividad escrita breve**, como redactar una síntesis, responder preguntas o crear un resumen. Usa etiquetas html para esta sección. Usa etiquetas html para esta sección.
                4. **Tres preguntas** con tres opciones y respuesta correcta (basadas en comprensión lectora).

                Datos del estudiante:
                {student_data}

                Datos académicos:
                {academic_data}

                Devuelve exclusivamente el siguiente JSON:
                {{
                "summary": "Resumen textual estructurado.",
                "recommendation": "Recomendaciones escritas.",
                "activity": "Actividad de lectura o escritura breve.",
                "questions": [
                    {{"text": "Pregunta 1", "type": "Respuesta Única", "options": ["A) Texto opción A", "B) Texto opción B", "C) Texto opción C"], "answer": "Texto opción A"}},
                    {{"text": "Pregunta 2", "type": "Respuesta Única", "options": ["A) Texto opción A", "B) Texto opción B", "C) Texto opción C"], "answer": "Texto opción A"}},
                    {{"text": "Pregunta 3", "type": "Respuesta Única", "options": ["A) Texto opción A", "B) Texto opción B", "C) Texto opción C"], "answer": "Texto opción A"}}
                ]
                }}
            """,
        }
        
        print("ERROR 08")
        client = genai.Client(api_key=config("MYGEMINI_API"))
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompts[learning_style],
            config={
                "response_mime_type": "application/json",
            },
        )
        data = response.text
        data = json.loads(data)

        print("ERROR 09")
        summary = AdaptedSummary.objects.create(
            title=current_lesson.title,
            content=data["summary"],
            student=current_student,
            related_class=current_lesson,
            completed=True,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            # image=data["media"][0]["description"]
        )

        print("ERROR 10")
        recommendation = AdaptedRecommendation.objects.create(
            title=current_lesson.title,
            content=data["recommendation"],
            student=current_student,
            related_class=current_lesson,
            completed=True,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            # image=data["media"][1]["description"]
        )

        print("ERROR 11")
        activity = AdaptedActivity.objects.create(
            title=current_lesson.title,
            content=data["activity"],
            student=current_student,
            related_class=current_lesson,
            completed=True,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            # image="Actividad visual tipo flujo de decisión sobre emociones"
        )

        print("ERROR 12")
        template = TemplateAssessment.objects.create(
            number_questions = 3,
            max_grade        = 20,
            type_questions   = TypeQuestion.objects.get(description="Respuesta Única"),
        )

        print("ERROR 13")
        questions = [{"question":q["text"],"option":q["options"],"answer":q["answer"]} for q in data["questions"]]
        for q in data["questions"]:
            AdaptedQuestion.objects.create(
                question=q["text"],
                options = q["options"],
                answer=q["answer"],
                status=False,
                student=current_student,
                related_class=current_lesson,
                template=template,
                completed=False,
                created_at=timezone.now(),
                updated_at=timezone.now(),
            )

    # calculating grade
    grade = 0
    status = None
    for question in current_test:

        if question.completed:

            grade += round(20/3,1) if  question.status == True else 0 
            status = "( Prueba Realizada )"

    lesson_data = {
        # subject
        "subjectcode":current_subject.pk,
        # lesson
        "lessoncode":current_lesson.pk,
        "title":current_lesson.title,
        "description":current_lesson.description,
        "goal":current_lesson.goal,
        "subject":current_lesson.subject,
        "expectation":current_lesson.expectation,
        # content
        "ppttitle":current_content.title,
        "ppt":current_content.location,
        # summary
        "summarycontent":current_summary[0].content,
        # recommendation
        "recommendationcontent":current_recommendation[0].content,
        # activity
        "activitycontent":current_activity[0].content,
        # question
        "test01":{"question":current_test[0].question,"options":list(current_test[0].options.replace("[","").replace("]","").split("',"))},
        "test02":{"question":current_test[1].question,"options":list(current_test[1].options.replace("[","").replace("]","").split("',"))},
        "test03":{"question":current_test[2].question,"options":list(current_test[2].options.replace("[","").replace("]","").split("',"))},
        # grade
        "grade": int(grade),
        # message for interactivity
        "status":status,
    }

    if learning_style == "Visual":

        return render(request,"lesson-visual.html", context={"lesson_data":lesson_data})

    if learning_style == "Auditivo":

        return render(request,"lesson-audio.html", context={"lesson_data":lesson_data})

    if learning_style == "Lectura":

        return render(request,"lesson-reading.html", context={"lesson_data":lesson_data})

    if learning_style == "Kinestésico":

        return render(request,"lesson-kinestesic.html", context={"lesson_data":lesson_data})

@login_required
@require_http_methods(["GET","POST"])
def mylearning(request):

    try:

        data = []
        current_student = Student.objects.get(user = request.user)
        all_courses = [Subject.objects.get(pk=course.subject.pk) for course in StudentSubject.objects.filter(student = current_student)]

        total_lessons = 0
        completed_lessons = 0
        grades = 0
        for course in all_courses:

            all_lessons = Lesson.objects.filter(subject=course.pk)
            for lesson in all_lessons:
                
                adapted_questions = AdaptedQuestion.objects.filter(student = current_student.pk, related_class= lesson.pk)
                question_completed = [question.completed for question in adapted_questions]

                if any(question_completed):
                    
                    completed_lessons += 1
                    status = [question.status for question in adapted_questions]
                    grades += int(sum(status) * round(20/3,1))

                total_lessons += 1

            data.append({
                "course":course,
                "progress":int((completed_lessons / total_lessons)*100),
                "avg_grade":int(grades/completed_lessons),
            })
            
            total_lessons = 0
            completed_lessons = 0
            grades = 0

    except:
        
        data = []

    finally:

        return render(request,"mylearning.html",context={"data":data})

@login_required
@require_http_methods(["GET","POST"])
def test_evaluation(request,code):

    # lesson
    current_lesson = Lesson.objects.get(pk=code)

    # student
    current_student = Student.objects.get(user = request.user)

    # real answer
    adapted_questions = [AdaptedQuestion.objects.get(pk=instance.pk) for instance in AdaptedQuestion.objects.filter(student=current_student,related_class=current_lesson).order_by("pk")]

    # user answer
    user_answers = [request.POST.get('test01'), request.POST.get('test02'), request.POST.get('test03')]

    #updating grades 
    idx = 0
    for answer in user_answers:

        if isinstance(answer, str) and (adapted_questions[idx].answer in answer):

            adapted_questions[idx].status = True
            adapted_questions[idx].completed = True

        else:

            adapted_questions[idx].status = False
            adapted_questions[idx].completed = True
        
        adapted_questions[idx].save()
        idx += 1

    return redirect('lesson', code=code)

@login_required
@require_http_methods(["GET","POST"])
def logout_view(request):

    logout(request)
    return redirect('login_view')