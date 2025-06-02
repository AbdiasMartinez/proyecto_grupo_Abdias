# Proyecto de Análisis de Datos de Publicaciones de Entidades Colombianas

¡Bienvenido a este proyecto! Aquí te explicamos de qué trata.

## ¿De qué se trata este proyecto? 
**Objetivo Principal**<br>
Este proyecto es una aplicación que te ayuda a **entender cuántas veces y qué tipo de datos publican las entidades del gobierno colombiano**. Usamos una fuente de datos oficial de Colombia (una API de datos abiertos).

Nuestro objetivo es:<br>
* **Importar y guardar** esos datos de publicaciones.
* **Contar cuántas veces publica cada entidad** para ver quién es más activa.
* **Encontrar patrones generales** en cómo se publican los datos.

## ¿Cómo está organizado el proyecto? (Arquitectura MVC)

Organizamos el código de una manera que sea clara y fácil de manejar, usando un patrón llamado **MVC (Modelo-Vista-Controlador)**:

* **Modelo (`app/models/datos_model.py`):** Es como la "base de datos inteligente". Aquí guardamos la información de las publicaciones (como la entidad, el tema y la fecha) y sabemos cómo hablar con nuestra base de datos (SQLite).
* **Controlador (`app/controllers/datos_controller.py`):** Es el "cerebro". Aquí está toda la lógica de lo que hace el programa: cómo traer datos de la API, cómo guardarlos, cómo actualizar o borrar, y cómo calcular cuántas publicaciones hay por entidad.
* **Vista (`run.py`):** Es la "pantalla de comandos". Aquí es donde interactúas con el programa. Ves un menú con opciones (listar, agregar, importar, etc.) y le dices al programa qué hacer.

## ¿Qué información trae la API? (Estructura de la API)
Nos conectamos a esta dirección para obtener los datos: `https://www.datos.gov.co/resource/w2ub-ctmm.json`
La información que trae la API sobre cada publicación incluye:
* `responsable`: Quién publica el dato.
* `actividad`: Una descripción de la publicación, a veces con el nombre de la entidad.
* `fecha`: Cuándo se publicó o actualizó el dato.
* También hay otros detalles como el idioma o cómo se guarda el dato.

**Importante:** A veces, el nombre de la entidad no siempre viene de la misma forma en los datos de la API. Nosotros hacemos nuestro mejor esfuerzo para identificar a cada entidad a pesar de esas pequeñas diferencias.

## ¿Qué información guardamos localmente? (Estructura del Dataset Local)
Cuando importamos los datos de la API, los guardamos en una base de datos más simple en tu computador (SQLite). Guardamos esto de cada publicación:
* **ID**: Un número único para cada publicación.
* **Entidad**: El nombre de la entidad que publica el dato (lo que logramos extraer).
* **Tema**: De qué trata el dato publicado.
* **Fecha de Actualización**: La última fecha en que se publicó o modificó.

## Tecnologías Utilizadas
| Herramienta       | Descripción                                                                                   |
| :-----------------|:----------------------------------------------------------------------------------------------|
| Python            | Es el lenguaje principal con el que construimos todo el proyecto.                             |
| Flask             | Una herramienta ligera para hacer que el programa funcione como una aplicación.               |
| Flask-SQLAlchemy  | Nos ayuda a conectar Python con la base de datos (SQLite).                                    |
| Requests          | Nos permite pedir y recibir datos de la API de internet.                                      |
| SQLite            | Es nuestra pequeña base de datos que guarda la información en un archivo local.               |
| Pytest            | Una herramienta para verificar que todo el código funciona correctamente (pruebas unitarias). |

## ¿Cómo arranco el proyecto?
Sigue estos pasos para poner el proyecto a funcionar:

1.  **Abre la carpeta del proyecto** en tu computador.
   
2.  **Asegúrese de tener Python** (versión 3.x) instalado.
   
3.  **Cree un "ambiente virtual"** (como un espacio de trabajo aislado para el proyecto). Esto es bueno para que no haya conflictos con otros proyectos:
    python -m venv .venv
    **Luego, actívelo:**<br>
    **Si está en Windows (CMD):**<br>
    .venv\Scripts\activate.bat<br>
    **Si está en Windows (PowerShell):**<br>
    .venv\Scripts\Activate.ps1<br>
    **Si está en Mac/Linux:**<br>
    source .venv/bin/activate
    
4.  **Instale las herramientas que necesita el proyecto:**<br>
    pip install -r requirements.txt<br>
    *(Asegúrese de que el archivo `requirements.txt` esté en la misma carpeta raíz del proyecto y contenga todas las dependencias necesarias, como Flask, Flask-SQLAlchemy, requests y pytest.)*
    
5.  **Ahora, inicie la aplicación:**<br>
    python run.py<br>
    Se presentará un menú en la terminal para que use el programa.

## Ejemplos de Uso
Una vez que la aplicación esté en funcionamiento (`python run.py`), se presentará el menú principal:
Menú
1. Listar datos locales
2. Agregar entidad
3. Actualizar entidad
4. Eliminar entidad
5. Traer datos desde API
6. Mostrar frecuencia de publicación por entidad
7. Ejecutar Pruebas Unitarias
0. Salir

A continuación, algunos ejemplos de interacción con el sistema:

**Importar datos de la API:**<br>
Para cargar información de las publicaciones desde la API de Datos Abiertos de Colombia, seleccione la opción `5`. La aplicación contactará la API e importará los registros.

**Aquí va tu captura de pantalla de la importación de datos:**<br>
![Image](https://github.com/user-attachments/assets/9b387eb0-1d8d-4275-8c1d-64c6fc18f637)

**Listar todos los datos:**<br>
Para visualizar los registros actualmente guardados en la base de datos local, seleccione la opción `1`.

**Captura de pantalla de la lista de datos:**<br>
![Image](https://github.com/user-attachments/assets/b607c1bb-70da-40dc-b857-fce9c95e292c)

**Agregar un nuevo dato:**<br>
Para añadir manualmente un nuevo registro a la base de datos, seleccione la opción `2`. Se le pedirá que ingrese la entidad, el tema y la fecha de actualización.

**Captura de pantalla de agregar dato:**<br>
![Image](https://github.com/user-attachments/assets/19ae8390-ed36-49a2-ac72-f43498b72050)

**Actualizar un dato existente:**<br>
Si necesita modificar la información de un registro ya existente, seleccione la opción `3`. Deberá proporcionar el ID del dato a actualizar y luego los nuevos valores para la entidad, el tema y la fecha.

**Captura de pantalla de actualizar dato:**<br>
![Image](https://github.com/user-attachments/assets/7cb11922-42b1-44ce-ae71-8f554614be94)

**Eliminar un dato:**<br>
Para remover un registro de la base de datos, seleccione la opción `4`. Se le solicitará el ID del dato que desea eliminar.

**Captura de pantalla de eliminar dato:**<br>
![Image](https://github.com/user-attachments/assets/514fdf78-d197-4770-887f-f2eeb86a1ca2)

**Calcular Frecuencia de Entidades:**<br>
Si desea conocer cuántas publicaciones ha realizado cada entidad, seleccione la opción `6`.

**Captura de pantalla de la frecuencia de entidades:**<br>
![Image](https://github.com/user-attachments/assets/6edc3414-22b6-455f-bca6-02185682e858)

## ¿Cómo sé que todo funciona? (Pruebas Unitarias)
El proyecto incluye "pruebas" para asegurar que las funciones más importantes del código trabajan correctamente. Se pueden ejecutar de dos maneras:

### 1. Ejecución Directa mediante Pytest (Recomendado para desarrollo)
Esta es la forma estándar de ejecutar las pruebas unitarias directamente desde la terminal, ideal para desarrolladores.

**Para ejecutar estas pruebas:**<br>
1.  Es importante que el ambiente virtual esté activo.
2.  Desde la carpeta principal del proyecto, simplemente escriba en la terminal:
    .venv\Scripts\python.exe -m pytest
    El sistema mostrará si las pruebas fueron exitosas o si se encontró algún inconveniente.

**Captura de pantalla de las pruebas unitarias directas:**<br>
![Image](https://github.com/user-attachments/assets/e8449bb4-8f56-455a-90eb-d0a45b3b8a7d)

### 2. Ejecución de Pruebas a través del Menú de la Aplicación
Hemos incluido una opción en el menú principal de la aplicación (`run.py`) para ejecutar las pruebas unitarias. Esto permite una verificación rápida de la funcionalidad sin salir de la interfaz del programa.

**Para ejecutar las pruebas desde el menú:**<br>
1.  Inicie la aplicación ejecutando `python run.py`.
2.  Una vez en el menú principal, seleccione la opción `7`.
    Menú:
    1. Listar datos
    ...
    7. Ejecutar pruebas unitarias
    8. Salir
    Seleccione una opción: 7
    El sistema mostrará la salida de Pytest directamente en la terminal, indicando si las pruebas fueron exitosas o si hubo algún error.

**Captura de pantalla de las pruebas unitarias desde el menú:**<br>
![Image](https://github.com/user-attachments/assets/4d2a3071-9c40-4114-a5c1-a8cf6f0966d6)
