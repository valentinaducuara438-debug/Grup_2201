from abc import ABC, abstractmethod

from excepciones.errores import ValidacionError


class Entidad(ABC):

    def __init__(self, id_):

        if id_ <= 0:
            raise ValidacionError(
                "El ID debe ser mayor que cero"
            )

        self._id = id_

    @abstractmethod
    def mostrar_info(self):
        pass