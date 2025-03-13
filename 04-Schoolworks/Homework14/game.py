import tkinter as tk
import tkinter as ttk
from tkinter import messagebox
import pickle  # Importando o módulo pickle para persistência de dados

class Jogo:
    def __init__(self, codigo, titulo, console, genero, preco):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__console = console
        self.__genero = genero
        self.__preco = preco
        self.__avaliacoes = []  # Lista para armazenar avaliações do jogo

    @property
    def codigo(self):
        return self.__codigo
   
    @property
    def titulo(self):
        return self.__titulo

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

    # Método para adicionar avaliação ao jogo
    def adicionar_avaliacao(self, avaliacao):
        if 1 <= avaliacao <= 5:
            self.__avaliacoes.append(avaliacao)
        else:
            raise ValueError("A avaliação deve ser um número entre 1 e 5.")

    # Método para calcular a média das avaliações
    def calcular_media_avaliacao(self):
        if not self.__avaliacoes:
            return None  # Se não houver avaliações, retorna None
        return sum(self.__avaliacoes) / len(self.__avaliacoes)
    

class ViewCadastraJogo(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x150')
        self.title("Cadastro de Jogo")
        self.controle = controle

        # Definindo os frames para organizar os widgets na tela
        self.frametitulo = tk.Frame(self)
        self.framecodigo = tk.Frame(self)
        self.frameconsole = tk.Frame(self)
        self.framegenero = tk.Frame(self)
        self.framepreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)

        self.framecodigo.pack()
        self.frametitulo.pack()
        self.frameconsole.pack()
        self.framepreco.pack()
        self.framegenero.pack()
        self.frameButton.pack()

        # Rótulos para os campos de entrada
        self.labelcodigo = tk.Label(self.framecodigo, text="Código: ")
        self.labeltitulo = tk.Label(self.frametitulo, text="Título: ")
        self.labelPreco = tk.Label(self.framepreco, text="Preço: ")
        self.labelcodigo.pack(side="left")
        self.labeltitulo.pack(side="left")
        self.labelPreco.pack(side="left")

        # Campos de entrada
        self.inputcodigo = tk.Entry(self.framecodigo, width=20)
        self.inputcodigo.pack(side="left")
        self.inputtitulo = tk.Entry(self.frametitulo, width=20)
        self.inputtitulo.pack(side="left")
        self.inputpreco = tk.Entry(self.framepreco, width=20)
        self.inputpreco.pack(side="left")

        # ComboBox para escolha do console
        self.labelConsole = tk.Label(self.frameconsole, text="Escolha Console: ")
        self.labelConsole.pack(side="left")
        self.escolhaconsole = tk.StringVar()
        self.comboboxconsole = ttk.Combobox(self.frameconsole, width=15, textvariable=self.escolhaconsole)
        self.comboboxconsole.pack(side="left")
        self.comboboxconsole['values'] = ['Xbox', 'PlayStation', 'Switch', 'PC']

        # ComboBox para escolha do gênero
        self.labelGenero = tk.Label(self.framegenero, text="Escolha Gênero: ")
        self.labelGenero.pack(side="left")
        self.escolhagenero = tk.StringVar()
        self.comboboxgenero = ttk.Combobox(self.framegenero, width=15, textvariable=self.escolhagenero)
        self.comboboxgenero.pack(side="left")
        self.comboboxgenero['values'] = ['Ação', 'Aventura', 'Estrategia', 'RPG', 'Simulação']

        # Botões
        self.buttonSubmit = tk.Button(self.frameButton, text="Cadastrar")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Limpar")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    # Método para exibir janela de mensagens
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)


class ViewConsultaAvaliacoes(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('300x200')
        self.title("Consulta por Avaliação")
        self.controle = controle

        # Rótulo para selecionar a avaliação
        self.labelEstrelas = tk.Label(self, text="Selecione a avaliação (estrelas):")
        self.labelEstrelas.pack()

        # ComboBox para selecionar as estrelas
        self.escolhaEstrelas = tk.StringVar()
        self.comboEstrelas = ttk.Combobox(self, textvariable=self.escolhaEstrelas, state="readonly")
        self.comboEstrelas['values'] = ['1 estrela', '2 estrelas', '3 estrelas', '4 estrelas', '5 estrelas']
        self.comboEstrelas.pack()

        # Botão para consultar jogos
        self.botaoConsultar = tk.Button(self, text="Consultar", command=self.controle.consultar_jogos)
        self.botaoConsultar.pack()


class CtrlJogo:
    def __init__(self):
        self.listaJogos = []  # Lista de jogos
        self.carregar_dados()  # Carrega os dados dos jogos ao iniciar o programa

    def salvar_dados(self):
        """Salva a lista de jogos no arquivo usando pickle"""
        with open("jogos.pickle", "wb") as f:
            pickle.dump(self.listaJogos, f)

    def carregar_dados(self):
        """Carrega os dados dos jogos de um arquivo, se o arquivo existir"""
        try:
            with open("jogos.pickle", "rb") as f:
                self.listaJogos = pickle.load(f)  # Carrega os jogos do arquivo
        except (FileNotFoundError, EOFError):
            self.listaJogos = []  # Caso o arquivo não exista ou esteja vazio, cria uma lista vazia

    def cadastrarjogo(self):
        self.viewInsere = ViewCadastraJogo(self)

    def consultar_avaliacoes(self):
        self.viewConsulta = ViewConsultaAvaliacoes(self)

    def filtrar_jogos_por_avaliacao(self, estrelas):
        jogos_filtrados = []
        for jogo in self.listaJogos:
            media = jogo.calcular_media_avaliacao()  # Calcula a média das avaliações
            if media is not None:
                if 0 < media <= 1 and estrelas == 1:
                    jogos_filtrados.append(jogo)
                elif 1 < media <= 2 and estrelas == 2:
                    jogos_filtrados.append(jogo)
                elif 2 < media <= 3 and estrelas == 3:
                    jogos_filtrados.append(jogo)
                elif 3 < media <= 4 and estrelas == 4:
                    jogos_filtrados.append(jogo)
                elif 4 < media <= 5 and estrelas == 5:
                    jogos_filtrados.append(jogo)
        return jogos_filtrados

    def consultar_jogos(self):
        estrelas_selecionadas = self.viewConsulta.escolhaEstrelas.get()
        if not estrelas_selecionadas:
            messagebox.showwarning("Erro", "Selecione uma quantidade de estrelas.")
            return

        estrelas = int(estrelas_selecionadas.split()[0])  # Converte o valor selecionado para inteiro
        jogos_filtrados = self.filtrar_jogos_por_avaliacao(estrelas)

        if jogos_filtrados:
            mensagem = "Jogos com avaliação de {} estrela(s):\n\n".format(estrelas)
            for jogo in jogos_filtrados:
                mensagem += f"{jogo.codigo} - {jogo.titulo} ({jogo.console})\n"
            messagebox.showinfo("Jogos Encontrados", mensagem)
        else:
            messagebox.showinfo("Jogos Não Encontrados", "Nenhum jogo encontrado com esta avaliação.")

    def enterHandler(self, event):
        try:
            codigo = self.viewInsere.inputcodigo.get().strip()
            if not codigo:
                raise ValueError("O código não pode estar vazio.")

            titulo = self.viewInsere.inputtitulo.get().strip()
            if not titulo:
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

            # Criação do jogo e adição à lista
            jogo = Jogo(codigo, titulo, console, genero, preco)
            self.listaJogos.append(jogo)

            # Após adicionar o jogo, salva os dados no arquivo
            self.salvar_dados()

            self.viewInsere.mostraJanela("Sucesso", "Jogo cadastrado com sucesso")
            self.clearHandler(event)

        except ValueError as e:
            self.viewInsere.mostraJanela("Erro", str(e))

    def clearHandler(self, event):
        self.viewInsere.inputcodigo.delete(0, tk.END)
        self.viewInsere.inputtitulo.delete(0, tk.END)
        self.viewInsere.inputpreco.delete(0, tk.END)
        self.viewInsere.escolhagenero.set("") 
        self.viewInsere.escolhaconsole.set("")  

    def fechaHandler(self, event):
        self.viewInsere.destroy()

    def enteravaliacao(self, event):
        try:
            codigo = self.viewavaliar.inputcodigo.get().strip()
            if not codigo:
                raise ValueError("O código do jogo não pode estar vazio.")

            avaliacao = self.viewavaliar.escolhaavaliacao.get()
            if not avaliacao:
                raise ValueError("Selecione uma quantidade de estrelas.")

            avaliacao = int(avaliacao)
            if not (1 <= avaliacao <= 5):
                raise ValueError("A avaliação deve ser um número entre 1 e 5.")

            # Busca o jogo pelo código
            jogo = next((j for j in self.listaJogos if j.codigo == codigo), None)
            if not jogo:
                raise ValueError("Jogo não encontrado para o código fornecido.")

            # Adiciona a avaliação ao jogo
            jogo.adicionar_avaliacao(avaliacao)

            # Salva os dados após adicionar a avaliação
            self.salvar_dados()

            self.viewavaliar.mostraJanela("Sucesso", f"Avaliação de {avaliacao} estrela(s) adicionada ao jogo {jogo.titulo}.")
            self.clearavaliacao(event)

        except ValueError as e:
            self.viewavaliar.mostraJanela("Erro", str(e))

    def clearavaliacao(self, event):
        self.viewavaliar.inputcodigo.delete(0, tk.END)
        self.viewavaliar.escolhaavaliacao.set("") 

    def fechaavaliacao(self, event):
        self.viewavaliar.destroy()
