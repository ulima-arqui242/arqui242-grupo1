# Patrón Cloud: Sidecar
## Problema:
Normalmente las funciones de las aplicaciones se ejecutan dentro del mismo proceso que la aplicación. Sin embargo esto significa que las funcionalidades de la aplicación no están aisladas y un fallo en una de estas puede afectar a otros componentes de la aplicación o a toda la aplicación. Debido a que el componente y la aplicación son muy dependientes entre sí.

En caso la aplicación se descomponga en microservicios, cada servicio tiene sus propias dependencias y requiere de bibliotecas específicas de su lenguaje para acceder a cualquier recurso compartido con la aplicación principal. Lo que implica que se debe gestionar estas bibliotecas por separado para cada servicio. 


## Solución:
Crear un sidecar el cual contiene tareas perfericas a la aplicación principal. Este sidecar se crea un su propio contenedor proporcionando una sola interfaz para todos los servicios de la aplicación.

Un sidecar no es necesariamente parte de la aplicación, pero esta conectado a ella. Son procesos o servicios de soporte que se implementan con la aplicación principal.

## Casos de aplicación:
 1. Si la aplicación principal utiliza distintos lenguajes y frameworks.
2. Se puede usar para tener controles de seguridad.
3. Puede implementarse como un caché local para mejorar el rendimiento del servicio principal.
4. El sidecar se puede utilizar como un proxy que gestiona las conextiones que entran y salen del servicio, permitiendo realizar acciones como el balanceo de carga, control de acceso o encriptación del tráfico.


## Posible aplicación en el trabajo en grupo: