import os

# func to save and load settings
def save_settings(time_on, value):
    with open('settings.txt', 'w') as f:
        f.write(str(time_on) + '\n')
        f.write(str(value) + '\n')

def load_settings():
    if 'settings.txt' in os.listdir():
        with open('settings.txt', 'r') as f:
            lines = f.readlines()
            time_on = lines[0].strip()
            print(time_on)
            print(type(time_on))
            if time_on != 'False':
                time_on = int(time_on)
            value = int(lines[1].strip())
            return time_on, value
    else:
        return None, 10000  # default values if no settings file found
