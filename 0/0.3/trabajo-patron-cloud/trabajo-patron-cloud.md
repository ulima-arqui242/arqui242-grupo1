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
