chee1# Write your code here :-)
from microbit import *
from gesture import *
import random

angles = [20, 50, 80, 100, 60, 120]

ges = Gesture()

while True:

    g = ges.read()

    if g == 'right':
        pin0.write_analog(180)
        sleep(1000)
        pin0.write_analog(25)
        sleep(1000)
    elif g == 'left':
        pin0.write_analog(100)
        sleep(1000)
        pin0.write_analog(30)
        sleep(1000)
    elif g == 'up':
        pin0.write_analog(random.choice(angles))