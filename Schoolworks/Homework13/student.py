import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox
import pickle
import os

class Aluno:
    def __init__(self, cpf, nome, email, TipoAula, NomeProf, nAulasSemanal):
        self.__cpf = cpf
        self.__nome = nome
        self.__email = email
        self.__TipoAula = TipoAula
        self.__NomeProf = NomeProf
        self.__nAulasSemanal = nAulasSemanal

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
    def TipoAula(self):
        return self.__TipoAula
    
    @property
    def NomeProf(self):
        return self.__NomeProf
    
    @property
    def nAulasSemanal(self):
        return self.__nAulasSemanal


class ViewCadastraAluno(tk.Toplevel):
    def __init__(self, controle, listaNomesProfissionais):
        tk.Toplevel.__init__(self)
        self.geometry('400x200')
        self.title("Cadastro de Aluno")
        self.controle = controle

        # Configuração dos frames para cada campo
        self.frameNome = tk.Frame(self)
        self.framecpf = tk.Frame(self)
        self.frameEmail = tk.Frame(self)
        self.frameTipoAula = tk.Frame(self)
        self.frameNomeProf = tk.Frame(self)
        self.framenAulasSemanal = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        # Empacota os frames
        self.framecpf.pack()
        self.frameNome.pack()
        self.frameEmail.pack()
        self.frameTipoAula.pack()
        self.frameNomeProf.pack()
        self.framenAulasSemanal.pack()
        self.frameButton.pack()

        # Configuração dos campos e labels
        self.labelcpf = tk.Label(self.framecpf, text="CPF: ")
        self.labelNome = tk.Label(self.frameNome, text="Nome: ")
        self.labelEmail = tk.Label(self.frameEmail, text="Email: ")
        self.labelcpf.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelEmail.pack(side="left")

        self.inputcpf = tk.Entry(self.framecpf, width=20)
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputEmail = tk.Entry(self.frameEmail, width=20)
        self.inputcpf.pack(side="left")
        self.inputNome.pack(side="left")
        self.inputEmail.pack(side="left")

        # ComboBox para Tipo de Aula
        self.labelTipoAula = tk.Label(self.frameTipoAula, text="Tipo de Aula:")
        self.labelTipoAula.pack(side="left")
        self.escolhaTipoAula = tk.StringVar()
        self.comboboxTipoAula = ttk.Combobox(self.frameTipoAula, width=15, textvariable=self.escolhaTipoAula)
        self.comboboxTipoAula['values'] = ['Pilates', 'Funcional']
        self.comboboxTipoAula.pack(side="left")

        # ComboBox para Nome do Professor
        self.labelNomeProf = tk.Label(self.frameNomeProf, text="Nome do Prof:")
        self.labelNomeProf.pack(side="left")
        self.escolhaNomeProf = tk.StringVar()
        self.comboboxProf = ttk.Combobox(self.frameNomeProf, width=15, textvariable=self.escolhaNomeProf)
        self.comboboxProf['values'] = listaNomesProfissionais
        self.comboboxProf.pack(side="left")

        # ComboBox para Número de Aulas Semanais
        self.labelNAulas = tk.Label(self.framenAulasSemanal, text="Nº Aulas Semanais:")
        self.labelNAulas.pack(side="left")
        self.escolhaNAulas = tk.StringVar()
        self.comboboxNAulas = ttk.Combobox(self.framenAulasSemanal, width=15, textvariable=self.escolhaNAulas)
        self.comboboxNAulas['values'] = [2, 3, 4]
        self.comboboxNAulas.pack(side="left")

        # Botões
        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class CtrlAluno:
    def __init__(self, ctrlprofissional):
        self.ctrlprofissional = ctrlprofissional
        self.listaAlunos = []
        self.carregaAlunos()  # Carrega alunos salvos no início

    # Método para carregar alunos salvos
    def carregaAlunos(self):
        if os.path.isfile("alunos.pickle"):
            with open("alunos.pickle", "rb") as f:
                self.listaAlunos = pickle.load(f)

    # Método para salvar alunos no arquivo
    def salvaAlunos(self):
        with open("alunos.pickle", "wb") as f:
            pickle.dump(self.listaAlunos, f)

    def cadastraaluno(self):
        listaNomesProfissionais = self.ctrlprofissional.getNomeProfissionais()
        self.viewInsere = ViewCadastraAluno(self, listaNomesProfissionais)

    def consultaaluno(self):
        try:
            cpf = simpledialog.askstring("Consulta de Aluno", "Digite o CPF do aluno:")
            if not cpf:
                raise ValueError("CPF não informado.")

            aluno = next((al for al in self.listaAlunos if al.cpf == cpf), None)
            if not aluno:
                raise ValueError("Aluno não encontrado.")

            mensagem = (
                f"Aluno: {aluno.nome}\nCPF: {aluno.cpf}\nEmail: {aluno.email}\n"
                f"Tipo de Aula: {aluno.TipoAula}\nProfessor: {aluno.NomeProf}\n"
                f"Nº Aulas Semanais: {aluno.nAulasSemanal}"
            )
            messagebox.showinfo("Dados do Aluno", mensagem)

        except ValueError as e:
            messagebox.showwarning("Erro", str(e))

    def enterHandler(self, event):
        try:
            # Validação dos campos
            cpf = self.viewInsere.inputcpf.get().strip()
            if not cpf.isdigit() or len(cpf) != 11:
                raise ValueError("CPF deve conter 11 dígitos numéricos.")

            nome = self.viewInsere.inputNome.get().strip()
            if not nome:
                raise ValueError("Nome não pode estar vazio.")

            email = self.viewInsere.inputEmail.get().strip()
            if "@" not in email or "." not in email:
                raise ValueError("Email inválido.")

            tipoAula = self.viewInsere.escolhaTipoAula.get().strip()
            if tipoAula not in ['Pilates', 'Funcional']:
                raise ValueError("Tipo de aula inválido.")

            nomeProf = self.viewInsere.escolhaNomeProf.get().strip()
            if not nomeProf:
                raise ValueError("Professor não selecionado.")

            nAulas = int(self.viewInsere.escolhaNAulas.get())
            if nAulas not in [2, 3, 4]:
                raise ValueError("Número de aulas semanais inválido.")

            # Cria e adiciona o aluno
            aluno = Aluno(cpf, nome, email, tipoAula, nomeProf, nAulas)
            self.listaAlunos.append(aluno)
            self.salvaAlunos()  # Salva após cadastro

            self.viewInsere.mostraJanela("Sucesso", "Aluno cadastrado com sucesso")
            self.clearHandler(event)

        except ValueError as e:
            self.viewInsere.mostraJanela("Erro", str(e))

    def clearHandler(self, event):
        self.viewInsere.inputcpf.delete(0, tk.END)
        self.viewInsere.inputNome.delete(0, tk.END)
        self.viewInsere.inputEmail.delete(0, tk.END)
        self.viewInsere.escolhaTipoAula.set("")
        self.viewInsere.escolhaNomeProf.set("")
        self.viewInsere.escolhaNAulas.set("")

    def fechaHandler(self, event):
        self.viewInsere.destroy()
