import pyautogui
import time


def print_cursor_coordinates():
    while True:
        x, y = pyautogui.position()
        print(f"Cursor Position: x = {x}, y = {y}")
        time.sleep(0.5)


if __name__ == "__main__":
    try:
        print("Press Ctrl-C to stop the script.")
        print_cursor_coordinates()
    except KeyboardInterrupt:
        print("Script terminated by user.")
