from Api.models import School, Hobby, LearningStyle, TypeQuestion, Subject, Lesson, Content

# Limpiar registros anteriores (opcional)
School.objects.all().delete()
Hobby.objects.all().delete()
LearningStyle.objects.all().delete()
TypeQuestion.objects.all().delete()
Subject.objects.all().delete()
Lesson.objects.all().delete()
Content.objects.all().delete()

# Crear Hobbies
Hobby.objects.create(name="Caminata", description="Explorar paisajes; se puede usar para enseñar biología, geografía o sostenibilidad.")
Hobby.objects.create(name="Manualidades", description="Crear objetos con las manos; permite personalizar tareas en física o geometría.")
Hobby.objects.create(name="Lectura", description="Afición a la literatura; útil para contextualizar comprensión lectora, historia o filosofía.")
Hobby.objects.create(name="Fotografía", description="Captura visual del entorno; útil en contenidos de arte, comunicación o multimedia.")
Hobby.objects.create(name="Baile", description="Expresión corporal cultural; aplicable en clases de música, historia o educación física.")
Hobby.objects.create(name="Cocina", description="Preparación de platos típicos; aplicable en ciencias, química o economía doméstica.")
Hobby.objects.create(name="Videojuegos", description="Pasatiempo digital común; se puede usar para gamificación o lógica algorítmica.")
Hobby.objects.create(name="Dibujo", description="Habilidad creativa muy presente en jóvenes; útil en contenidos visuales, diseño o geometría.")
Hobby.objects.create(name="Música", description="Afición a interpretar canciones; útil para asociar con aprendizaje auditivo o de idiomas.")
Hobby.objects.create(name="Fútbol", description="Deporte más practicado y seguido; se puede usar para ejemplos matemáticos o físicos.")

# Crear Schools
electronica = School.objects.create(name="Ingeniería Electrónica", description="Los estudiantes de Ingeniería Electrónica se especializan en el análisis, diseño y desarrollo de circuitos, dispositivos y sistemas electrónicos. Tienen un fuerte enfoque en señales, microcontroladores, electrónica de potencia y automatización. En un sistema de aprendizaje adaptativo, estos estudiantes podrían beneficiarse de rutas que integren simulaciones interactivas de circuitos, proyectos basados en hardware, y contenidos vinculados a IoT, instrumentación y control automático. Prefieren actividades visuales y prácticas que les permitan modelar y probar circuitos digitales o analógicos.")
telecomunicaciones = School.objects.create(name="Ingeniería de Telecomunicaciones", description="Los estudiantes de esta especialidad tienen un enfoque en la transmisión de datos, redes digitales, sistemas de comunicación y tecnologías inalámbricas. Manejan conceptos complejos como modulación, espectro de frecuencias, fibra óptica, protocolos de red y sistemas satelitales. En un sistema de aprendizaje adaptativo, se sugiere el uso de animaciones explicativas, simuladores de redes (como Cisco Packet Tracer), análisis de casos reales de infraestructura de comunicaciones, y contenido ajustado a su nivel de abstracción matemática. Valoran la claridad visual y la contextualización práctica de los sistemas de telecomunicaciones.")
mecatronica = School.objects.create(name="Ingeniería Mecatrónica", description="Esta carrera combina electrónica, informática, mecánica y control para el diseño de sistemas automáticos inteligentes. Los estudiantes de Ingeniería Mecatrónica se interesan en la robótica, automatización, sistemas embebidos y controladores PID. En el sistema adaptativo, es ideal ofrecerles contenidos que integren aprendizaje visual-cinestésico, entornos de simulación de robots, programación de controladores (como Arduino o PLC), y casos de uso de sistemas mecatrónicos industriales. Prefieren actividades que mezclen la teoría con la implementación práctica de prototipos.")
informatica = School.objects.create(name="Ingeniería Informática", description="Los estudiantes de Ingeniería Informática poseen habilidades avanzadas en programación, diseño de software, estructuras de datos, redes y sistemas operativos. Tienden a destacar en lógica computacional, resolución de problemas mediante algoritmos y desarrollo de sistemas robustos. En un entorno de aprendizaje adaptativo, requieren módulos que integren entornos de codificación interactivos, resolución de desafíos algorítmicos personalizados, análisis de ciberseguridad y temas de inteligencia artificial. Aprenden bien a través de proyectos de desarrollo colaborativo, retos de programación, y contenidos secuenciales.")

# Crear Learning Styles
LearningStyle.objects.create(name="Lectura", description="Prefiere contenidos secuenciales, estructurados y con razonamiento. Preferencia por texto escrito, análisis estructurado")
LearningStyle.objects.create(name="Kinestésico", description="Aprende a través de la acción, el movimiento o la experimentación física. Se beneficia de actividades prácticas, simulaciones, juegos o interacción manipulativa.")
LearningStyle.objects.create(name="Auditivo", description="Prefiere aprender mediante el uso del oído: explicaciones orales, podcasts, canciones, grabaciones o diálogos. La retroalimentación oral o explicativa es clave.")
LearningStyle.objects.create(name="Visual", description="El estudiante aprende mejor mediante imágenes, diagramas, mapas conceptuales, infografías y esquemas. Requiere contenido que estimule la vista y favorezca la comprensión visual.")

# Crear Type Questions
TypeQuestion.objects.create(description="Respuesta Única")
TypeQuestion.objects.create(description="Respuesta Libre")
TypeQuestion.objects.create(description="Selección Múltiple")

# Materias para Ingeniería Electrónica
cir_elect = Subject.objects.create(
    name="Circuitos Eléctricos",
    description="Estudio de leyes fundamentales, análisis de mallas, nodos y redes resistivas, capacitivas e inductivas.",
    school=electronica,
    year=1,
    ciclo=1,
    image = "Subject/circuitos.jpg"
)

cir_elect_l1 = Lesson.objects.create(
    title="Ley de Ohm y Leyes de Kirchhoff",
    description="Fundamentos de la electricidad básica: voltaje, corriente y resistencia.",
    goal="Comprender y aplicar la ley de Ohm y las leyes de Kirchhoff a circuitos simples.",
    expectation="El estudiante será capaz de resolver circuitos básicos por mallas y nodos.",
    subject=cir_elect
)
Content.objects.create(
    title="Teoría de Circuitos - Lección 1",
    format=".pdf",
    location="Content/electrónica.pdf",
    related_class=cir_elect_l1
)

cir_elect_l2 = Lesson.objects.create(
    title="Análisis de Mallas",
    description="Resolución de circuitos con múltiples ramas usando la técnica de mallas.",
    goal="Aplicar el método de mallas a redes eléctricas.",
    expectation="Analizar correctamente el flujo de corriente en circuitos planos.",
    subject=cir_elect
)
Content.objects.create(
    title="Análisis de Mallas - Lección 2",
    format=".pdf",
    location="Content/electrónica.pdf",
    related_class=cir_elect_l2
)

cir_elect_l3 = Lesson.objects.create(
    title="Análisis de Nodos",
    description="Resolución de circuitos con la técnica de nodos y corriente.",
    goal="Desarrollar habilidad para analizar tensiones en redes por nodos.",
    expectation="Resolver correctamente circuitos eléctricos por nodos.",
    subject=cir_elect
)
Content.objects.create(
    title="Nodos en Circuitos - Lección 3",
    format=".pdf",
    location="Content/electrónica.pdf",
    related_class=cir_elect_l3
)

cir_elect_l4 = Lesson.objects.create(
    title="Teoremas de Thevenin y Norton",
    description="Uso de equivalencias para simplificar circuitos.",
    goal="Simplificar análisis con modelos equivalentes.",
    expectation="Aplicar teoremas de manera práctica en circuitos complejos.",
    subject=cir_elect
)
Content.objects.create(
    title="Teoremas de Circuitos - Lección 4",
    format=".pdf",
    location="Content/electrónica.pdf",
    related_class=cir_elect_l4
)

cir_elect_l5 = Lesson.objects.create(
    title="Circuitos en AC",
    description="Análisis de circuitos con fuentes sinusoidales.",
    goal="Comprender el comportamiento de circuitos ante corriente alterna.",
    expectation="Resolver ejercicios aplicando fasores y frecuencia.",
    subject=cir_elect
)
Content.objects.create(
    title="Circuitos AC - Lección 5",
    format=".pdf",
    location="Content/electrónica.pdf",
    related_class=cir_elect_l5
)

# Materias para Ingeniería Informática
programacion = Subject.objects.create(
    name="Programación",
    description="Curso orientado al aprendizaje de herramientas de desarrollo de software como lo son los LP de bajo y alto nivel. Este curso logrará formar un pensamiento lógico y analítico para que el alumno pueda aplicarlo en la creación de programas y herramientas de software.",
    school=informatica,
    year=2,
    ciclo=2,
    image = "Subject/programacion.jpg"
)

programacion_l1 = Lesson.objects.create(
    title="Lógica de Programación",
    description="Introducción al pensamiento algorítmico y resolución de problemas computacionales.",
    goal="Fomentar la comprensión del flujo lógico mediante pseudocódigo y diagramas de flujo.",
    expectation="No se requieren conocimientos previos, pero se espera interés por resolver problemas.",
    subject=programacion
)
Content.objects.create(
    title="Programación - Lección 1",
    format=".pdf",
    location="Content/informática.pdf",
    related_class=programacion_l1
)

programacion_l2 = Lesson.objects.create(
    title="Estructuras Condicionales",
    description="Implementación de decisiones simples y compuestas en el flujo de programas.",
    goal="Dominar estructuras if, else y elif.",
    expectation="Ser capaz de simular decisiones en programas sencillos.",
    subject=programacion
)
Content.objects.create(
    title="Programación - Lección 2",
    format=".pdf",
    location="Content/informática.pdf",
    related_class=programacion_l2
)

programacion_l3 = Lesson.objects.create(
    title="Bucles y Repetición",
    description="Uso de bucles for y while para controlar iteraciones.",
    goal="Diseñar algoritmos repetitivos controlados por condiciones o contadores.",
    expectation="El estudiante usará ciclos para recorrer estructuras.",
    subject=programacion
)
Content.objects.create(
    title="Programación - Lección 3",
    format=".pdf",
    location="Content/informática.pdf",
    related_class=programacion_l3
)

programacion_l4 = Lesson.objects.create(
    title="Funciones y Modularidad",
    description="Creación y uso de funciones para reutilización de código.",
    goal="Dividir un programa en funciones para facilitar su mantenimiento.",
    expectation="Comprender paso de parámetros y retorno de valores.",
    subject=programacion
)
Content.objects.create(
    title="Programación - Lección 4",
    format=".pdf",
    location="Content/informática.pdf",
    related_class=programacion_l4
)

programacion_l5 = Lesson.objects.create(
    title="Manejo de Archivos",
    description="Leer y escribir archivos como fuente y destino de datos.",
    goal="Introducir persistencia en los programas mediante archivos.",
    expectation="El estudiante leerá y generará archivos txt.",
    subject=programacion
)
Content.objects.create(
    title="Programación - Lección 5",
    format=".pdf",
    location="Content/informática.pdf",
    related_class=programacion_l5
)

# Materias para Ingeniería de Telecomunicaciones
teoria_senal = Subject.objects.create(
    name="Teoría de la Señal",
    description="Fundamentos del análisis y procesamiento de señales continuas y discretas en el tiempo.",
    school=telecomunicaciones,
    year=2,
    ciclo=2,
    image = "Subject/señales.jpg"
)

teoria_senal_l1 = Lesson.objects.create(
    title="Señales en el dominio del tiempo",
    description="Caracterización de señales en el dominio temporal.",
    goal="Identificar y clasificar tipos de señales según su comportamiento temporal.",
    expectation="Conocerá los conceptos básicos de amplitud, energía y potencia.",
    subject=teoria_senal
)
Content.objects.create(
    title="Teoría de la Señal - Lección 1",
    format=".pdf",
    location="Content/telecomunicaciones.pdf",
    related_class=teoria_senal_l1
)

teoria_senal_l2 = Lesson.objects.create(
    title="Señales periódicas y aperiódicas",
    description="Clasificación y análisis de señales periódicas y no periódicas.",
    goal="Distinguir entre señales según su periodicidad.",
    expectation="Aplicará transformadas básicas para entender sus propiedades.",
    subject=teoria_senal
)
Content.objects.create(
    title="Teoría de la Señal - Lección 2",
    format=".pdf",
    location="Content/telecomunicaciones.pdf",
    related_class=teoria_senal_l2
)

teoria_senal_l3 = Lesson.objects.create(
    title="Transformada de Fourier",
    description="Representación de señales en frecuencia mediante la Transformada de Fourier.",
    goal="Aplicar la transformada para analizar señales periódicas.",
    expectation="Comprenderá espectros y filtrado en frecuencia.",
    subject=teoria_senal
)
Content.objects.create(
    title="Teoría de la Señal - Lección 3",
    format=".pdf",
    location="Content/telecomunicaciones.pdf",
    related_class=teoria_senal_l3
)

teoria_senal_l4 = Lesson.objects.create(
    title="Transformada de Laplace",
    description="Uso de la transformada de Laplace en el análisis de sistemas lineales.",
    goal="Resolver ecuaciones diferenciales mediante la transformada.",
    expectation="Interpretará polos y ceros.",
    subject=teoria_senal
)
Content.objects.create(
    title="Teoría de la Señal - Lección 4",
    format=".pdf",
    location="Content/telecomunicaciones.pdf",
    related_class=teoria_senal_l4
)

teoria_senal_l5 = Lesson.objects.create(
    title="Convolución de señales",
    description="Aplicación de la operación de convolución para el análisis de sistemas.",
    goal="Evaluar la salida de un sistema mediante la convolución.",
    expectation="Comprenderá cómo afecta una señal a otra al pasar por un sistema.",
    subject=teoria_senal
)
Content.objects.create(
    title="Teoría de la Señal - Lección 5",
    format=".pdf",
    location="Content/telecomunicaciones.pdf",
    related_class=teoria_senal_l5
)

# Materias para Ingeniería Mecatrónica
sistemas_control = Subject.objects.create(
    name="Sistemas de Control",
    description="Introducción al modelado y análisis de sistemas dinámicos y su control mediante retroalimentación.",
    school=mecatronica,
    year=3,
    ciclo=5,
    image = "Subject/control.jpg"
)

sistemas_control_l1 = Lesson.objects.create(
    title="Modelado de Sistemas Dinámicos",
    description="Técnicas para modelar sistemas físicos usando ecuaciones diferenciales.",
    goal="Formular modelos matemáticos de sistemas eléctricos, térmicos y mecánicos.",
    expectation="Aplicar modelos para predecir comportamientos dinámicos.",
    subject=sistemas_control
)
Content.objects.create(
    title="Sistemas de Control - Lección 1",
    format=".pdf",
    location="Content/mecatrónica.pdf",
    related_class=sistemas_control_l1
)

sistemas_control_l2 = Lesson.objects.create(
    title="Representación en Espacio de Estados",
    description="Uso de vectores de estado y matrices para representar sistemas.",
    goal="Desarrollar representación compacta de sistemas multivariables.",
    expectation="Relacionar estados, entradas y salidas.",
    subject=sistemas_control
)
Content.objects.create(
    title="Sistemas de Control - Lección 2",
    format=".pdf",
    location="Content/mecatrónica.pdf",
    related_class=sistemas_control_l2
)

sistemas_control_l3 = Lesson.objects.create(
    title="Respuesta en Frecuencia",
    description="Análisis de la estabilidad y desempeño a diferentes frecuencias.",
    goal="Evaluar comportamiento ante señales senoidales.",
    expectation="Interpretar diagramas de Bode y Nyquist.",
    subject=sistemas_control
)
Content.objects.create(
    title="Sistemas de Control - Lección 3",
    format=".pdf",
    location="Content/mecatrónica.pdf",
    related_class=sistemas_control_l3
)

sistemas_control_l4 = Lesson.objects.create(
    title="Control PID",
    description="Diseño e implementación de controladores proporcionales-integrales-derivativos.",
    goal="Sintonizar parámetros PID para mejorar la respuesta del sistema.",
    expectation="Lograr reducción de error y mayor estabilidad.",
    subject=sistemas_control
)
Content.objects.create(
    title="Sistemas de Control - Lección 4",
    format=".pdf",
    location="Content/mecatrónica.pdf",
    related_class=sistemas_control_l4
)

sistemas_control_l5 = Lesson.objects.create(
    title="Controladores Digitales",
    description="Implementación de controladores discretos usando microcontroladores.",
    goal="Codificar lógica de control en entornos embebidos.",
    expectation="Desarrollar prototipos funcionales de lazo cerrado.",
    subject=sistemas_control
)
Content.objects.create(
    title="Sistemas de Control - Lección 5",
    format=".pdf",
    location="Content/mecatrónica.pdf",
    related_class=sistemas_control_l5
)
