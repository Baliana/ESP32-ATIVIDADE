from machine import Pin 
from utime import sleep

ledGreen = Pin(16,Pin.OUT)
ledYellow = Pin(15,Pin.OUT)
ledRed = Pin(14,Pin.OUT)

while True:
    ledGreen.on()
    print("ledGreen ON,ligado")
    sleep(20)
    ledGreen.off()
    print("led OFF, desligado!")
    sleep(0.5)

    ledYellow.on()
    print("ledYellow ON,ligado")
    sleep(10)
    ledYellow.off()
    print("led OFF, desligado!")
    sleep(0.5)

    ledRed.on()
    print("ledRed ON,ligado")
    sleep(7)
    leledRedd.off()
    print("led OFF, desligado!")
    sleep(0.5)