import tkinter as tk
from tkinter import messagebox
import estudante as est 
import disciplina as disc
import turma as trm

# Classe responsável por definir a interface principal do programa
class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')  # Define o tamanho da janela principal

        # Criação do menu principal e submenus
        self.menubar = tk.Menu(self.root)
        self.estudanteMenu = tk.Menu(self.menubar)
        self.discipMenu = tk.Menu(self.menubar)
        self.turmaMenu = tk.Menu(self.menubar)
        self.sairMenu = tk.Menu(self.menubar)

        # Configuração do menu de Estudantes
        self.estudanteMenu.add_command(label="Insere", \
                    command=self.controle.insereEstudantes)  # Opção para inserir estudantes
        self.estudanteMenu.add_command(label="Mostra", \
                    command=self.controle.mostraEstudantes)  # Opção para mostrar estudantes
        self.menubar.add_cascade(label="Estudante", \
                    menu=self.estudanteMenu)

        # Configuração do menu de Disciplinas
        self.discipMenu.add_command(label="Insere", \
                    command=self.controle.insereDisciplinas)  # Opção para inserir disciplinas
        self.discipMenu.add_command(label="Mostra", \
                    command=self.controle.mostraDisciplinas)  # Opção para mostrar disciplinas
        self.menubar.add_cascade(label="Disciplina", \
                    menu=self.discipMenu)

        # Configuração do menu de Turmas
        self.turmaMenu.add_command(label="Insere", \
                    command=self.controle.insereTurmas)  # Opção para inserir turmas
        self.turmaMenu.add_command(label="Mostra", \
                    command=self.controle.mostraTurmas)  # Opção para mostrar turmas
        self.menubar.add_cascade(label="Turma", \
                    menu=self.turmaMenu)

        # Configuração do menu de Sair
        self.sairMenu.add_command(label="Salva", \
                    command=self.controle.salvaDados)  # Opção para salvar os dados e sair
        self.menubar.add_cascade(label="Sair", \
                    menu=self.sairMenu)

        # Aplica o menu configurado à janela principal
        self.root.config(menu=self.menubar)

# Classe que gerencia as ações do programa e suas interações com os controles
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()  # Cria a janela principal

        # Inicializa os controladores de estudante, disciplina e turma
        self.ctrlEstudante = est.CtrlEstudante()  # Gerencia dados e ações relacionadas a estudantes
        self.ctrlDisciplina = disc.CtrlDisciplina()  # Gerencia dados e ações relacionadas a disciplinas
        self.ctrlTurma = trm.CtrlTurma(self)  # Gerencia dados e ações relacionadas a turmas

        # Cria a interface principal
        self.limite = LimitePrincipal(self.root, self)

        # Define o título da janela principal
        self.root.title("Exemplo MVC")
        # Inicia o loop principal do Tkinter
        self.root.mainloop()

    # Métodos para chamar as ações dos controladores específicos
    def insereEstudantes(self):
        self.ctrlEstudante.insereEstudantes()

    def mostraEstudantes(self):
        self.ctrlEstudante.mostraEstudantes()

    def insereDisciplinas(self):
        self.ctrlDisciplina.insereDisciplinas()

    def mostraDisciplinas(self):
        self.ctrlDisciplina.mostraDisciplinas()

    def insereTurmas(self):
        self.ctrlTurma.insereTurmas()

    def mostraTurmas(self):
        self.ctrlTurma.mostraTurmas()

    def salvaDados(self):
        # Salva os dados de estudantes, disciplinas e turmas
        self.ctrlEstudante.salvaEstudantes()
        self.ctrlDisciplina.salvaDisciplinas()
        self.ctrlTurma.salvaTurmas()
        # Fecha a aplicação
        self.root.destroy()

# Ponto de entrada do programa
if __name__ == '__main__':
    c = ControlePrincipal()
