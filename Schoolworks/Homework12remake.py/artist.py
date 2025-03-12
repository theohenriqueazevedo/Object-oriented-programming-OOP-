import tkinter as tk
from tkinter import messagebox

class ArtistModel:
    def __init__(self, name):
        self._name = name
        self._albums = []

    @property
    def name(self):
        return self._name
    
    @property
    def albums(self):
        return self._albums

    def get_name(self):
        return self._name

class AddArtistView(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)
        self.geometry('400x200')
        self.title("Novo Artista")
        self.controller = controller

        self.frame_name = tk.Frame(self)
        self.frame_buttons = tk.Frame(self)

        self.frame_name.pack()
        self.frame_buttons.pack()

        self.label_name = tk.Label(self.frame_name, text="Nome do Artista:")
        self.label_name.pack(side="left")
        self.input_name = tk.Entry(self.frame_name, width=25)
        self.input_name.pack(side="left")

        self.button_submit = tk.Button(self.frame_buttons, text="Enviar")
        self.button_submit.pack(side="left")
        self.button_submit.bind("<Button-1>", self.controller.submit_artist)

        self.button_clear = tk.Button(self.frame_buttons, text="Limpar")
        self.button_clear.pack(side="left")
        self.button_clear.bind("<Button-1>", self.controller.clear_form)

        self.button_close = tk.Button(self.frame_buttons, text="Fechar")
        self.button_close.pack(side="left")
        self.button_close.bind("<Button-1>", self.controller.close_window)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

class ViewArtistsView(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)
        self.geometry('600x400')
        self.title("Ver Artistas")
        self.controller = controller

        self.frame_name = tk.Frame(self)
        self.frame_name.pack()
        self.frame_buttons = tk.Frame(self)
        self.frame_buttons.pack()

        self.label_name = tk.Label(self.frame_name, text="Nome do Artista:")
        self.label_name.pack(side="left")
        self.input_name = tk.Entry(self.frame_name, width=25)
        self.input_name.pack(side="left")

        self.button_view = tk.Button(self.frame_buttons, text="Ver Artista")
        self.button_view.pack(side="left")
        self.button_view.bind("<Button-1>", self.controller.view_artist_details)

        self.text_result = tk.Text(self)
        self.text_result.pack()

    def display_result(self, text):
        self.text_result.delete(1.0, tk.END)
        self.text_result.insert(tk.END, text)

class ArtistController:
    def __init__(self):
        self.artists = []

    def add_artist(self):
        self.add_artist_view = AddArtistView(self)

    def show_artists(self):
        self.view_artist_view = ViewArtistsView(self)

    def submit_artist(self, event):
        name = self.add_artist_view.input_name.get()
        artist = ArtistModel(name)
        self.artists.append(artist)
        self.add_artist_view.show_message('Sucesso', 'Artista adicionado com sucesso')
        self.add_artist_view.destroy()

    def clear_form(self, event):
        self.add_artist_view.input_name.delete(0, tk.END)

    def close_window(self, event):
        self.add_artist_view.destroy()

    def view_artist_details(self, event):
        name = self.view_artist_view.input_name.get()
        artist = next((a for a in self.artists if a.get_name() == name), None)
        if artist:
            result = f"Artista: {artist.name}\nÁlbuns:\n"
            for album in artist.albums:
                result += f"{album.title} ({album.year})\n"
            self.view_artist_view.display_result(result)
        else:
            self.view_artist_view.show_message('Erro', 'Artista não encontrado')

    def get_artist_names(self):
        return [artist.name for artist in self.artists]

    def get_artist_by_name(self, name):
        return next((artist for artist in self.artists if artist.get_name() == name), None)
