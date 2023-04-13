import json

class Faturamento:
    def __init__(self) -> None:
        None
   
    def maior_menor_valor(self, data):
        maior_f = 0
        menor_f = 0

        for i in data:
            if i['valor'] != 0:
                if maior_f < i['valor']:
                   maior_f = i['valor']
                   if menor_f == 0:
                       menor_f = i['valor']
                
                if menor_f > i['valor']:
                    menor_f = i['valor']
        
        return {'maior': maior_f,'menor': menor_f}

    def media(self, data):
        media = 0
        soma = 0
        dias = 0

        for i in data:
            if i['valor'] != 0:
               
                soma = soma + i['valor']
                dias += 1
        
        media = soma / dias 

        return media

    def dias_faturamento_elevado(self, data, media):
        cont = 0

        for i in data:
            if i['valor'] != 0:
                if media < i['valor']:
                    cont += 1 
        
        return cont
    
    def calcular(self, path):
        with open(f'{path}', encoding='utf-8') as my_json:
            data = json.load(my_json)
        
        lista = [] 
        lista.append(self.maior_menor_valor(data))
        m = self.media(data)
        lista.append(self.dias_faturamento_elevado(data, m))

        return lista
    