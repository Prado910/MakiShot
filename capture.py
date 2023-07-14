import win32gui

from PIL import ImageGrab
from pynput import mouse
from tkinter import filedialog, Tk


class CaptureImage:
    def __init__(self) -> None:
        self.rect = None
        self.image = None

    def get_window_rect(self) -> tuple:
        """Get the coordinates of the foreground window.

        Returns:
            tuple: A list of window coordinates.
        """
        window = win32gui.GetForegroundWindow()
        rect = win32gui.GetWindowRect(window)
        return rect

    def capture_region(self):
        """Capture a specific region of the screen.
        """
        self.rect = self.select_region()
        self.image = ImageGrab.grab(bbox=self.rect)
        self.save_image()

    def capture_screen(self):
        """Capture all the screen.
        """
        self.image = ImageGrab.grab()
        self.save_image()

    def capture_window(self):
        """Capture a spedific window.
        """
        self.rect = self.get_window_rect()
        self.image = ImageGrab.grab(bbox=self.rect)
        self.save_image()

    def select_region(self) -> tuple:
        """Select the region to be captured.

        Returns:
            tuple: A list of window coordinates.
        """
        rect = list()

        def on_click(x, y, button, pressed):
            rect.extend((x, y))
            if not pressed:
                return False

        with mouse.Listener(on_click=on_click) as listener:
            listener.join()

        if rect[0] > rect[2]:
            rect[0], rect[2] = rect[2], rect[0]
        if rect[1] > rect[3]:
            rect[1], rect[3] = rect[3], rect[1]

        return rect

    def save_image(self):
        save_path = filedialog.asksaveasfilename(defaultextension=".png")
        if save_path:
            self.image.save(save_path)
