from pywinauto.application import Application
from pywinauto import Desktop
import time

# === Step 0: Launch ERA Explorer ===
print("🚀 Launching ERA Explorer...")
app = Application(backend="uia").start(r"C:\Program Files\ERA Explorer\ERA Explorer.exe")

# Wait for main window with title containing "ERA Explorer"
main_win = app.window(title_re=".*ERA Explorer.*")

# === Step 1: Wait and click Proceed ===
print("⏳ Waiting for Proceed button...")
proceed_clicked = False
for i in range(60):
    try:
        proceed_btn = main_win.child_window(title="Proceed", control_type="Button")
        proceed_btn.wait('exists ready', timeout=1)
        proceed_btn.click_input()
        print("✅ Proceed clicked.")
        proceed_clicked = True
        break
    except:
        time.sleep(1)

if not proceed_clicked:
    print("❌ Proceed button never appeared. Exiting.")
    exit()

# === Step 2: Wait and click Skip Wizard ===
print("⏳ Waiting for Skip Wizard to appear...")
skip_clicked = False

for i in range(30):  # wait up to 30 seconds
    try:
        # Correctly instantiate Desktop with backend
        desktop = Desktop(backend="uia")
        active_win = desktop.active_window()

        # Attempt to find "Skip Wizard" button
        skip_btn = active_win.child_window(title="Skip Wizard", control_type="Button")
        if skip_btn.exists(timeout=1):
            skip_btn.click_input()
            print("✅ Skip Wizard clicked.")
            skip_clicked = True
            break

    except Exception as e:
        print(f"⏳ Retrying... {i+1}/30 | Error: {e}")
        time.sleep(1)

if not skip_clicked:
    print("⚠️ Skip Wizard button not found. Maybe skipped automatically or in new UI.")
