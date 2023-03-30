from Codes.Attendance import Attendance
from Codes.window import Window


class Menu(Window):
    def __init__(self):
        super().__init__("Menu", "Designs\Menu.ui")
        self.form.attendance.clicked.connect(self.showAttendance)
        self.form.payments.clicked.connect(self.showPayments)
        self.form.logOutButton.clicked.connect(self.logOut)
        self.form.officeHoursButton.clicked.connect(self.showOfficeHours)

    def showAttendance(self):
        Window.windows["Attendance"]["window"].show()
        self.hide()

    def showPayments(self):
        Window.windows["Payments"]["window"].show()
        Window.windows["Payments"]["object"].search()
        self.hide()

    def showOfficeHours(self):
        Window.windows["OfficeHours"]["window"].show()
        self.hide()

    def logOut(self):
        Window.windows["Authorization"]["window"].show()
        self.hide()
        with open("authorizationInfo.txt", "w") as f:
            f.seek(0)
            f.write("")
