#Menu com EMAIL, SENHA, DUAS ABAS PARA ESCOLHER PASTAS
import PySimpleGUI as sg

sg.theme('reddit')

layout = [
    [sg.Text('Email'),sg.Input(key ='Email')],
    [sg.Text('Senha'),sg.Input(key ='Senha',password_char='*')],
    [sg.FolderBrowse('Escolher pasta anexos', target = 'input_anexos'), sg.Input( key = 'input_anexos')],
    [sg.FileBrowse('Escolher Pasta Planilha', target='input_planilha'), sg.Input(key = 'input_planilha')],
    [sg.Button('Salvar')]
]

janela = sg.Window('Menu', layout= layout)

while True:
    evento, informacoes = janela.read() 
    if evento == sg.WIN_CLOSED:
        break
    elif evento == 'Salvar':
        email = informacoes['Email']
        senha = informacoes['Senha']
        caminho_anexo = informacoes['input_anexos']
        caminho_planilha = informacoes['input_planilha']

    
        print(email)
        print(senha)
        print(caminho_anexo)
        print(caminho_planilha)