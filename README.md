# 🧠 Sistema de Aprendizaje Adaptativo Basado en Inteligencia Artificial

Este proyecto implementa un **Sistema de Aprendizaje Adaptativo** que utiliza **Inteligencia Artificial** para personalizar la experiencia educativa de cada estudiante.  
Desarrollado en **Python** con el framework **Django**, el sistema analiza el perfil académico, intereses y estilo de aprendizaje del estudiante para generar contenidos, evaluaciones y recomendaciones dinámicas.

---

## 🚀 Características Principales

- Adaptación del contenido según el perfil del estudiante.
- Integración con **Google Gemini API** para la generación de contenido educativo basado en IA.
- Sistema de autenticación para estudiantes y administradores.
- Evaluaciones automatizadas con retroalimentación inteligente.
- Interfaz intuitiva con formularios dinámicos y resultados visuales.
- Panel administrativo para gestión de usuarios, materias y resultados.

---

## 🧩 Tecnologías Utilizadas

- **Lenguaje:** Python 3.x  
- **Framework web:** Django  
- **Integración IA:** Google GenAI (Gemini)  
- **Configuración segura:** python-decouple  
- **Base de datos:** SQLite (por defecto en desarrollo)  

---

## ⚙️ Instalación y Ejecución Local

Sigue estos pasos para levantar el proyecto localmente:

### 1️⃣ Requisitos previos
Asegúrate de tener instalado:
- [Python 3.9 o superior](https://www.python.org/downloads/)
- `pip` (administrador de paquetes de Python)

### 2️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 3️⃣ Instalar dependencias necesarias
```bash
pip install django python-decouple google-genai
```

### 4️⃣ Configurar variables de entorno
```bash
MYGEMINI_API = AQUISUTOKENDEAPIDEGEMINY
```

### 5️⃣ Ejecutar el servidor local
```bash
python manage.py runserver
```

Una vez ejecutado, abre en tu navegador:
http://127.0.0.1:8000/
