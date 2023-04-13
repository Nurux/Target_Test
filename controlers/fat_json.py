from classe.faturamento_json import Faturamento

class Fatu_Json:
    def __init__(self) -> None:
        None
    
    def calc_json(self, path):
        faturar = Faturamento()
        lista = faturar.calcular(path)
        valores = [lista[0]['maior'], lista[0]['menor'], lista[1]]
        lista_texto = []

        lista_texto.append(f'O Maior Faturamento: {valores[0]}')
        lista_texto.append(f'O Menor Faturamento: {valores[1]}')
        lista_texto.append(f'Dias superiores a media mensal: {valores[2]}')

        return lista_texto