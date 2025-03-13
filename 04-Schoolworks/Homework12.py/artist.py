import tkinter as tk
from tkinter import messagebox

class Artista:

    def __init__(self, nome):
        self.__nome = nome
    
    @property
    def nome(self):
        return self.__nome

class ViewInsereArtista(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Artista")
        self.controle = controle

        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNome.pack()
        self.frameButton.pack()
        
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNome.pack(side="left")  
     
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")             
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class ViewMostraArtista():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)

      
class CtrlArtista():       
    def __init__(self):
        self.listaArtistas = [
            Artista( 'Joao Santos'),
            Artista('Marina Cintra'),
            Artista( 'Felipe Reis'),
            Artista('Ana Souza')
        ]

    def getArtista(self, ):
        artista = None
        for artista in self.listaArtistas:
            if artista == self.listaArtistas:
                artistaValido = artista
        return artistaValido

    def insereArtistas(self):
        self.limiteIns = ViewInsereArtista(self) 

    def mostraArtistas(self):
        str = '--Nome--\n'
        for artista in self.listaArtistas:
            str += artista.nome + '\n'       
        self.limiteLista = ViewMostraArtista(str)

    def enterHandler(self, event):
        nome = self.limiteIns.inputNome.get()
        Artista = Artista(nome)
        self.listaArtistas.append(Artista)
        self.limiteIns.mostraJanela('Sucesso', 'Artista cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.dartistaroy()
    