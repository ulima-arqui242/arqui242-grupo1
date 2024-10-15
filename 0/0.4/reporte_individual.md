# Data Warehouse vs Data Lake vs Data Mesh

## Definiciones

### ¿Que es un Data Warehouse?
Un Data Warehouse (DW) es una almacén de datos estructurados donde generalmente una empresa u organización mantiene una gran cantidad de información. Los datos de un Data Warehouse se almacenan de forma que sea fácil acceder a esta información y son estructurados y procesados previamente para facilitar su uso en análisis de negocios y generación de reportes. Para poder procesar la información previo a su almacenamiento se sigue un proceso ETL (Extract, Transform, Load) optimizandolo asi para consultas. Los DW usualmente tienen un esquema definido.

### ¿Que es un Data Lake?
Un Data Lake (DL) es un repositorio centralizado que almacena datos en su estado original, sean estructurados, semi-estructurados y no estructurados. Los Data Lakes al no necesitar de un esquema predefinido y aceptar cualquier formato de datos evita que sean necesarios los procesos ETL para cargar la información, en su lugar, un proceso llamado ELT (Extract, Load, Transform) se lleva a cabo, esto los hace especialmente útiles para análisis en tiempo real, dashboards, machine learning y big data, ya que permiten la flexibilidad de manipular datos crudos sin necesidad de transformarlos antes del almacenamiento.

### ¿Que es un Data Mesh?
Un Data Mesh (DM) es una arquitectura de datos descentralizada, este enfoque arquitectónico promueve la colaboración ya que a diferencia de los dos almacenes de datos vistos previamente (DW y DL) el Data Mesh divide a la información en múltiples dominios dentro de una organización donde cada dominio es controlado por un equipo independiente. Esta arquitectura mira a los datos como productos, el equipo de cada dominio procesa su información y la vuelve un Data Product (DP) lista para ser compartida con los demas dominios, por ejemplo, un producto de datos (DP) creado por el equipo de inventario puede ser aprovechado por el equipo de marketing u otros dominios dentro de la empresa para diversos fines. Los DM buscan resolver los desafíos de escalabilidad y colaboración que surgen con la centralización de datos, promoviendo la democratización de la información y una gestión más ágil.

## Características y herramientas utilizadas


## Ventajas y desventajas


## Demo
Para realizar una pequeña demostración he utilizado Google Big Query para mostrar como se maneja la información de un Data Warehouse usando un pequeño archivo CSV como ejemplo. Y para mostrar la flexibilidad de un Data Lake he usado Databricks para manejar información almacenada dentro de buckets en Google Cloud, estos buckets te permiten almacenar "objetos" los cuales no estan limitados a un solo tipo de dato.
