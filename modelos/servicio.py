from abc import ABC, abstractmethod

from excepciones.errores import ValidacionError


class Servicio(ABC):

    def __init__(
        self,
        nombre,
        precio_base,
        disponible=True
    ):

        if precio_base <= 0:
            raise ValidacionError(
                "El precio base debe ser mayor a cero"
            )

        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = disponible

    @abstractmethod
    def calcular_costo(self, *args, **kwargs):
        pass

    @abstractmethod
    def descripcion(self):
        pass