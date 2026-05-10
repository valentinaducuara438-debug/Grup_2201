class SistemaError(Exception):
    """Clase base para errores del sistema"""
    pass


class ValidacionError(SistemaError):
    """Errores de validación"""
    pass


class ReservaError(SistemaError):
    """Errores relacionados con reservas"""
    pass


class ServicioNoDisponibleError(SistemaError):
    """Servicio no disponible"""
    pass