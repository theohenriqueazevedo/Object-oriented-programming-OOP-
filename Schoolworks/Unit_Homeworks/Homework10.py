import tkinter as tk
from tkinter import messagebox, simpledialog

class ModelCliente:
    def __init__(self, codigo, nome, email):
        self.__codigo = codigo
        self.__nome = nome
        self.__email = email

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

class View:
    def __init__(self, master, controller):
        self.controller = controller
        self.janela = tk.Frame(master)
        self.janela.pack()
        
        self.frame_codigo = tk.Frame(self.janela)
        self.frame_nome = tk.Frame(self.janela)
        self.frame_email = tk.Frame(self.janela)
        self.frame_codigo.pack()
        self.frame_nome.pack()
        self.frame_email.pack()

        # Campos para entrada de código, nome e email
        self.labelCodigo = tk.Label(self.frame_codigo, text="Código: ")
        self.labelNome = tk.Label(self.frame_nome, text="Nome: ")
        self.labelEmail = tk.Label(self.frame_email, text="Email: ")
        
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelEmail.pack(side="left")

        self.inputCodigo = tk.Entry(self.frame_codigo, width=20)
        self.inputNome = tk.Entry(self.frame_nome, width=20)
        self.inputEmail = tk.Entry(self.frame_email, width=20)
        
        self.inputCodigo.pack(side="left")
        self.inputNome.pack(side="left")
        self.inputEmail.pack(side="left")

        # Botões de ação
        self.buttonSubmit = tk.Button(self.janela, text="Salvar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.salvaHandler)

        self.buttonClear = tk.Button(self.janela, text="Limpar")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)

        self.buttonDisplay = tk.Button(self.janela, text="Mostrar")
        self.buttonDisplay.pack(side="left")
        self.buttonDisplay.bind("<Button>", controller.displayHandler)

        self.buttonConsulta = tk.Button(self.janela, text="Consultar por Código")
        self.buttonConsulta.pack(side="left")
        self.buttonConsulta.bind("<Button>", controller.consultaHandler)

    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)
        
class Controller:       
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('400x200')
        self.listaClientes = []
        self.view = View(self.root, self)

        self.root.title("Cadastro de Clientes")
        self.root.mainloop()

    def salvaHandler(self, event):
        codigoCli = self.view.inputCodigo.get()
        nomeCli = self.view.inputNome.get()
        emailCli = self.view.inputEmail.get()

        cliente = ModelCliente(codigoCli, nomeCli, emailCli)
        self.listaClientes.append(cliente)
        self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputCodigo.delete(0, tk.END)
        self.view.inputNome.delete(0, tk.END)
        self.view.inputEmail.delete(0, tk.END)

    def displayHandler(self, event):
        lista_janela = tk.Toplevel(self.root)
        lista_janela.title("Lista de Clientes")
        lista_janela.geometry("300x200")

        listbox_clientes = tk.Listbox(lista_janela, width=40, height=10)
        listbox_clientes.pack(pady=10)

        for cliente in self.listaClientes:
            listbox_clientes.insert(tk.END, f"Código: {cliente.codigo} | Nome: {cliente.nome} | Email: {cliente.email}")

        btn_fechar = tk.Button(lista_janela, text="Fechar", command=lista_janela.destroy)
        btn_fechar.pack(pady=5)

    def consultaHandler(self, event):
        codigo = simpledialog.askstring("Consulta Cliente", "Digite o código do cliente:")

        cliente_encontrado = None
        for cli in self.listaClientes:
            if cli.codigo == codigo:
                cliente_encontrado = cli
                break
            
        if cliente_encontrado:
            self.view.mostraJanela("Cliente Encontrado", f"Nome: {cliente_encontrado.nome}\nEmail: {cliente_encontrado.email}")
        else:
            self.view.mostraJanela("Erro", "Código não cadastrado")

if __name__ == '__main__':
    c = Controller()
