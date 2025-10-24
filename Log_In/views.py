from django.shortcuts import render, redirect
from Api.models import User, Student, School, LearningStyle, StudentHobby, Hobby
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

# Create your views here.

@require_http_methods(["GET","POST"])
def signin_view(request):

    # to create new user
    if request.method == "POST":

        # get data from form in html
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        student_code = request.POST.get("student_code")
        email = request.POST.get("email")
        career = request.POST.get("career")
        year = int(request.POST.get("year"))
        cicle = int(request.POST.get("cicle"))
        pw1 = request.POST.get("password1")
        pw2 = request.POST.get("password2")

        # user exists based on username
        if User.objects.filter(username=username).exists():
            print("El nombre de usuario ya existe.")
            return render(request, "signin.html")

        # minimun characters of student code
        if len(student_code) != 10:
            print("Código de Estudiante Invalido")
            return render(request, "signin.html")
        
        # user exists based on student code
        student_code = int(student_code)
        student = Student.objects.filter(code=student_code).first()
        if student:
            print("Estudiante ya se encuentra registrado")
            return render(request, "signin.html")
        
        # validate extension of email
        if "@unfv.edu.pe" not in email:
            print("Correo con dominio no valido")
            return render(request, "signin.html")
        
        # user exists based on email
        if User.objects.filter(username=email).exists():
            print("Correo ya registrado")
            return render(request, "signin.html")

        # secure for credentials
        if len(pw1) < 6:
            print("La contraseña debe tener al menos 6 caracteres.")
            return render(request, "signin.html")

        # compatibility of password
        if pw1 != pw2:
            print("Las contraseñas no coinciden.")
            return render(request, "signin.html")

        # creation of user
        user = User.objects.create_user(
            username=username, 
            email=email, 
            password=pw1, 
            first_name = first_name, 
            last_name = last_name,
        )
        print("Cuenta creada exitosamente.")

        # creation of student
        career_choosen = School.objects.get(name=career)
        student = Student.objects.create(
            code=student_code,
            user=user,
            career=career_choosen,
            year=year,
            cycle=cicle,
        )
        print("Estudiante creado exitosamente.")

        # move to login view
        return redirect("login_view")

    # to show template
    return render(request, "signin.html")

@require_http_methods(["GET","POST"])
def login_view(request):

    # to check credential
    if request.method == "POST":

        # info form html form
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        # user exsits with right credentials
        if user is None:
            print("Credenciales inválidas. Intenta nuevamente")
            return redirect("login_view")
        
        # right validation
        print(f"Bienvenido, {user.username}")
        login(request, user)

        # check if the learning style is created or user must be redirected
        student = Student.objects.get(user = user)
        if student.learning_style is None:
            print("Estilo de Aprendizaje no definido")
            return redirect("qa_vark")
        
        # template for sucessfull login
        return redirect("search") 
    
    # to show template
    return render(request, "login.html")

@login_required
@require_http_methods(["GET","POST"])
def qa_vark(request):

    # to send data for VARK form
    if request.method == "POST":

        # identify user from session
        student = Student.objects.filter(user=request.user)
        if not student.exists():
            logout(request)
            print("Solamente pueden acceder perfiles para estudiantes")
            return redirect("login_view") 

        # identify student from current user
        student = student.first()
        if student.learning_style == None:

            respuestas = [
                request.POST.get("q1"),
                request.POST.get("q2"),
                request.POST.get("q3"),
                request.POST.get("q4"),
            ]

            estilos = [
                "Visual",       
                "Auditivo",       
                "Lectura",       
                "Kinestésico",
            ]

            contabilizacion = [
                respuestas.count("Visual"),       
                respuestas.count("Auditivo"),       
                respuestas.count("Lectura"),       
                respuestas.count("Kinestésico"),
            ]        

            if max(contabilizacion) == 4 or max(contabilizacion) == 3 or max(contabilizacion) == 2:

                learning_style = estilos[contabilizacion.index(max(contabilizacion))]
                learning_style = LearningStyle.objects.get(name=learning_style)
                student.learning_style = learning_style
                student.save()
                print("Se definió el estilo de Aprendizaje")

            print("El questionario VARK del alumno ya fue completado")
            return redirect("qa_hobbies")
        
        return redirect("search")       

    # to show template
    return render(request,"qa_vark.html")

@login_required
@require_http_methods(["GET","POST"])
def qa_hobbies(request):

    # to send data for HOBBIES form
    if request.method == "POST":

        # get current user
        student = Student.objects.filter(user=request.user)
        if not student.exists():
            logout(request)
            print("Solamente pueden acceder perfiles para estudiantes")
            return redirect("login_view") 

        # get current student
        student = student.first()
        studenthobby = Hobby.objects.filter(studenthobby__student = student)
        if not studenthobby.exists():
        
            hobbies_seleccionados = request.POST.getlist("hobbies")
            # Asociar cada hobby al estudiante
            for hobby_nombre in hobbies_seleccionados:

                hobby = Hobby.objects.get(name=hobby_nombre)
                StudentHobby.objects.create(hobby=hobby, student=student)
            
            print("Hobbies Definidos")
            return redirect("search")

        return redirect("search")

    # to show template
    return render(request,"qa_hobbies.html")