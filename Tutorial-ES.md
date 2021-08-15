# 20-21_viagdi

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/osint/catalog/static/images/CyberPeek.png" />
</p>

En este documento mostramos un pequeño tutprial a traves de la herramienta web para mostrar cómo funciona y todas sus utilidades.

## Comienzo

Abriendo una terminal en el directorio donde tengamos clonado el repositorio del proyecto, activamos el entorno virtual creado para el proyecto.
Una vez activado, desde el directorio osint/, ejecutar el siguiente comando para lebantar el servidor web de la herramienta:

```bash
python manage.py runserver
```

Este comando levantará el servidor web y nos proporcionará una url, normalmente http://127.0.0.1:8000/, mediante la cual accederemos a la interfaz web de la herrameinta.

Por la url anterior se peude ver que Django levanta el servidor en el puesto 8000 por defecto. Si queremos levantarlo utilizando otro
puerto, ejecutar el comando

```bash
python manage.py runserver <port>
```

accediendo a la url que nos especifique Django, accederemos a la página de inicio de la herramienta

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/ImagesTutorial/inicio.jpg" />
</p>
