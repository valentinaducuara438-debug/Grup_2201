# Software FJ - Sistema Integral de Gestión de Clientes, Servicios y Reservas

## Descripción del Proyecto

Este proyecto fue desarrollado en Python utilizando Programación Orientada a Objetos (POO) con el objetivo de gestionar clientes, servicios y reservas para la empresa Software FJ.

El sistema permite administrar diferentes tipos de servicios como:

- Reserva de salas
- Alquiler de equipos
- Asesorías especializadas

La aplicación funciona sin bases de datos, utilizando objetos, listas y archivos de logs para registrar eventos y errores del sistema.

---

# Objetivos del Proyecto

- Aplicar Programación Orientada a Objetos.
- Implementar herencia, encapsulación, abstracción y polimorfismo.
- Manejar excepciones de forma robusta.
- Registrar errores y eventos mediante logs.
- Garantizar la estabilidad del sistema ante errores.

---

# Tecnologías Utilizadas

- Python
- Visual Studio Code
- Git y GitHub
- Programación Orientada a Objetos
- Logging

---

# Estructura del Proyecto

```text
software_fj/

│
├── main.py
├── README.md
│
├── logs/
│   └── sistema.log
│
├── core/
│   ├── __init__.py
│   ├── entidad.py
│   ├── cliente.py
│   ├── reserva.py
│
├── services/
│   ├── __init__.py
│   ├── servicio.py
│   ├── reserva_sala.py
│   ├── alquiler_equipo.py
│   └── asesoria.py
│
├── exceptions/
│   ├── __init__.py
│   └── custom_exceptions.py
│
└── utils/
    ├── __init__.py
    └── logger.py