import RPi.GPIO as gpio
import time


def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

gpio.setmode(gpio.BCM)
dac = [10,9,11,5,6,13,19,26]
dac = list(reversed(dac))
gpio.setup(dac,gpio.OUT,initial = 1)
period = float(input("Введите значение периода в сек"))
try:
    _range = list(range(256)) + list(range(254, 0, -1))
    print(_range)
    for num in _range:
        gpio.output(dac, decimal2binary(num))
        time.sleep(period / 512)

finally:
    gpio.output(dac,0)
    gpio.cleanup()
