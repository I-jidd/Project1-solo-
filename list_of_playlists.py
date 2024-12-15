from playlist import Playlist

class List_of_Playlist:
    def __init__(self):
        self.__list_playlist = []
        self.__playlist = Playlist()
        
    def get_list_playlist(self):
        return self.__list_playlist
    
    def get_playlist_title(self):
        return self.__playlist
    
    def add_playlist_on_list(self, playlist_title:Playlist):
        if self.get_playlist_title() not in self.get_list_playlist():
            self.__list_playlist.append(playlist_title)
        else:
            print(f"{playlist_title} is already created")