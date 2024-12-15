import json
from playlist_queue import Circular_queue

menu = {
    'main':{
        1:'Play',
        2:'Create Playlist',
        3:'View Playlist',
        4:'Add track',
        5:'View tracks',
        6:'Exit'
    },
    'play':{
        1:'Play from Music Library',
        2:'Play from Playlist'
    }
}
queue = Circular_queue()

with open('musicLibrary.json', 'r') as file:
    music_library = json.load(file)

TRACKS = music_library['tracks']

def display(menu):
    for key, item in menu.items():
        print(f"[{key}] {item} ")

def main_menu():
    while True:
        display(menu['main'])
        try:
            choice = int(input('Enter your choice: '))
            
            if choice == 1:
                play()
            elif choice == 2:
                pass
        except ValueError:
            print('\nError. Please enter a valid input\n')

def play():
    while True:
        display(menu['play'])
        try:
            choice = input('Enter you choice or "e" to exit: ')
            
            if int(choice) == 1:
                play_musiclibrary()
            elif int(choice) == 2:
                play_playlist()
            elif choice == "e":
                break
        except ValueError:
            print('\nError. Please enter a valid input\n')

def play_musiclibrary():
    for track in TRACKS:
        queue.enqueue(track)

def play_next():
    queue.dequeue()

    

def play_playlist():
    print('playlist')
        
    

    
    
    
if __name__ == '__main__':
    main_menu()