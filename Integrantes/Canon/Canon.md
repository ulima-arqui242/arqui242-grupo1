
# Anthony Canon

## Nombre y carrera
#### Anthony Canon, ingeniería en sistemas

## Experiencia en desarrollo de software
#### 5 meses como practicante de desarrollo web

## Tecnologias que conozco
#### JS, C#, java, gitlab, angular

## Cual es mi expectativa del curso
#### Aprender como construir una arquitectura de software de manera optima, asi como aumentar mi conocimiento en tecnologias

## Como me veo en 10 años
#### Trabajando como ing de software o similar


# Tema individual: LLMs (Modelos de lenguaje a gran escala)

# Marco Teorico
### Modelos a gran escala
Los modelos de lenguaje a gran escala estan basados en la arquitectura de Transformers, estan 
entrenados con una gran cantidad de datos para procesar y generar texto natural. Estos modelos están diseñados para entender,
producir y modificar lenguaje humano de manera coherente, permitiendo realizar tareas  complejas
como la traducción, el análisis de texto, la generación de preguntas y respuestas, ec.

### Incrustaciones (Vectores de alto contexto)
En el tema de Procesamiento de lenguaje natural (NLP en ingles) son extremadamente importantes, ya que transforman datos de entrada (como texto o imágenes) en un formato numérico que el modelo puede procesar. En el contexto de IA generativa, las incrustaciones son representaciones densas y de baja dimensionalidad de los datos que capturan su significado semántico y estructura.
Ejemplo de secuencia de incrustaciones que representa una oración:

### Refinamiento
Se refiere al proceso de mejorar el rendimiento del modelo usando datos especificos, después de su entrenamiento inicial que usualmente es realizado con un gran cuerpo de datos generales de internet. Este proceso puede implicar ajustes en el modelo, en los datos de entrenamiento o en los hiperparámetros, con el objetivo de optimizar la capacidad del modelo para generalizar bien sobre datos no vistos anteriomente y reducir errores. El refinamiento es una etapa crítica para obtener un modelo que realiza la tarea de manera optima y hace predicciones robustas.
Ejemplo de opciones que  se pueden ajustar para tener mejor modelo:
```
# Hiperparametros
learning_rate = 0.001
batch_size = 32
epochs = 50
momentum = 0.9
dropout_rate = 0.5
```

### Entradas/Salidas
Los inputs/outputs pueden variar según el tipo de tarea que el modelo esté realizando. Los modelos están diseñados para crear contenido nuevo en base de los datos de entrada que reciben, por lo tanto un modelo que  recibe datos de baja calidad, pocos datos o inexactos, tendra como consecuencia un modelo que no cumple con las expectativas.
![Alt text](grabage.png)

A continuación se describen las entradas y salidas más comunes en modelos generativos, especialmente aquellos que se utilizan para la generación de texto, como GPT.

# herramientas utilizadas

## Requerimientos

### Pip
```
pip install streamlit
pip install python-dotenv
pip install google-generativeai
```

## Modelos
- GPT (Generative Pretrained Transformer)
- Gemini
- BERT
### Proceso de refinamiento
1. Generar un dataset que ya esta limpiado y contiene información relevante para lograr refinar el modelo 
2. Para la creación de chatbots podemos seleccionar modelos generativos como GPT o Gemini, modelos como BERT y XLNET son comunmente usados en tareas de clasificación y regresión.
3. 

## Dataset

# Demo

