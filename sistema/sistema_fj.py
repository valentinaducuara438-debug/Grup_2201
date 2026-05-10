import logging

from modelos.cliente import Cliente
from modelos.servicio import Servicio
from modelos.reserva import Reserva

from excepciones.errores import ValidacionError


# CONFIGURACIÓN DE LOGS
logging.basicConfig(
    filename='logs/sistema.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class SistemaFJ:

    def __init__(self):

        self.clientes = []
        self.servicios = []
        self.reservas = []

    # =========================
    # CLIENTES
    # =========================

    def agregar_cliente(self, cliente):

        try:

            if not isinstance(cliente, Cliente):
                raise ValidacionError(
                    "Objeto cliente inválido"
                )

            self.clientes.append(cliente)

            logging.info(
                f"Cliente agregado: "
                f"{cliente.nombre}"
            )

            print(
                f"Cliente agregado: "
                f"{cliente.nombre}"
            )

        except ValidacionError as e:

            logging.error(e)

            print(
                f"Error agregando cliente: {e}"
            )

        finally:

            print("Proceso de cliente finalizado")

    # =========================
    # SERVICIOS
    # =========================

    def agregar_servicio(self, servicio):

        try:

            if not isinstance(servicio, Servicio):
                raise ValidacionError(
                    "Objeto servicio inválido"
                )

            self.servicios.append(servicio)

            logging.info(
                f"Servicio agregado: "
                f"{servicio.nombre}"
            )

            print(
                f"Servicio agregado: "
                f"{servicio.nombre}"
            )

        except ValidacionError as e:

            logging.error(e)

            print(
                f"Error agregando servicio: {e}"
            )

        finally:

            print("Proceso de servicio finalizado")

    # =========================
    # RESERVAS
    # =========================

    def agregar_reserva(self, reserva):

        try:

            if not isinstance(reserva, Reserva):
                raise ValidacionError(
                    "Objeto reserva inválido"
                )

            self.reservas.append(reserva)

            logging.info(
                "Reserva agregada correctamente"
            )

            print(
                "Reserva agregada correctamente"
            )

        except ValidacionError as e:

            logging.error(e)

            print(
                f"Error agregando reserva: {e}"
            )

        finally:

            print("Proceso de reserva finalizado")

    # =========================
    # MOSTRAR CLIENTES
    # =========================

    def mostrar_clientes(self):

        print("\nCLIENTES REGISTRADOS")

        if not self.clientes:
            print("No hay clientes registrados")

        else:

            for cliente in self.clientes:
                print(cliente.mostrar_info())

    # =========================
    # MOSTRAR SERVICIOS
    # =========================

    def mostrar_servicios(self):

        print("\nSERVICIOS DISPONIBLES")

        if not self.servicios:
            print("No hay servicios registrados")

        else:

            for servicio in self.servicios:
                print(servicio.descripcion())

    # =========================
    # MOSTRAR RESERVAS
    # =========================

    def mostrar_reservas(self):

        print("\nRESERVAS REALIZADAS")

        if not self.reservas:
            print("No hay reservas registradas")

        else:

            for reserva in self.reservas:
                print(reserva)