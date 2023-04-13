class Fatestado():
    def __init__(self) -> None:
        None
    
    def calcular(self, lista):
        soma = 0

        for i in lista:
            soma += i
        
        lista_porcent = []

        for i in lista:
            x = (i * 100) / soma

            lista_porcent.append(x)
        
        lista_porcent.append(soma)

        return lista_porcent