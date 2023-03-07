from PyQt6.QtWidgets import QApplication

from Codes.Attendance import Attendance
from Codes.Authorization import Authorization
from Codes.Menu import Menu

win = QApplication([])
menu = Menu()

attendance = Attendance()
authorization = Authorization()
authorization.show()
win.exec()
