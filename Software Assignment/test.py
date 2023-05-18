import vlc
import os
import sys
import numpy as np
from pynput import keyboard
# import time
# import tty
# import termios
# import select
# import traceback

# player = vlc.MediaPlayer()

media = []

instance = vlc.Instance()
player = instance.media_player_new()

folder_path = '/home/vaibhav/Downloads'
file_list = os.listdir(folder_path)
video_files = [f for f in file_list if f.endswith('.mp4')]

for video_file in video_files:
    video_path = os.path.join(folder_path, video_file)
    # media.append(vlc.Media(video_path))
    media.append(instance.media_new(video_path))
    print(f"loading video: {video_file}")
# media.append(instance.media_new(os.path.join(folder_path, "1 SECOND VIDEO (NOT CLICKBAIT).mp4")))
# media1 = vlc.Media('/home/vaibhav/Downloads/IMG_0571.mp4')
# media2 = vlc.Media('/home/vaibhav/Downloads/IMG_0570.mp4')

n_songs = len(media)
array = np.arange(n_songs)
np.random.shuffle(array)
random_numbers = list(array)

current = random_numbers[0]
random_numbers.remove(current)
player.set_media(media[current])
player.play()


def play_next():
    global player
    global random_numbers
    global array
    global current
    player.pause()
    if(len(random_numbers)==0):
        # random_numbers = list(range(20))
        # random.shuffle(random_numbers)
        np.random.shuffle(array)
        random_numbers = list(array)    
    choice = random_numbers[0]
    random_numbers.remove(choice)
    # player = instance.media_player
    instance = vlc.Instance()
    player = instance.media_player_new()
    events = player.event_manager()
    
    
    events.event_attach(vlc.EventType.MediaPlayerEndReached, video_end_handle)
    player.set_media(media[choice])
    current = choice
    player.play()


# Create a function to handle keyboard events
def on_key_press(key):
    if key == keyboard.Key.space:
        play_next()
    elif key == keyboard.KeyCode.from_char('q'):
        player.stop()
        sys.exit()
        
def video_end_handle(event):
    if event.type == vlc.EventType.MediaPlayerEndReached:
        play_next()

events = player.event_manager()
events.event_attach(vlc.EventType.MediaPlayerEndReached, video_end_handle)

# Create a listener for keyboard events
listener = keyboard.Listener(on_press=on_key_press)
listener.start()

while(True):
    pass