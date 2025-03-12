import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, messagebox

class Automovel:
    def __init__(self, codigo, modelo, marca, tipo, ano, preco):
        self.__codigo = codigo
        self.__modelo = modelo
        self.__marca = marca
        self.__tipo = tipo
        self.__ano = ano
        self.__preco = preco

    @property
    def codigo(self):
        return self.__codigo
   
    @property
    def modelo(self):
        return self.__modelo

    @property
    def marca(self):
        return self.__marca
    
    @property
    def tipo(self):
        return self.__tipo
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def ano(self):
        return self.__ano

    @marca.setter
    def marca(self, valor):
        self.marcas = ["Branco", "Tinto", "Rose", "Espumante"]
        if not valor in self.marcas:
            raise ValueError("marca inválido: {}".format(valor))
        else:
            self.__marca = valor

    @tipo.setter
    def tipo(self, valor):
        self.tipos = ["Branco", "Tinto", "Rose", "Espumante"]
        if not valor in self.marcas:
            raise ValueError("marca inválido: {}".format(valor))
        else:
            self.__marca = valor

    
class ViewCadastraAutomovel(tk.Toplevel):
    def __init__(self, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x150')
        self.title("Automovel")
        self.controle = controle

        self.framemodelo = tk.Frame(self)
        self.framecodigo = tk.Frame(self)
        self.framemarca = tk.Frame(self)
        self.framepreco = tk.Frame(self)
        self.frameAno = tk.Frame(self)
        self.frametipo = tk.Frame(self)    
        self.frameButton = tk.Frame(self)    

        self.framecodigo.pack()
        self.framemodelo.pack()
        self.framemarca.pack()
        self.frametipo.pack()
        self.frameAno.pack()
        self.framepreco.pack()
        self.frameButton.pack()

        self.labelcodigo = tk.Label(self.framecodigo, text="Codigo: ")
        self.labelmodelo = tk.Label(self.framemodelo, text="Modelo: ")
        self.labelPreco = tk.Label(self.framepreco, text="Preço: ")
        self.labelAno = tk.Label(self.frameAno, text="Ano: ")
        self.labelcodigo.pack(side="left")
        self.labelmodelo.pack(side="left")
        self.labelPreco.pack(side="left")
        self.labelAno.pack(side="left")

        self.inputcodigo = tk.Entry(self.framecodigo, width=20)
        self.inputcodigo.pack(side="left")
        self.inputmodelo = tk.Entry(self.framemodelo, width=20)
        self.inputmodelo.pack(side="left")
        self.inputpreco = tk.Entry(self.framepreco, width=20)
        self.inputpreco.pack(side="left")
        self.inputAno = tk.Entry(self.frameAno, width=20)
        self.inputAno.pack(side="left")

        self.labelmarca = tk.Label(self.framemarca, text="Escolha marca: ")
        self.labelmarca.pack(side="left")
        self.escolhamarca = tk.StringVar()
        self.comboboxmarca = ttk.Combobox(self.framemarca, width=15, textvariable=self.escolhamarca)
        self.comboboxmarca.pack(side="left")
        self.comboboxmarca['values'] = ['Ford', 'Chevrolet', 'Toyota', 'Honda','BMW', 'Mercedes']

        self.labeltipo = tk.Label(self.frametipo, text="Escolha tipo: ")
        self.labeltipo.pack(side="left")
        self.escolhatipo = tk.StringVar()
        self.comboboxtipo = ttk.Combobox(self.frametipo, width=15, textvariable=self.escolhatipo)
        self.comboboxtipo.pack(side="left")
        self.comboboxtipo['values'] = ['Sedan', 'SUV', 'Hatch', 'Picape', 'Conversível', 'Esportivo']

        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)

        self.buttonClear = tk.Button(self.frameButton, text="Clear")
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, modelo, msg):
        messagebox.showinfo(modelo, msg)


class ViewConsultaAutomovel(tk.Toplevel):
    def __init__(self, tipos, marcas, controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x250')
        self.title("Consultar Automóveis")
        self.ctrl = controle

        self.frameCombos = tk.Frame(self)
        self.frameCombos.pack(pady=10)

        self.labelTipos = tk.Label(self.frameCombos, text="Tipos: ")
        self.labelTipos.pack(side="left")
        self.escolhaTipo = tk.StringVar()
        self.comboboxTipo = ttk.Combobox(self.frameCombos, width=15, values=tipos, textvariable=self.escolhaTipo)
        self.comboboxTipo.pack(side="left")
        self.comboboxTipo.bind("<<ComboboxSelected>>", self.ctrl.exibeTipo)

        self.labelMarcas = tk.Label(self.frameCombos, text="Marcas: ")
        self.labelMarcas.pack(side="left")
        self.escolhaMarca = tk.StringVar()
        self.comboboxMarca = ttk.Combobox(self.frameCombos, width=15, values=marcas, textvariable=self.escolhaMarca)
        self.comboboxMarca.pack(side="left")
        self.comboboxMarca.bind("<<ComboboxSelected>>", self.ctrl.exibeMarca)

        self.frameAutomoveis = tk.Frame(self)
        self.frameAutomoveis.pack()
        self.textAutomoveis = tk.Text(self.frameAutomoveis, height=20, width=50)
        self.textAutomoveis.pack()
        self.textAutomoveis.config(state=tk.DISABLED)


class CtrlAutomovel():
    def __init__(self):
        self.listaAutomovels = []

    def cadastrar_automovel(self):
        self.viewcadastra = ViewCadastraAutomovel(self)

    def consultar_automovel(self):
        #listas preenchidas com a categoria de automveis existentes
        self.tipos = []
        self.marcas = []
        for automovel in self.listaAutomovels:
            if(not automovel.tipo in self.tipos):
                self.tipos.append(automovel.tipo)
            if(not automovel.marca in self.marcas):
                self.marcas.append(automovel.marca)
        self.limiteconsulta = ViewConsultaAutomovel(self.tipos, self.marcas, self)
    
    def exibeTipo(self, event):
        self.limiteconsulta.comboboxMarca.set("---") # Limpa a seleção de marcas
        tipoSel = self.limiteconsulta.comboboxTipo.get() # Obtém o tipo selecionado
        self.limiteconsulta.textAutomoveis.config(state='normal')  # Habilita edição no Text
        self.limiteconsulta.textAutomoveis.delete("1.0", tk.END) # Limpa o conteúdo do Text
        for automovel in self.listaAutomovels:
            if automovel.tipo == tipoSel: # Filtra por tipo
                automovelSel = f"Modelo: {automovel.modelo}\nMarca: {automovel.marca}\nAno: {automovel.ano}\nPreço: {automovel.preco}\n\n"
                self.limiteconsulta.textAutomoveis.insert(tk.END, automovelSel)
        self.limiteconsulta.textAutomoveis.config(state='disabled')

    def exibeMarca(self, event):
        self.limiteconsulta.comboboxTipo.set("---")
        marcaSel = self.limiteconsulta.comboboxMarca.get()
        self.limiteconsulta.textAutomoveis.config(state='normal')
        self.limiteconsulta.textAutomoveis.delete("1.0", tk.END)
        for automovel in self.listaAutomovels:
            if automovel.marca == marcaSel:
                automovelSel = f"Modelo: {automovel.modelo}\nTipo: {automovel.tipo}\nAno: {automovel.ano}\nPreço: {automovel.preco}\n\n"
                self.limiteconsulta.textAutomoveis.insert(tk.END, automovelSel)
        self.limiteconsulta.textAutomoveis.config(state='disabled')


    def enterHandler(self, event):
        try:
            # Validações de entrada
            codigo = self.viewcadastra.inputcodigo.get().strip()
            if not codigo:
                raise ValueError("O código não pode estar vazio.")

            modelo = self.viewcadastra.inputmodelo.get().strip()
            if not modelo:
                raise ValueError("O título não pode estar vazio.")

            marca = self.viewcadastra.escolhamarca.get().strip()
            if marca not in ['Ford', 'Chevrolet', 'Toyota', 'Honda','BMW', 'Mercedes']:
                raise ValueError("Marca: {} inválida".format(marca))

            tipo = self.viewcadastra.escolhatipo.get().strip()
            if tipo not in ['Sedan', 'SUV', 'Hatch', 'Picape', 'Conversível', 'Esportivo']:
                raise ValueError("Tipo: {} inválido".format(tipo))
            
            ano = self.viewcadastra.inputAno.get().strip()
            try:
                ano = int(ano)
                if not (1980 <= ano <= 2024):  # Valida se o ano está no intervalo permitido
                    raise ValueError(f"Ano inválido: {ano}. Deve estar entre 1980 e 2024.")
            except ValueError:
                raise ValueError("O ano deve ser um número válido entre 1980 e 2024.")

            preco_str = self.viewcadastra.inputpreco.get().strip()
            try:
                preco = float(preco_str)
                if preco <= 0:
                    raise ValueError
            except ValueError:
                raise ValueError("O preço deve ser um número maior que zero")

            # Cria o objeto Automovel e adiciona à lista
            automovel = Automovel(codigo, modelo, marca, tipo, ano, preco)
            self.listaAutomovels.append(automovel)

            # Exibe mensagem de sucesso
            self.viewcadastra.mostraJanela("Sucesso", "Automovel cadastrado com sucesso")
            self.clearHandler(event)

        except ValueError as e:
            # Exibe mensagem de erro
            self.viewcadastra.mostraJanela("Erro", str(e))


        

    def clearHandler(self, event):
    # Limpa os campos de entrada de texto e combobox
        self.viewcadastra.inputcodigo.delete(0, tk.END)
        self.viewcadastra.inputmodelo.delete(0, tk.END)
        self.viewcadastra.inputpreco.delete(0, tk.END)
        self.viewcadastra.escolhamarca.set("") 
        self.viewcadastra.escolhatipo.set("")  

    def fechaHandler(self, event):
        # Fecha a janela de cadastro de Automovel
        self.viewcadastra.destroy()

