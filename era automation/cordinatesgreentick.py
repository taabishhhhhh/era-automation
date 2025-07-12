import pyautogui
import time

print("Move your mouse to TOP-LEFT corner of tick area in 5 seconds...")
time.sleep(5)
top_left = pyautogui.position()
print("Top-left corner:", top_left)

print("Now move to BOTTOM-RIGHT corner of tick area in 5 seconds...")
time.sleep(5)
bottom_right = pyautogui.position()
print("Bottom-right corner:", bottom_right)

width = bottom_right.x - top_left.x
height = bottom_right.y - top_left.y
print(f"TICK_REGION = ({top_left.x}, {top_left.y}, {width}, {height})")
