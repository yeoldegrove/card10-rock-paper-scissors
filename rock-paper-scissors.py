import leds
import utime
import display
import urandom
import light_sensor
import leds
import color

def rock():
    with display.open() as disp:
        disp.clear()
        disp.circ(70, 50, 20, size=3, filled=True)
        disp.circ(80, 40, 15, size=3, filled=True)
        disp.circ(60, 30, 17, size=3, filled=True)
        disp.update()

def paper():
    with display.open() as disp:
        disp.clear()
        disp.rect(30, 20, 110, 60, col=None, filled=True, size=1)
        disp.update()

def scissors():
    with display.open() as disp:
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


# clear
with display.open() as disp:
    disp.clear()
    disp.update()

# items
items = [rock, paper, scissors]

# rules
text1 = "Let's play!"
text2 = "cover me..."

with display.open() as disp:
    disp.print(text1, fg=(255, 0, 0), posx=80 - round(len(text1) / 2 * 14), posy=20)
    disp.print(text2, fg=(255, 0, 0), posx=80 - round(len(text1) / 2 * 14), posy=42)
    disp.update()


light_sensor.start()

threshold = 25
while True:
    light = light_sensor.get_reading()
    if light < threshold:
        check()
        urandom.choice(items)()

light_sensor.stop()

