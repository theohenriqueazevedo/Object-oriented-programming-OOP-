import tkinter as tk
import profissional as profi
import aluno as aluno

class ViewPrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')  # Define o tamanho da janela principal
        self.menubar = tk.Menu(self.root)  # Cria uma barra de menu

        # Menu de opções para Profissional
        self.profissionalMenu = tk.Menu(self.menubar)
        self.profissionalMenu.add_command(label="Cadastra", command=self.controle.cadastraprofissionais)
        self.profissionalMenu.add_command(label="Lista", command=self.controle.listaprofissionais)
        self.profissionalMenu.add_command(label="Faturamento", command=self.controle.faturamentoprofissional)
        self.menubar.add_cascade(label="Profissional", menu=self.profissionalMenu)

        # Menu de opções para Aluno
        self.alunoMenu = tk.Menu(self.menubar)
        self.alunoMenu.add_command(label="Cadastra", command=self.controle.cadastraaluno)
        self.alunoMenu.add_command(label="Consulta", command=self.controle.consultaaluno)
        self.menubar.add_cascade(label="Aluno", menu=self.alunoMenu)

        self.root.config(menu=self.menubar)  # Adiciona a barra de menu à janela principal

class ControlePrincipal:
    def __init__(self):
        self.root = tk.Tk()

        # Instanciando CtrlAluno primeiro
        # Inicializa o controlador de aluno sem dependências no início
        self.ctrlaluno = aluno.CtrlAluno(None)

        # Instanciando CtrlProfissional depois de CtrlAluno
        # Inicializa o controlador de profissional e passa CtrlAluno como dependência
        self.ctrlprofissional = profi.CtrlProfissional(self.ctrlaluno)

        # Passando CtrlProfissional para CtrlAluno após ter sido instanciado
        # Agora CtrlAluno tem acesso a CtrlProfissional, formando a relação bidirecional
        self.ctrlaluno.ctrlprofissional = self.ctrlprofissional

        # Cria a interface gráfica principal
        self.limite = ViewPrincipal(self.root, self)

        self.root.title("Sistema Estudio")  # Define o título da janela
        self.root.mainloop()  # Inicia o loop principal da interface gráfica

    # Métodos para delegar ações de menu ao respectivo controlador
    def cadastraprofissionais(self):
        self.ctrlprofissional.cadastraprofissionais()

    def listaprofissionais(self):
        self.ctrlprofissional.listaprofissionais()

    def faturamentoprofissional(self): 
        self.ctrlprofissional.faturamentoprofissional()

    def cadastraaluno(self):
        self.ctrlaluno.cadastraaluno()

    def consultaaluno(self):
        self.ctrlaluno.consultaaluno()

# Ponto de entrada da aplicação
if __name__ == '__main__':
    c = ControlePrincipal()
