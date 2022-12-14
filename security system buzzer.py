'''
Example: Measure distance using Ultrasonic sensor and display results on LED matrix in micro:bit
By: Meqdad Darwish
'''
from microbit import *
from ultrasonic import Ultrasonic

# default pins in Ultrasonic class are:
# trigger: pin13
# echo: pin15

ultrasonic_sensor = Ultrasonic()
# or
# ultrasonic_sensor = Ultrasonic(trig=pin13, echo=pin15)

while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    if distance_value > 15:
        pin0.write_digital(0)
        pin1.write_digital(1)
    if distance_value < 15:
        pin0.write_digital(1)
        pin1.write_digital(0)
        
    # sleep(2000)