import RPi.GPIO as gpio



def decimal2binary(value): 
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


gpio.setmode(gpio.BCM)
dac = [10,9,11,5,6,13,19,26]
dac = list(reversed(dac))
gpio.setup(dac,gpio.OUT,initial = 1)
try:
    num = ''
    while num != 'q':
        print('Input number in range 0 - 255')
        num = input()
        
        if not num.isdigit():
            print('Its not a  number')
        elif '.' in num:
            print('Its not a integer number')
        else:
            num = int(num)
            if num > 255 or num < 0:
                print('Error: number out of range')
            else:
                binary_num = decimal2binary(num)
                gpio.output(dac, binary_num)

                print('The voltage: %f' % (3.3 / 256 * num))

finally:
    gpio.output(dac,0)
    gpio.cleanup()