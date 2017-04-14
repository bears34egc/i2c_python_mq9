# ADXL345 Python library for Raspberry Pi
#
# author:  Jonathan Williamson
# license: BSD, see LICENSE.txt included in this package
#
# This is a Raspberry Pi Python implementation to help you get started with
# the Adafruit Triple Axis ADXL345 breakout board:
# http://shop.pimoroni.com/products/adafruit-triple-axis-accelerometer

import smbus, os
from time import sleep
from datetime import datetime
from pushbullet import Pushbullet

pb = Pushbullet('o.EZiuid3oCjU9aUM153BRs41bHYglKNee')

# busNumber = int(os.getenv("I2C_BUS"))

bus = smbus.SMBus(1)
sleep(.3)

# ADC121C_MQ9 address, 0x50(80)
# Read data back from 0x00(00), 2 bytes
# raw_adc MSB, raw_adc LSB
data = bus.read_i2c_block_data(0x50, 0x00, 2)
sleep(.3)
# Convert the data to 12-bits
raw_adc = (data[0] & 0x0F) * 256 + data[1]
ppm = (1000.0 / 4096.0) * raw_adc + 10



while True:
    # print "Carbon Monoxide Concentration : %.2f ppm" %ppm
    push = pb.push_note("the ppm is ", ppm)
    sleep(500)

