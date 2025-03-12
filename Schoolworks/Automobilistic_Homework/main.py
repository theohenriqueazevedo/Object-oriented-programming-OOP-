import tkinter as tk
from tkinter import messagebox
import automovel as automovel

class ViewPrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x200')
        self.menubar = tk.Menu(self.root)  
        self.automovelMenu = tk.Menu(self.menubar)   

        self.automovelMenu.add_command(label="Cadastrar", \
                    command=self.controle.cadastrar_automovel)     
        self.menubar.add_cascade(label="Automóvel", \
                    menu=self.automovelMenu)           
        self.automovelMenu.add_command(label="Consultar", \
                    command=self.controle.consultar_automovel)


        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlautomovel = automovel.CtrlAutomovel()

        self.limite = ViewPrincipal(self.root, self) 

        self.root.title("Sistema de automoveis")
        # Inicia o mainloop
        self.root.mainloop()
       
    def cadastrar_automovel(self):
        self.ctrlautomovel.cadastrar_automovel()

    def consultar_automovel(self):
        self.ctrlautomovel.consultar_automovel()

if __name__ == '__main__':
    c = ControlePrincipal()