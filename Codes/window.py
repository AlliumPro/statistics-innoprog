from Codes.path import resource_path
from PyQt6 import uic
from Codes.Database import Database

class Window:
    windows = {}
    db=Database()
    def __init__(self, name, path):
        Form, Windows = uic.loadUiType(resource_path(path))
        self.window = Windows()
        self.form = Form()
        self.form.setupUi(self.window)
        Window.windows[name] = {'window': self.window, 'form': self.form}

    def show(self):
        self.window.show()

    def hide(self):
        self.window.hide()
