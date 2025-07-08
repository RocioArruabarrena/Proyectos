class Reloj:
    _inst_singleton = None

    def __init__(self, h, m, s):
        self._hora = h % 24
        self._minuto = m % 60
        self._segundo = s % 60

    def __str__(self):
        return f"{self._hora:02d}:{self._minuto:02d}:{self._segundo:02d}"

    def adelantar_minutos(self, minutos):
        total = self._hora * 60 + self._minuto + minutos
        self._hora = (total // 60) % 24
        self._minuto = total % 60

    def update_hora(self, h, m, s):
        self._hora = h % 24
        self._minuto = m % 60
        self._segundo = s % 60

    def es_igual(self, otro):
        return (self._hora == otro._hora and
                self._minuto == otro._minuto and
                self._segundo == otro._segundo)

    @classmethod
    def obtener_instancia(cls, h, m, s):
        if cls._inst_singleton is None:
            cls._inst_singleton = Reloj(h, m, s)
        return cls._inst_singleton
