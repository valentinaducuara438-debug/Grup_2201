import logging

from datetime import datetime

from modelos.cliente import Cliente
from modelos.servicio import Servicio

from excepciones.errores import (
    ValidacionError,
    ReservaError,
    ServicioNoDisponibleError
)


class Reserva:

    def __init__(
        self,
        cliente,
        servicio,
        duracion
    ):

        if not isinstance(cliente, Cliente):
            raise ValidacionError(
                "Cliente inválido"
            )

        if not isinstance(servicio, Servicio):
            raise ValidacionError(
                "Servicio inválido"
            )

        if duracion <= 0:
            raise ValidacionError(
                "La duración debe ser positiva"
            )