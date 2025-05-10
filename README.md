OBJETIVO DEL PROYECTO
Este proyecto tiene como finalidad analizar y clasificar los conjuntos de datos abiertos publicados por entidades públicas en Colombia, con base en el esquema oficial de publicación. El análisis se centrará en categorizar los datasets por temática (como salud, educación, transporte, tecnología, entre otros), identificar su frecuencia de actualización, y evaluar el cumplimiento de las fechas prometidas de publicación. A través de este estudio se busca diagnosticar el estado actual de la apertura de datos en distintos sectores del Estado colombiano, detectar oportunidades de mejora en cuanto a transparencia digital, y contribuir con recomendaciones para fortalecer el acceso a la información pública.


ESTRUCTURA DE DATASET
El dataset contiene información sobre los conjuntos de datos que las entidades públicas de Colombia deben publicar en sus sitios web oficiales. Las columnas clave del archivo son:

- ENTIDAD: Nombre de la entidad del gobierno responsable del conjunto de datos.
- NOMBRE DEL CONJUNTO DE DATOS: Título del dataset publicado.
- DESCRIPCION DEL CONJUNTOS DE DATOS: Breve explicación sobre el contenido del dataset.
- FRECUENCIA DE ACTUALIZACION: Periodicidad comprometida por la entidad (Mensual, Trimestral, Anual, etc.).
- FECHA DE ULTIMA DE ACTUALIZACION: Fecha en que se publicó o actualizó por última vez.
- RESPONSABLE DE PUBLICACION: Persona o área encargada dentro de la entidad.
- URL DE ACCESO: Enlace directo al dataset publicado.

TECNOLOGIAS UTILIZADAS
Herramienta	    Descripción
Python 3.12	    Lenguaje principal del proyecto.
requests	    Librería para realizar solicitudes HTTP y consumir la API de Datos Abiertos.