import pyautogui
import time
import subprocess
from PIL import ImageGrab
import pytesseract
import csv
# --- Configuration ---
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

ERA_PATH = r"C:\Program Files\ERA Explorer\ERA Explorer.exe"
TICK_REGION = (487, 642, 904, 808)

PROCEED_IMAGE = r"C:\Users\Administrator\Desktop\era automation\Assets\proceed_button.png"
SKIP_WIZARD_IMAGE = r"C:\Users\Administrator\Desktop\era automation\Assets\skip wizard interface.PNG"
LOGIN_AGAIN_IMAGE = r"C:\Users\Administrator\Desktop\era automation\Assets\loginAgain.PNG"
USERPASS_INTERFACE_IMAGE = r"C:\Users\Administrator\Desktop\era automation\Assets\UserPassInterface.png"
LOGIN_SUCCESS_INTERFACE_IMAGE = r"C:\Users\Administrator\Desktop\era automation\Assets\LoginSuccessInterface.png"
RESUME_LEARNING_BUTTON_IMAGE = r"C:\Users\Administrator\Desktop\era automation\Assets\ResumeLearningButton.PNG"
SESSION_INTERFACE_IMAGE = r"C:\Users\Administrator\Desktop\era automation\Assets\SessionInterface.png"
WITHOUT_GREENLINES_IMAGE = r"C:\Users\Administrator\Desktop\era automation\Assets\without_greenlines.png"

LOGIN_AGAIN_COORDS = (232, 657)
RESUME_LEARNING_COORDS = (365, 387)
USER_FIELD = (280, 427)
PASS_FIELD = (286, 493)
LOGIN_BUTTON = (245, 614)
SCROLL_FOCUS_COORDS = (204, 230)

CSV_PATH = r"C:\Users\Administrator\Desktop\era automation\users.csv"

# --- Functions ---
def load_users(csv_path):
    users = []
    with open(csv_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append({'username': row['username'], 'password': row['password']})
    return users

def launch_era():
    print("🔄 Launching ERA Explorer...")
    subprocess.Popen(ERA_PATH)
    time.sleep(5)

def wait_for_ready_ticks():
    print("🕵️‍♂️ Waiting for green ticks using OCR...")
    while True:
        screenshot = ImageGrab.grab(bbox=TICK_REGION)
        text = pytesseract.image_to_string(screenshot).lower()
        print("🔍 OCR Text:", text)
        if "ready" in text or "proceed" in text:
            print("✅ Green ticks detected!")
            break
        time.sleep(1)

def wait_for_button(image_path, button_name):
    print(f"⌛ Waiting for '{button_name}' button...")
    while True:
        try:
            location = pyautogui.locateOnScreen(image_path, confidence=0.8)
            if location:
                center = pyautogui.center(location)
                print(f"✅ '{button_name}' button found at {center}")
                return center
        except:
            pass
        time.sleep(0.5)

def click_button(center, name="button"):
    pyautogui.moveTo(center.x, center.y, duration=0.5)
    pyautogui.click()
    print(f"🖱️ Clicked '{name}'")

def wait_for_login_interface():
    print("⌛ Waiting for login interface...")
    while True:
        try:
            location = pyautogui.locateOnScreen(USERPASS_INTERFACE_IMAGE, confidence=0.85)
            if location:
                print("✅ Login interface detected")
                return
        except Exception as e:
            print("⚠️ Error detecting login interface:", e)
        time.sleep(0.5)

def login_user(username, password):
    print(f"🔐 Logging in as: {username}")
    wait_for_login_interface()
    pyautogui.click(USER_FIELD)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(username, interval=0.05)
    pyautogui.click(PASS_FIELD)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(password, interval=0.05)
    pyautogui.click(LOGIN_BUTTON)
    print("🔓 Login button clicked.")
    time.sleep(3)
    handle_active_session()

def handle_active_session():
    print("🔎 Checking for 'Login Again'...")
    try:
        location = pyautogui.locateOnScreen(LOGIN_AGAIN_IMAGE, confidence=0.8)
        if location:
            pyautogui.moveTo(LOGIN_AGAIN_COORDS[0], LOGIN_AGAIN_COORDS[1], duration=0.5)
            pyautogui.click()
            print("✅ Clicked 'Login Again'")
    except Exception as e:
        print("❌ Error handling active session:", e)

def wait_for_login_success_and_click_resume():
    print("⌛ Waiting for login success interface...")
    while True:
        try:
            location = pyautogui.locateOnScreen(LOGIN_SUCCESS_INTERFACE_IMAGE, confidence=0.85)
            if location:
                print("✅ Login success detected")
                pyautogui.moveTo(RESUME_LEARNING_COORDS, duration=0.5)
                pyautogui.click()
                print("🎯 Clicked 'Resume Learning'")
                return
        except Exception as e:
            print("⚠️ Error detecting login success interface:", e)
        time.sleep(0.5)

def wait_for_session_interface():
    print("⌛ Waiting for session interface...")
    while True:
        try:
            location = pyautogui.locateOnScreen(SESSION_INTERFACE_IMAGE, confidence=0.85)
            if location:
                print("✅ Session interface detected.")
                return
        except Exception as e:
            print("⚠️ Error detecting session interface:", e)
        time.sleep(1)

def scroll_and_click_incomplete_sessions(max_sessions=2, region=(0, 24, 317, 869), confidence=0.9):
    print("🔍 Searching for incomplete sessions...")
    pyautogui.moveTo(SCROLL_FOCUS_COORDS)
    pyautogui.click()

    sessions_clicked = 0
    scrolls = 0
    seen = set()

    while sessions_clicked < max_sessions and scrolls < 40:
        try:
            found = pyautogui.locateAllOnScreen(WITHOUT_GREENLINES_IMAGE, region=region, confidence=confidence)
            for session in found:
                center = pyautogui.center(session)
                if (center.x, center.y) not in seen:
                    pyautogui.moveTo(center)
                    pyautogui.click()
                    print(f"✅ Clicked incomplete session at {center}")
                    sessions_clicked += 1
                    seen.add((center.x, center.y))
                    time.sleep(6)
                    pyautogui.hotkey("alt", "left")
                    time.sleep(3)
                    break

            if sessions_clicked < max_sessions:
                pyautogui.scroll(-500)
                scrolls += 1
                print(f"🔽 Scrolling down... (scroll {scrolls})")
                time.sleep(0.8)
        except Exception as e:
            print("⚠️ Error during scroll:", e)
            break

    if sessions_clicked == 0:
        print("🚫 No incomplete sessions found.")
    else:
        print(f"🎯 Clicked {sessions_clicked} incomplete session(s)")

# --- Main Execution ---
launch_era()
wait_for_ready_ticks()

proceed = wait_for_button(PROCEED_IMAGE, "Proceed")
click_button(proceed, "Proceed")

time.sleep(3)
skip = wait_for_button(SKIP_WIZARD_IMAGE, "Skip Wizard")
click_button(skip, "Skip Wizard")

users = load_users(CSV_PATH)
if users:
    login_user(users[0]['username'], users[0]['password'])
    wait_for_login_success_and_click_resume()
    wait_for_session_interface()
    scroll_and_click_incomplete_sessions()
else:
    print("⚠️ No users found in CSV!")
