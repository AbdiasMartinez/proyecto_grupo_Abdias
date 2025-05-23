## OBJETIVO DEL PROYECTO

Desarrollar una aplicación que importe, almacene y realice un análisis exploratorio de los datos de publicación de entidades colombianas disponibles a través de la API de datos abiertos de Colombia (`https://www.datos.gov.co/resource/w2ub-ctmm.json`). El proyecto se enfoca en identificar patrones generales de actividad de publicación y cuantificar la frecuencia de las mismas por entidad.


## ESTRUCTURA DE DATASET 
El dataset contiene información sobre los conjuntos de datos que las entidades públicas de Colombia deben publicar en sus sitios web oficiales. Las columnas clave del archivo son:

- ENTIDAD: Nombre de la entidad del gobierno responsable del conjunto de datos.
- NOMBRE DEL CONJUNTO DE DATOS: Título del dataset publicado.
- DESCRIPCION DEL CONJUNTOS DE DATOS: Breve explicación sobre el contenido del dataset.
- FRECUENCIA DE ACTUALIZACION: Periodicidad comprometida por la entidad (Mensual, Trimestral, Anual, etc.).
- FECHA DE ULTIMA DE ACTUALIZACION: Fecha en que se publicó o actualizó por última vez.
- RESPONSABLE DE PUBLICACION: Persona o área encargada dentro de la entidad.
- URL DE ACCESO: Enlace directo al dataset publicado.

## PRUEBAS UNITARIAS

El proyecto incluye "pruebas" para asegurar que las funciones más importantes del código trabajan correctamente.

## PARA EJECUTAR LAS PRUEBAS

- Es importante que el ambiente virtual esté activo.
- Desde la carpeta principal del proyecto, simplemente escriba en la terminal **pytest**. O a través del programa con la opción 7 del menú.
- El sistema mostrará si las pruebas fueron exitosas o si se encontró algún inconveniente.

## TECNOLOGIAS UTILIZADAS

| Herramienta      | Descripción                                                                         |
|------------------|-------------------------------------------------------------------------------------|
| Python           | Es el lenguaje principal con el que construimos todo el proyecto.                   |
| Flask            | Una herramienta ligera para hacer que el programa funcione como una aplicación.     |
| Flask-SQLAlchemy | Nos ayuda a conectar Python con la base de datos (SQLite).                          |
| Requests         | Nos permite pedir y recibir datos de la API de internet.                            |
| SQLite           | Es nuestra pequeña base de datos que guarda la información en un archivo local.     |
| Pytest           | Una herramienta para verificar que todo el código funciona correctamente (pruebas). |