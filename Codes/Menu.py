from Codes.Attendance import Attendance
from Codes.window import Window


class Menu(Window):
    def __init__(self):
        super().__init__("Menu", "Designs\Menu.ui")
        self.form.attendance.clicked.connect(self.showAttendance)

    def showAttendance(self):
        Window.windows['Attendance']['window'].show()
        self.hide()
