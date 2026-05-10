from modelos.cliente import Cliente
from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import Asesoria
from modelos.reserva import Reserva
from sistema.sistema_fj import SistemaFJ

print("=====================================")
print("      SISTEMA SOFTWARE FJ")
print("=====================================")

sistema = SistemaFJ()

# =========================
# CLIENTES (2 válidos, 1 inválido)
# =========================

datos_clientes = [
    (1, "Juan Perez", "juan@gmail.com"),   # válido
    (2, "Maria Lopez", "maria@gmail.com"), # válido
    (3, "", "correo_malo")                 # inválido (para probar error)
]

for id, nombre, correo in datos_clientes:
    try:
        cliente = Cliente(id, nombre, correo)
    except Exception as e:
        print(f"Error: {e}")
    else:
        sistema.agregar_cliente(cliente)
        print("Cliente agregado correctamente")
    finally:
        print("Proceso cliente finalizado")

# =========================
# SERVICIOS
# =========================

try:
    s1 = ReservaSala("Sala de Juntas", 100)
    s2 = AlquilerEquipo("Portátiles", 80)
    s3 = Asesoria("Asesoría Empresarial", 150)

    sistema.agregar_servicio(s1)
    sistema.agregar_servicio(s2)
    sistema.agregar_servicio(s3)

    print("Servicios registrados correctamente")

except Exception as e:
    print(f"Error: {e}")

# =========================
# RESERVAS (ahora sí funcionan)
# =========================

for i in range(5):
    try:
        if not sistema.clientes:
            raise Exception("No hay clientes disponibles")

        cliente = sistema.clientes[i % len(sistema.clientes)]
        servicio = sistema.servicios[i % len(sistema.servicios)]

        reserva = Reserva(cliente, servicio, i + 1)

        # confirmar si tu clase lo tiene
        if hasattr(reserva, "confirmar"):
            reserva.confirmar()

    except Exception as e:
        print(f"Error en reserva: {e}")
    else:
        sistema.agregar_reserva(reserva)
        print("Reserva creada correctamente")
    finally:
        print("Proceso de reserva finalizado")

# =========================
# RESULTADOS
# =========================

print("\nCLIENTES REGISTRADOS")
if sistema.clientes:
    for c in sistema.clientes:
        print(c)
else:
    print("No hay clientes registrados")

print("\nSERVICIOS DISPONIBLES")
for s in sistema.servicios:
    print(s.descripcion())

print("\nRESERVAS REALIZADAS")
if sistema.reservas:
    for r in sistema.reservas:
        print(r)
else:
    print("No hay reservas registradas")