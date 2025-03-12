import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Classe Playlist representa a entidade Playlist
class Playlist:
    def __init__(self, codigo, nome):
        self.__codigo = codigo
        self.__nome = nome
        self.__musicas = []  # Lista de músicas associadas à Playlist

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nome(self):
        return self.__nome

    @property
    def musicas(self):
        return self.__musicas


# View para Inserir Playlist
class ViewInserePlaylist(tk.Toplevel):
    def __init__(self, controle, listaMusicas):
        tk.Toplevel.__init__(self)
        self.geometry('400x300')
        self.title("Criar Playlist")
        self.controle = controle

        # Frames
        self.frameCodigo = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameMusica = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameMusica.pack()
        self.frameButton.pack()

        # Entrada de Código da Playlist
        self.labelCodPlaylist = tk.Label(self.frameCodigo, text="Código da Playlist: ")
        self.labelCodPlaylist.pack(side="left")
        self.inputCodPlaylist = tk.Entry(self.frameCodigo, width=20)
        self.inputCodPlaylist.pack(side="left")

        # Entrada de Nome da Playlist
        self.labelNomePlaylist = tk.Label(self.frameNome, text="Nome da Playlist: ")
        self.labelNomePlaylist.pack(side="left")
        self.inputNomePlaylist = tk.Entry(self.frameNome, width=20)
        self.inputNomePlaylist.pack(side="left")

        # Listbox para escolha de músicas
        self.labelMusica = tk.Label(self.frameMusica, text="Escolha as músicas: ")
        self.labelMusica.pack(side="left")
        self.listboxMusicas = tk.Listbox(self.frameMusica, selectmode=tk.MULTIPLE)
        self.listboxMusicas.pack(side="left")
        for musica in listaMusicas:
            self.listboxMusicas.insert(tk.END, musica)

        # Botões
        self.buttonCria = tk.Button(self.frameButton, text="Criar Playlist", command=self.criaPlaylist)
        self.buttonCria.pack(side="left")

        self.buttonFecha = tk.Button(self.frameButton, text="Concluir", command=self.destroy)
        self.buttonFecha.pack(side="left")

    def criaPlaylist(self):
        codigo = self.inputCodPlaylist.get()
        nome = self.inputNomePlaylist.get()
        musicas_selecionadas = [self.listboxMusicas.get(i) for i in self.listboxMusicas.curselection()]

        if codigo and nome and musicas_selecionadas:
            self.controle.criaPlaylist(codigo, nome, musicas_selecionadas)
            messagebox.showinfo("Sucesso", f"Playlist '{nome}' criada com sucesso!")
        else:
            messagebox.showerror("Erro", "Preencha todos os campos e selecione pelo menos uma música.")


# View para Mostrar Playlists
class LimiteMostraPlaylists:
    def __init__(self, playlists):
        if playlists:
            mensagem = ""
            for playlist in playlists:
                mensagem += f"Código: {playlist.codigo}\nNome: {playlist.nome}\nMúsicas:\n"
                for musica in playlist.musicas:
                    mensagem += f"  - {musica}\n"
                mensagem += "--------\n"
            messagebox.showinfo("Playlists", mensagem)
        else:
            messagebox.showinfo("Playlists", "Nenhuma playlist criada.")


# Controlador da Playlist
class CtrlPlaylist:
    def __init__(self):
        self.listaPlaylists = []
        self.listaMusicas = ["Música 1", "Música 2", "Música 3", "Música 4"]  # Lista de músicas disponíveis

    def inserePlaylists(self):
        self.viewInserePlaylist = ViewInserePlaylist(self, self.listaMusicas)

    def criaPlaylist(self, codigo, nome, musicas):
        playlist = Playlist(codigo, nome)
        playlist.musicas.extend(musicas)
        self.listaPlaylists.append(playlist)

    def mostraPlaylists(self):
        LimiteMostraPlaylists(self.listaPlaylists)


# Exemplo de como usar o controlador
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Playlists")
    root.geometry("200x150")

    ctrlPlaylist = CtrlPlaylist()

    # Menu para gerenciar playlists
    menu = tk.Menu(root)
    playlistMenu = tk.Menu(menu, tearoff=0)
    playlistMenu.add_command(label="Criar Playlist", command=ctrlPlaylist.inserePlaylists)
    playlistMenu.add_command(label="Listar Playlists", command=ctrlPlaylist.mostraPlaylists)
    menu.add_cascade(label="Playlist", menu=playlistMenu)

    root.config(menu=menu)
    root.mainloop()
