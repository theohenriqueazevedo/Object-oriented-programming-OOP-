import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Album:

    def __init__(self, titulo, ano):
        self.__codigo = titulo
        self.__ano = ano

    @property
    def titulo(self):
        return self.__codigo
    
    @property
    def ano(self):
        return self.__ano




class ViewInsereAlbum(tk.Toplevel):
    def __init__(self, controle, listaCodDiscip, listaNroMatric):

        tk.Toplevel.__init__(self)
        self.geometry('300x250')
        self.title("Album")
        self.controle = controle

        self.frameCodAlbum = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodAlbum.pack()
        self.frameButton.pack()        

        self.labelCodAlbum = tk.Label(self.frameCodAlbum,text="Informe o código da Album: ")
        self.labelCodAlbum.pack(side="left")
        self.inputCodAlbum = tk.Entry(self.frameCodAlbum, width=20)
        self.inputCodAlbum.pack(side="left")

        self.escolhaCombo = tk.StringVar()
        self.combobox.pack(side="left")
        self.combobox['values'] = listaCodDiscip
          
        self.labelEst = tk.Label(self.frameEstudante,text="Escolha o estudante: ")
        self.labelEst.pack(side="left") 
        self.listbox = tk.Listbox(self.frameEstudante)
        self.listbox.pack(side="left")
        for nro in listaNroMatric:
            self.listbox.insert(tk.END, nro)

        self.buttonInsere = tk.Button(self.frameButton ,text="Insere Aluno")           
        self.buttonInsere.pack(side="left")
        self.buttonInsere.bind("<Button>", controle.insereAluno)

        self.buttonCria = tk.Button(self.frameButton ,text="Cria Album")           
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaAlbum)    

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)            

class LimiteMostraAlbums():
    def __init__(self, str):
        messagebox.showinfo('Lista de Albums', str)

class CtrlAlbum():       
    def __init__(self, controlePrincipal):
        self.ctrlPrincipal = controlePrincipal
        self.listaAlbums = []

    def insereAlbums(self):        
        self.listaAlunosAlbum = []
        listaCodDisc = self.ctrlPrincipal.ctrlano.getListaCodanos()
        listaNroMatric = self.ctrlPrincipal.ctrlEstudante.getListaNroMatric()
        self.limiteIns = ViewInsereAlbum(self, listaCodDisc, listaNroMatric)

    def criaAlbum(self, event):
        codAlbum = self.limiteIns.inputCodAlbum.get()
        discSel = self.limiteIns.escolhaCombo.get()
        disc = self.ctrlPrincipal.ctrlano.getano(discSel)
        Album = Album(codAlbum, disc, self.listaAlunosAlbum)
        self.listaAlbums.append(Album)
        self.limiteIns.mostraJanela('Sucesso', 'Album criada com sucesso')
        self.limiteIns.destroy()

    def insereAluno(self, event):
        alunoSel = self.limiteIns.listbox.get(tk.ACTIVE)
        aluno = self.ctrlPrincipal.ctrlEstudante.getEstudante(alunoSel)
        self.listaAlunosAlbum.append(aluno)
        self.limiteIns.mostraJanela('Sucesso', 'Aluno matriculado')
        self.limiteIns.listbox.delete(tk.ACTIVE)
        
    def mostraAlbums(self):
        str = ''
        for Album in self.listaAlbums:
            str += 'Código: ' + Album.titulo + '\n'
            str += 'ano: ' + Album.ano.titulo + '\n'
            str += ':\n'
            for estud in Album:
                str += estud.nroMatric + ' - ' + estud.nome + '\n'
            str += '--------\n'

        self.limiteLista = LimiteMostraAlbums(str)


    