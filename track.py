class Track:
    def __init__(self, title, artist, album, minutes, seconds, additional_artist = None):
        self.__title = title
        self.__artist = artist
        self.__album = album
        self.__duration = Duration(minutes, seconds)
        self.__additional_artist = additional_artist
    
    @property
    def title(self):
        return self.__title
    
    @property
    def artist(self):
        return self.__artist
    
    @property
    def album(self):
        return self.__album
    
    @property
    def duration(self):
        return self.__duration
    
    @property
    def additional_artist(self):
        return self.__additional_artist
    
    def __str__(self):
        return (f"Title: {self.title} \n"
                f"Artist: {self.artist}\n"
                f"Additional Artist: {self.additional_artist}\n"
                f"Album: {self.album} \n"
                f"Duration: {self.duration.getDuration()}")
    
class Duration:
    def __init__(self, minutes, seconds):
        self.__minutes = minutes
        self.__seconds = seconds
    
    @property
    def minutes(self):
        return self.__minutes
    
    @property
    def seconds(self):
        return self.__seconds
    
    @minutes.setter
    def minutes(self, new):
        if new < 0:
            raise ValueError('Minutes must not be negative')
        self.__minutes = new
        
    @seconds.setter
    def seconds(self, new):
        if new < 0 or new > 60:
            raise ValueError('seconds must not be negative/greater than 60')
        self.__seconds = new
    
    def getDuration(self):
        hr = 0
        minutes = self.minutes
        seconds = self.seconds
        
        if minutes >= 60:
            hr = minutes // 60
            minutes = minutes % 60
        
        if seconds == 60:
            minutes += 1
            seconds = seconds % 60
            
        return f"{hr}:{minutes:02}:{seconds:02}" if hr != 0 else f"{minutes:02}:{seconds:02}"
        
            
        
    