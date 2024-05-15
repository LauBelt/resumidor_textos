# Resumidor de Texto

Esta es una aplicación web que permite resumir texto en los idiomas español e inglés utilizando la API de OpenAI. La aplicación está construida con Flask y utiliza un modelo de lenguaje de OpenAI para generar los resúmenes.

## Características

- Resumir texto en español.
- Resumir texto en inglés.
- Interfaz de usuario sencilla y amigable.

## Requisitos

- Python
- Una clave de API de OpenAI

## Instalación

1. Clona el repositorio:
2. Crea un entorno virtual y actívalo: python -m venv venv - 
3. Activacion entorno virtual en Windows usa `venv\Scripts\activate`
4. pip install -r requirements.txt
5. En el archivo .env añade tu clave de API de OpenAI API_KEY=tu-clave-api-de-openai

## Ejecución

1. Asegúrate de que el entorno virtual esté activado.
2. Ejecuta la aplicación: `python app.py`
3. Abre tu navegador y ve a http://127.0.0.1:5000.

## Uso

1. Ingresa el texto que deseas resumir.
2. Selecciona el idioma del resumen.
3. Haz clic en "Resumir" para ver el resultado.
