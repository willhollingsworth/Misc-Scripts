from pyautogui import click,hotkey,keyDown,press,keyUp,mouseDown,mouseUp,moveTo,position
from time import sleep
from datetime import datetime

'''     coordinates of left seek bar for google music
        x start, x end, y '''
l_seek_coords= (1,1704,1330) 
l_focus = (335,1357) # blank area of window, used to focus area
l_play = (83,1360) # play button

'''     coordinates of second seek bar'''
r_seek_coords = (2281,2876,1376)
r_focus = (2378,1338)
r_play = (2581,1341)
'''     total pixel size of seek bar'''

l_seek_size = l_seek_coords[1] - l_seek_coords[0]
r_seek_size = r_seek_coords[1] - r_seek_coords[0]

left_active =  True

def cclick(coords,delay=.2):
    sleep(delay)
    mouseDown(coords,button='left')
    sleep(.1)
    mouseUp(coords,button='left')
    sleep(delay)

def seek_to_percent(side='left',percent=10):
    if side == 'left':
        coords = l_seek_coords
        cclick(l_focus)
    else:
        coords = r_seek_coords
        cclick(r_focus)
    seek_size = coords[1] - coords[0]
    seek_pixel_pos = int( coords[0] + seek_size*percent/100) 
    cclick((seek_pixel_pos,coords[2]))

def run_loop(percent=10,times=1,duration=5): 
    setup_system_percent(percent)     
    for x in range(times):
        if x == 0:
            alttab()
            hotkey('space')
        seek_to_percent('right',percent)
        cclick(l_focus)
        sleep(duration)
        transition(r_play)
        seek_to_percent('left',percent)
        cclick(r_focus)
        sleep(duration)
        if x == times-1:
            hotkey('space')
            continue
        transition(l_play) 
    finish()

def transition(coords):
    moveTo(coords)
    hotkey('space')
    click()

def setup_system_percent(percent=0):
    global mousepos 
    mousepos = position()
    seek_to_percent('left',percent)
    seek_to_percent('right',percent)

def setup_system_sec(sec=0):
    global mousepos 
    mousepos = position()
    seek_to_secs(sec)
    switch_focus
    seek_to_secs(sec)

def finish():
    alttab(1)
    moveTo(mousepos)

def switch_focus():
    if left_active: cclick(r_focus)
    else : cclick(l_focus)
    left_active = not left_active # toggle active side

def alttab(repeat=0):
    for x in range(repeat+1):
        keyDown('alt')
        keyDown('tab')
        # sleep(.1)
        hotkey('enter')
        keyUp('tab')
        keyUp('alt')

def convert_time_to_secs(input):
    mins,secs = input.split(':')
    total =  int(mins) * 60 + int(secs)
    if not total : return 1
    else : return total

def player_swapper(start_time='0:10',swap_duration=2,swap_count=1,song_duration='2:40'):
    global song_length_seconds
    song_length_seconds = convert_time_to_secs(song_duration)
    l_pps = l_seek_size / song_length_seconds  # pixels per sec of song
    r_pps = r_seek_size / song_length_seconds

    l_duration_pixels_length = l_pps * swap_duration
    r_duration_pixels_length = r_pps * swap_duration
 
    next_seek = 0
    current_pos_secs = 0
    start_sec = convert_time_to_secs(start_time)   
    setup_system_sec(start_sec)
    # for x in range(swap_count):
    #     if x == 0:
    #         alttab()
    #         hotkey('space')
    #     current_pos_secs += swap_duration 

    #     left_active = not left_active # toggle active side

def calc_current_place():
    pass

def calc_prnt_from_sec(secs):
    return  secs / song_length_seconds 


def seek_to_secs(secs):
    if left_active : seek_coords,seek_size = r_seek_coords,r_seek_size
    else : seek_coords,seek_size = l_seek_coords,l_seek_size
    increment_seek = seek_size * calc_prnt_from_sec(secs)
    seek_pixel_pos = int( seek_coords[0] + increment_seek) 
    cclick((seek_pixel_pos,seek_coords[2]))

player_swapper('0:30',2,2,'2:40')
# run_loop(10,3,1)  
# setup_system(percent)
# finish()    

