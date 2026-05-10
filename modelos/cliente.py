import re

from modelos.entidad import Entidad
from excepciones.errores import ValidacionError


class Cliente(Entidad):

    def __init__(self, id_, nombre, email):
        super().__init__(id_)

        self.nombre = nombre
        self.email = email

    # =========================
    # NOMBRE
    # =========================
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):

        if not value.strip():
            raise ValidacionError("El nombre no puede estar vacío")

        if len(value.strip()) < 3:
            raise ValidacionError("El nombre debe tener mínimo 3 caracteres")

        self._nombre = value.title()

    # =========================
    # EMAIL
    # =========================
    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):

        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(patron, value):
            raise ValidacionError("Correo electrónico inválido")

        self._email = value

    # =========================
    # MÉTODOS
    # =========================
    def mostrar_info(self):
        return f"Cliente: {self.nombre} - {self.email}"

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.email}"