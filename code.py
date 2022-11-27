import os
import ipaddress
import wifi
import socketpool
import board
import digitalio
import time
import neopixel

from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.group import AnimationGroup
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.color import PURPLE, AMBER, JADE, WHITE
from adafruit_led_animation import helper
#Wifi connection
print("connecting to WiFi")
wifi.radio.connect('INFECTED 2','adampete')
print("Connected to WIFI!")
print("My IP Address: ", wifi.radio.ipv4_address)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT
led.value = True

#import of LED configuration
pixel_pin = board.GP16
pixel_num = 32
pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.1, auto_write=False)

WHITELOW=(100,100,100)
WHITEHIGH=(255,255,255)
BLACK=(0,0,0)

def colorwheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0, 0)
    if pos < 85:
        return (255 - pos * 3, pos * 3, 0, 0)
    if pos < 170:
        pos -= 85
        return (0, 255 - pos * 3, pos * 3, 0)
    pos -= 170
    return (pos * 3, 0, 255 - pos * 3, 0)


def color_chase(color, wait):
    for i in range(pixel_num):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(pixel_num):
            rc_index = (i *255 // pixel_num) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)
        
def solid_color():
    
    solid = Solid(pixels,color=WHITE)
    solid.animate()
def blink():
    
    colormax = 255
    
    for i in range(colormax):
        
        
        
        
def icicle():
    dripspeed = 0.08
    dropspeed = 0.015
    icicleLength = 8
    for i in range(icicleLength):
        pixels[i] = WHITELOW
    pixels.show()
    #brighten for drops
    for i in range(icicleLength):
        time.sleep(dripspeed)
        dripspeed = dripspeed +0.02
        if pixels[i] != 1:
            pixels[i-1] = WHITELOW
        pixels[i] = WHITEHIGH
        pixels.show()
    time.sleep(0.5) 
    pixels[icicleLength-1] = WHITELOW
#	  begin drop function
#     pixel_num
    for i in range(9,32):
        time.sleep(dropspeed)
#         dropspeed = dripspeed -0.01
        if pixels[i] != 9:
            pixels[i-1] = BLACK
        pixels[i] = WHITEHIGH
        pixels.show()  
    
def turn_off():
    pixels.fill(BLACK)
    pixels.show()


while True:
    icicle()
    
    



    
