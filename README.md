# Marui M3 Super 90 Counter

Hello everyone, this is a little project to upgrade your Marui M3 Super 90 shotgun!

I created this project because it's very difficult to count shots when you play airsoft with a shotgun. This shotgun fires 3 rounds at a time, and with 30 BBs per shell, you have only 10 shots. So I thought to fix this problem with a Raspberry Pi Pico W, a 3D printer, and a little code.

It's very easy to use, just some little soldering and time, and you will be able to play better with your shotgun!

## How to Use

Starting the counter (by inserting batteries), the Raspberry Pi Pico will start a hotspot connection called 'RPI_PICO_AP'*. Connect to the network on your phone, tablet, or PC with the password: '12345678'. (You can change the network name and password in the `main.py` file). Now open your browser and go to `192.168.4.1`. A web page will appear.

![Image](img/Screenshot_20230714_171331_Chrome.jpg)

Here you can set the time to choose if you want the LEDs to turn down after some time (useful for night games!) and adjust the LED brightness. The brightness ranges from 0 (no light) to 65000 (max power), and by clicking "increase" and "decrease," the LEDs will change brightness.

After choosing your settings, you can click "start," and the LEDs will turn off. Your settings will be saved in a file called `settings.txt`. After that, you cannot change the settings; you must reload the device by pulling and pushing the battery again.

*You have only 60 seconds to access the web page; otherwise, the device will load the saved settings.

## Features

- **Shot Counting**: The system keeps track of the number of shots fired and displays the count via the LEDs.
- **Web Interface**: Control the device via a web interface to adjust LED brightness and set a time for LEDs to turn off.
- **Setting Saving**: Settings such as brightness value and time are saved in a file and can be loaded between sessions.

## Circuit Diagram

- **Red LED**: Connected to pin 5.
- **Green LED**: Connected to pin 13.
- **Button (Endstop)**: Connected to pin 0, configured with pull-up.
