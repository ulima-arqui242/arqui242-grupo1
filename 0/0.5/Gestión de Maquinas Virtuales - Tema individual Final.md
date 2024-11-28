### **Introducción**
La virtualización es importante en cuanto a la optimización de recursos, la gestión eficiente de sistemas y la reducción de los costos operativos. Por lo que las máquinas virtuales son entornos de computación que simulan un sistema físico dentro de un sistema operativo principal (Como si tuviesemos una computadora dentro de nuestra laptop o pc), lo que nos permite ejecutar aplicaciones o sistemas operativos completos de manera aislada a lo que tenemos actualmente en nuestro dispositivo. Esto es util para probar software, aprender sobre diferentes sistemas operativos, como veremos en el presente trabajo donde se ejecutara un sistema operativo windows 11 dentro de una computadora que solo tiene capacidades para ejecutar windows 10 y esto se hara mediante una Vm. Tambien se puede crear entornos de desarrollo y hacer pruebas sin comprometer la estabilidad o seguridad del sistema principal.

Para esto usare VirtualBox, que es una plataforma de virtualización de código abierto y gratis de usar que nos permite crear y gestionar diversas maquinas virtuales. En este informe, se detallará el proceso de creación de una máquina virtual utilizando VirtualBox, la instalación de **Windows 11** en una máquina virtual, y se veran diversos aspectos, como las ventajas y desventajas de las máquinas virtuales, comparaciones con otros métodos de virtualización.

![image](https://github.com/user-attachments/assets/b2721bdb-3f88-4adb-ba49-6634ca4dd839)

---

### **¿Qué son las Máquinas Virtuales?**

Como se mencionó en la introudcción, las máquinas virtuales son entornos completamente funcionales que emulan una computadora física, pero se ejecutan sobre un sistema operativo anfitrión. Tienen sus propios recursos virtualizados, lo que vendría a ser el CPU, RAM, almacenamiento, etc. Que son manejadas por un hipervisor, el cual es como una capa de software que se encarga de gestionar estos recursos al momentos de asignarlos a la maquina virtual.

#### **Componentes de una Máquina Virtual:**

A continuación se mencionarán los componentes de una Vm acorde a la pagina oficial y documentación proporcionada por VirtualBox.

1. **CPU Virtualizada:** La máquina virtual se ejecuta sobre la CPU del host, pero se comporta como si tuviera su propio procesador.
2. **Memoria RAM:** La VM utiliza una cantidad específica de RAM que se asigna de forma estática o dinámica desde el sistema host.
3. **Almacenamiento Virtual:** El disco duro virtual de la máquina contiene el sistema operativo y las aplicaciones que ejecuta la VM. Este disco puede tener un tamaño dinámico, aumentando según las necesidades.
4. **Adaptadores de Red Virtuales:** Permiten que la máquina virtual se conecte a redes internas o externas, dependiendo de la configuración.
5. **Controladores Virtuales:** Controlan dispositivos virtualizados como monitores, impresoras o adaptadores USB, entre otros.

![image](https://github.com/user-attachments/assets/63c07f72-43f0-400b-b577-9b4898459ee2)

---

### **Ventajas de las Máquinas Virtuales**
Las ventajas son tanto para un usuario como para una empresa que quiera optimizar sus procesos o infraestructura de ti.

1. **Aislamiento y Seguridad:**
   - Las máquinas virtuales están completamente aisladas entre sí, lo que significa que si una máquina virtual se ve comprometida por malware o tiene un error, entonces las otras vm no se ven afectadas ni la fisica, sino solo la vm comprometida, la cual podría ser restaurada mediante un snapshot posiblemente o eliminarla.
   - Esto también permite realizar pruebas de software o configuraciones peligrosas sin poner en riesgo el sistema principal que es nuestra Pc en el caso actual.

2. **Pruebas y Desarrollo:**
   - Las VM permiten realizar pruebas de software en diferentes sistemas operativos (Ya sea: Windows, Linux, macOS, etc.) sin necesidad de tener múltiples dispositivos físicos. Como se verá en la demo.
   - Es ideal para desarrolladores que necesitan simular diferentes configuraciones de sistemas o redes.

3. **Consolidación de Recursos:**
   - Como se mencionó previamente, la máquina virtual permite ejecutar múltiples sistemas operativos en una sola máquina física, lo que optimiza el uso del hardware.
   - Las organizaciones pueden reducir el número de servidores físicos que necesitan al virtualizar muchos de sus servicios, lo cual a la vez ahorra espacio físico y también consumo energético.

4. **Escalabilidad y Flexibilidad:**
   - Estas maquinas son fácilmente modificadas en cuanto a la cantidad de CPU, RAM o almacenamiento. Todo depende de lo que queremos usar y esto se puede configurar directamente previo a la creación de una.
   - También se pueden clonar, respaldar o migrar con facilidad, lo cual es util para administrar la infraestructura.

5. **Compatibilidad de Software:**
   - VirtualBox, por ejemplo, permite ejecutar sistemas operativos antiguos o no compatibles con el hardware físico actual, lo que puede ser útil para software legacy o para aplicaciones que requieren un entorno específico. Como se verá en mi demo donde tengo windows 10 pero ejecutaré windows 11 que no es compatible con mi dispositivo.

![image](https://github.com/user-attachments/assets/d5d08e49-10f4-463a-bdc4-e61f1a71800a)

---

### **Desventajas de las Máquinas Virtuales**

A pesar de sus muchas ventajas, las máquinas virtuales también presentan ciertas limitaciones o desventajas.

1. **Rendimiento Inferior al Hardware Nativo:**
   - Las máquinas virtuales, al compartir los recursos del sistema anfitrión, no alcanzan el mismo nivel de rendimiento que una máquina física dedicada. Esto puede ser especialmente notorio cuando se utilizan aplicaciones que requieren mucho poder de cómputo, como software de edición de video o simulaciones 3D.
   - Aunque las VMs son bastante eficientes, la sobrecarga de la virtualización puede ser un inconveniente en entornos de alto rendimiento.

2. **Requiere Recursos Adicionales:**
   - Aunque las máquinas virtuales permiten consolidar recursos, también requieren que el sistema anfitrión tenga suficiente poder de cómputo, memoria RAM y almacenamiento para ejecutar múltiples VMs al mismo tiempo.
   - La virtualización no es ideal para equipos con recursos limitados.

3. **Complejidad de Configuración:**
   - Configurar y administrar múltiples máquinas virtuales puede resultar complejo, especialmente cuando se manejan redes o configuraciones avanzadas. Sin un buen entendimiento de la virtualización, el proceso de creación y mantenimiento puede ser desafiante.

4. **Dependencia de un Hipervisor:**
   - La estabilidad de la máquina virtual depende completamente del hipervisor (como VirtualBox, VMware, Hyper-V, etc.). Si el hipervisor presenta problemas, todas las VMs pueden verse afectadas.

![image](https://github.com/user-attachments/assets/2b29de08-8c3c-4050-989e-88f5c37916d3)

---

### **Proceso de Instalación de Windows 11 en VirtualBox**

Ahora que hemos entendido los beneficios y limitaciones de las máquinas virtuales, procederemos a describir el proceso de instalación de Windows 11 en una máquina virtual usando VirtualBox.

#### **Paso 1: Descargar VirtualBox**
1. Dirígete a la página oficial de VirtualBox en [https://www.virtualbox.org/](https://www.virtualbox.org/).
2. Descarga la versión adecuada para tu sistema operativo (Windows, Linux o macOS) y sigue las instrucciones para la instalación.
   ![image](https://github.com/user-attachments/assets/aa1cd2da-5246-44dd-86ea-787e109021f3)

#### **Paso 2: Obtener la ISO de Windows 11**
La imagen ISO de Windows 11 es un archivo que contiene todos los archivos necesarios para instalar el sistema operativo. Para obtener la ISO de Windows 11:
1. Ve a [https://www.microsoft.com/es-es/software-download/windows11](https://www.microsoft.com/es-es/software-download/windows11).
2. Descarga la ISO de Windows 11 desde la opción de "Descargar ahora" o utiliza la herramienta de creación de medios de Microsoft.
   ![image](https://github.com/user-attachments/assets/ee99f032-b7eb-47f9-9336-70821d83251a)


#### **Paso 3: Crear la Máquina Virtual en VirtualBox**
1. **Inicia VirtualBox** y haz clic en **"Nuevo"**.
2. Asigna un **nombre** a la máquina virtual (por ejemplo, "Windows 11").
3. En **Tipo**, selecciona **Microsoft Windows** y en **Versión**, elige **Windows 11 (64-bit)**.
4. En la siguiente ventana, asigna **4 GB de RAM** (recomendable para Windows 11).
5. Crea un **disco duro virtual** de al menos **50 GB** en formato VDI (VirtualBox Disk Image). Elige un tamaño **dinámico** para permitir que el disco crezca a medida que se necesite espacio.

![image](https://github.com/user-attachments/assets/2bbc92e3-0132-4901-97c9-55765cd03ff0)
![image](https://github.com/user-attachments/assets/e00c9471-381c-4886-90c3-4c8be3696c8c)

#### **Paso 4: Configurar la Máquina Virtual**
1. Una vez creada la VM, haz clic en **"Configuración"**.
2. En la pestaña **"Almacenamiento"**, selecciona el ícono de CD junto a "Vacío" y luego **"Seleccionar archivo de disco"**.
3. Busca la ISO de Windows 11 que descargaste y selecciona el archivo.
4. Configura los adaptadores de red si es necesario para que la VM tenga acceso a Internet.
![image](https://github.com/user-attachments/assets/971c2afe-6fcd-40f4-bda7-77679882b49e)


#### **Paso 5: Iniciar la Instalación de Windows 11**
1. Haz clic en **"Iniciar"** para arrancar la máquina virtual.
2. El proceso de instalación de Windows 11 comenzará. Selecciona el idioma, la región y sigue las instrucciones.
3. Si se te solicita, puedes omitir la clave de producto o ingresar una clave válida de Windows 11.
![image](https://github.com/user-attachments/assets/a6c7c179-ef3b-4975-afdd-d0d67c517a3f)

#### **Paso 6: Configuración y Finalización**
1. Durante la instalación, la máquina virtual se reiniciará varias veces y puede demorar en total más de una hora, como fue en mi caso.
2. Después de completar la instalación, configura las opciones iniciales de Windows 11, como la creación de una cuenta de usuario y la configuración de la red.

#### **Paso 7: Maquina Virtual lista para usar**



---

### **Comparación entre VirtualBox y Otras Herramientas de Virtualización**

| Característica         | VirtualBox            | VMware Workstation      | Hyper-V                  |
|------------------------|-----------------------|-------------------------|--------------------------|
| **Costo**              | Gratuito              | De pago (con versión gratuita) | Gratuito en Windows Pro y Enterprise |
| **Compatibilidad**     | Windows, Linux, macOS | Windows, Linux          | Solo Windows             |
| **Rendimiento**        | Bueno, pero con sobrecarga | Mejor rendimiento que VirtualBox | Alto rendimiento (integrado en Windows) |
| **Facilidad de Uso**   | Fácil de usar, interfaz amigable | Interfaz robusta pero más compleja | Interfaz básica, fácil para usuarios avanzados |
| **Compatibilidad con SO Invitado** | Amplia (Windows, Linux, BSD, etc.) | Soporta muchos sistemas operativos | Solo soporta Windows |

---

### **Conclusión**

Las **máquinas virtuales** representan una herramienta poderosa y versátil que ofrece muchos beneficios, como el aislamiento, la optimización de recursos y la flexibilidad para ejecutar diferentes sistemas operativos en una sola máquina física. **VirtualBox**, en particular, es una opción accesible y eficiente para usuarios que buscan una solución gratuita para virtualizar sus entornos. Si bien las máquinas virtuales tienen algunas limitaciones de rendimiento, su capacidad para ejecutar múltiples sistemas operativos simultáneamente las convierte en una herramienta invaluable para el desarrollo, pruebas y administración de sistemas.

---

### **Referencias**
- VirtualBox: [https://www.virtualbox.org/](https://www.virtualbox.org/)
- Microsoft Windows 11: [https://www.microsoft.com/es-es/software-download/windows11](https://www.microsoft.com/es-es/software-download/windows11)
