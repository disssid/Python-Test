import Adafruit_BBIO.GPIO as GPIO
import time as t

TIME = 5
TIME_HEATER = 15

GPIO.setup("P8_8",GPIO.OUT)
GPIO.setup("P8_10",GPIO.OUT)
GPIO.setup("P8_12",GPIO.OUT)
GPIO.setup("P9_23",GPIO.OUT)
GPIO.setup("P9_27",GPIO.OUT)

print("GPIO setup successful")
print("P8_08 : Red   LED")
print("P8_10 : Green LED")
print("P8_12 : Blue  LED")
print("P9_23 : Fan")
print("P9_27 : Heater")

print("**********************************")
print("Testing each pins for High and Low")
print("**********************************")

print("-------------------------")
print("Testing P8_08 : Red   LED")

GPIO.output("P8_8",GPIO.HIGH)
print("Check if the Red LED is On")

t.sleep(TIME)

GPIO.output("P8_8",GPIO.LOW)
print("Check if the Red LED is Off")
 
print("Testing P8_10 : Green  LED")

GPIO.output("P8_10",GPIO.HIGH)
print("Check if the Green LED is On")

t.sleep(TIME)

GPIO.output("P8_10",GPIO.LOW)
print("Check if the Green LED is Off")

print("Testing P8_12 : Blue  LED")

GPIO.output("P8_12",GPIO.HIGH)
print("Check if the Blue LED is On")

t.sleep(TIME)

GPIO.output("P8_12",GPIO.LOW)
print("Check if the Blue LED is Off")
 
GPIO.output("P9_23",GPIO.HIGH)
print("Check if the Fan is On")

t.sleep(TIME)

GPIO.output("P9_23",GPIO.LOW)
print("Check if the Fan is Off")
 
GPIO.output("P9_27",GPIO.HIGH)
print("Check if the Heater is On (this check remains on for"+ TIME_HEATER +"seconds)")

t.sleep(TIME_HEATER)

GPIO.output("P9_27",GPIO.LOW)
print("Check if the Heater is Off")
