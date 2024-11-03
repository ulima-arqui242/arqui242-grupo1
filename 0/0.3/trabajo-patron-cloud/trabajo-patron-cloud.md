# Patrón Cloud: Compensating Transaction

## Introducción

En esta investigación se abordará el patrón de diseño **Compensating Transaction**, uno de los patrones propuestos por Microsoft para arquitecturas de software en la nube. En un mundo donde los sistemas distribuidos son cada vez más frecuentes, garantizar la consistencia de las transacciones entre múltiples servicios es un desafío clave. A través del uso de este patrón, se busca manejar los errores de forma controlada, mediante la ejecución de operaciones compensatorias que reviertan los efectos de las transacciones fallidas. Este patrón es de gran relevancia cuando no es posible utilizar transacciones distribuidas tradicionales, como en los casos donde los servicios no pueden participar en una transacción ACID.

El objetivo de este trabajo es describir en detalle el funcionamiento del patrón, explicar su contexto de uso y presentar una implementación práctica utilizando tecnologías modernas como **NestJS**, **Prisma** y **NATS** en una arquitectura basada en microservicios.

## ¿Qué es el Patrón Compensating Transaction?

El patrón **Compensating Transaction** es una técnica utilizada en sistemas distribuidos para revertir los efectos de operaciones fallidas. En un entorno tradicional, las transacciones siguen el principio ACID (Atomicidad, Consistencia, Aislamiento y Durabilidad), lo que garantiza que todas las operaciones dentro de una transacción se completen con éxito o, en caso contrario, ninguna lo haga. Sin embargo, cuando trabajamos en sistemas distribuidos, donde varios servicios interactúan entre sí, la implementación de transacciones ACID no siempre es posible o eficiente.

El patrón **Compensating Transaction** consiste en definir una operación de compensación para cada operación en el sistema. Si una parte de la transacción falla, las operaciones que ya se completaron con éxito pueden ser revertidas mediante estas transacciones compensatorias, lo que garantiza que el sistema vuelva a un estado consistente.

Este patrón es útil en los siguientes escenarios:

- Las transacciones abarcan múltiples sistemas o servicios distribuidos.
- Los recursos distribuidos no soportan transacciones ACID de manera nativa.
- Se necesita revertir operaciones sin afectar otras transacciones exitosas.

Un ejemplo común del uso de este patrón es un sistema de reservas de viajes, donde un usuario reserva un vuelo, hotel y coche en diferentes servicios. Si uno de estos servicios falla, como el de reserva del coche, las reservas del vuelo y el hotel deben ser revertidas para evitar inconsistencias en el sistema.

## Contexto de Uso

El patrón **Compensating Transaction** es especialmente útil en arquitecturas de microservicios, donde múltiples servicios autónomos necesitan colaborar para realizar una operación que abarca diferentes bases de datos o sistemas externos. A continuación, se describen algunos contextos en los que este patrón es recomendable:

1. **Sistemas distribuidos**: En arquitecturas de microservicios o sistemas distribuidos, los servicios interactúan de manera independiente y no todos soportan transacciones distribuidas. Este patrón asegura que las operaciones realizadas en diferentes servicios puedan ser revertidas en caso de fallos.

2. **Sistemas con consistencia eventual**: En aplicaciones que priorizan la disponibilidad y escalan horizontalmente, como en aplicaciones en la nube, puede que no se requiera consistencia inmediata. En este escenario, la compensación es una manera de asegurar que el sistema finalmente llegará a un estado consistente, aunque con cierta latencia.

3. **Operaciones que no se pueden deshacer de manera tradicional**: En ciertos sistemas, las operaciones, como el procesamiento de pagos o reservas, no pueden ser revertidas fácilmente, por lo que es necesario realizar pasos compensatorios. El patrón asegura que estas operaciones sean deshechas de manera controlada.

4. **Idempotencia**: Las operaciones que participan en una transacción distribuida deben ser idempotentes, es decir, que puedan ser ejecutadas múltiples veces sin causar efectos secundarios no deseados. Esto asegura que las operaciones de compensación o los reintentos no introduzcan inconsistencias adicionales en el sistema.

## Posible Aplicación del Patrón Compensating Transaction en MedSysPro

En **MedSysPro**, el patrón **Compensating Transaction** puede jugar un papel clave en la gestión de la consistencia de datos entre varios módulos interdependientes, como el módulo de gestión de citas, historial médico, teleconsulta y recetas. Dado que la plataforma maneja operaciones distribuidas, como el agendamiento de citas, la actualización de diagnósticos y la emisión de recetas, es crucial garantizar que cualquier fallo en uno de los microservicios pueda ser compensado, restaurando el estado del sistema sin afectar la experiencia del usuario.

### Escenario de Uso: Proceso de Cita, Diagnóstico y Emisión de Recetas

Un escenario donde el patrón **Compensating Transaction** sería útil en **MedSysPro** involucra el flujo de trabajo completo de una consulta médica, que incluye la gestión de citas, diagnóstico, actualización del historial médico y emisión de recetas. Este flujo de trabajo podría involucrar los siguientes módulos:

1. **Servicio de Gestión de Citas**: El paciente agenda una cita con un médico, el cual se registra en el sistema.
2. **Servicio de Historial Médico**: Durante la cita, el médico consulta y actualiza el historial médico del paciente.
3. **Servicio de Chatbot de Diagnóstico**: El chatbot sugiere diagnósticos y tratamientos basados en los síntomas ingresados por el médico.
4. **Servicio de Gestión de Recetas**: Después de la consulta, el médico genera una receta para el paciente.
5. **Servicio de Resultados**: Los resultados de análisis o estudios de laboratorio son añadidos al historial del paciente.

#### Posible Problema

Si un paciente agenda una cita y el proceso continúa normalmente, pero el **Servicio de Gestión de Recetas** falla al emitir una receta, esto dejaría el flujo en un estado inconsistente: el historial médico ya ha sido actualizado, pero el paciente no ha recibido la receta correspondiente. En este caso, el sistema necesita deshacer parte del proceso o proporcionar un mecanismo que compense este fallo.

#### Aplicación del Patrón

Para mitigar este tipo de problemas, el patrón **Compensating Transaction** permitiría definir operaciones de reversión para cada uno de los servicios en caso de fallo. Por ejemplo:

- **Transacción Principal**: El paciente agenda una cita, asiste a la consulta, el historial médico se actualiza, y se emite una receta.
- **Operación Compensatoria**: Si la receta no puede generarse correctamente, el sistema podría revertir la actualización del historial médico, dejando una notificación al médico para revisar el caso o reintentar la emisión de la receta. Alternativamente, se podría permitir que el paciente reprograme la cita para corregir el problema.

### Detalle del Flujo de Compensación

1. **Agendamiento de Citas**: El paciente agenda una cita, lo que bloquea el horario en la agenda del médico.

   - **Compensación**: Si el servicio de citas falla o se detecta un problema en el flujo, la operación compensatoria sería liberar el horario del médico y notificar al paciente.

2. **Actualización del Historial Médico**: El médico actualiza el historial médico del paciente con los detalles de la consulta.

   - **Compensación**: Si la emisión de recetas falla, la operación compensatoria sería revertir la actualización del historial médico para evitar inconsistencias en los datos clínicos.

3. **Chatbot de Diagnóstico y Sugerencia de Tratamientos**: El chatbot proporciona sugerencias de diagnóstico y tratamiento basadas en los datos del paciente.

   - **Compensación**: Si falla el proceso de generación de recetas, el sistema podría deshacer las sugerencias generadas por el chatbot o marcarlas como incompletas hasta que se pueda resolver el problema.

4. **Gestión de Recetas**: El médico emite una receta para el paciente al finalizar la consulta.
   - **Compensación**: Si la receta no puede ser emitida correctamente, el sistema puede deshacer la receta generada o notificar al médico para que reemita manualmente la receta en otro momento.

### Ejemplo en el Módulo de Gestión de Citas

- **Transacción Principal**: El paciente programa una cita, asiste a la consulta, y el historial médico es actualizado con los resultados.
- **Operación Compensatoria**: Si el médico no puede finalizar la emisión de recetas por un fallo en el sistema, el historial médico se marca como pendiente de revisión y el paciente recibe una notificación para realizar una nueva consulta o reintentar la generación de la receta.

### Ventajas del Patrón en MedSysPro

- **Consistencia de Datos**: Al aplicar operaciones compensatorias, los datos críticos del paciente, como su historial médico y recetas, se mantienen consistentes, evitando que se queden en estados intermedios.
- **Mejora en la experiencia del usuario**: En caso de fallos, el sistema garantiza que se puedan revertir los procesos sin afectar la experiencia del paciente o del médico, asegurando que la atención médica no se vea comprometida.
- **Manejo de Fallos Complejo**: Este patrón permite a **MedSysPro** manejar fallos en procesos críticos (como la emisión de recetas o la actualización de historiales médicos) de forma robusta, recuperándose de errores sin introducir inconsistencias en el sistema.

## Implementación Teórica del Patrón

Implementar el patrón **Compensating Transaction** implica realizar varias etapas clave:

1. **Dividir la operación en pasos**: El primer paso es identificar las diferentes operaciones que conforman una transacción distribuida. Cada operación debe ser claramente delimitada, y debe ser posible revertirla de manera individual.

2. **Definir operaciones compensatorias**: Para cada operación, se debe definir una transacción compensatoria que sea capaz de revertir los efectos si algo falla en el proceso. Por ejemplo, si un servicio de reserva realiza una operación que bloquea un asiento en un avión, la operación compensatoria debe liberar dicho asiento en caso de un fallo en otra parte del proceso.

3. **Orquestación de las transacciones**: Un servicio, denominado **orquestador**, es el encargado de coordinar las operaciones de la transacción distribuida. Este orquestador invoca cada operación secuencialmente y, en caso de que una falle, comienza a invocar las transacciones compensatorias en orden inverso.

4. **Gestión de fallos y reintentos**: El patrón requiere una lógica robusta para manejar los fallos. Los servicios que implementan operaciones compensatorias deben ser capaces de manejar reintentos y recuperarse de fallos intermitentes, lo que implica garantizar que estas operaciones sean idempotentes.

### Ejemplo Práctico

Consideremos un sistema de e-commerce donde un cliente puede realizar un pedido, procesar el pago y ajustar el inventario. Cada una de estas operaciones ocurre en un microservicio independiente:

- **Servicio de pedidos**: Crea el pedido en la base de datos.
- **Servicio de inventario**: Reduce el inventario del producto en cuestión.
- **Servicio de pago**: Procesa el pago del cliente.

Si el pago falla, el sistema debe revertir tanto el ajuste de inventario como la creación del pedido. Aquí es donde entran en juego las transacciones compensatorias: la operación de "cancelar pedido" y "restaurar inventario" serían las operaciones compensatorias a realizar.

## Conclusión

El patrón **Compensating Transaction** es una solución eficaz en escenarios donde las transacciones distribuidas ACID no son posibles. A través de la definición de operaciones compensatorias, se asegura que el sistema pueda manejar errores y mantener la consistencia en un entorno distribuido. Este patrón se usa ampliamente en arquitecturas de microservicios y sistemas distribuidos, donde las fallas en los servicios pueden afectar transacciones críticas. En la sección siguiente, se mostrará una implementación práctica del patrón utilizando **NestJS**, **Prisma** y **NATS**, demostrando cómo se orquesta la lógica de compensación en un sistema distribuido real.

## Referencias

- Microsoft Azure Patterns: <https://learn.microsoft.com/en-us/azure/architecture/patterns/>
