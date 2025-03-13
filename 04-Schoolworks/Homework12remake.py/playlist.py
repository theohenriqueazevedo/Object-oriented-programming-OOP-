import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Playlist:
    def __init__(self, name, tracks):
        self._name = name
        self._tracks = tracks

    @property
    def name(self):
        return self._name
    
    @property
    def tracks(self):
        return self._tracks

class AddPlaylistView(tk.Toplevel):
    def __init__(self, controller, artist_list):
        tk.Toplevel.__init__(self)
        self.geometry('350x300')
        self.title("New Playlist")
        self.controller = controller

        self.frame_name = tk.Frame(self)
        self.frame_artist = tk.Frame(self)
        self.frame_tracks = tk.Frame(self)
        self.frame_buttons = tk.Frame(self)

        self.frame_name.pack()
        self.frame_artist.pack()
        self.frame_tracks.pack()
        self.frame_buttons.pack()

        self.label_name = tk.Label(self.frame_name, text="Playlist Name:")
        self.label_name.pack(side="left")
        self.input_name = tk.Entry(self.frame_name, width=25)
        self.input_name.pack(side="left")

        self.label_artist = tk.Label(self.frame_artist, text="Select Artist:")
        self.label_artist.pack(side="left")
        self.artist_combo = ttk.Combobox(self.frame_artist, values=artist_list, state="readonly")
        self.artist_combo.pack(side="left")
        self.artist_combo.bind("<<ComboboxSelected>>", self.controller.display_tracks)
        
        self.label_tracks = tk.Label(self.frame_tracks, text="Select Tracks:")
        self.label_tracks.pack(side="left")
        self.track_listbox = tk.Listbox(self.frame_tracks, selectmode=tk.MULTIPLE)
        self.track_listbox.pack(side="left")

        self.button_add_track = tk.Button(self.frame_buttons, text="Add Track")
        self.button_add_track.pack(side="left")
        self.button_add_track.bind("<Button-1>", self.controller.add_track_to_playlist)

        self.button_create_playlist = tk.Button(self.frame_buttons, text="Create Playlist")
        self.button_create_playlist.pack(side="left")
        self.button_create_playlist.bind("<Button-1>", self.controller.finalize_playlist)

    def show_message(self, title, message):
        messagebox.showinfo(title, message)

class ViewPlaylistsView(tk.Toplevel):
    def __init__(self, controller):
        tk.Toplevel.__init__(self)
        self.geometry('600x400')
        self.title("View Playlists")
        self.controller = controller

        self.frame_name = tk.Frame(self)
        self.frame_name.pack()
        self.frame_buttons = tk.Frame(self)
        self.frame_buttons.pack()

        self.label_name = tk.Label(self.frame_name, text="Playlist Name:")
        self.label_name.pack(side="left")
        self.input_name = tk.Entry(self.frame_name, width=25)
        self.input_name.pack(side="left")

        self.button_view = tk.Button(self.frame_buttons, text="View Playlist")
        self.button_view.pack(side="left")
        self.button_view.bind("<Button-1>", self.controller.view_playlist_details)

        self.text_result = tk.Text(self)
        self.text_result.pack()

    def display_result(self, text):
        self.text_result.delete(1.0, tk.END)
        self.text_result.insert(tk.END, text)

class PlaylistController:
    def __init__(self, main_controller):
        self.main_controller = main_controller
        self.playlists = []

    def create_playlist(self):
        self.current_tracks = []
        artist_list = self.main_controller.artist_controller.get_artist_names()
        self.add_playlist_view = AddPlaylistView(self, artist_list)

    def view_playlists(self):
        self.view_playlist_view = ViewPlaylistsView(self)

    def finalize_playlist(self, event):
        name = self.add_playlist_view.input_name.get()
        playlist = Playlist(name, self.current_tracks)
        self.playlists.append(playlist)
        self.add_playlist_view.show_message('Success', 'Playlist created successfully')
        self.add_playlist_view.destroy()

    def add_track_to_playlist(self, event):
        selected_tracks = self.add_playlist_view.track_listbox.curselection()
        for i in selected_tracks:
            track_name = self.add_playlist_view.track_listbox.get(i)
            track = self.main_controller.album_controller.get_track_by_name(track_name)
            self.current_tracks.append(track)
        self.add_playlist_view.show_message('Success', 'Tracks added successfully')

    def view_playlist_details(self, event):
        name = self.view_playlist_view.input_name.get()
        playlist = next((p for p in self.playlists if p.name == name), None)
        if playlist:
            result = f"Playlist: {playlist.name}\nTracks:\n"
            for track in playlist.tracks:
                result += f"{track.track_number} - {track.name}\n"
            self.view_playlist_view.display_result(result)
        else:
            self.view_playlist_view.show_message('Error', 'Playlist not found')

    def display_tracks(self, event):
        artist_name = self.add_playlist_view.artist_combo.get()
        self.add_playlist_view.track_listbox.delete(0, tk.END)
        track_list = self.main_controller.album_controller.get_tracks_by_artist(artist_name)
        for track in track_list:
            self.add_playlist_view.track_listbox.insert(tk.END, track)
