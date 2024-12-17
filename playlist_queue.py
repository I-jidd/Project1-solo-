#circular queue so that it can be repeated
import json
import random as random

class Circular_queue:
    def __init__(self, size):    
        self.size = size
        self.rear = self.front = -1
        self.queue = [None] * self.size
        self.history = []
        self.currently_played = []
        self.current_track = 0
        self.items_per_page = 10
        self.repeat = False
        self.shuffle = False
        self.pause = False
        self.queue_copy = self.queue # this is the copy of the entire queue for repeat option
        
    def is_empty(self):
        return self.front == -1
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def is_repeat(self):
        return 'Yes' if self.repeat else 'No'
    
    def is_shuffle(self):
        return 'Yes' if self.shuffle else 'No'
    
    def is_pause(self):
        return '(Paused)' if self.pause else ''
    
    def is_repeat(self):
        return 'Yes' if self.repeat else ' No'
        
    def repeat_play(self):
        current_track = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.rear = (self.rear + 1) % self.size
        return current_track
    
    def repeat_next(self):
        self.front = (self.front + 1) % self.size
        self.rear = (self.rear + 1) % self.size
        return self.queue_copy[self.front]
    
    def repeat_previous(self):
        self.front = (self.front - 1) % self.size
        self.rear = (self.rear - 1) % self.size
        return self.queue_copy[self.front]
    
    def repeat_shuffle(self):
        queue = self.queue_copy
        shuffle_queue = random.shuffle(queue)
        self.enable_shuffle()
        print('Queue has been shuffled.')
        return shuffle_queue
    
    def enable_repeat(self):
        if self.repeat:
            self.repeat = False
        else:
            self.repeat = True
        return self.repeat
    
    def enable_shuffle(self):
        if self.shuffle:
            self.shuffle = False
        else:
            self.shuffle = True
        return self.shuffle
    
    def enable_pause(self):
        if self.pause:
            self.pause = False
        else:
            self.pause = True
        return self.pause
    
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
        return current_track
    
    def queue_status(self, track):
        if self.repeat:
            track = self.queue_copy[self.front]
        else:
            track = self.currently_played[-1]
        title = track['title']
        artist = track['artist']
        duration = track['duration']
        
        print(f'\nTotal Duration: ')
        print(f'Shuffled: {self.is_shuffle()}')
        print(f'Repeat: {self.is_repeat()}')
        print('Tracks:\n')
        print(f'Currently playing {self.is_pause()}: {title} - {artist} ({duration})\n')
    
    def play_next(self):
        track = self.currently_played.pop()
        self.history.append(track)
        self.play_queue()
    
    def play_previous(self):
        if self.history:
            track = self.history.pop()
            self.currently_played.append(track)
            self.queue_status(track)
            return track
        else:
            print("\nThere's no available tracks.")
            return False
    
    def shuffle_queue(self):
        queue = self.queue
        shuffle_queue = random.shuffle(queue)
        self.enable_shuffle()
        print('Queue has been shuffled.')
        return shuffle_queue
    
    

# with open('musicLibrary.json', 'r') as file:
#     music_library = json.load(file)

# TRACKS = music_library['tracks']

# q = Circular_queue(len(TRACKS))
# for track in TRACKS:
#     q.enqueue(track)
# q.enable_repeat()
# track = q.repeat_previous()
# q.queue_status(track)
# track = q.repeat_next()
# q.queue_status(track)