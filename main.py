import socket
import network
import gc
import select
import os
import utime

from web_page import web_page
import settings
import leds

# connection's variable
gc.collect()

ssid = 'RPI_PICO_AP'
password = '12345678'

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)

# access point check
while ap.active() == False:
    pass

print('Connection is successful')
print(ap.ifconfig())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

poller = select.poll()
poller.register(s, select.POLLIN)

running = True
timeout = 60000

time_on, value = settings.load_settings()

check_timer = 0

while running:
    res = poller.poll(timeout)
    
    if res:
        conn, addr = s.accept()
        print('Got a connection from %s' % str(addr))
        request = conn.recv(1024)
        request = str(request)
        print('Content = %s' % request)
        request_line = request.split('\n')[0]
        request_line = request_line.split(' ')[1]

        if request_line == '/increase' and 5000 <= value <= 60000:
            value += 5000
            leds.leds_together(value)
        
        elif request_line == '/increase' and value <= 5000:
            value += 500
            leds.leds_together(value)
        
        elif request_line == '/decrease' and value > 5000:
            value -= 5000
            leds.leds_together(value)
        
        elif request_line == '/decrease' and value <= 5000:
            value -= 500
            leds.leds_together(value)
            
        elif request_line.startswith('/set_time'):
            time_on_str = request_line.split('?')[1].split('=')[1]
            time_on = int(time_on_str)
            check_timer = 1
            print('Time on set to %s ms' % time_on)

        elif request_line == '/start':
            if check_timer == 0:
                time_on = 'False'
            
            leds.save_value(value)
            leds.leds_together(0)
            settings.save_settings(time_on, value) # saving settings
            running = False

        response = web_page(value)
        conn.send('HTTP/1.0 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('\n')
        conn.sendall(response)
        conn.close()

    else:  # if no connection within timeout
        print("Timeout: no connection within 30 seconds.")
        led_light = 65000
        running = False
        print('no devices connected')
        leds.flash_if_not_connected(led_light)

    if not running:
        break

brightness = value

while True:
    counter = 10
    while counter > 0:
        current_time = utime.ticks_ms()
        
        if leds.endstop.value() != leds.previous_state and not leds.endstop.value():
            if utime.ticks_diff(current_time, leds.last_change) > 100:
                leds.previous_state = leds.endstop.value()
                leds.last_change = current_time
                counter -= 1
                print(counter)
                leds.led_on(counter, brightness)
                leds.led_timer = current_time 

        elif leds.endstop.value():
            leds.previous_state = leds.endstop.value()

        if time_on != 'False' and utime.ticks_diff(current_time, leds.led_timer) > time_on:
            leds.leds_together(0)
            
        utime.sleep_ms(10)
