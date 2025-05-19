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

## TECNOLOGIAS UTILIZADAS

| Herramienta      | Descripción                                                                                |
|------------------|--------------------------------------------------------------------------------------------|
| Python           | Lenguaje de programación principal.                                                        |
| Flask            | Framework web ligero para construir la aplicación.                                         |
| Flask-SQLAlchemy | Extensión de Flask para interactuar con bases de datos relacionales (SQLite en este caso). |
| Requests         | Librería de Python para realizar solicitudes HTTP a la API.                                |
| SQLite           | Base de datos local para almacenar los datos importados.                                   |