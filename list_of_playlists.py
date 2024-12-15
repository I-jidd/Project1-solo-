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
        if playlist_title not in self.get_list_playlist():
            self.__list_playlist.append(playlist_title)
        else:
            print(f"{playlist_title} is already created")
    
    def display_all_playlists(self):
        if self.get_list_playlist():
            for playlist in self.get_list_playlist():
                print(playlist)
                return True
        else:
            print('You have to create a playlist first')
            return False
