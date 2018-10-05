import pygame.mixer
import time

def sound(fn):
    pygame.mixer.init()
    pygame.mixer.music.load(fn)
    pygame.mixer.music.play(1)
    time.sleep(2)
    pygame.mixer.music.stop()

for i in range(30):
    sound("sitdown.wav")
    time.sleep(6)
    sound("little.wav")
    time.sleep(2)
    sound("up.wav")
    time.sleep(5)
    if i==24:sound("little.wav")
