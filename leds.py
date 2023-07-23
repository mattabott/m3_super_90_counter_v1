from machine import Pin, PWM
import utime

#button's variables
endstop = Pin(0, Pin.IN, Pin.PULL_UP)

previous_state = endstop.value()
last_change = utime.ticks_ms()

#PWM for leds
led_red = PWM(Pin(5)) 
led_green = PWM(Pin(13))

led_timer = 0

def save_value(value):
    print('Saving value: %s' % value)

def leds_together(value):
    led_red.duty_u16(value)
    led_green.duty_u16(value)

def flash_if_not_connected(value):
    for i in range(5):
        leds_together(value)
        
        utime.sleep(1)
    
        leds_together(0)
        
        utime.sleep(1)

def led_on(num, brightness):
    led_red.duty_u16(0)
    led_green.duty_u16(0)
    
    if num > 1:
        led_green.duty_u16(brightness)
    
    if 0 < num < 5:        
        led_red.duty_u16(brightness)
