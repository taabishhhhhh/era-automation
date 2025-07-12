import pyautogui
import time

# Give you 5 seconds to switch to the ERA window
time.sleep(5)

# Coordinates
username_field = (228, 436)
password_field = (244, 502)
login_button = (223, 613)

# Credentials
username = "aaa64431"
password = "cccaaabbb"

# Type username
pyautogui.click(username_field)
time.sleep(0.5)
pyautogui.write(username, interval=0.1)

# Type password
pyautogui.click(password_field)
time.sleep(0.5)
pyautogui.write(password, interval=0.1)

# Click Login
pyautogui.click(login_button)