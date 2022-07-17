#!!!---IMPORTANTE---!!! Leia o READ.ME antes de utilizar!

from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
import PySimpleGUI as sg

class PainelGrafico:
    
    def __init__(self):
        
        sg.theme('SystemDefault')
        
        layout = [
            [sg.Push(), sg.Image('Img/imagem.png'), sg.Image('Img/mordomo.png'), sg.Push()],
            [sg.Text('Usuário: ', font='Arial'), sg.InputText(size=(18, 50), justification='c', key='-USUARIO-', 
            default_text=PainelGrafico.buscar_credencial_login())],
            [sg.Text('Senha:   ', font='Arial'), sg.InputText(size=(18, 50), key='-SENHA-', password_char='*', justification='c', 
            default_text=PainelGrafico.buscar_credencial_senha())], 
            [sg.Text('Cole seu texto aqui:', font='Arial'), sg.InputText(size=(7, 50), key='-MENSAGEM-', 
            default_text=PainelGrafico.buscar_mensagem())],
            [sg.Text('Lembrar', font='Arial'), sg.CBox('', key='-LEMBRAR-')],
            [sg.Button('Sair'), sg.Push(), sg.Button('Iniciar')]
        ]
        self.window = sg.Window('Robô Mordomo', layout)

    def iniciar(self):
        while True:  
            self.events, self.values = self.window.read()
            if self.events == 'Iniciar':
                PainelGrafico.salvar_credenciais(self)
                BotInsta.iniciar_bot(self)
            elif self.events == 'Sair' or self.events == sg.WINDOW_CLOSED:
                break 
    
    def salvar_credenciais(self):
        if self.values['-LEMBRAR-'] == True:
            usuario = self.values['-USUARIO-']
            senha = self.values['-SENHA-']
            mensagem = self.values['-MENSAGEM-']
            with open('usr.txt', 'w') as arquivo:
                escrever_arquivo = arquivo.write(f' Usuario = {usuario}\nSenha = {senha}\nMensagem = {mensagem}')
                arquivo.close()

    def buscar_credencial_login():
        with open('usr.txt', 'r') as arquivo:
            ler_arquivo = arquivo.readlines()
            transformar_em_lista = list(ler_arquivo[0])
            unificar_lista = ''.join(transformar_em_lista[10:])
            tratamento_lista = unificar_lista.strip()
            return tratamento_lista

    def buscar_credencial_senha():
        with open('usr.txt', 'r') as arquivo:
            ler_arquivo = arquivo.readlines()
            transformar_em_lista = list(ler_arquivo[1])
            unificar_lista = ''.join(transformar_em_lista[8:])
            tratamento_lista = unificar_lista.strip()
            return tratamento_lista

    def buscar_mensagem():
        with open('usr.txt', 'r') as arquivo:
            ler_arquivo = arquivo.readlines()
            transformar_em_lista = list(ler_arquivo[2])
            unificar_lista = ''.join(transformar_em_lista[10:])
            tratamento_lista = unificar_lista.strip()
            return tratamento_lista
                
class BotInsta:

    def abrir_dicionario_html(self):
        self.endereços_HTML = {
            'Login Usuario xpath': '//*[@id="loginForm"]/div/div[1]/div/label/input', 
            'Login Senha xpath': '//*[@id="loginForm"]/div/div[2]/div/label/input', 
            'Botao Entrar Login xpath': '//*[@id="loginForm"]/div/div[3]', 
            'Botao Fechar Popup 1 xpath': '//*[@id="react-root"]/section/main/div/div/div/div/button', 
            'Botao Fechar Popup 2 class': '_a9--', 
            'Botao Enviar Mensagem class': '_acan', 
            'Botao Mensagem tag_name': 'textarea', 
            'Botao Enviar xpath': '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button', 
            'Botao Mensagem Nao Lida xpath': '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[3]/div', 
            'Botao Messenger Dm xpath': '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[1]/div/div[3]/div/div[2]/a', 
            'Botao Messenger Home xpath': '/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a',
            'Botao Messenger Dm class': '_ab8l',
            'Botao Fechar Popup 2 xpath': '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]'}

    def coletar_dados_usuario(self):
        self.user_client_insta = self.values['-USUARIO-']
        self.password_client_insta = self.values['-SENHA-']
        self.mensagem_automatica = self.values['-MENSAGEM-']
        
    def abrir_pagina(self):
        self.pagina = webdriver.Chrome()
        self.pagina.get('https://www.instagram.com')
    
    def fazer_login(self):
        time.sleep(3)
        self.pagina.find_element(By.XPATH, self.endereços_HTML['Login Usuario xpath']).send_keys(self.user_client_insta) 
        self.pagina.find_element(By.XPATH, self.endereços_HTML['Login Senha xpath']).send_keys(self.password_client_insta) 
        self.pagina.find_element(By.XPATH, self.endereços_HTML['Botao Entrar Login xpath']).click() 
    
    def pular_popups(self):
        try:
            time.sleep(5)
            self.pagina.find_element(By.XPATH, self.endereços_HTML['Botao Fechar Popup 1 xpath']).click() 
        except:
            time.sleep(3)
            self.pagina.find_element(By.XPATH, self.endereços_HTML['Botao Fechar Popup 2 xpath']).click()    
    
    def entrar_direct(self):
        time.sleep(2)
        self.pagina.find_element(By.XPATH, self.endereços_HTML['Botao Messenger Home xpath']).click()
        try:
            time.sleep(3)
            self.pagina.find_element(By.CLASS_NAME, self.endereços_HTML['Botao Fechar Popup 2 class']).click()
        except:
            pass
        
    def enviar_mensagem(self):
        while True:
            try:
                self.pagina.find_element(By.CLASS_NAME, self.endereços_HTML['Botao Messenger Dm class']).click()
                time.sleep(1)
                self.pagina.find_element(By.TAG_NAME, self.endereços_HTML['Botao Mensagem tag_name']).send_keys(self.mensagem_automatica)
                self.pagina.find_element(By.XPATH, self.endereços_HTML['Botao Enviar xpath']).click()
                time.sleep(1)   
                self.pagina.find_element(By.XPATH, self.endereços_HTML['Botao Messenger Dm xpath']).click()
            except:
                pass
    
    def iniciar_bot(self):
        BotInsta.abrir_dicionario_html(self)
        BotInsta.coletar_dados_usuario(self)
        BotInsta.abrir_pagina(self)
        BotInsta.fazer_login(self)
        BotInsta.pular_popups(self)
        BotInsta.entrar_direct(self)
        BotInsta.enviar_mensagem(self)

a = PainelGrafico()
a.iniciar()
a.salvar_credenciais()

             
