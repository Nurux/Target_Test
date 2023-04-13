from classe.conversor_string import Convert_String

class Convert():
    def __init__(self) -> None:
        None

    def convert(self, string):
        if string == '':
            return 'Primeiro digite uma Frase para ser invertida!'

        x = Convert_String()
        
        return  x.converter(string)
