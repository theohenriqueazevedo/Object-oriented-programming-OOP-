import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle
import os

# Classe que representa um profissional com atributos básicos
class Profissional:
    def __init__(self, cpf, nome, email, ValorAuPila, ValorAuFunc):
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__ValorAuPila = float(ValorAuPila) # Valor da aula de Pilates
        self.__ValorAuFunc = float(ValorAuFunc) # Valor da aula Funcional

    # Getters para acessar os atributos do profissional
    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def email(self):
        return self.__email

    @property
    def ValorAuPila(self):
        return self.__ValorAuPila

    @property
    def ValorAuFunc(self):
        return self.__ValorAuFunc

# Interface gráfica para cadastrar um profissional
class ViewCadastraProfi(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x150') # Define o tamanho da janela
        self.title("Profissional") # Define o título da janela
        self.controle = controle

        # Frames para organizar os campos de entrada
        self.frameNome = tk.Frame(self)
        self.framecpf = tk.Frame(self)
        self.frameEmail = tk.Frame(self)
        self.frameValorAuPila = tk.Frame(self)
        self.frameValorAuFunc = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.framecpf.pack()
        self.frameNome.pack()
        self.frameEmail.pack()
        self.frameValorAuFunc.pack()
        self.frameValorAuPila.pack()
        self.frameButton.pack()

        # Labels e campos de entrada
        self.labelcpf = tk.Label(self.framecpf, text="CPF: ")
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelEmail = tk.Label(self.frameEmail, text="Email: ")
        self.labelValorAuPila = tk.Label(self.frameValorAuPila, text="Valor Aula Pilates: ")
        self.labelValorAuFunc = tk.Label(self.frameValorAuFunc, text="Valor Aula Funcional: ")
        self.labelcpf.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelEmail.pack(side="left")
        self.labelValorAuPila.pack(side="left")
        self.labelValorAuFunc.pack(side="left")

         # Campos de entrada de texto
        self.inputcpf = tk.Entry(self.framecpf, width=20)
        self.inputcpf.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")
        self.inputEmail = tk.Entry(self.frameEmail, width=20)
        self.inputEmail.pack(side="left")
        self.inputValorAuPila = tk.Entry(self.frameValorAuPila, width=20)
        self.inputValorAuPila.pack(side="left")
        self.inputValorAuFunc = tk.Entry(self.frameValorAuFunc, width=20)
        self.inputValorAuFunc.pack(side="left")

        # Botões para ações
        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    # Método para exibir mensagens na interface
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


# Interface para exibir uma lista de profissionais cadastrados
class LimiteMostraProfissionals:
    def __init__(self, str):
        messagebox.showinfo('Lista de Profissionais', str)


# Controlador responsável por gerenciar profissionais
class CtrlProfissional:
    def __init__(self, ctrlaluno):
        self.ctrlaluno = ctrlaluno  # Referência ao controlador de alunos
        self.listaProfissionais = [] # Lista para armazenar os profissionais
        self.carregaProfissionais()  # Carrega dados ao iniciar

    # Persistência: Carrega dados do arquivo
    def carregaProfissionais(self):
        if os.path.isfile("profissionais.pickle"):
            with open("profissionais.pickle", "rb") as f:
                self.listaProfissionais = pickle.load(f)


    # Persistência: Salva dados no arquivo
    def salvaProfissionais(self):
        with open("profissionais.pickle", "wb") as f:
            pickle.dump(self.listaProfissionais, f)


     # Retorna uma lista com os nomes dos profissionais cadastrados
    def getNomeProfissionais(self):
        return [profi.nome for profi in self.listaProfissionais]

    # Abre a interface para cadastrar um novo profissional
    def cadastraprofissionais(self):
        self.viewInsere = ViewCadastraProfi(self)

     # Lista todos os profissionais cadastrados
    def listaprofissionais(self):
        if not self.listaProfissionais:
            messagebox.showinfo("Lista Vazia", "Nenhum profissional cadastrado.")
            return
        str = 'CPF -- Nome -- E-mail -- Valor Aula Pila -- Valor Aula Func\n'
        for profi in self.listaProfissionais:
            str += f"{profi.cpf} -- {profi.nome} -- {profi.email} -- R${profi.ValorAuPila:.2f} -- R${profi.ValorAuFunc:.2f}\n"
        LimiteMostraProfissionals(str)


    # Manipulador para salvar um novo profissional
    def enterHandler(self, event):
        try:
            # Validações de entrada
            cpf = self.viewInsere.inputcpf.get().strip()
            if not cpf.isdigit() or len(cpf) != 11:
                raise ValueError("CPF deve conter 11 dígitos numéricos.")

            nome = self.viewInsere.inputNome.get().strip()
            if not nome:
                raise ValueError("O nome não pode estar vazio.")

            email = self.viewInsere.inputEmail.get().strip()
            if "@" not in email or "." not in email:
                raise ValueError("Email inválido.")

            valor1 = self.viewInsere.inputValorAuFunc.get().strip()
            valor2 = self.viewInsere.inputValorAuPila.get().strip()
            try:
                valor1 = float(valor1)
                valor2 = float(valor2)
                if valor1 <= 0 or valor2 <= 0:
                    raise ValueError("Os valores das aulas devem ser positivos.")
            except ValueError:
                raise ValueError("Valores das aulas devem ser números válidos.")

            # Cria e adiciona o profissional à lista
            profissional = Profissional(cpf, nome, email, valor2, valor1)
            self.listaProfissionais.append(profissional)
            self.salvaProfissionais()  # Salva após cadastro

            # Exibe mensagem de sucesso
            self.viewInsere.mostraJanela('Sucesso', 'Profissional cadastrado com sucesso')
            self.clearHandler(event)

        except ValueError as e:
            self.viewInsere.mostraJanela("Erro", str(e))

    #Limpa os campos de entrada na interface
    def clearHandler(self, event):
        self.viewInsere.inputcpf.delete(0, tk.END)
        self.viewInsere.inputNome.delete(0, tk.END)
        self.viewInsere.inputEmail.delete(0, tk.END)
        self.viewInsere.inputValorAuPila.delete(0, tk.END)
        self.viewInsere.inputValorAuFunc.delete(0, tk.END)


    # Calcula o faturamento de um profissional com base nos alunos
    def faturamentoprofissional(self):
        try:
            cpf = simpledialog.askstring("Faturamento", "Digite o CPF do profissional:")
            if not cpf:
                raise ValueError("CPF não informado.")

            profissional = next((profi for profi in self.listaProfissionais if profi.cpf == cpf), None)
            if not profissional:
                raise ValueError(f"Profissional com CPF {cpf} não encontrado.")

            valor_pilates = 0
            valor_funcional = 0
            for aluno in self.ctrlaluno.listaAlunos:
                if aluno.NomeProf == profissional.nome:
                    custo_base = profissional.ValorAuPila if aluno.TipoAula == "Pilates" else profissional.ValorAuFunc
                    if aluno.nAulasSemanal == 3:
                        custo_base *= 1.4
                    elif aluno.nAulasSemanal == 4:
                        custo_base *= 1.8

                    if aluno.TipoAula == "Pilates":
                        valor_pilates += custo_base
                    else:
                        valor_funcional += custo_base

            mensagem = (
                f"Faturamento do profissional: {profissional.nome}\n"
                f"Valor Pilates: R${valor_pilates:.2f}\n"
                f"Valor Funcional: R${valor_funcional:.2f}"
            )
            messagebox.showinfo("Faturamento", mensagem)

        except ValueError as e:
            messagebox.showwarning("Erro", str(e))

    def fechaHandler(self, event):
        self.viewInsere.destroy()
