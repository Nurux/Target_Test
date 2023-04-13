from classe.fibonacci import Fibonnaci

class Calc_Fibo():
    def __init__(self) -> None:
        None
    
    def calc_fibonacci(self, num):
        convert = Fibonnaci()

        if convert.verificar(num):
            text = f'O numero {num} está presente na sequencia de Fibonacci'
            return text
        else:
            text = f'O numero {num} não está presente na sequencia de Fibonacci'
            return text