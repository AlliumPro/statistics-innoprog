from PyQt6.QtWidgets import QApplication

from Codes.Attendance import Attendance
from Codes.Authorization import Authorization
from Codes.Menu import Menu
from Codes.Payments import Payments

win = QApplication([])
menu = Menu()

attendance = Attendance()
authorization = Authorization()
payments = Payments()
authorization.show()
win.exec()
