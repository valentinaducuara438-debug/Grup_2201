from modelos.servicio import Servicio
from excepciones.errores import ValidacionError


class Asesoria(Servicio):

    def calcular_costo(
        self,
        horas,
        tipo="normal",
        impuesto=0
    ):

        if horas <= 0:
            raise ValidacionError(
                "Las horas deben ser positivas"
            )

        multiplicador = (
            1.5 if tipo == "especializada"
            else 1
        )

        subtotal = (
            self.precio_base
            * horas
            * multiplicador
        )

        subtotal += subtotal * impuesto

        return subtotal

    def descripcion(self):

        return "Servicio de asesoría especializada"