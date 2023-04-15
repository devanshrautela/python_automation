import webbrowser
import time

# set the URL of the YouTube video you want to play
url = "https://www.youtube.com/shorts/EEWiTSVgRZg"

# set the number of private windows you want to open
num_windows = 3

# specify the path to the Brave browser executable
brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# open multiple private windows and play the video in mute
for i in range(num_windows):
    # open a new private window
    webbrowser.register("brave", None, webbrowser.BackgroundBrowser(brave_path))
    webbrowser.get("brave").open_new("--incognito")

    # wait for the browser to open
    time.sleep(2)

    # play the video in mute
    webbrowser.get("brave").open_new_private_tab(url + "&mute=1")