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
with open('authorizationInfo.txt','r') as f:
    filelines=f.readlines()

if filelines and menu.db.getAuthorizationInfo(filelines[0].strip(), filelines[1].strip()) is not None:
    menu.show()
else:
    authorization.show()
win.exec()
