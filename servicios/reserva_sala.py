from modelos.servicio import Servicio
from excepciones.errores import ValidacionError


class ReservaSala(Servicio):

    def calcular_costo(
        self,
        horas,
        impuesto=0,
        descuento=0
    ):

        if horas <= 0:
            raise ValidacionError(
                "Las horas deben ser positivas"
            )

        subtotal = self.precio_base * horas

        subtotal += subtotal * impuesto
        subtotal -= subtotal * descuento

        return subtotal

    def descripcion(self):

        return (
            "Servicio de reserva de salas"
        )