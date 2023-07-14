import pystray

from capture import CaptureImage
from PIL import Image
from pystray import MenuItem as item
from pywinauto import keyboard


def capture_window():
    keyboard.send_keys("%{TAB}")  # Activate the window
    capture.capture_window()


capture = CaptureImage()
image = Image.open("MakiShot.ico")

menu = (
    item("Capture Screen [ctrl + insert]", capture.capture_screen),
    item("Capture Window [alt + insert]", capture_window),
    item("Capture Region [insert]", capture.capture_region),
    item("Exit", lambda: icon.stop()),
)

icon = pystray.Icon("MakiShot", image, "MakiShot", menu)
icon.run()
