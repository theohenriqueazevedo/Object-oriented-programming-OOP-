import tkinter as tk
from tkinter import messagebox
import album
import playlist
import artista

class MainAppView:
    def __init__(self, root, controller):
        self.controller = controller
        self.root = root
        self.root.geometry('400x300')
        
        self.menu_bar = tk.Menu(self.root)
        
        self.artist_menu = tk.Menu(self.menu_bar)
        self.album_menu = tk.Menu(self.menu_bar)
        self.playlist_menu = tk.Menu(self.menu_bar)

        self.artist_menu.add_command(label="Adicionar Artista", command=self.controller.add_artist)
        self.artist_menu.add_command(label="Ver Artistas", command=self.controller.view_artists)
        self.menu_bar.add_cascade(label="Artista", menu=self.artist_menu)

        self.album_menu.add_command(label="Adicionar Álbum", command=self.controller.add_album)
        self.album_menu.add_command(label="Ver Álbuns", command=self.controller.view_albums)
        self.menu_bar.add_cascade(label="Álbum", menu=self.album_menu)

        self.playlist_menu.add_command(label="Criar Playlist", command=self.controller.create_playlist)
        self.playlist_menu.add_command(label="Ver Playlists", command=self.controller.view_playlists)
        self.menu_bar.add_cascade(label="Playlist", menu=self.playlist_menu)

        self.root.config(menu=self.menu_bar)

class MainAppController:
    def __init__(self):
        self.root = tk.Tk()

        self.artist_controller = artista.ArtistController()
        self.album_controller = album.AlbumController(self)
        self.playlist_controller = playlist.PlaylistController(self)

        self.main_view = MainAppView(self.root, self)

        self.root.title("Exemplo MVC")
        self.root.mainloop()

    def add_artist(self):
        self.artist_controller.add_artist()

    def view_artists(self):
        self.artist_controller.show_artists()

    def add_album(self):
        self.album_controller.add_album()

    def view_albums(self):
        self.album_controller.show_albums()

    def create_playlist(self):
        self.playlist_controller.create_playlist()

    def view_playlists(self):
        self.playlist_controller.show_playlists()

if __name__ == '__main__':
    app = MainAppController()
