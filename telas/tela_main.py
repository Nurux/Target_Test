import PySimpleGUI as sg
from controlers.fat_estado import Fatura_Estado
from controlers.fat_json import Fatu_Json
from controlers.calc_fibonacci import Calc_Fibo
from controlers.conv_string import Convert

class Tela():
    def __init__(self) -> None:
        None

    def tela_main(self):
        sg.theme('LightGrey1')
        sg.set_options(font='Roboto 14')

        layout = [[sg.Titlebar('Desafios Target')],
                [sg.Image('./img/logo_small.png')],
                [sg.Button('Testador de Fibonacci', size=(20, 2), border_width='0',key='fibo')],
                [sg.Button('Faturamento JSON', key='f_json')],
                [sg.Button('Faturamento Estados', key='f_estado')],
                [sg.Button('Inversor de String', key='invert_string' )]]

        janela = sg.Window('Salve', layout= layout, size=(500, 500), element_justification='center')

        while True:
            event, value = janela.read()

            if event == sg.WIN_CLOSED:
                break

            if event == 'fibo':
                self.tela_fibonacci()
                continue
                
            if event == 'f_json':
                self.tela_faturamento_json()
                continue

            if event == 'f_estado':
                self.tela_faturamento_estado()
                continue

            if event == 'invert_string':
                self.tela_conversor_string()
        
        janela.close()

    def tela_faturamento_estado(self):
        sg.theme('LightGrey1')

        layout = [
            [sg.Titlebar('Faturamento dos estados')],
            [sg.Text('Estados', justification='left', expand_x=True), sg.Text('Porcentagem %', justification='right', expand_x=True)],
            [sg.Text('SP', size=(5, 1)), sg.InputText(size=15, key='sp'), sg.Text(key='txt_sp', justification='center', expand_x=True)],
            [sg.Text('RJ', size=(5, 1)), sg.InputText(size=15, key='rj'), sg.Text(key='txt_rj', justification='center', expand_x=True)],
            [sg.Text('MG', size=(5, 1)), sg.InputText(size=15, key='mg'), sg.Text(key='txt_mg', justification='center', expand_x=True)],
            [sg.Text('ES', size=(5, 1)), sg.InputText(size=15, key='es'), sg.Text(key='txt_es', justification='center', expand_x=True)],
            [sg.Text('Outros', size=(5, 1)), sg.InputText(size=15, key='ot'), sg.Text(key='txt_ot', justification='center', expand_x=True)],
            [sg.Text('Total de faturamento: ', expand_x=True), sg.Text(key='total', justification='center', expand_x=True)],
            [sg.Button('Calcular Faturamento', key='calc', expand_x=True), sg.Button('Sair', key='sair', expand_x=True)]
        ]

        janela = sg.Window('Faturamento', layout= layout, size=(400, 300))

        while True:
            event, value = janela.read()

            if event == sg.WIN_CLOSED or event == 'sair':
                break
            
            if event == 'calc':
                nomes = ['sp', 'rj', 'mg', 'es', 'ot']
                text = ['txt_sp', 'txt_rj', 'txt_mg', 'txt_es', 'txt_ot', 'total']
                valor = []

                for i in nomes:
                    valor.append(value[i])

                calcular = Fatura_Estado()
                
                resultados = calcular.calc_estado(valor)
                cont = 0

                while cont < len(resultados):

                    if cont != 5:
                        janela[text[cont]].update('%2.f' % resultados[cont] + '%')
                    else:
                        janela[text[cont]].update(resultados[cont])

                    cont+=1

                continue
        
        janela.close()

    def tela_faturamento_json(self):
        sg.theme('LightGrey1')

        layout = [[sg.Titlebar('Faturamento Json')],
                [sg.Text('Escolha o seu arquivo .json: ')],
                [sg.InputText(key='path', size=(30, 2)), sg.FileBrowse(file_types=[('JSON Files', '*.json')],button_text='Buscar arquivo')],
                [sg.Button('Realizar fauturamento', key='click', expand_x=True), sg.Button('Sair', key='saida', expand_x=True)],
                [sg.Text(key='maior', text_color='green')],
                [sg.Text(key='menor', text_color='red')],
                [sg.Text(key='dias')]]
        
        janela_js = sg.Window('Faturamento', layout= layout, size=(500,250))

        while True:
            event, values = janela_js.read()

            if event == sg.WINDOW_CLOSED or event == 'saida':
                break

            if event == 'click':
                calcular = Fatu_Json()
                lista = calcular.calc_json(values['path'])
                janela_js['maior'].update(lista[0])
                janela_js['menor'].update(lista[1])
                janela_js['dias'].update(lista[2])
                continue
        
        janela_js.close()

    def tela_fibonacci(self):
        sg.theme('LightGrey1')

        layout = [  [sg.Titlebar('Testador de Fibonacci!')],
                    [sg.Text('Digite um numero inteiro para a verificação: ', font='Roboto 12')],
                    [sg.InputText(key='number')],
                    [sg.Button('Verificar', key='active')],
                    [sg.Button('Sair', key='exit')],
                    [sg.Text(key='output', font='Roboto 12')] ]

        janela = sg.Window(title='Janela teste', layout= layout)

        while True:
            event, values = janela.read()

            if event == sg.WIN_CLOSED or event == 'exit':
                break

            if event == 'active':
                calculo = Calc_Fibo()
                text = calculo.calc_fibonacci(int(values['number']))
                janela['output'].update(text)
                continue

        janela.close()

    def tela_conversor_string(self):
        layout = [
            [sg.Titlebar('Conversor de strings')],
            [sg.Text('Digite uma frase: ')],
            [sg.InputText(key='string')],
            [sg.Button('Inverter', key='inv'), sg.Button('Sair', key='sair')],
            [sg.Text(key='output')]
        ]

        janela = sg.Window('Conversor', layout= layout)

        while True:
            event, value = janela.read()

            if event == sg.WINDOW_CLOSED or event == 'sair':
                break

            if event == 'inv':
                conversor = Convert()
                string = conversor.convert(value['string'])
                janela['output'].update(string)
                continue
        
        janela.close()

