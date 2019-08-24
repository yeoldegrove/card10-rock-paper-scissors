import display
import bhi160
import leds
import utime
import urandom
import color

def rules():
    text1 = "Let's play!"
    text2 = "3 rounds!"
    text3 = "Shake Me!"
    disp.clear()
    disp.print(text1, fg=(255, 0, 0), posy=20)
    disp.print(text2, fg=(255, 0, 0), posy=42)
    disp.print(text3, fg=(255, 0, 0), posy=64)
    disp.update()

def rock():
    disp.clear()
    disp.circ(70, 50, 20, size=3, filled=True)
    disp.circ(80, 40, 15, size=3, filled=True)
    disp.circ(60, 30, 17, size=3, filled=True)
    disp.update()

def paper():
    disp.clear()
    disp.rect(30, 20, 110, 60, col=None, filled=True, size=1)
    disp.update()

def scissors():
    disp.clear()
    disp.line(30, 30, 90, 60, size=2)
    disp.line(30, 60, 90, 30, size=2)
    disp.circ(100, 26, 10, size=3, filled=0)
    disp.circ(100, 62, 10, size=3, filled=0)
    disp.update()

def check():
    leds.set_all([
        color.WHITE,
        color.WHITE,
        color.WHITE,
        color.WHITE,
        color.WHITE,
        color.WHITE,
        color.WHITE,
        color.WHITE,
        color.WHITE,
        color.WHITE,
        color.WHITE,
        color.WHITE,
        color.WHITE,
        color.WHITE,
        color.WHITE,
        ])
    utime.sleep(1)
    leds.clear()

disp = display.open()
items = [rock, paper, scissors]
sensor = bhi160.BHI160Accelerometer()
threshold = 2.0

# shake
# kudos to https://badge.team/projects/schnick_schnack_schnuck
while True:
    rules()
    round = 0
    while round < 3:
        samples = sensor.read()
    
        if len(samples) > 0:
            sample = samples[0]
    
            x = abs(sample.x)
            y = abs(sample.y)
            z = abs(sample.z)
    
            value = x + y + z
            if (value > threshold):
                check()
                urandom.choice(items)()
                utime.sleep(2)
                round += 1
