
import pyautogui
import keyboard
import time

print("Hover your mouse over the fields one-by-one and press Ctrl+Shift+P to capture.")
print("Press ESC to stop.\n")

positions = []

while True:
    if keyboard.is_pressed("ctrl+shift+p"):
        pos = pyautogui.position()
        print(f"Captured: {pos}")
        positions.append(pos)
        time.sleep(1)
    elif keyboard.is_pressed("esc"):
        break

print("\nCaptured Positions:")
for i, pos in enumerate(positions, 1):
    print(f"{i}. {pos}")