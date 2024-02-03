import time
import pyautogui
import keyboard

def simulate_key_press(key, duration=0.1):
    pyautogui.press(key)
    time.sleep(duration)

def simulate_mouse_movement(x, y):
    pyautogui.moveTo(x, y)

def simulate_mouse_click(button='left', clicks=1, interval=0.1):
    pyautogui.click(button=button, clicks=clicks, interval=interval)



def main():
        while True:
            # ---------- Change p to whatever key you want your macro to be on ---------- #
            if keyboard.read_key() == "p":
                # Key press
                simulate_key_press('6')  # Simulate pressing the '6' key

                # Mouse things
                # Move and click 1
                simulate_mouse_movement(2050, 900)  # Move the mouse to coordinates (2050, 900)
                time.sleep(0.5)  # Pause for 0.2 second
                simulate_mouse_click()  # Simulate a left mouse click

                # Move and click 2
                #simulate_mouse_movement(1000, 500)  # Move the mouse to coordinates (1000, 500)
                time.sleep(0.5)  # Pause for 0.2 second
                simulate_mouse_click()  # Simulate a left mouse click

                # Move and click 3
                simulate_mouse_movement(1540, 540)  # Move the mouse to coordinates (1000, 1000)
                time.sleep(0.5)  # Pause for 0.2 second
                simulate_mouse_click()  # Simulate a left mouse click

            # ---------- Escape the scripting ---------- #
            elif keyboard.read_key() == "esc":
                 break


main()