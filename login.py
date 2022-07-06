from PySimpleGUI import PySimpleGUI as sg
#Layout
sg.theme('Green Mono')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(30, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(30, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')]
]
#Janela
janela = sg.Window('Tela de Login', icon=r'C:\Users\Coridon\Downloads\LogotipoGsaTeste.ico').Layout(layout)

#Ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'Bruna' and valores['senha'] == '123456':
            print('Bem vindo!')
