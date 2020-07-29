import time
import busio
import adafruit_lps2x

i2c = busio.I2C()
# uncomment and comment out the line after to use with the LPS22
lps = adafruit_lps2x.LPS22(i2c, address=93)
# lps = adafruit_lps2x.LPS25(i2c)
while True:
    print("Pressure: %.2f hPa" % lps.pressure)
    print("Temperature: %.2f C" % lps.temperature)
    time.sleep(1)
                     