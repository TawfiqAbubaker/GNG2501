from pynput.mouse import Button, Controller
from pynput import keyboard

mouse = Controller()


def on_press(key):
    try:
        if key.char == 'p':
            with open('sens.txt','r') as f:
                contents = f.readlines()
            contents[0] = contents[0][:len(contents[0]) - 1]
            mouse.scroll(0,-int(contents[0]))
        elif key.char == 'o':
            with open('sens.txt','r') as f:
                contents = f.readlines()
            contents[0] = contents[0][:len(contents[0]) - 1]
            mouse.scroll(0,int(contents[1]))
        # print('alphanumeric key {0} pressed'.format(
        #     key.char))
    except AttributeError:
        print('special key {0} pressekkd'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
