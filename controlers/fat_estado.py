from classe.faturamento_estado import Fatestado

class Fatura_Estado:
    def __init__(self) -> None:
        None

    def calc_estado(self, lista):
        lista = [float(i) for i in lista]
        estado = Fatestado()
        return estado.calcular(lista)