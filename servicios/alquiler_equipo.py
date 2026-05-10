from modelos.servicio import Servicio
from excepciones.errores import ValidacionError


class AlquilerEquipo(Servicio):

    def calcular_costo(
        self,
        dias,
        descuento=0,
        impuesto=0
    ):

        if dias <= 0:
            raise ValidacionError(
                "Los días deben ser positivos"
            )

        subtotal = self.precio_base * dias

        subtotal -= subtotal * descuento
        subtotal += subtotal * impuesto

        return subtotal

    def descripcion(self):

        return (
            "Servicio de alquiler de equipos"
        )