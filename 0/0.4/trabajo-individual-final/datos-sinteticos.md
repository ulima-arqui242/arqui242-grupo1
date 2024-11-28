## Generación de datos sintéticos para pruebas

En entornos de desarrollo es necesario trabajar con altos volumenes de datos para analizar el rendimiento y funcionalidad del sistema. Sin embargo, utilizar datos reales puede presentar desafíos importantes, como problemas de privacidad y limitaciones en su disponibilidad. Para superar estas dificultades se utilizan herramientas como Faker, que genera datos sintéticos, y Locust, que se emplea para realizar pruebas de carga. Estas herramientas permiten simular escenarios realistas sin poner en riesgo información sensible.

### Faker
Faker es una biblioteca de Python que permite generar datos ficticios de manera flexible y personalizable. Su principal utilidad es proporcionar datos realistas para pruebas de software y desarrollo, sin comprometer la privacidad ni depender de datos reales. Faker es capaz de generar datos aleatorios de diferentes tipos, como nombres, direcciones, correos electrónicos, números de teléfono, textos, fechas, números de tarjetas de crédito, entre otros. Sus ventajas incluyen:
- **Facilidad de uso:** Unas pocas líneas de código son suficientes para generar datos variados.
- **Extensible:** Puedes crear tus propios "providers" personalizados.
- **Localizado:** Soporta múltiples idiomas y formatos regionales, adaptándose a distintas configuraciones culturales.

Al decir que Faker es extensible me refiero al uso de "Providers", estos son módulos que encapsulan métodos para generar conjuntos específicos de datos. Cada tipo de datos, como nombres, direcciones, números de teléfono o información financiera, pertenece a un provider. Por ejemplo ciertos providers incluyen:

- **Información personal:** name, address, phone_number.
- **Datos financieros:** credit_card_number, iban, currency_code.
- **Internet:** email, url, ipv4, domain_name.
- **Texto genérico:** word, sentence, paragraph.
- **Fechas y horas:** date, time, date_time.

### Locust
Locust es una herramienta de código abierto para realizar pruebas de carga y rendimiento. Permite definir el comportamiento de los usuarios mediante código Python, lo que facilita la creación de escenarios de prueba complejos. Algunas ventajas de Locust incluyen:
- **Escalabilidad:** Puede simular millones de usuarios simultáneos distribuidos en múltiples máquinas.
- **Flexibilidad:** Al estar basado en Python, es altamente configurable y extensible.
- **Interfaz web:** Proporciona una interfaz web para monitorear y controlar las pruebas en tiempo real.

Esta herramienta es ideal para evaluar cómo un sistema maneja cargas concurrentes y para identificar posibles cuellos de botella en aplicaciones web y otros servicios.

### Demo
Como parte de una demostración, he creado tres tablas utilizando SQLite en Python y desarrollado dos escenarios diferentes. En el primer escenario, utilicé Faker para generar la información necesaria y poblar únicamente las tablas creadas. En el segundo escenario, generé datos de manera masiva, simulando una gran cantidad de información con Locust, que a la par permite visualizar en tiempo real los ... ERRORES, TIMEOUTS????

Video: 

