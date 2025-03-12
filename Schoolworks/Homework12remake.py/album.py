import tkinter as tk
from tkinter import messagebox
import artista

class AlbumModel:
    def __init__(self, title, year, artist):
        self._title = title
        self._year = year
        self._artist = artist
        self._tracks = []

    @property
    def title(self):
        return self._title
    
    @property
    def year(self):
        return self._year
    
    @property
    def artist(self):
        return self._artist
    
    @property
    def tracks(self):
        return self._tracks

class TrackModel:
    def __init__(self, track_number, name):
        self._track_number = track_number
        self._name = name

    @property
    def track_number(self):
        return self._track_number
    
    @property
    def name(self):
        return self._name

class AddAlbumView(tk.Toplevel):
    def __init__(self, controller, artist_list):
        tk.Toplevel.__init__(self)
        self.geometry('350x250')
        self.title("Novo Álbum")
        self.controller = controller

        self.frame_title = tk.Frame(self)
        self.frame_year = tk.Frame(self)
        self.frame_artist = tk.Frame(self)
        self.frame_buttons = tk.Frame(self)

        self.frame_title.pack()
        self.frame_year.pack()
        self.frame_artist.pack()
        self.frame_buttons.pack()

        self.label_title = tk.Label(self.frame_title, text="Título do Álbum:")
        self.label_title.pack(side="left")
        self.input_title = tk.Entry(self.frame_title, width=25)
        self.input_title.pack(side="left")

        self.label_year = tk.Label(self.frame_year, text="Ano:")
        self.label_year.pack(side="left")
        self.input_year = tk.Entry(self.frame_year, width=25)
        self.input_year.pack(side="left")

        self.label_artist = tk.Label(self.frame_artist, text="Artista:")
        self.label_artist.pack(side="left")
        self.artist_combo = tk.ttk.Combobox(self.frame_artist, values=artist_list, state="readonly")
        self.artist_combo.pack(side="left")

        self.button_submit = tk.Button(self.frame_buttons, text="Enviar")
        self.button_submit.pack(side="left")
        self.button_submit.bind("<Button-1>", self.controller.submit_album)

        self.button_clear = tk.Button(self.frame_buttons, text="Limpar")
        self.button_clear.pack(side="left")
        self.button_clear.bind("<Button-1>", self.controller.clear_form)

        self.button_close = tk.Button(self.frame_buttons, text="Fechar")
        self.button_close.pack(side="left")
        self.button_close.bind("<Button-1>", self.controller.close_window)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

class ViewAlbumsView(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)
        self.geometry('600x400')
        self.title("Ver Álbuns")
        self.controller = controller

        self.frame_title = tk.Frame(self)
        self.frame_title.pack()
        self.frame_buttons = tk.Frame(self)
        self.frame_buttons.pack()

        self.label_title = tk.Label(self.frame_title, text="Título do Álbum:")
        self.label_title.pack(side="left")
        self.input_title = tk.Entry(self.frame_title, width=25)
        self.input_title.pack(side="left")

        self.button_view = tk.Button(self.frame_buttons, text="Ver Álbum")
        self.button_view.pack(side="left")
        self.button_view.bind("<Button-1>", self.controller.view_album_details)

        self.text_result = tk.Text(self)
        self.text_result.pack()

    def display_result(self, text):
        self.text_result.delete(1.0, tk.END)
        self.text_result.insert(tk.END, text)

class AlbumController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.albums = []

    def add_album(self):
        artist_list = self.main_controller.artist_controller.get_artist_names()
        self.add_album_view = AddAlbumView(self, artist_list)

    def show_albums(self):
        self.view_album_view = ViewAlbumsView(self)

    def submit_album(self, event):
        title = self.add_album_view.input_title.get()
        year = self.add_album_view.input_year.get()
        artist_name = self.add_album_view.artist_combo.get()
        artist = self.main_controller.artist_controller.get_artist_by_name(artist_name)
        album = AlbumModel(title, year, artist)
        artist.albums.append(album)
        self.albums.append(album)
        self.add_album_view.show_message('Sucesso', 'Álbum adicionado com sucesso')
        self.add_album_view.destroy()

    def clear_form(self, event):
        self.add_album_view.input_title.delete(0, tk.END)
        self.add_album_view.input_year.delete(0, tk.END)

    def close_window(self, event):
        self.add_album_view.destroy()

    def view_album_details(self, event):
        title = self.view_album_view.input_title.get()
        album = next((a for a in self.albums if a.title == title), None)
        if album:
            result = f"Álbum: {album.title}\nAno: {album.year}\nArtista: {album.artist.name}\nFaixas:\n"
            for track in album.tracks:
                result += f"{track.track_number} - {track.name}\n"
            self.view_album_view.display_result(result)
        else:
            self.view_album_view.show_message('Erro', 'Álbum não encontrado')

    def get_track_by_name(self, name):
        for album in self.albums:
            track = next((t for t in album.tracks if t.name == name), None)
            if track:
                return track
        return None

    def get_tracks_by_artist(self, artist_name):
        tracks = []
        for album in self.albums:
            if album.artist.name == artist_name:
                tracks.extend([track.name for track in album.tracks])
        return tracks
