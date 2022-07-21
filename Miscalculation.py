from random import Random, randint, random
import PySimpleGUI as sg


class TelaCalc:
    def __init__(self):
        # layout
        sg.theme("DefaultNoMoreNagging")
        layout = [
            [sg.Text('Primeiro número'), sg.Input(size=(15, 0), key='a')],
            [sg.Text('Segundo número'), sg.Input(size=(15, 0), key="b")],
            [sg.Button('Calcular')],
            [sg.Output(size=(6, 3))]

        ]
        # janela
        self.janela = sg.Window("Calculadora").layout(layout)

    def Iniciar(self):
        while True:
            # extração de dados
            self.button, self.values = self.janela.Read()
            a = int(self.values['a'])
            b = int(self.values['b'])
            s = a + b
            if s % 2 == 0:
                print(s + randint(0, 10))
            else:
                print(s - randint(0, 10))


tela = TelaCalc()
tela.Iniciar()
