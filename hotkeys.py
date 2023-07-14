import keyboard
from capture import CaptureImage

capture = CaptureImage()

keyboard.add_hotkey("ctrl + insert", capture.capture_screen)
keyboard.add_hotkey("alt + insert", capture.capture_window)
keyboard.add_hotkey("insert", capture.capture_region)
