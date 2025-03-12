import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox

class Vinho:
    def __init__(self, codigo, nome, console, genero, preco):
        self.__codigo = codigo
        self.__nome = nome
        self.__console = console
        self.__genero = genero
        self.__preco = preco
        self.__avaliacoes = []

    @property
    def codigo(self):
        return self.__codigo
   
    @property
    def nome(self):
        return self.__nome

    @property
    def console(self):
        return self.__console
    
    @property
    def genero(self):
        return self.__genero
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def avaliacoes(self):
        return self.__avaliacoes

    def adicionar_avaliacao(self, avaliacao):
        if 1 <= avaliacao <= 5:
            self.__avaliacoes.append(avaliacao)
        else:
            raise ValueError("A avaliação deve ser um número entre 1 e 5.")

    def calcular_media_avaliacao(self):
        if not self.__avaliacoes:
            return None  # Sem avaliações
        return sum(self.__avaliacoes) / len(self.__avaliacoes)
    

    
class ViewCadastraVinho(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x150')
        self.title("Vinho")
        self.controle = controle

        self.framenome = tk.Frame(self)
        self.framecodigo = tk.Frame(self)
        self.frameconsole = tk.Frame(self)
        self.framegenero = tk.Frame(self)
        self.framepreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framecodigo.pack()
        self.framenome.pack()
        self.frameconsole.pack()
        self.framepreco.pack()
        self.framegenero.pack()
        self.frameButton.pack()

        self.labelcodigo = tk.Label(self.framecodigo, text="Codigo: ")
        self.labelnome = tk.Label(self.framenome, text="nome: ")
        self.labelPreco = tk.Label(self.framepreco, text="Escolha Preço: ")
        self.labelcodigo.pack(side="left")
        self.labelnome.pack(side="left")
        self.labelPreco.pack(side="left")

        self.inputcodigo = tk.Entry(self.framecodigo, width=20)
        self.inputcodigo.pack(side="left")
        self.inputnome = tk.Entry(self.framenome, width=20)
        self.inputnome.pack(side="left")
        self.inputpreco = tk.Entry(self.framepreco, width=20)
        self.inputpreco.pack(side="left")

        self.labelConsole = tk.Label(self.frameconsole, text="Escolha Console: ")
        self.labelConsole.pack(side="left")
        self.escolhaconsole = tk.StringVar()
        self.comboboxconsole = ttk.Combobox(self.frameconsole, width=15, textvariable=self.escolhaconsole)
        self.comboboxconsole.pack(side="left")
        self.comboboxconsole['values'] = ['Xbox', 'PlayStation', 'Switch', 'PC'] 

        self.labelGenero = tk.Label(self.framegenero, text="Escolha Gênero: ")
        self.labelGenero.pack(side="left")
        self.escolhagenero = tk.StringVar()
        self.comboboxgenero = ttk.Combobox(self.framegenero, width=15, textvariable=self.escolhagenero)
        self.comboboxgenero.pack(side="left")
        self.comboboxgenero['values'] = ['Ação', 'Aventura', 'Estrategia', 'RPG', 'Simulação']

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, nome, msg):
        messagebox.showinfo(nome, msg)

class LimiteMostraVinhos():
    def __init__(self, str):
        messagebox.showinfo('Lista de Profissionais', str)

class ViewAvaliarVinho(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x150')
        self.title("Avaliar Vinho")
        self.controle = controle

        self.framecodigo = tk.Frame(self)
        self.frameavaliacao = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framecodigo.pack()
        self.frameavaliacao.pack()
        self.frameButton.pack()

        self.labelcodigo = tk.Label(self.framecodigo, text="Código: ")
        self.labelcodigo.pack(side="left")

        self.inputcodigo = tk.Entry(self.framecodigo, width=20)
        self.inputcodigo.pack(side="left")

        self.labelavaliacao = tk.Label(self.frameavaliacao, text="Escolha a quantidade de estrelas: ")
        self.labelavaliacao.pack(side="left")
        self.escolhaavaliacao = tk.StringVar()
        self.comboboxavaliacao = ttk.Combobox(self.frameavaliacao, width=15, textvariable=self.escolhaavaliacao)
        self.comboboxavaliacao.pack(side="left")
        self.comboboxavaliacao['values'] = [1, 2, 3, 4, 5]

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enteravaliacao)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearavaliacao)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaavaliacao)

    def mostraJanela(self, nome, msg):
        messagebox.showinfo(nome, msg)


class ViewConsultaAvaliacoes(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('300x200')
        self.title("Consulta por Avaliação")
        self.controle = controle

        self.labelEstrelas = tk.Label(self, text="Selecione a avaliação (estrelas):")
        self.labelEstrelas.pack()

        self.escolhaEstrelas = tk.StringVar()
        self.comboEstrelas = ttk.Combobox(self, textvariable=self.escolhaEstrelas, state="readonly")
        self.comboEstrelas['values'] = ['1 estrela', '2 estrelas', '3 estrelas', '4 estrelas', '5 estrelas']
        self.comboEstrelas.pack()

        self.botaoConsultar = tk.Button(self, text="Consultar", command=self.consultar_Vinhos)
        self.botaoConsultar.pack()

    def consultar_Vinhos(self):
        estrelas_selecionadas = self.comboEstrelas.get()
        if not estrelas_selecionadas:
            messagebox.showwarning("Erro", "Selecione uma quantidade de estrelas.")
            return

        # Obtém o número de estrelas selecionado
        estrelas = int(estrelas_selecionadas.split()[0])
        Vinhos_filtrados = self.controle.filtrar_Vinhos_por_avaliacao(estrelas)

        if Vinhos_filtrados:
            mensagem = "Vinhos com avaliação de {} estrela(s):\n\n".format(estrelas)
            for Vinho in Vinhos_filtrados:
                mensagem += f"{Vinho.codigo} - {Vinho.nome} ({Vinho.console})\n"
            messagebox.showinfo("Vinhos Encontrados", mensagem)
        else:
            messagebox.showinfo("Vinhos Não Encontrados", "Nenhum Vinho encontrado com esta avaliação.")


class CtrlVinho():
    def __init__(self):
        self.listaVinhos = []
        self.listaavaliacao = []

    def cadastrarVinho(self):
        self.viewInsere = ViewCadastraVinho(self)

    def consultar_avaliacoes(self):
        self.viewConsulta = ViewConsultaAvaliacoes(self)

    def filtrar_Vinhos_por_avaliacao(self, estrelas):
        Vinhos_filtrados = []
        for Vinho in self.listaVinhos:
            media = Vinho.calcular_media_avaliacao()
            if media is not None:
                if 0 < media <= 1 and estrelas == 1:
                    Vinhos_filtrados.append(Vinho)
                elif 1 < media <= 2 and estrelas == 2:
                    Vinhos_filtrados.append(Vinho)
                elif 2 < media <= 3 and estrelas == 3:
                    Vinhos_filtrados.append(Vinho)
                elif 3 < media <= 4 and estrelas == 4:
                    Vinhos_filtrados.append(Vinho)
                elif 4 < media <= 5 and estrelas == 5:
                    Vinhos_filtrados.append(Vinho)
        return Vinhos_filtrados

    def avaliarVinho(self):
        self.viewavaliar = ViewAvaliarVinho(self)

    def enterHandler(self, event):
        try:
            # Validações de entrada
            codigo = self.viewInsere.inputcodigo.get().strip()
            if not codigo:
                raise ValueError("O código não pode estar vazio.")

            nome = self.viewInsere.inputnome.get().strip()
            if not nome:
                raise ValueError("O título não pode estar vazio.")

            console = self.viewInsere.escolhaconsole.get().strip()
            if console not in ['Xbox', 'PlayStation', 'Switch', 'PC']:
                raise ValueError("O console selecionado é inválido.")

            genero = self.viewInsere.escolhagenero.get().strip()
            if genero not in ['Ação', 'Aventura', 'Estrategia', 'RPG', 'Simulação']:
                raise ValueError("O gênero selecionado é inválido.")

            preco_str = self.viewInsere.inputpreco.get().strip()
            try:
                preco = float(preco_str)
                if preco <= 0 or preco > 500:
                    raise ValueError
            except ValueError:
                raise ValueError("O preço deve ser um número maior que zero e menor ou igual a 500.")

            # Cria o objeto Vinho e adiciona à lista
            Vinho = Vinho(codigo, nome, console, genero, preco)
            self.listaVinhos.append(Vinho)

            # Exibe mensagem de sucesso
            self.viewInsere.mostraJanela("Sucesso", "Vinho cadastrado com sucesso")
            self.clearHandler(event)

        except ValueError as e:
            # Exibe mensagem de erro
            self.viewInsere.mostraJanela("Erro", str(e))

    def clearHandler(self, event):
    # Limpa os campos de entrada de texto e combobox
        self.viewInsere.inputcodigo.delete(0, tk.END)
        self.viewInsere.inputnome.delete(0, tk.END)
        self.viewInsere.inputpreco.delete(0, tk.END)
        self.viewInsere.escolhagenero.set("") 
        self.viewInsere.escolhaconsole.set("")  

    def fechaHandler(self, event):
        # Fecha a janela de cadastro de Vinho
        self.viewInsere.destroy()


    def enteravaliacao(self, event):
        try:
            codigo = self.viewavaliar.inputcodigo.get().strip()
            if not codigo:
                raise ValueError("O código do Vinho não pode estar vazio.")
            
            avaliacao = self.viewavaliar.escolhaavaliacao.get()
            if not avaliacao:
                raise ValueError("Selecione uma quantidade de estrelas.")

            avaliacao = int(avaliacao)  # Converte a avaliação para inteiro
            if not (1 <= avaliacao <= 5):
                raise ValueError("A avaliação deve ser um número entre 1 e 5.")

            # Busca o Vinho pelo código
            Vinho = next((j for j in self.listaVinhos if j.codigo == codigo), None)
            if not Vinho:
                raise ValueError("Vinho não encontrado para o código fornecido.")

            # Adiciona a avaliação ao Vinho
            Vinho.adicionar_avaliacao(avaliacao)

            self.viewavaliar.mostraJanela("Sucesso", f"Avaliação de {avaliacao} estrela(s) adicionada ao Vinho {Vinho.nome}.")
            self.clearavaliacao(event)

        except ValueError as e:
            self.viewavaliar.mostraJanela("Erro", str(e))
        
    def clearavaliacao(self, event):
        self.viewavaliar.inputcodigo.delete(0, tk.END)
        self.viewavaliar.escolhaavaliacao.set("")

    def fechaavaliacao(self, event):
        # Fecha a janela de cadastro de Vinho
        self.viewavaliar.destroy()