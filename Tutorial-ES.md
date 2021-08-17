# 20-21_viagdi

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/osint/catalog/static/images/CyberPeek.png" />
</p>

En este documento mostramos un pequeño tutprial a traves de la herramienta web para mostrar cómo funciona y todas sus utilidades.

Antes de comenzar con el tutorial, hay que realizar las migraciones para instalar las dependencias necesarias y prerrequisitos indicados en el README.md 
del repositorio.

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
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/inicio.jpg" />
</p>

## Registro de un usuario

Para registrarse en la herramienta y crear una cuenta de usuario, accedemos en el panel lateral a "Regístrarse"

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/registroUsuario.JPG" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/formulario_registro_usuarios.JPG" />
</p>

## Login 

Para logearse en la herramienta, accedemos desde el panel lateral com oen la siguiente imagen, y rellenamos el formulario

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/loginLateral.JPG" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/login.JPG" />
</p>

Una vez logeado, el nombre de usuario aparece en el panel lateral para indicar este hecho

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/loggeado.jpg" />
</p>

## LogOut
Para cerrar sesión en la herramienta, accedemos a la pestaña del panel lateral "Logout"

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/logout.JPG" />
</p>

## Listas de Entidades e Individuos Registrados de un usuario

Una vez loggeado en la herramienta, un usuario puede acceder a la lista de entidades de las cuales tiene permiso para acceder y con ello a editar y trabajar sobre ella
(y lo mismo con la lista de individuos), ya sea porque las haya registrado el propio usuario , o porque esos permisos se los haya otorgado otro 
usuario de la herramieta. Para acceder a las listas de entidades e individuos (por separado), hay que pinchar en las pestañas "Mis Entidades" o "Mis Individuos" del panel lateral

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/MisEntidades.jpg" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/MisIndividuos.JPG" />
</p>

y las páginas que muestran dichas listas se muestran en las siguientes imágenes:

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/EntidadesLista.jpg" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/IndividuosLista.jpg" />
</p>

## Registro de una Entidad en la herramienta

Para registrar una nueva entidad, se accede a "Mis Entidades" mediante la pestaña dedicada en el panel lateral, y pichamos 
el botón "Registrar" que se muestra en la siguiente imagen

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/RegistroEntidad.JPG" />
</p>

y después se nos redirige a un formulario de registro con los campos que se muestran a continuación

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/registroEnt1.jpg" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/registroEnt2.JPG" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/registroEnt3.JPG" />

####(En esta imagen se puede ver el campo "borrower". Este campo me permite seleccionar de entre los usuarios de la herramienta aquellos con quienes quiero compartir esta entidad que voy a registrar. Para seleccionar varios usuarios a la vez, pinchar todos los usuarios pulsando a la vez la tecla Control)
</p>

Antes de rellenar todo el formulario, hay que añadir las personas vinculadas (altos cargos de la entidad) a la entidad
que se registra si no han sido registradas anteriormente, así que para ello, hay que hacer clic en "Añadir" en la primera
imagen para que se nos redirija al formulario correspondiente

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/AñadirPersVinc.jpg" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/FormularioPersVinc.jpg" />
</p>

Y de nuevo, vemos que antes de rellenar todo el formulario de un administrador de una entidad, es necesario añadir las otras
entidades vinculadas a este administrador (que seran las entidades relacionadas a una entidad que tenga a este administrador
ocupando un alto cargo en ella), que son otras entidades en las que ocupa otros cargos o son de su propiedad. Para ello, 
pinchamos en "Añadir" como en la imagen, y seremos redirigidos al formulario correspondiente

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/AñadirEntVinc.jpg" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/FormularioEntVinc.jpg" />
</p>

Una vez rellenado este último formulario, guardamos, y el resultado es, por ejemplo

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/EjemploEntRel.JPG" />
</p>

Para volver atrás hasta llegar a la página del formulario de persona vinculada y seguir rellenando dicho formulario,
vamos "atrás" con el navegador hasta llegar y actualizamos la página para que el formulario se actualice y nos muestre 
en el campo de "other entities" la entidad que acabamos de guardar

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/other_entities.JPG" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/EjemploPersVincFormulario.jpg" />
</p>

El resultado de guardar el formulario es

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/PersonaVinculada4.JPG" />
</p>

Para volver al formulario de registro de una entidad con el que empezamos esta sección, de la misma forma que antes, vamos "atrás"
con el anvegador hasta llegar al formulario de registro de una entidad y actualizamos la página para actualizar con ella el 
campo de "Administradores" y que aparezca la opción de "Persona Vinculada 4" que registramo antes

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/administradores.JPG" />
</p>

Rellenamos el resto del formulario y el resultado, como ejemplo, es la página de detalle de la entidad registrada

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/entityDetail.JPG" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/entityDetail2.JPG" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/entityDetail3.jpg" />
</p>

Como se puede ver, desde esta página de detalle podemos eliminar esta entidad o editarla pinchando en los botones
"Editar" o "Eliminar".

En eta página de detalle podemos ver también la interfaz de comentarios para facilitar el trabajo en equipo entre analistas permitiendo
añadir anotaciones adicionales sobre la entidad en cuestión

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/comentarios.JPG" />
</p>

y podemos ver también el grafo que relaciona la entidad en cuestión con las personas vinculadas a la misma y con otras
entidades relacionadas. En el grafo se pueden aplicar filtros para mostrar solo las personas vinculadas, solo las entidades
relacionadas, o todas a la vez como en la imagen anterior

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/grafoOpciones.JPG" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/grafoPersVinc.JPG" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/grafoEntRel.jpg" />
</p>

## Registro de un individuo en la herramienta

Para registrar un nuevo individuo, se accede a "Mis Individuos" mediante la pestaña dedicada en el panel lateral, y pichamos 
el botón "Registrar" que se muestra en la siguiente imagen

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/IndividuosLista.jpg" />
</p>

y después se nos redirige a un formulario de registro con los campos que se muestran a continuación

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/registroInd1.JPG" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/registroInd2.JPG" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/registroInd3.JPG" />

####(En esta imagen se puede ver el campo "borrower". Este campo me permite seleccionar de entre los usuarios de la herramienta aquellos con quienes quiero compartir este individuo que vamos a registrar. Para seleccionar varios usuarios a la vez, pinchar todos los usuarios pulsando a la vez la tecla Control)
</p>

Antes de rellenar todo el formulario, hay que añadir, si es necesario, las redes sociales, los vehículos, las cuentas de email 
y las segundas residencias del individuo que se registra, Evidentemente  esto es opcional, pero más completa será la información
sobre el individuo. Pinchando en "Añadir" del campo correspondiente nos redirigirá al formulario correspondiente para registrar
los objetos que se acaban de mencionar. Estos formularios tienen la siguiente forma


<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/FormularioRedSocial.JPG" />

#### (Formulario de registro de una red social de un individuo)

</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/redSocial.jpg" />

#### (Vista de una cuenta de red social registrada. Para volver al formulario de registro del individuo, ir "atrás" con el navegador hasta llegar al midmo y actualizar la página)
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/FormularioVehiculo.jpg" />

#### (Formulario de registro de un vehículo de un individuo)
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/vehiculo.JPG" />

#### (Vista de un vehículo registrado. Para volver al formulario de registro del individuo, ir "atrás" con el navegador hasta llegar al midmo y actualizar la página)
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/FormularioEmail.JPG" />

#### (Formulario de registro de un email de un individuo)
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/EjemploEmail.jpg" />

#### (Vista de un email registrado. Para volver al formulario de registro del individuo, ir "atrás" con el navegador hasta llegar al midmo y actualizar la página)
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/FormularioDirección.jpg" />

#### (Formulario de registro de una dirección de un individuo)
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/EjemploDirección.JPG" />

#### (Vista de una dirección registrada. Para volver al formulario de registro del individuo, ir "atrás" con el navegador hasta llegar al midmo y actualizar la página)
</p>

Ahora, para volver al formulario de registro de un individuo con el que empezamos esta sección, de la misma forma que antes, vamos
"atrás" con el anvegador hasta llegar al formulario de registro de un individuo y actualizamos la página para actualizar 
con ella Todos los campos referentes a los registros de los objetos que acabamos de comentar, y veremos como en los campos 
correspondientes aparecen los objetos arriba registrados, como por ejemplo:

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/other_address.jpg" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/social_accounts.jpg" />
</p>

Rellenamos el resto del formulario y el resultado, como ejemplo, es la página de detalle del individuo registrado

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/indivDetail1.JPG" />
</p>

<p align="center">
  <img src="https://github.com/MCYP-UniversidadReyJuanCarlos/20-21_viagdi/blob/main/ImagesTutorial/indivDetail2.jpg" />
</p>

