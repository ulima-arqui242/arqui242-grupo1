# Data Warehouse vs Data Lake vs Data Mesh

## Definiciones

### ¿Que es un Data Warehouse?
Un Data Warehouse (DW) es una almacén de datos estructurados donde generalmente una empresa u organización mantiene una gran cantidad de información. Los datos de un Data Warehouse se almacenan de forma que sea fácil acceder a esta información y son estructurados y procesados previamente para facilitar su uso en análisis de negocios y generación de reportes. Para poder procesar la información previo a su almacenamiento se sigue un proceso ETL (Extract, Transform, Load) optimizandolo asi para consultas. Los DW usualmente tienen un esquema definido.

### ¿Que es un Data Lake?
Un Data Lake (DL) es un repositorio centralizado que almacena datos en su estado original, sean estructurados, semi-estructurados y no estructurados. Los Data Lakes al no necesitar de un esquema predefinido y aceptar cualquier formato de datos evita que sean necesarios los procesos ETL para cargar la información, en su lugar, un proceso llamado ELT (Extract, Load, Transform) se lleva a cabo, esto los hace especialmente útiles para análisis en tiempo real, dashboards, machine learning y big data, ya que permiten la flexibilidad de manipular datos crudos sin necesidad de transformarlos antes del almacenamiento.

### ¿Que es un Data Mesh?
Un Data Mesh (DM) es una arquitectura de datos descentralizada, este enfoque arquitectónico promueve la colaboración ya que a diferencia de los dos almacenes de datos vistos previamente (DW y DL) el Data Mesh divide a la información en múltiples dominios dentro de una organización donde cada dominio es controlado por un equipo independiente. Esta arquitectura mira a los datos como productos, el equipo de cada dominio procesa su información y la vuelve un Data Product (DP) lista para ser compartida con los demas dominios, por ejemplo, un producto de datos (DP) creado por el equipo de inventario puede ser aprovechado por el equipo de marketing u otros dominios dentro de la empresa para diversos fines. Los DM buscan resolver los desafíos de escalabilidad y colaboración que surgen con la centralización de datos, promoviendo la democratización de la información y una gestión más ágil.

## Características y herramientas utilizadas


### Herramientas
**Data Warehouse (DW):**
- **BigQuery**: Servicio de Data Warehouse en la nube de Google, diseñado para consultas en grandes volúmenes de datos utilizando SQL.
- **Amazon Redshift**: Ofrecido por AWS, Redshift es un Data Warehouse en la nube que destaca por su capacidad para manejar grandes escalas de datasets, ofreciendo un rendimiento rápido para las consultas.
- **Snowflake**: Plataforma de Data Warehousing basada en la nube que separa el almacenamiento y computo, permitiendo a los usuarios escalar recursos de forma independiente y pagar por lo que usan, facilitando el manejo de datos sin preocuparse por la gestión de infraestructura.

**Data Lake (DL):**
- **Azure Data Lake**: Solución de almacenamiento en la nube de Microsoft diseñada para almacenar grandes volúmenes de datos en su forma original, facilitando el análisis de Big Data.
- **Amazon S3 (Amazon Simple Storage Service)**: Servicio de almacenamiento de objetos de AWS que ofrece escabilidad, seguridad, rendimiento y disponibilidad de datos.
- **Hadoop**: Framework de software que permite el procesamiento distribuido de grandes datos a través de clusters de computadoras, utilizando simple modelado de datos y almacenamiento a gran escala.

**Data Mesh (DM):**
- **Kafka**: Plataforma de streaming de eventos distribuida que permite publicar, suscribir, almacenar y procesar flujos de registros en tiempo real, siendo fundamental para la arquitectura de microservicios y procesamiento de eventos.
- **Confluent**: Plataforma que se construye alrededor de Kafka para mejorar su capacidad, gestionabilidad y seguridad, ofreciendo herramientas para construir y gestionar aplicaciones basadas en flujos de datos en tiempo real.


## Ventajas y desventajas
### DATA WAREHOUSE  
*Ventajas:*
- **Optimización para Consultas:** Los DW están altamente optimizados para realizar consultas complejas, permitiendo análisis avanzados y respuestas rápidas a preguntas de negocio.
- **Consistencia de Datos:** Al almacenar datos que ya han sido procesados y estructurados, garantizan una alta consistencia y calidad de los datos.
- **Facilidad de Uso:** Las herramientas de BI que se conectan a los DW suelen ser fáciles de usar, permitiendo a los usuarios no técnicos generar informes y visualizaciones.
- **Seguridad de Datos:** Ofrecen robustas capacidades de seguridad, lo cual es esencial para cumplir con normativas en varios sectores.
- **Historial de Datos:** Almacenan datos históricos, lo que permite análisis longitudinales y de tendencias.

*Desventajas:*
- **Costo:** La implementación y el mantenimiento pueden ser costosos, requiriendo inversiones significativas en infraestructura y software.
- **Rigidez:** La estructura fija y el esquema predefinido pueden ser limitantes, especialmente cuando se necesita incorporar rápidamente nuevos tipos de datos o cambios en los requisitos.
- **Latencia de Datos:** Los procesos ETL introducen latencias que pueden limitar la capacidad de realizar análisis en tiempo real.
- **Complejidad:** La configuración y mantenimiento de un DW requieren experiencia técnica.
- **Escalabilidad:** Aunque han mejorado con soluciones en la nube, la escalabilidad puede ser un desafío.

### DATA LAKE  
*Ventajas:*
- **Flexibilidad:** Son capaces de almacenar datos no estructurados, semi-estructurados y estructurados, lo que ofrece una gran adaptabilidad.
- **Escalabilidad:** Son altamente escalables, especialmente en entornos de nube, permitiendo almacenar grandes cantidades de datos a bajo costo.
- **Costo-Efectividad:** Generalmente son más económicos que los Data Warehouses para almacenar grandes volúmenes de datos.
- **Innovación en Datos:** Ideal para data science y machine learning, ya que los científicos de datos pueden acceder a datos crudos y experimentar con ellos.
- **Agilidad:** Los usuarios pueden acceder y analizar datos rápidamente sin necesidad de procesos ETL extensivos.

*Desventajas:*
- **Gestión Compleja:** Requiere una gestión cuidadosa para evitar convertirse en un "data swamp" donde los datos son difíciles de encontrar y utilizar.
- **Seguridad y Gobernanza:** La seguridad y la gobernanza de datos son más complejas y pueden ser difíciles de implementar de manera efectiva.
- **Calidad de Datos:** Puede ser complicado garantizar la calidad de los datos, dado que se almacenan en su formato crudo.
- **Herramientas Especializadas:** A menudo se requieren herramientas y habilidades especializadas para procesar y analizar datos almacenados en un Data Lake.
- **Dependencia de Expertos:** Depende en gran medida de especialistas en datos para extraer valor.

### DATA MESH  
*Ventajas:*
- **Descentralización:** Facilita la descentralización de la gestión de datos, permitiendo que los equipos de cada dominio gestionen sus propios datos.
- **Agilidad:** Mejora la agilidad al reducir las dependencias centralizadas.
- **Escalabilidad:** Permite una escalabilidad efectiva distribuyendo la carga y el procesamiento de datos a través de múltiples dominios.
- **Calidad de Datos Mejorada:** Cada dominio es responsable de la calidad de sus datos, lo que puede mejorar la precisión y la utilidad general de los datos.
- **Colaboración:** Promueve una mayor colaboración entre equipos, ya que facilita compartir y acceder a datos entre dominios.

*Desventajas:*
- **Complejidad Organizativa:** Requiere cambios organizativos significativos y una redefinición de los procesos y responsabilidades.
- **Inversión en Tecnología:** Puede requerir una inversión inicial significativa en tecnología y formación para una implementación efectiva.
- **Gobernanza Desafiante:** La gobernanza puede ser más complicada debido a la naturaleza distribuida de los datos.
- **Riesgos de Seguridad:** La distribución de datos aumenta los riesgos de seguridad.
- **Dependencia de la Cultura de Datos:** Requiere una fuerte cultura de gestión y colaboración de datos para ser efectiva.


## Demo
Para realizar una pequeña demostración he utilizado Google Big Query para mostrar como se maneja la información de un Data Warehouse usando un pequeño archivo CSV como ejemplo. Y para mostrar la flexibilidad de un Data Lake he usado Databricks para manejar información almacenada dentro de buckets en Google Cloud, estos buckets te permiten almacenar "objetos" los cuales no estan limitados a un solo tipo de dato.
