import json
from playlist_queue import Circular_queue

with open("musicLibrary.json", "r") as file:
    musicLibrary = json.load(file)

tracks = musicLibrary['tracks']
queue = Circular_queue(len(tracks))

for track in tracks:
    queue.enqueue(track)

def display_page(tracks, page, items_per_page = 10):
    total_tracks = len(tracks)
    total_pages = (total_tracks + items_per_page - 1)// items_per_page
    start_index = (page - 1) * items_per_page
    end_index = start_index + items_per_page
    
    if start_index >= total_tracks or page <= 0:
        print(f"Invalid page number. Please choose between 1 and {total_pages}.")
        return

    print(f"Page {page} of {total_pages}")
    print("-" * 40)
    idx = 0
    for track in tracks[start_index:end_index]:
        idx += 1
        title = track['title']
        artist = track['artist']
        duration = track['duration']
        if 'additional_artist(s)' in track:
            print(f"({idx}) {title} - {artist},{track['additional_artist(s)']} ({duration})")
        print(f"({idx}) {title} - {artist} ({duration})")
    print("-" * 40)

queue.play_next()
queue.play_next()
queue.play_next()
queue.play_next()
queue.play_previous()