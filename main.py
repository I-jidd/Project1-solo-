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
    },
    'settings': {
        1:'Pause',
        2:'Next',
        3:'Previous',
        4:'Shuffle',
        5:'Repeat',
        6:'Exit'
    }
}

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
    
    with open('musicLibrary.json', 'r') as file:
        music_library = json.load(file)

    TRACKS = music_library['tracks']

    queue = Circular_queue(len(TRACKS))
    for track in TRACKS:
        queue.enqueue(track)
    
    track = queue.play_queue()
    queue.queue_status(track)
    while True:
        if queue.is_pause():
            print('[1] Play')
        print('[1] Pause')
        print('[2] Next')
        print('[3] Previous')
        print('[4] Shuffle')
        print('[5] Repeat')
        print('[6] Exit')
        choice = int(input('Enter you choice: '))
        if choice == 1:
            queue.enable_pause()
            queue.queue_status(track)
        elif choice == 2:
            queue.play_next()
            queue.queue_status(track)
        elif choice == 3:
            previous = queue.play_previous()
            if not previous:
                queue.queue_status(track)
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            break
    
    

def play_playlist():
    print('playlist')
    

    
    
    
if __name__ == '__main__':
    main_menu()