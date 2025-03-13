import tkinter as tk
import album as alb
import artistas as art
import musicas as musc
import playlist as play

class ViewPrincipal():
    def __init__(self, root, controle):
        self.controle = controle  # Referência ao controlador principal
        self.root = root  # Janela principal
        self.root.geometry('300x250')  # Definir tamanho da janela
        self.menubar = tk.Menu(self.root)  # Menu principal
        
        # Criando submenus para artista, albumplina e playlist
        self.artistaMenu = tk.Menu(self.menubar)
        self.albumMenu = tk.Menu(self.menubar)
        self.playlistMenu = tk.Menu(self.menubar)

        # Adicionando comandos aos menus
        self.artistaMenu.add_command(label="Insere", command=self.controle.insereArtista)
        self.artistaMenu.add_command(label="Mostra", command=self.controle.mostraArtista)
        self.menubar.add_cascade(label="Artista", menu=self.artistaMenu)
        self.albumMenu.add_command(label="Insere", command=self.controle.insereAlbum)
        self.albumMenu.add_command(label="Mostra", command=self.controle.mostraAlbum)
        self.menubar.add_cascade(label="Album", menu=self.albumMenu)
        self.playlistMenu.add_command(label="Insere", command=self.controle.inserePlaylist)
        self.playlistMenu.add_command(label="Mostra", command=self.controle.mostraPlaylist)
        self.menubar.add_cascade(label="Playlist", menu=self.playlistMenu)
        self.root.config(menu=self.menubar)  # Configura o menu


      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()  # Cria a janela principal

        self.ctrlAlbum = alb.CtrlAlbum(self)  # Controlador para album
        
        self.ctrlArtista = art.CtrlArtista()  # Controlador para artista
        
        self.ctrPlaylist = play.CtrlPlaylist(self)  # Controlador para playlist
        
        self.limite = ViewPrincipal(self.root, self)  # A interface com os menus
        self.root.mainloop()  # Inicia o loop da interface gráfica

       
    def insereArtista(self):
        self.ctrlArtista.insereArtista()

    def mostraArtista(self):
        self.ctrlArtista.mostraArtista()

    def inserealbum(self):
        self.ctrlAlbum.inserealbum()

    def mostraalbum(self):
        self.ctrlAlbum.mostraalbum()

    def inserePlaylist(self):
        self.ctrPlaylist.inserePlaylist()

    def mostraPlaylist(self):
        self.ctrPlaylist.mostraPlaylist()

if __name__ == '__main__':
    c = ControlePrincipal()