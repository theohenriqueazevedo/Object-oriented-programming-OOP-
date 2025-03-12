import tkinter as tk
from tkinter import messagebox
import jogo as jogo

# Classe responsável pela interface principal do sistema
class ViewPrincipal():
    def __init__(self, root, controle):
        self.controle = controle  # Controle principal do sistema
        self.root = root  # Janela principal
        self.root.geometry('300x200')  # Define o tamanho da janela
        self.menubar = tk.Menu(self.root)  # Criação da barra de menu

        # Menu relacionado a jogos
        self.jogoMenu = tk.Menu(self.menubar)

        # Opção para cadastrar um novo jogo
        self.jogoMenu.add_command(label="Cadastrar", \
                                  command=self.controle.cadastrarjogo)
        # Opção para avaliar um jogo já cadastrado
        self.jogoMenu.add_command(label="Avaliar", \
                                  command=self.controle.avaliarjogo)
        # Adiciona o menu de jogos à barra de menu
        self.menubar.add_cascade(label="JOGO", \
                                 menu=self.jogoMenu)
        # Opção para consultar jogos por avaliação
        self.jogoMenu.add_command(label="Consultar", \
                                  command=self.controle.consultar_avaliacoes)

        # Configura a barra de menu na janela principal
        self.root.config(menu=self.menubar)


# Classe responsável por controlar o fluxo principal do sistema
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()  # Instancia a janela principal

        # Instancia o controlador dos jogos
        self.ctrljogo = jogo.CtrlJogo()

        # Instancia a interface principal passando a janela e o controle
        self.limite = ViewPrincipal(self.root, self)

        # Define o título da janela principal
        self.root.title("Sistema de jogos")
        # Inicia o loop principal do tkinter
        self.root.mainloop()
       
    # Chamado quando o menu de "Cadastrar" é clicado
    def cadastrarjogo(self):
        self.ctrljogo.cadastrarjogo()

    # Chamado quando o menu de "Avaliar" é clicado
    def avaliarjogo(self):
        self.ctrljogo.avaliarjogo()

    # Chamado quando o menu de "Consultar" é clicado
    def consultar_avaliacoes(self):
        self.ctrljogo.consultar_avaliacoes()

# Ponto de entrada do programa
if __name__ == '__main__':
    c = ControlePrincipal()
