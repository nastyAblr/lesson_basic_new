"""
Создать систему управления музыкальными плейлистами.
Можно создать абстрактный класс Playlist,
который определяет общий интерфейс для всех плейлистов и
классы FavoritePlaylist, RecentPlaylist и GenrePlaylist,
которые наследуются от Playlist и предоставляют конкретную реализацию
для каждого типа плейлистов
"""
from abc import ABC, abstractmethod
#from cgi import maxlen

from collections import deque



class Playlist(ABC):
    def __init__(self, name):
        self.name = name
        self.songs = []

    @abstractmethod
    def add_song(self, song):
        pass

    @abstractmethod
    def remove_song(self, song):
        pass

    @abstractmethod
    def play(self):
        pass

    def get_songs(self):
        return self.songs


class FavoritePlayList(Playlist):
    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            print(f'Песня "{song}" добавлена в подборку Избранные ')
        else:
            print(f'Песня "{song}" уже находится в Избранных')

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f'Песня "{song}" удалена из Избранных ')
        else:
            print(f'Песня "{song}" не найдена в Избранных')

    def play(self):
        print(f'Воспроизведение избранных песен "{self.name}":')
        for song in self.songs:
            print(f'▶️ "{song.title}"')


class RecentPlayList(Playlist):
    def __init__(self, name, max_size=10):
        super().__init__(name)
        self.max_size = max_size

        self.songs = deque(maxlen=max_size)  # храним последние песни в ограниченном размере

    # def add_song(self, song):
    #     if song in self.songs:
    #         self.songs.remove(song)
    #         print(f'Песня "{song}" удалена из Недавних')
    #     else:
    #         print(f'Песня "{song}" не найдена в Недавних')
    #     self.songs.append(song)
    #     print(f'Песня "{song}" добавлена в недавние')
    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            print(f'Песня "{song}" добавлена в Недавние')
        else:
            print(f'Песня "{song}" уже находится в недавних')
    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f'Песня "{song}" удалена из Недавних')
        else:
            print(f'Песня "{song}" не найдена в Недавних')



    def play(self):
        print(f'Воспроизведение последних песен "{self.name}":')
        for song in self.songs:
            print(f'▶️ "{song}"')


class GenrePlayList(Playlist):
    def __init__(self, name, genre):
        super().__init__(name)
        self.genre = genre

    def add_song(self, song):
        if getattr(song, 'genre', None) == self.genre:  # Без getattr при попытке обратиться к несуществующему атрибуту
            # возникнет ошибка AttributeError.
            if song in self.songs:
                self.songs.append(song)
                print(f'Песня "{song.title}" добавлена в жанр {self.genre}')
            else:
                print(f'Песня "{song.title}" уже в плейлисте жанра {self.genre}')
        else:
            print(f'Песня "{song.title}" не подходит по жанру {self.genre}')

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f'Песня "{song.title}" удалена из плейлиста жанра {self.genre}')
        else:
            print(f'Песня "{song.title}" не найдена в плейлисте жанра {self.genre}')

    def play(self):
        print(f'Воспроизведение плейлиста жанра "{self.genre}":')
        for song in self.songs:
            print(f"▶️ {song.title}")

class Song:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def __eq__(self, other):
        return (isinstance(other, Song)
                and self.title == other.title and self.genre == other.genre)
    def __hash__(self):
        return  hash((self.title, self.genre))
    def __repr__(self):
        return f'Song(title="{self.title}", genre="{self.genre}")'

fav = FavoritePlayList("Избранные")
fav.add_song("Song A")
fav.add_song("Song B")
fav.play()

recent = RecentPlayList("Недавние", max_size=3)
recent.add_song("Song A")
recent.add_song("Song C")
recent.add_song("Song B")
recent.add_song("Song D")  # при max_size=3 будет удалена самая старая песня
recent.play()

rock_playlist = GenrePlayList("Rock Hits", "rock")
song1 = Song("Bohemian Rhapsody", "rock")
song2 = Song("Imagine", "pop")

rock_playlist.add_song(song1)
rock_playlist.add_song(song2)  # не добавится, т.к. не рок
rock_playlist.play()


