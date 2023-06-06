from aiy.voice import tts
from aiy.leds import Leds, Color
from aiy.board import Board
import time
Leds().update(Leds.rgb_off())
i = 0
while i == 0 :
    i = 2
    Leds().update(Leds.rgb_off())
    tts.say("please press the button to run the program.")
    Board().button.wait_for_press()
    tts.say("please input the color code for red.")
    r = int(input("Please input color code R"))
    if 0 < r < 256:
        g = int(input("Please input color code G"))
        if 0 < g < 256:
            b = int(input("Please input color code B"))
            if 0 < b < 256:
                Leds().update(Leds.rgb_on((r ,g ,b)))
                time.sleep(5)
                i = 0
            else:
                tts.say("see you soon")
                i = 1
        else:
            tts.say("see you soon")
            i = 1
    else:
        tts.say("see you soon")
        i = 1

if i == 1:
    Leds().update(Leds.rgb_on(Color.RED))
    time.sleep(1)
    Leds().update(Leds.rgb_on(Color.GREEN))
    time.sleep(1)
    Leds().update(Leds.rgb_on(Color.BLUE))
    time.sleep(1)
    Leds().update(Leds.rgb_off())
