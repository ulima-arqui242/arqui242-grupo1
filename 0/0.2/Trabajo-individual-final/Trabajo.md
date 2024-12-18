
# Marco conceptual

La seguridad de contenedores hace referencia a la implementación de políticas, prácticas y herramientas que aseguran la protección de aplicaciones y servicios que se ejecutan en entornos de contenedores. Los contenedores como los que provee DOcker y Kubernetes, encapsulan aplicaciones junto con sus dependencias para brindar portabilidad y escalabilidad. Sin embargo, su naturaleza flexible también introduce desafíos específicos en términos de la seguridad de los mismos.


## Elementos clave en la seguridad de contenedores

- **Imágenes de contenedores seguras:** Las imágenes de contenedores deben provenir de fuentes oficiales, estar libres de vulnerabilidades conocidas y mantenerse actualizadas. 
- **Control de acceso:** Se refiere al uso de principios de privilegios y autenticación para garantizar que solo usuarios y procesos autorizados que los necesitan interactúen con los contenedores.
- **Políticas de seguridad en tiempo de ejecución:** Monitorear los contenedores mientras están en ejecución para identificar comportamientos anómalos que podrían indicar un ataque o vulnerabilidad.
- **Seguridad en la red:** Se refiere a la configuracion de reglas para proteger las comunicaciones internas y externas entre contenedores usado firewall y políticas de red.

## Herrmienta a usar: Kyverno

Kyverno es una herramienta de DevSecOps de política declarativa diseñada para Kubernetes. Permite a los equipos definir y validar políticas de seguridad para los recursos de Kubernetes de manera sencilla y explicable.
### Beneficios de Usar Kyverno
- Permite implementar seguridad de manera consistente en todos los entornos.
- Puede manejar políticas a gran escala en clústeres distribuidos.
- Integra con Kubernetes sin necesidad de lenguajes externos o que sean complejos.

### Flujo de la arquitectura de kyverno
- inicia con una solicitud API, que pasa por pasos de autenticación, mutación, validación de esquema y admisión.
- En el núcleo, el Admission Controller aplica las políticas mediante varios controladores. El Webhook Controller intercepta solicitudes, mientras que el Engine procesa la lógica central.
- Kyverno utiliza configuraciones de webhook, secretos y políticas como entradas. Sus salidas presentan limpieza de recursos, reportes de cumplimiento y actualizaciones procesadas, de esa manera garantiza la conformidad y automatización en la gestión de recursos de Kubernetes.

Diagrama de la arquitectura de Kyverno:
![Alt text](kyverno-architecture.png)

## DEMO

### Requerimientos
- Kubernetes cluster
- minikube
- kubectl
- Kyverno

### Comandos
- minikube start **(iniciar minikube)**
- kubectl cluster-info **(revisar cluster)**
- kubectl create -f https://github.com/kyverno/kyverno/releases/latest/download/install.yaml **(instalar kyverno)**
- kubectl get pods -n kyverno **(ver que kyverno esta activo)**
- kubectl apply -f require-labels.yaml **(crear politica)**
- kubectl apply -f test-pod.yaml **(crear pod para testear politica)**

### Archivos
- YAML de kyverno para crear politicas
- YAML de creación de pod que no usa las politicas definidas
- YAML de creación de pod que si usa las politicas definidas

### Recomendaciones
- Definir estándares de organización: Antes de implementar Kyverno, acordar políticas comunes con todos los equipos involucrados
- Estandar de Configuraciones: Establecer políticas para asegurar que los recursos de Kubernetes (pods, namespaces, etc.) cumplan con configuraciones.
- Crear políticas a la necesidad: Desarrollar políticas que se adapten al nivel de madurez del equipo
- Pruebas en Entornos de dev: Validar las políticas en entornos de prueba para evitar errores que puedan afectar producción.
- Reglas de exclusión: Configurar excepciones para evitar conflictos con componentes críticos del clúster



  ### Link : https://drive.google.com/file/d/1P4fudT36PtWpykhipjHsoWSAKPxSF_ir/view?usp=sharing
