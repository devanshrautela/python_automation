import subprocess
import time
import pyautogui

# set the URL of the YouTube video you want to play
url = "https://www.youtube.com/shorts/EEWiTSVgRZg"

# set the number of private windows you want to open
num_windows = 50
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# open multiple private windows and play the video in mute
for i in range(num_windows):
    j = 0
    for j in range(10):
    # open a new incognito window in Brave
        process = subprocess.Popen([brave_path, '--incognito', '--new-window', '--mute-audio', url])

    # wait for the browser to open
        time.sleep(10)

    # print the updated value of is
        print("Finished loop", i)

    for z in range(10):
        # simulate keypresses to close the tab when the video ends
        time.sleep(10)
        pyautogui.hotkey('ctrl', 'w')