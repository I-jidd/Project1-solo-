from track import Track

class Playlist:
    def __init__(self):
        self.__p_title = None
        self.__total_duration = None
        self.__playlist_list = [] #lists of playlists
        self.__tracks = [] #lists of tracks on playlist
    #getters
    def get_playlist_title(self):
        return self.__p_title

    def get_playlist_lists(self):
        return self.__playlist_list
    
    def get_playlist_tracks(self):
        return self.__tracks
    
    def create_playlist(self, title):
        self.__p_title = title
        newPlaylist = self.__p_title
        
        if self.playlist_title not in self.get_playlist_lists():
            self.__playlist.append(newPlaylist)
            return True
        else:
            print(f"{newPlaylist} is already on exist")
            return False
    
    def add_track_on_playlist(self, track_title:Track):
        #enter the track_title
        #then magsearch sya if the title exist on music library
        #if it exists ma-add, else if 2 exists with the same title, mag-output ang 2 tracks with same title
        if self.get_playlist_lists():
            print('Please create a playlist')
            return False
        else:
            if track_title not in self.get_playlist_tracks():
                self.__tracks.append(track_title)
                print(f'{track_title} is successfully addded to track')
                return True
            else:
                print(f"{track_title} is already in the playlist")
                return False
    def display_tracks(self):
        pass
    def test(self):
        if self.get_playlist_lists():
            return True
        else:
            return False

p = Playlist()
p.add_track_on_playlist('In the end')
# print(p.test())