import pyautogui
import time

def get_mouse_coordinates():
    try:
        while True:
            x, y = pyautogui.position()
    except KeyboardInterrupt:
        print(f"Mouse coordinates: X: {x}, Y: {y}")
    return x,y

#Mouse coordinates: X: 1363, Y: 162

def click_next_button():
    try:
        while True:
            x, y = 1363, 162
            pyautogui.moveTo(x, y)
            pyautogui.click()
            time.sleep(5)  # allow the next page to load
    except KeyboardInterrupt:
        print("Automation stopped by user.")

click_next_button()