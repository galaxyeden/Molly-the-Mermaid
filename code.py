import time
import board
from rainbowio import colorwheel
import neopixel
import digitalio
import pwmio

pixel_pin = board.GP22
led_left = pwmio.PWMOut(board.GP14)
led_right = pwmio.PWMOut(board.GP15)
body_pin_1 = board.GP0
body_pin_2 = board.GP1
button_up = digitalio.DigitalInOut(board.GP21)
button_down = digitalio.DigitalInOut(board.GP19)
button_left = digitalio.DigitalInOut(board.GP20)
button_right = digitalio.DigitalInOut(board.GP18)
button_a = digitalio.DigitalInOut(board.GP16)
button_b = digitalio.DigitalInOut(board.GP17)
raspberry_led = digitalio.DigitalInOut(board.GP25)

raspberry_led.direction = digitalio.Direction.OUTPUT

button_a.direction = digitalio.Direction.INPUT
button_b.direction = digitalio.Direction.INPUT
button_up.direction = digitalio.Direction.INPUT
button_down.direction = digitalio.Direction.INPUT
button_left.direction = digitalio.Direction.INPUT
button_right.direction = digitalio.Direction.INPUT

button_a.pull = digitalio.Pull.UP
button_b.pull = digitalio.Pull.UP
button_up.pull = digitalio.Pull.UP
button_down.pull = digitalio.Pull.UP
button_left.pull = digitalio.Pull.UP
button_right.pull = digitalio.Pull.UP

num_pixels = 5
eyes_count = 2
active_pixel = 2

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)
eyes = neopixel.NeoPixel(body_pin_1, eyes_count, brightness=0.1, auto_write=False)

def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        if button_a.value:
            break
        time.sleep(wait)

while True:
    led_left.duty_cycle = 200
    led_right.duty_cycle = 200
    eyes.fill([0, 80, 140])
    eyes.show()
    raspberry_led.value = False
    if button_up.value == False:
        active_pixel -= 1
        if active_pixel < 0:
            active_pixel = 4
    if button_down.value == False:
        active_pixel += 1
        if active_pixel > 4:
            active_pixel = 0
    pixels.fill([75, 0, 55])    
    pixels[active_pixel] = ([0, 80, 140])
    pixels.show()
    while button_left.value == False:
        led_left.duty_cycle = 15000
    while button_right.value == False:
        led_right.duty_cycle = 15000
    while button_b.value == False:
        eyes.fill([30, 0, 150])
        eyes.show()
        raspberry_led.value = True
    while button_a.value == False:
        rainbow_cycle(0.1)
    time.sleep(0.1)