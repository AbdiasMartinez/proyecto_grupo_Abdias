Proyecto: Análisis de Publicación de Datos Abiertos en Colombia

Este proyecto tiene como objetivo analizar los conjuntos de datos abiertos publicados por entidades públicas en Colombia. A partir de la información proporcionada por la API oficial de datos abiertos, se determina el cumplimiento en la publicación de información por parte de cada entidad, según su frecuencia de actualización, sector y última fecha de actualización.

OBJETIVO
Este proyecto tiene como finalidad analizar y clasificar los conjuntos de datos abiertos publicados por entidades públicas en Colombia, evaluando su cumplimiento con las obligaciones de transparencia y acceso a la información establecidas en la Ley 1712 de 2014 (Ley de Transparencia y del Derecho de Acceso a la Información Pública Nacional) y la Resolución 1519 de 2020 del MinTIC. Se busca identificar las entidades que no cumplen con la publicación oportuna de datos, determinar las consecuencias de dicho incumplimiento y establecer las frecuencias de actualización requeridas para cada tipo de entidad.

SANCIONES POR INCUMPLIMIENTO
Las entidades públicas que no cumplan con las obligaciones de publicación y actualización de datos abiertos pueden enfrentar las siguientes sanciones, según la Ley 1480 de 2011 (Estatuto del Consumidor) y otras normativas relacionadas:

- MULTAS ECONOMICAS: Hasta 2.000 salarios mínimos mensuales legales vigentes (SMMLV), dependiendo de la gravedad de la infracción. 
- CIERRE TEMPORAL O DEFINITIVO DEL ESTABLECIMIENTO: En casos de infracciones graves o reiteradas. 
- PROHIBICIÓN DE PRODUCIR O DISTRIBUIR CIERTOS PRODUCTOS O SERVICIOS: Cuando se afecta la salud o seguridad de los consumidores. 
- MULTAS SUCESIVAS: Hasta 1.000 SMMLV por inobservancia de órdenes o instrucciones emitidas por las autoridades competentes. 
Estas sanciones son impuestas por la Superintendencia de Industria y Comercio (SIC) o las alcaldías municipales, según corresponda.

Frecuencias de Actualización de Datos
La Resolución 1519 de 2020 del MinTIC establece las frecuencias mínimas de actualización de los conjuntos de datos abiertos, las cuales varían según la naturaleza de la información:

- Datos de alta demanda o impacto: Actualización mensual.
- Datos de uso medio: Actualización trimestral.
- Datos de baja demanda: Actualización semestral o anual.

Además, la Hoja de Ruta Nacional de Datos Abiertos Estratégicos prioriza ciertos conjuntos de datos críticos para su disponibilidad y actualización, alineándose con los compromisos del Plan de Acción de Gobierno Abierto.


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
SQLAlchemy      ORM para manejar bases de datos con Python.
SQLite          Base de datos liviana, integrada en un archivo.