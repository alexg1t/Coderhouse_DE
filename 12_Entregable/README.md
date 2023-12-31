# Proyecto de Ingeniería de Datos - CoderHouse

## Descripción
Este proyecto de ingeniería de datos ha sido desarrollado como parte del curso de CoderHouse. Proporciona una solución para extraer,transformar y cargar datos hacia un warehouse.

## Características Principales
- Procesamiento de datos en batch.
- Integración con una API de cryptomonedas.
- Almacenamiento en un warehouse de Amazon Redshift.
- Envío de correos que detallen alarmas sobre aumento predeterminado de alguna cryptomoneda.

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto en tu entorno local, tienes que tener OBLIGATORIAMENTE Docker Desktop:

1. Clona el repositorio o forkealo:


2. Navega al directorio del proyecto:

    ```bash
    cd nombre-del-repo
    ```

3. Construye la imagen de Docker el nombre de la imagen "de-ch" es necesario en el docker-compose.yaml:

    ```bash
    docker build . -t de-ch
    ```

4. Levanta los contenedores con Docker Compose:

    ```bash
    docker-compose up
    ```
5. Para observar el DAG en airlow tiene que ingresar mediante un explorador web a http://localhost:8080 :

Con estos pasos, el proyecto debería estar en funcionamiento en tu entorno local. Asegúrate de tener Docker y Docker Compose instalados antes de ejecutar estos comandos.

## Uso
Es NECESARIO detallar algunas credenciales propias y/o claves de aplicación de mensajería de GMAIL. Todas pueden ser detalladas en /dags/etlpy/cryptoetl.py y son variables que
tienen como valor '**********'.

## Contribución
Si deseas contribuir al proyecto, ¡te animamos a que lo hagas! Abre problemas, envía solicitudes de extracción y ayuda a mejorar este proyecto.


## Contacto
Si tienes preguntas o comentarios, no dudes en ponerte en contacto conmig

## Agradecimientos
Queremos expresar nuestro agradecimiento a CoderHouse por proporcionar la plataforma y los recursos necesarios para llevar a cabo este proyecto.

¡Gracias por tu interés en nuestro proyecto de ingeniería de datos!

