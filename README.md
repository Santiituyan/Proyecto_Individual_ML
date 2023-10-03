# Proyecto_Individual_ML
![store_home_share](https://github.com/Santiituyan/Proyecto_Individual_ML/assets/115497418/ec69f3fd-76fa-4017-82e8-5115fc35383d)


Link de la rama donde estan los archivos de todo el proceso totalmente crudos, junto al EDA y el ETL [aquí](https://github.com/Santiituyan/Proyecto_Individual_ML/tree/raw)

# Proyecto Individual - Recomendación de videojuegos

_Este repositorio forma parte de la evaluación de habilidades del bootcamp de Data Science y su propósito principal es la aplicación práctica de los conocimientos y competencias adquiridos a lo largo del programa. En este proyecto, nos enfocaremos en actividades relacionadas con el análisis de datos, la ingeniería de datos y la construcción de modelos de aprendizaje automático._

## Estructura del Repositorio

-   **.gitignore**: En este archivo, se establecen las directrices para que Git ignore ciertos archivos y directorios en el repositorio.

-   **ETL**: Dentro de este archivo, se lleva a cabo el proceso de extracción, transformación y carga de datos, incluyendo algunas transformaciones específicas.

-   **Nlp.ipynb**: Archivo Python que implementa análisis de sentimientos utilizando NLTK.

-   **Funciones**: Archivo Jupyter Notebook que muestra las funciones del proyecto.

-   **EDA.ipynb**: Archivo Jupyter Notebook con análisis exploratorio de datos.

-   **Ml.ipynb**: En este archivo Jupyter Notebook, encontrarás el proceso de creación y evaluación de el modelo de aprendizaje automático.

-   **Archivos csv**: Datasets donde esta la informacion importantede las funciones/Endpoints.

-   **Main.py**: Archivo principal para iniciar la API.

-   **Requirements.txt**: Archivo que especifica las dependencias y librerías.

## Etapas


El proyecto se estructura en las siguientes etapas:

1. **Extracción de Datos**: En esta fase, se llevaron a cabo procesos exhaustivos para limpiar y transformar los datos que se obtuvieron de las bases de datos disponibles.

2. **Análisis de Sentimientos**: Utilizando un archivo que contiene los títulos y etiquetas de los videojuegos, se realizó un análisis de sentimientos para evaluar la polaridad de las opiniones asociadas a ellos.

3. **Funciones de Consulta**: Se desarrollaron diversas funciones que permiten realizar consultas específicas sobre la información contenida en los datos, facilitando así la obtención de datos concretos de interés.
-   _PlayTimeGenre(genero: str)_: En esta funcion se recibe el genero que se desea consultar para mostrar el anio donde se tuvo mayor playtime
-   _UserForGenre(genero: str)_: En esta se recibe el genero en formato string para mostrar al usuario con el mayor playtime del genero y su cantidad de playtime a lo largo de los   anios
-   _game_recommendations( game_id : int )_: Se recibe el id de algun juego en especifico para mostrar 5 de las recomendaciones

4. **API**: Implementamos una API utilizando FastAPI para exponer las funciones de consulta como endpoints. Además, se utilizó Render para facilitar la generación de respuestas. Puedes encontrar la documentación completa de la API en el siguiente [enlace](https://proyecto-individual-01-oirf.onrender.com/docs).

5. **EDA** (Análisis Exploratorio de Datos): Se llevó a cabo un exhaustivo Análisis Exploratorio de Datos para obtener información adicional y reveladora sobre los datos relacionados con los videojuegos.

6. **Modelo de Aprendizaje Automático**: Desarrollamos un modelo de k-vecinos para recomendar 5 juegos con base en un ID de juego específico, ofreciendo así una funcionalidad adicional y útil para los usuarios.

## Explicacion del deploy

[Video](https://youtu.be/yqPhGD6VH14)


## Instrucciones
Para comenzar a utilizar este proyecto, sigue estos pasos:

Clonar el repositorio en tu máquina local:
_git clone https://github.com/Santiituyan/Proyecto_Individual_ML_

Instalar las dependencias necesarias ejecutando el siguiente comando:
_pip install -r requirements.txt_

Luego, sigue las instrucciones detalladas en cada uno de los archivos Jupyter Notebook incluidos en el proyecto para ejecutar y explorar las diferentes etapas y funcionalidades del mismo. ¡Disfruta del proyecto!

## Autor

**Santiago Ituyan Figueroa** - [Santiituyan](https://github.com/Santiituyan)
