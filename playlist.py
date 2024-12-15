from track import Track

class Playlist:
    def __init__(self):
        self.__p_title = None
        self.__total_duration = None
        self.__tracks = [] # key of title and value of tracks
        self.__playlist = {} #dictionary: key of p_title and value of __tracks
    #getters
    def get_playlist_title(self):
        return self.__p_title

    def get_playlist_lists(self):
        return self.__playlist_list
    
    def get_playlist_tracks(self):
        return self.__tracks
    
    def get_playlist(self):
        return self.__playlist
    
    def create_playlist(self, title):
        self.__p_title = title
        self.__playlist = {self.__p_title:self.__tracks}
        
    def add_track_on_playlist(self, track_title:Track):
        #enter the track_title
        #then magsearch sya if the title exist on music library
        #if it exists ma-add, else if 2 exists with the same title, mag-output ang 2 tracks with same title
        playlist = self.__playlist
        if playlist:
            if track_title not in self.get_playlist_tracks():
                playlist[self.get_playlist_title()].append(track_title)
                return True
            else:
                print(f"{track_title} is already in the playlist")
                return False
        else:
            print('Please create a playlist')
            return False
            
    def display_tracks(self):
        playlist = self.__playlist
        if playlist:
            idx = 0
            for track in playlist[self.get_playlist_title()]:
                idx += 1
                print(f"[{idx}] {track}")
        else:
            print('please create a playlist')
            return False