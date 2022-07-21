from random import Random, randint, random
import PySimpleGUI as sg


class TelaCalc:
    def __init__(self):
        # layout
        layout = [
            [sg.Text('Primeiro número'), sg.Input(size=(15, 0), key='a')],
            [sg.Text('Segundo número'), sg.Input(size=(15, 0), key="b")],
            [sg.Button('Calcular')],
            [sg.Output(size=(6, 6))]

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


'''
num1 = int(input("insira um numéro: "))
num2 = int(input("insira outro numéro: "))
soma = num1 + num2

if soma % 2 == 0:
    print(soma + randint(0, 10))
else:
    print(soma - randint(0, 10))
'''
