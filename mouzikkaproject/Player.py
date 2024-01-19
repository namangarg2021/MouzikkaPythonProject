import os
from tkinter import filedialog

from mutagen.mp3 import MP3
from pygame import mixer

import Model


class Player:
    def __init__(self):
        mixer.init()
        self.my_model = Model.Model()

    def get_db_status(self):
        return self.my_model.get_db_status()

    def close_player(self):
        mixer.music.stop()
        self.my_model.close_db_conn()

    def set_volume(self, volume_level):
        mixer.music.set_volume(volume_level)

    def add_song(self):
        song_path_tuple = filedialog.askopenfilename(title="Select a song...", filetypes=[("mp3 files", ".mp3")],
                                                     multiple=True)
        if len(song_path_tuple) == 0:
            return []
        song_names = []
        for song_path in song_path_tuple:
            song_name = os.path.basename(song_path)
            self.my_model.add_song(song_name, song_path)
            song_names.append(song_name)
        return song_names

    def remove_song(self, song_name):
        self.my_model.remove_song(song_name)

    def get_song_length(self, song_name):
        self.song_path = self.my_model.get_song_path(song_name)
        self.audio_tag = MP3(self.song_path)
        self.song_length = self.audio_tag.info.length
        return self.song_length

    def play_song(self):
        mixer.quit()
        mixer.init(frequency=self.audio_tag.info.sample_rate)
        mixer.music.load(self.song_path)
        mixer.music.play()

    def stop_song(self):
        mixer.music.stop()

    def pause_song(self):
        mixer.music.pause()

    def unpause_song(self):
        mixer.music.unpause()

    def add_song_in_favourites(self, song_name):
        song_path = self.my_model.get_song_path(song_name)
        result = self.my_model.add_song_in_favourites(song_name, song_path)
        return result

    def load_songs_from_favourites(self):
        result = self.my_model.load_songs_from_favourites()
        return result, self.my_model.song_dict

    def remove_song_from_favourites(self, song_name):
        result = self.my_model.remove_song_from_favourite(song_name)
        return result

    def get_song_count(self):
        return self.my_model.get_song_count()

    def play_from_passed_time(self, new_time):
        mixer.music.play(start=new_time)
