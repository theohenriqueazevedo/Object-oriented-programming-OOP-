import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

# Classe Produto
class Produto:
    def __init__(self, codigo, descricao, valor_unitario):
        self.codigo = codigo
        self.descricao = descricao
        self.valor_unitario = valor_unitario

    def __str__(self):
        return f"{self.codigo} - {self.descricao} - R${self.valor_unitario:.2f}"


# Classe CupomFiscal
class CupomFiscal:
    def __init__(self, nro_cupom):
        self.nro_cupom = nro_cupom
        self.itens_cupom = []

    def adicionar_item(self, produto):
        self.itens_cupom.append(produto)

    def calcular_total(self):
        return sum(produto.valor_unitario for produto in self.itens_cupom)

    def agrupar_itens(self):
        agrupados = {}
        for produto in self.itens_cupom:
            if produto.codigo in agrupados:
                agrupados[produto.codigo]['quantidade'] += 1
                agrupados[produto.codigo]['subtotal'] += produto.valor_unitario
            else:
                agrupados[produto.codigo] = {
                    'descricao': produto.descricao,
                    'quantidade': 1,
                    'subtotal': produto.valor_unitario
                }
        return agrupados


# Classe de Persistência (com arquivos de texto)
class Persistencia:
    @staticmethod
    def salvar_produtos(produtos):
        with open("produtos.txt", "w") as file:
            for produto in produtos:
                file.write(f"{produto.codigo};{produto.descricao};{produto.valor_unitario}\n")

    @staticmethod
    def carregar_produtos():
        produtos = []
        try:
            with open("produtos.txt", "r") as file:
                for linha in file:
                    codigo, descricao, valor_unitario = linha.strip().split(";")
                    produtos.append(Produto(int(codigo), descricao, float(valor_unitario)))
        except FileNotFoundError:
            pass
        return produtos

    @staticmethod
    def salvar_cupons(cupons):
        with open("cupons.txt", "w") as file:
            for cupom in cupons:
                itens = "|".join([str(produto.codigo) for produto in cupom.itens_cupom])
                file.write(f"{cupom.nro_cupom};{itens}\n")

    @staticmethod
    def carregar_cupons(produtos):
        cupons = []
        try:
            with open("cupons.txt", "r") as file:
                for linha in file:
                    nro_cupom, itens_str = linha.strip().split(";")
                    cupom = CupomFiscal(int(nro_cupom))
                    for codigo in itens_str.split("|"):
                        produto = next((p for p in produtos if p.codigo == int(codigo)), None)
                        if produto:
                            cupom.adicionar_item(produto)
                    cupons.append(cupom)
        except FileNotFoundError:
            pass
        return cupons


# Classe Aplicação
class Aplicacao:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Loja de Conveniência")
        self.produtos = Persistencia.carregar_produtos()
        self.cupons = Persistencia.carregar_cupons(self.produtos)

        # Menu principal
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        menu_produto = tk.Menu(menu_bar, tearoff=0)
        menu_produto.add_command(label="Cadastrar", command=self.cadastrar_produto)
        menu_produto.add_command(label="Consultar", command=self.consultar_produto)
        menu_bar.add_cascade(label="Produto", menu=menu_produto)

        menu_cupom = tk.Menu(menu_bar, tearoff=0)
        menu_cupom.add_command(label="Criar", command=self.criar_cupom)
        menu_cupom.add_command(label="Consultar", command=self.consultar_cupom)
        menu_bar.add_cascade(label="Cupom Fiscal", menu=menu_cupom)

        self.root.mainloop()

    def cadastrar_produto(self):
        codigo = simpledialog.askinteger("Cadastrar Produto", "Digite o código:")
        descricao = simpledialog.askstring("Cadastrar Produto", "Digite a descrição:")
        valor_unitario = simpledialog.askfloat("Cadastrar Produto", "Digite o valor unitário:")

        if not any(p.codigo == codigo for p in self.produtos):
            produto = Produto(codigo, descricao, valor_unitario)
            self.produtos.append(produto)
            Persistencia.salvar_produtos(self.produtos)
            messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Código já cadastrado!")

    def consultar_produto(self):
        codigo = simpledialog.askinteger("Consultar Produto", "Digite o código:")
        produto = next((p for p in self.produtos if p.codigo == codigo), None)

        if produto:
            mensagem = f"Código: {produto.codigo}\nDescrição: {produto.descricao}\nValor: R${produto.valor_unitario:.2f}"
        else:
            mensagem = "Produto não encontrado."
        messagebox.showinfo("Consulta de Produto", mensagem)

    def criar_cupom(self):
        nro_cupom = simpledialog.askinteger("Criar Cupom", "Digite o número do cupom:")
        cupom = CupomFiscal(nro_cupom)

        janela = tk.Toplevel(self.root)
        janela.title("Criar Cupom Fiscal")

        produtos_frame = tk.Frame(janela)
        produtos_frame.pack()

        tk.Label(produtos_frame, text="Selecione os produtos:").pack()
        lista_produtos = ttk.Combobox(produtos_frame, values=[f"{p.codigo} - {p.descricao}" for p in self.produtos])
        lista_produtos.pack()

        def adicionar_produto():
            produto_selecionado = lista_produtos.get()
            if produto_selecionado:
                codigo = int(produto_selecionado.split(" - ")[0])
                produto = next((p for p in self.produtos if p.codigo == codigo), None)
                if produto:
                    cupom.adicionar_item(produto)
                    messagebox.showinfo("Adicionado", f"Produto {produto.descricao} adicionado.")

        tk.Button(produtos_frame, text="Adicionar Produto", command=adicionar_produto).pack()

        def fechar_cupom():
            self.cupons.append(cupom)
            Persistencia.salvar_cupons(self.cupons)
            total = cupom.calcular_total()
            messagebox.showinfo("Cupom Fiscal", f"Cupom {nro_cupom} fechado. Total: R${total:.2f}")
            janela.destroy()

        tk.Button(produtos_frame, text="Fechar Cupom", command=fechar_cupom).pack()

    def consultar_cupom(self):
        nro_cupom = simpledialog.askinteger("Consultar Cupom", "Digite o número do cupom:")
        cupom = next((c for c in self.cupons if c.nro_cupom == nro_cupom), None)

        if cupom:
            mensagem = f"Cupom {cupom.nro_cupom}\n"
            agrupados = cupom.agrupar_itens()
            for item in agrupados.values():
                mensagem += f"{item['quantidade']}x {item['descricao']} - R${item['subtotal']:.2f}\n"
            mensagem += f"Total: R${sum(item['subtotal'] for item in agrupados.values()):.2f}"
        else:
            mensagem = "Cupom não encontrado."
        messagebox.showinfo("Consulta de Cupom", mensagem)


if __name__ == '__main__':
    Aplicacao()
