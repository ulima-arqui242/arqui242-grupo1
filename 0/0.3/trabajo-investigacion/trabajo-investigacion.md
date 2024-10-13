# Análisis de Código Estático

## Índice

- [Análisis de Código Estático](#análisis-de-código-estático)
  - [Índice](#índice)
  - [Fundamentos del Análisis de Código Estático](#fundamentos-del-análisis-de-código-estático)
    - [¿Qué es el Análisis de Código Estático?](#qué-es-el-análisis-de-código-estático)
    - [Propósito del Análisis Estático](#propósito-del-análisis-estático)
  - [Tipos de Errores y Problemas Detectados](#tipos-de-errores-y-problemas-detectados)
    - [1. Errores de Estilo y Convenciones](#1-errores-de-estilo-y-convenciones)
    - [2. Errores de Seguridad](#2-errores-de-seguridad)
    - [3. Problemas de Complejidad y Mantenimiento](#3-problemas-de-complejidad-y-mantenimiento)
  - [Herramientas de Análisis de Código Estático](#herramientas-de-análisis-de-código-estático)
  - [Métricas de Evaluación en el Análisis de Código Estático](#métricas-de-evaluación-en-el-análisis-de-código-estático)
    - [1. Complejidad Ciclomática](#1-complejidad-ciclomática)
    - [2. Cobertura de Código](#2-cobertura-de-código)
    - [3. Technical Debt (Deuda Técnica)](#3-technical-debt-deuda-técnica)
    - [4. Security Hotspots](#4-security-hotspots)
    - [5. Issues (Problemas)](#5-issues-problemas)
    - [6. Maintainability Rating](#6-maintainability-rating)
    - [7. Reliability Rating](#7-reliability-rating)
    - [8. Duplicated Lines/Duplicated Blocks](#8-duplicated-linesduplicated-blocks)
    - [9. Cyclomatic Complexity per Function](#9-cyclomatic-complexity-per-function)
  - [Integración del Análisis Estático en CI/CD](#integración-del-análisis-estático-en-cicd)
    - [Demo con Sonarqube](#demo-con-sonarqube)
    - [Configuración](#configuración)

## Fundamentos del Análisis de Código Estático

### ¿Qué es el Análisis de Código Estático?

El análisis de código estático se refiere a la evaluación del código fuente sin ejecutarlo. A diferencia del análisis dinámico, que requiere que el programa esté en ejecución, el análisis estático se enfoca en examinar el código fuente directamente, buscando problemas relacionados con la seguridad, la calidad del código, y las mejores prácticas de programación. Este tipo de análisis es especialmente útil en las primeras etapas del desarrollo, ya que ayuda a identificar errores que podrían ser costosos de corregir más adelante.

Según la [Fundación OWASP](https://owasp.org/www-community/controls/Static_Code_Analysis), el análisis de código estático es una herramienta fundamental en el desarrollo seguro de software, ya que permite la identificación temprana de vulnerabilidades antes de que el código sea ejecutado.

### Propósito del Análisis Estático

El propósito principal del análisis estático es detectar problemas en el código que podrían afectar su funcionalidad, seguridad o rendimiento. Estos problemas incluyen errores de lógica, malas prácticas de codificación, vulnerabilidades de seguridad y áreas donde el código puede ser optimizado. Además, ayuda a garantizar que el código siga los estándares de la organización y cumple con las directrices de calidad.

## Tipos de Errores y Problemas Detectados

### 1. Errores de Estilo y Convenciones

El análisis de código estático puede detectar violaciones a las convenciones de codificación, como el uso de nombres inapropiados para las variables, falta de comentarios, o el uso incorrecto de espacios en blanco y sangría. Estas reglas de estilo ayudan a mantener un código más legible y mantenible a largo plazo.

### 2. Errores de Seguridad

El análisis estático es crucial para la detección de vulnerabilidades de seguridad. Según OWASP, las herramientas de análisis estático pueden identificar fallos en la gestión de entradas de usuarios, como inyecciones de SQL, ataques de scripting entre sitios (XSS), y errores en la gestión de autenticación. Estas vulnerabilidades, si no se detectan a tiempo, pueden ser explotadas por atacantes malintencionados para comprometer la seguridad de la aplicación.

### 3. Problemas de Complejidad y Mantenimiento

Un código con alta complejidad ciclomatica tiende a ser difícil de entender, probar y mantener. Las herramientas de análisis estático pueden medir la complejidad del código y sugerir áreas donde se necesita simplificación o refactorización para mejorar la mantenibilidad. La complejidad ciclomatica mide el número de caminos independientes que existen en el código fuente, lo cual indica cuán complejo es el flujo de control.

## Herramientas de Análisis de Código Estático

Existen varias herramientas populares para realizar análisis de código estático. A continuación, se mencionan algunas de las más comunes:

- **PMD**: Analiza código Java y encuentra defectos como variables no utilizadas, construcciones de código complejas y duplicadas.
- **ESLint**: Utilizada principalmente para proyectos en JavaScript, esta herramienta detecta problemas de sintaxis y estilo.
- **FindBugs**: Herramienta para analizar código Java y detectar errores comunes.
- **Sonarqube**: Plataforma de análisis de código estático que proporciona métricas detalladas sobre la calidad del código.

## Métricas de Evaluación en el Análisis de Código Estático

### 1. Complejidad Ciclomática

La complejidad ciclomatica mide la cantidad de caminos lógicos que un programa puede tomar durante su ejecución. Un valor alto de complejidad indica que el código es difícil de entender y propenso a errores, lo que sugiere la necesidad de refactorización. Esta métrica es particularmente útil para identificar funciones o métodos que requieren simplificación.

### 2. Cobertura de Código

La cobertura de código se refiere al porcentaje de código que está cubierto por pruebas automatizadas. Un alto porcentaje de cobertura asegura que el código ha sido bien probado y que es menos probable que contenga errores no detectados.

### 3. Technical Debt (Deuda Técnica)

La deuda técnica se refiere al costo futuro en tiempo y esfuerzo que implica no resolver problemas en el código a medida que se desarrollan. Las herramientas como Sonarqube generan una métrica que estima cuánto tiempo tomaría resolver todos los problemas detectados, ayudando a priorizar mejoras.

### 4. Security Hotspots

Son áreas del código que, aunque no presentan una vulnerabilidad inmediata, podrían convertirse en un riesgo de seguridad dependiendo de cómo se utilicen. Sonarqube marca estos _hotspots_ para que los desarrolladores los revisen manualmente.

### 5. Issues (Problemas)

Los problemas detectados por las herramientas de análisis de código estático se clasifican en diferentes niveles de severidad:

- **Bugs**: Errores que podrían provocar comportamientos incorrectos o fallos en la aplicación.
- **Code Smells**: Patrones que indican un código con mala estructura o diseño, aunque no sean errores inmediatos.
- **Vulnerabilidades**: Problemas de seguridad que pueden comprometer la integridad o seguridad del sistema.

### 6. Maintainability Rating

Es una métrica que evalúa la facilidad con la que se puede mantener el código. Normalmente, se representa con una escala que va de "A" (muy fácil de mantener) a "E" (muy difícil de mantener), y está basada en factores como la deuda técnica y la complejidad del código.

### 7. Reliability Rating

Esta métrica mide la probabilidad de que el código contenga errores que afecten su funcionamiento. Se basa en la cantidad y severidad de los _bugs_ encontrados. Al igual que la mantenibilidad, se mide en una escala de "A" a "E".

### 8. Duplicated Lines/Duplicated Blocks

Mide el porcentaje de líneas o bloques de código que están duplicados. Un alto nivel de duplicación puede ser un indicador de mala calidad del código, ya que el código duplicado es difícil de mantener y puede introducir inconsistencias en las modificaciones.

### 9. Cyclomatic Complexity per Function

Además de medir la complejidad ciclomatica global del proyecto, algunas herramientas permiten ver esta métrica a nivel de función o método. Esto ayuda a identificar específicamente qué funciones necesitan ser refactorizadas.

## Integración del Análisis Estático en CI/CD

El análisis estático de código es una parte fundamental de los procesos modernos de integración continua y entrega continua (CI/CD). Al integrar herramientas como Sonarqube en los pipelines de CI/CD, los equipos de desarrollo pueden recibir retroalimentación inmediata sobre la calidad del código con cada cambio o commit realizado. Esto ayuda a mantener la calidad del código a lo largo del ciclo de vida del proyecto y permite la detección temprana de problemas, reduciendo los costos asociados con la corrección de errores en fases tardías.

### Demo con Sonarqube

[Sonarqube](https://www.sonarqube.org/) es una plataforma de análisis de código estático que permite la evaluación continua de la calidad del código en proyectos de software. Es una herramienta muy utilizada en entornos de desarrollo, ya que proporciona métricas detalladas sobre la seguridad, mantenibilidad y fiabilidad del código. Además, Sonarqube se puede integrar fácilmente en pipelines de integración continua (CI/CD) para automatizar el análisis de código en cada cambio.

### Configuración
