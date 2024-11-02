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
5. recopilacion de logs del servicio principal y enviarlos a una plataforma de monitoreo sin que el servicio principal se vea afectado o modificado.


## Posible aplicación en el trabajo en grupo:

Para MedSysPro, la implementación del patrón Sidecar en una arquitectura de microservicios podría ser una solución que permita a los diferentes modulos comunicarse de manera más eficiente, sin que cada microservicio tenga que gestionar directamente las dependencias o funciones secundarias. 
Algunas formas en que se podría aplicar el patrón Sidecar
1. Comunicación eficiente entre microservicios: En lugar de depender de conexiones directas y configuraciones específicas en cada módulo, un sidecar podría centralizar y gestionar las comunicaciones, siriviendo como intermediario entre servicios.
2. Centralización de funciones secundarias: Funciones como el registro de logs, el monitoreo de rendimiento y la autenticación de usuarios pueden aplicarse en el sidecar, eliminando la necesidad de replicarlas en cada microservicio.
3. Escalabilidad Independiente: Gracias a la separación de funciones, MedSysPro podría escalar servicios específicos sin afectar a toda la aplicación. Por ejemplo, si el módulo de Teleconsulta tiene un aumento en la demanda, el sidecar puede gestionar las solicitudes adicionales sin necesidad de escalar otros módulos de manera directa, lo que reduce los costos y optimiza el uso de recursos.

# Desarrollo de Código y Demo


## Link del repositorio
### https://github.com/Sebastian1335/SideCarCloudPattern.git

## Introducción

Este proyecto demuestra la implementación del patrón Sidecar en un escenario de microservicios. La arquitectura consta de un microservicio principal desarrollado con **NestJS** y dos microservicios secundarios, un servicio de usuario y un sidecar, desarrollados con **ExpressJS**. El objetivo es mostrar cómo el patrón Sidecar actúa como intermediario para gestionar la autenticación y la comunicación entre los microservicios.

## Caso Real

El sistema se compone de los siguientes componentes:

- **User Service**: Proporciona la funcionalidad de autenticación y perfil de usuario.
- **Sidecar**: Actúa como un intermediario que gestiona las solicitudes de autenticación y recuperación de perfil hacia el User Service, además de implementar lógica adicional de negocio, como la simulación de un token de autenticación.
- **Main Microservice**: Maneja las solicitudes del cliente y las redirige al sidecar para autenticación y recuperación de perfil.

## Proceso de Implementación

### 1. Configuración del Entorno

Para comenzar, se debe contar con **Node.js** instalado en el sistema. Se procede a clonar el repositorio que contiene el proyecto y navegar a la carpeta correspondiente.

### 2. Instalación de Dependencias

Cada microservicio tiene su propia carpeta, donde se deben instalar las dependencias necesarias mediante el comando correspondiente de `npm`.

Ejecuar 'npm install' en la carpeta principal de cada microservicio

### 3. Código del User Service

El User Service se configura para manejar la autenticación del usuario y la recuperación de su perfil. Se implementan las rutas necesarias para gestionar estas funcionalidades, asegurando que se manejen correctamente los tokens de autenticación.

### 4. Código del Sidecar

El Sidecar se establece como un servidor que intercepta las solicitudes del Main Microservice y las redirige al User Service. Se implementa la lógica para recibir las credenciales del usuario, validar la autenticación y obtener el perfil correspondiente, comunicándose con el User Service mediante solicitudes HTTP.

### 5. Código del Main Microservice

El Main Microservice actúa como punto de entrada para las solicitudes de los clientes. Se configuran las rutas que permiten la autenticación del usuario y la recuperación de su perfil, redirigiendo estas solicitudes al Sidecar, que se encarga de interactuar con el User Service.

### 6. Pruebas

Una vez que todos los servicios están en ejecución, se realizan pruebas para verificar la autenticación y la recuperación del perfil. Se utilizan comandos `curl` para simular las solicitudes HTTP, asegurando que el flujo de datos entre los microservicios funcione correctamente.

Iniciar User Service:
cd user-service
node index.js

Inicia el Sidecar
cd sidecar
node server.js

iniciar el main-microservice
cd-microservice
npm run start

Ejecutar en el símbolo del sistema
`curl -X POST http://localhost:3001/user/login -H "Content-Type: application/json" -d "{\"username\":\"admin\",\"password\":\"password\"}"`

Luego de recibir el token, realizar la recuperación del perfil
`curl -X GET http://localhost:3001/user/profile -H "Authorization: Bearer <TOKEN_RECIBIDO>"`

## Conclusiones

El patrón Sidecar facilita el desacoplamiento de la lógica de negocio de la infraestructura de servicios. Esta implementación permite gestionar la autenticación y la comunicación entre microservicios de manera eficiente, creando un marco flexible para futuras extensiones de funcionalidad.

## Requisitos

- Node.js
- npm
- Conexión a Internet para descargar dependencias


