from machine import Pin, ADC, PWM
import utime

pot_value = ADC(0)
LED = PWM(Pin(7))

LED.freq(1000)

led_pin = machine.Pin(25, machine.Pin.OUT)

while True:
    LED.duty_u16(pot_value.read_u16())

while True:
    led_pin.value(1)
    utime.sleep(0.5)
    led_pin.value(0)
    utime.sleep(0.5)
    print("gugi")