import tkinter as tk
from tkinter import messagebox
import os.path 
import pickle

# Classe que representa o Estudante com informações de matrícula e nome
class Estudante:
    def __init__(self, nroMatric, nome):
        self.__nroMatric = nroMatric  
        self.__nome = nome 

    @property
    def nroMatric(self):
        return self.__nroMatric 
    
    @property
    def nome(self):
        return self.__nome 

# Classe para a interface gráfica de cadastro de estudantes
class ViewInsereEstudante(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Estudante")  # Título da janela
        self.controle = controle  # Controle responsável pela lógica de cadastro

        # Definição dos frames para organizar os widgets
        self.frameNro = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        # Adiciona os frames na janela
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameButton.pack()

        # Definindo os rótulos e os campos de entrada (Entry)
        self.labelNro = tk.Label(self.frameNro, text="Nro Matrícula: ")
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")

        # Campos para entrada de matrícula e nome
        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")

        # Definindo os botões e suas ações
        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    # Função para exibir mensagens para o usuário
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

# Classe para mostrar a lista de estudantes cadastrados
class ViewMostraEstudante():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)  # Exibe a lista em uma janela de mensagem

# Classe que controla o cadastro e consulta dos estudantes
class CtrlEstudante():
    def __init__(self):
        # Verifica se o arquivo de dados dos estudantes já existe
        if not os.path.isfile("estudante.pickle"):
            self.listaEstudantes = []  # Se não existir, cria uma lista vazia
        else:
            # Caso o arquivo exista, carrega os dados dos estudantes
            with open("estudante.pickle", "rb") as f:
                self.listaEstudantes = pickle.load(f)

    # Método para salvar os dados dos estudantes no arquivo
    def salvaEstudantes(self):
        if len(self.listaEstudantes) != 0:
            with open("estudante.pickle", "wb") as f:
                pickle.dump(self.listaEstudantes, f)

    # Método para obter um estudante pela matrícula
    def getEstudante(self, nroMatric):
        estRet = None
        for est in self.listaEstudantes:
            if est.nroMatric == nroMatric:
                estRet = est
        return estRet

    # Método para retornar uma lista com os números de matrícula dos estudantes
    def getListaNroMatric(self):
        listaNro = []
        for est in self.listaEstudantes:
            listaNro.append(est.nroMatric)
        return listaNro

    # Método para abrir a janela de cadastro de estudantes
    def insereEstudantes(self):
        self.limiteIns = ViewInsereEstudante(self)

    # Método para mostrar os estudantes cadastrados
    def mostraEstudantes(self):
        str = 'Nro Matric. -- Nome\n'
        for est in self.listaEstudantes:
            str += est.nroMatric + ' -- ' + est.nome + '\n'
        self.limiteLista = ViewMostraEstudante(str)

    # Método que trata o evento de pressionar o botão "Enter" para cadastrar o estudante
    def enterHandler(self, event):
        try:
            nroMatric = self.limiteIns.inputNro.get()  # Obtém a matrícula
            nome = self.limiteIns.inputNome.get()  # Obtém o nome

            # Valida a matrícula e o nome
            if not nroMatric or not nome:
                raise ValueError("Matrícula e Nome são obrigatórios.")
            
            # Cria um novo estudante e adiciona à lista
            estudante = Estudante(nroMatric, nome)
            self.listaEstudantes.append(estudante)

            # Exibe a mensagem de sucesso
            self.limiteIns.mostraJanela('Sucesso', 'Estudante cadastrado com sucesso')
            self.clearHandler(event)

        except ValueError as e:
            # Exibe a mensagem de erro caso algum dado seja inválido
            self.limiteIns.mostraJanela('Erro', str(e))

    # Método para limpar os campos após o cadastro
    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, tk.END)
        self.limiteIns.inputNome.delete(0, tk.END)

    # Método para fechar a janela de cadastro de estudante
    def fechaHandler(self, event):
        self.limiteIns.destroy()
