
# Marco conceptual

La seguridad de contenedores hace referencia a la implementación de políticas, prácticas y herramientas que aseguran la protección de aplicaciones y servicios que se ejecutan en entornos de contenedores. Los contenedores como los que provee DOcker y Kubernetes, encapsulan aplicaciones junto con sus dependencias para brindar portabilidad y escalabilidad. Sin embargo, su naturaleza flexible también introduce desafíos específicos en términos de la seguridad de los mismos.


## Elementos clave en la seguridad de contenedores

- **Imágenes de contenedores seguras:** Las imágenes de contenedores deben provenir de fuentes oficiales, estar libres de vulnerabilidades conocidas y mantenerse actualizadas. 
- **Control de acceso:** Se refiere al uso de principios de privilegios y autenticación para garantizar que solo usuarios y procesos autorizados que los necesitan interactúen con los contenedores.
- **Políticas de seguridad en tiempo de ejecución:** Monitorear los contenedores mientras están en ejecución para identificar comportamientos anómalos que podrían indicar un ataque o vulnerabilidad.
- **Seguridad en la red:** Se refiere a la configuracion de reglas para proteger las comunicaciones internas y externas entre contenedores usado firewall y políticas de red.

## Herrmienta a usar: Kyverno

Kyverno es una herramienta de DevSecOps de política declarativa diseñada para Kubernetes. Permite a los equipos definir y validar políticas de seguridad para los recursos de Kubernetes de manera sencilla y explicable.


