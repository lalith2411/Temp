import datetime
import subprocess
import time
import pyautogui
import argparse
parser = argparse.ArgumentParser(description="Send automated message using pyautogui")

parser.add_argument('-m','--message', type=str, required=True, help="The text message to send")
parser.add_argument('-t','--time', type=str, required=True, help="Time to send message in HH:MM format (24-hour)")
parser.add_argument('-c','--contact', type=str, required=True, help="Contact name or number (for display/reference)")
args = parser.parse_args()

# Get current datetime and target datetime
now = datetime.datetime.now()
target_hour, target_minute = map(int, args.time.split(':'))

target_time = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)

# If target time is earlier today, assume it's for tomorrow
delta_time = 0
if target_time < now:
    target_time += datetime.timedelta(days=1)
    delta_time = (target_time - now).total_seconds()

# Calculate the time delta
print("sleeping for", delta_time,"seconds")
time.sleep(delta_time)

subprocess.Popen(
    ["explorer.exe", r"shell:AppsFolder\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"])

time.sleep(2.6)


# search
pyautogui.click(x=168, y=116)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('backspace')
pyautogui.write(args.contact)
time.sleep(1)

# first contact
pyautogui.click(x=205, y=191)
time.sleep(0.3)

# text input
pyautogui.click(x=562, y=737)
pyautogui.hotkey('ctrl', 'a')
pyautogui.press('backspace')
pyautogui.write(args.message)
pyautogui.press('enter')

# import pyautogui
# import time
# time.sleep(3)
# print("Mouse position:", pyautogui.position())
