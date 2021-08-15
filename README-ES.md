# 20-21_viagdi

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/osint/catalog/static/images/CyberPeek.png" />
</p>

# Descripción del proyecto

CyberPeek es una herramienta de análisis de ciberinteligencia desarrollada para permitir la gestión de la información y las pruebas recogidas en un análisis de fuentes OSINT, sobre los diferentes elementos implicados (individuos, sociedades, relaciones, etc.), así como la representación automática de esta información mediante modelos visuales. 

El objetivo de esta herramienta sería entonces facilitar el análisis de la información recogida mostrando, en todo momento, las relaciones existentes entre los elementos identificados.

Esta herramienta permite el trabajo conjunto de los analistas, de forma que puedan compartir estudios específicos de aquellas entidades/individuos que consideren oportunos, añadiendo comentarios entre ellos en la misma investigación.

# Características / Instalación

Utilizar [pip](https://pip.pypa.io/en/stable/) para instalar las librerías de django y bootstrap para desarrollar y diseñar la herramienta:

```bash
pip install django
```

```bash
pip install django-bootstrap
```

Bootstrap se utiliza para diseñar los ficheros .css que ajustan la estética de la interfaz web.

# Preparación de la herramienta

Primero, crear un entorno virtual en el directorio donde se quiera clonar el proyecto/repositorio de la herramienta:

```bash
python3 -m venv /path/to/new/virtual/environment
```

Después, instalar los requisitos de librerías reogidos en el fichero requirements.txt

```bash
pip install -r requirements.txt
```

Ahora, clonar el repositorio localmente. Luego, utilizando alguna herramienta de programación en python como PyCharm, abrir una terminal. 
Desde el directorio 20-21_viagdi/osint/, ejecutar los siguientes comandos para configurar los modelos django del proyecto:

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

Ahora la herramienta está lista para usarse.

# Utilización básica

Para ejecutar el proyecto, ejecutar el siguiente comando desde una terminal con el entorno virtual del proyecto activado, 
y desde el directorio 20-21_viagdi/osint/

```bash
python manage.py runserver 
```
Accediendo a la url http://127.0.0.1:8000/ se accede a la interfaz web de la herramienta para utilizarla.

Ahora puedes registrarte en la herramienta, o loggearte con una cuenta de usuario creada específicamente para probar la herramienta:

```bash
username: user

password: user1234
```

# Documentación de desarrollo

# Architecture

Este proyecto tiene dos paquetes python, osint y catalog. el paquete osint es creado por defecto por Django y contiene los principales archivos python para desarrollar un proyecto django. el paquete catalog contiene todos los archivos relacionados con los modelos del proyecto, y todos los archivos relacionados con el diseño de la interfaz.

# Prepare development/execution environment
