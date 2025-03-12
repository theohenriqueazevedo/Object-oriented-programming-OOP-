import tkinter as tk
from tkinter import messagebox

class Musica:

    def __init__(self, titulo, nroFaixa):
        self.__titulo = titulo
        self.__nroFaixa = nroFaixa

    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def nroFaixa(self):
        return self.__nroFaixa

class VieewInsereMusica(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Musica")
        self.controle = controle

        self.framenroFaixa = tk.Frame(self)
        self.frametitulo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frametitulo.pack()
        self.framenroFaixa.pack()
        self.frameButton.pack()
      
        self.labeltitulo = tk.Label(self.frametitulo,text="Código: ")
        self.labelnroFaixa = tk.Label(self.framenroFaixa,text="nroFaixa: ")
        self.labeltitulo.pack(side="left")
        self.labelnroFaixa.pack(side="left")  

        self.inputtitulo = tk.Entry(self.frametitulo, width=20)
        self.inputtitulo.pack(side="left")
        self.inputnroFaixa = tk.Entry(self.framenroFaixa, width=20)
        self.inputnroFaixa.pack(side="left")             
      
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

class LimiteMostraMusicas():
    def __init__(self, str):
        messagebox.showinfo('Lista de Musicas', str)

      
class CtrlMusica():       
    def __init__(self):
        self.listaMusicas = [
            Musica('XDES02', 'Programação OO'),
            Musica('XDES03', 'Programação Web'),
            Musica('XMAC02', 'Métodos Matemáticos')
        ]

    def getListaMusicas(self):
        return self.listaMusicas

    def getMusica(self, codDisc):
        discRet = None
        for disc in self.listaMusicas:
            if disc.titulo == codDisc:
                discRet = disc
        return discRet

    def getListaCodMusicas(self):
        listaCod = []
        for disc in self.listaMusicas:
            listaCod.append(disc.titulo)
        return listaCod

    def insereMusicas(self):
        self.limiteIns = VieewInsereMusica(self) 

    def mostraMusicas(self):
        str = 'Código -- nroFaixa\n'
        for disc in self.listaMusicas:
            str += disc.titulo + ' -- ' + disc.nroFaixa + '\n'
        self.limiteLista = LimiteMostraMusicas(str)

    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputtitulo.get()
        nroFaixa = self.limiteIns.inputnroFaixa.get()
        Musica = Musica(nroMatric, nroFaixa)
        self.listaMusicas.append(Musica)
        self.limiteIns.mostraJanela('Sucesso', 'Musica cadastrada com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputtitulo.delete(0, len(self.limiteIns.inputtitulo.get()))
        self.limiteIns.inputnroFaixa.delete(0, len(self.limiteIns.inputnroFaixa.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()
    