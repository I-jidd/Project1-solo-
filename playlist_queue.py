#circular queue so that it can be repeated
import random

class Circular_queue:
    def __init__(self, size): #size will be then length of playlist
        self.size = size
        self.rear = self.front = -1
        self.queue = [None] * self.size
        self.history = []
        self.current_index = None
    
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    
    def is_empty(self):
        return self.front == -1
    
    def enqueue(self, title):
        next_rear = (self.rear + 1) % self.size
        
        if self.is_full():
            print('The queue is full and cannot be added. Thank you')
            return False
        else:
            if self.front == -1: #if added with the first element
                self.front = 0
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = title
    
    def dequeue(self):
        if self.is_empty():
            print('The queue is empty. Nothing to be remove')
            return False
    
        temp = self.queue[self.front]
        self.history.append(self.front)
        
        if self.rear == self.front:
            self.rear = self.front = -1
        self.front = (self.front + 1) % self.size
        return temp
    
    def shuffle_queue(self):
        if self.queue:
            shuffled = random.shuffle(self.queue)
            return shuffled
        else:
            print('The queue is empty. Nothing to shuffle')
            return False
    
    def play_next(self):
        track = self.dequeue()
        
        if track:
            self.current_index = self.front
            print(f'Playing next track: {track}')
        return track

    def play_previous(self):
        if not self.history:
            print('No previous track available.')
            return False
        prev_index = self.history.pop()
        self.current_index = prev_index
        track = self.queue[prev_index]
        print(f'Playing previous track: {track}')
        return track
    
    def display_queue(self):
        for tracks in self.queue:
            print(tracks)

        