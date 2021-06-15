I2CBUS = 1
ADDRESS = 0x38
from RPi import GPIO
import smbus
import time
E = 21
RS = 20

I2CBUS = 1
# class i2c_device:
#     def __init__(self,addr, port=I2CBUS):
#         self.addr = addr
#         self.bus = smbus.SMBus(port)
    
class i2c_device:
    def __init__(self,addr,port=I2CBUS):
        self.addr = addr
        self.bus = smbus.SMBus(port)

    def write_cmd(self, cmd):
        self.bus.write_byte(self.addr, cmd)
        time.sleep(0.0001)

class lcd():
    def __init__(self):
        self.lcd_device = i2c_device(ADDRESS)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(E, GPIO.OUT)
        GPIO.setup(RS,GPIO.OUT)
        self.lcd_write(0b00111000)
        self.lcd_write(0b00001100)
        self.lcd_write(0b00000001)
        time.sleep(0.2)

    def lcd_write(self, value):
        GPIO.output(RS,GPIO.HIGH)
        self.lcd_write_eight_bits(value)
        GPIO.output(E, GPIO.LOW)
        GPIO.output(E,GPIO.HIGH)
        time.sleep(0.01)
    
    def lcd_write_eight_bits(self,value):
        GPIO.output(RS,GPIO.LOW)
        self.lcd_device.write_cmd(value)
        GPIO.output(E, GPIO.LOW)
        GPIO.output(E,GPIO.HIGH)
        time.sleep(0.01)

    def send_char(self,value):
        GPIO.output(RS, GPIO.HIGH)
        self.lcd_device.write_cmd(value)

        GPIO.output(E,GPIO.LOW)
        GPIO.output(E, GPIO.HIGH)
        time.sleep(0.01)

    def lcd_display_string(self, string, line=1):
        if line == 1:
            pos_new = 0x00
        elif line == 2:
            pos_new = 0x40
    

        self.lcd_write(0x80 + pos_new)

        for char in string:
            self.send_char(ord(char))
