import pyautogui
import time

print("Hover your mouse over any target. Coordinates will print every 2 seconds.\nPress Ctrl+C to stop.\n")
time.sleep(2)

try:
    while True:
        x, y = pyautogui.position()
        print(f"X={x}, Y={y}")
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[+] Done grabbing coordinates.")
