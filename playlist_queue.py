#circular queue so that it can be repeated
import random

class Circular_queue:
    def __init__(self, size):    
        self.size = size
        self.rear = self.front = -1
        self.queue = [None] * self.size
        self.history = []
        self.currently_played = []
        self.current_track = 0
        self.items_per_page = 10
        self.is_repeat = False
        self.is_shuffle = False
    
    def is_empty(self):
        return self.front == 1
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def enqueue(self, track):
        if self.is_full():
            print('The queue is full and cannot be added.')
            return 
        
        if self.front == -1:
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = track
        
    def dequeue(self):
        if self.is_empty():
            print('The queue is empty. Nothing to be removed.')
            return
        
        track = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        return track

    def play_queue(self):
        current_track = self.dequeue()
        self.currently_played.append(current_track)
        track = self.currently_played[0]
        title = track['title']
        artist = track['artist']
        duration = track['duration']
        print(f'Currently playing: {title} - {artist} ({duration})')
        return current_track
    
    def play_next(self):
        track = self.currently_played.pop()
        self.history.append(track)
        self.play_queue()
    
    def play_previous(self):
        pass
        