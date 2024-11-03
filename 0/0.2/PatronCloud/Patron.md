
# Patron: Queue-Based Load Leveling

## Problema
Cuando los usuarios envían un gran número de solicitudes simultáneas, los componentes pueden verse abrumados,
resultando en tiempos de respuesta lentos o incluso fallos en el sistema. El punto es 
tener un sistema robusto que sea capaz de manejar gran volumen de solicitudes y evite caerse o experimentar
reduccion en el rendimiento en la experiencia del usuario, sobretodo 
cuando se maximiza la capacidad que tiene el sistema de procesar solicitudes.
## Solución
El patrón utiliza una cola de mensajes como intermediario para manejar solicitudes. Esto quiere decir que en lugar de enviar todas las solicitudes directamente al servicio que tiene que procesarlas, lo cual podría sobrecargarlo en momentos de alta demanda, las solicitudes se guardan en una lista de espera o cola. Posteriomente el servicio las va tomando y procesando a su propio ritmo de acuerdo con su capacidad para atender solicitudes en ese momento. Se icluyen los siguientes beneficios como parte de la implementación del patron:
- Se evita que los servicios de procesamiento se vean saturados en picos de demanda, sino que las solicitudes no se pierden y se procesan de forma organizada, sin importar cuántas lleguen a la vez.
- Se mejora la robustez del sistema, permitiendo que los consumidores retomen el procesamiento cuando estén listos, sin perder solicitudes.
- Si en algún instante el servicio se detiene o falla, las solicitudes quedan en la cola y pueden ser atendidas tan pronto como el sistema vuelva a disponibilidad completa.

## Casos de uso
El patron Queue-Based Load Leveling se puede usar como ejemplo para optimizar las operaciones de las siguientes empresas:

- Sistemas de mensajería y notificaciones: Las redes sociales ofrecen servicios de mensajería, como estas que envían alertas a usuarios sobre mensajes o notificaciones, este patrón ayudaria a que el sistema sea escalable y confiable. En lugar de enviar todos los mensajes a la vez y arriesgarse a saturar el servicio de envío, cada notificación se coloca en una cola y se va enviando de forma ordenada y escalonada. Esto es ideal para empresas cuya plataforma que está en pleno crecimiento.

- E-commerce: EN el caso de plataformas de comercio durante eventos de alta demanda como el black friday o cyber monday, es común que haya una gran numero de transacciones y solicitudes de compra paralelamente. Con este patrón cada pedido se coloca en una cola, permitiendo que el sistema gestione cada solicitud sin llegar a la sobrecarga. Así los clientes pueden completar sus compras sin experimentar lentitud o fallas y las transacciones se procesan de manera confiable para la empresa y usuario.
- Bancos y servicios financieros: Los sistemas bancarios que procesan transacciones, como pagos o transacciones de diferente tipo o cantidad , pueden recibir muchas solicitudes simultáneas todos los dias 24/7. Este patrón asegura que todas las transacciones se guarden en una cola y se procesen en el orden que llegaron, mantiene el sistema estable y evita que colapse. Así los usuarios pueden realizar sus transacciones sin errores o demoras, sabiendo que la disponibilidad de este tipo de sistema es critico para millones de personas.

## Pruebas

### Herramientas
- Locust
- redis
- flask
- prometheus
