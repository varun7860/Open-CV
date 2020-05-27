import pyfirmata

board = pyfirmata.Arduino('com8')
servo_pin1 = board.get_pin('d:Pin Number:s')
servo_pin2 = board.get_pin('d:Pin Number:s')
servo_pin3 = board.get_pin('d:Pin Number:s')
servo_pin4 = board.get_pin('d:Pin Number:s')

'''  here "d" means digital pin . you can also use "a" for analog pin '''
