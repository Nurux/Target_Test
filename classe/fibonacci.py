class Fibonnaci :   
    def __init__(self) -> None:
        None

    def verificar(self, num):
        suc = 0
        ant = 0
        cont = 0

        while cont <= num+1:
            if cont == 1:
                suc = 1
                ant = 0
            else: 
                suc = suc + ant 
                ant = suc - ant

            if suc == num:
                return True
            
            cont += 1
        
        return False
        