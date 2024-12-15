#circular queue so that it can be repeated
import random

class Circular_queue:
    def __init__(self, size): #size will be then length of playlist
        self.size = size
        self.rear = self.front = -1
        self.queue = [None] * self.size
    
    def enqueue(self, title):
        next_rear = (self.rear + 1) % self.size
        
        if next_rear == self.front:
            print('The queue is full and cannot be added. Thank you')
            return False
        else:
            if self.front == -1: #if added with the first element
                self.front = 0
            self.rear = next_rear
            self.queue[self.rear] = title
    
    def dequeue(self):
        if self.rear == self.front == -1:
            print('The queue is empty. Nothing to be remove')
            return False
        else:
            temp = self.queue[self.front]
            self.queue[self.front] = None
            
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
    
    def display_queue(self):
        for tracks in self.queue:
            print(tracks)

    