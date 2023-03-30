from PyQt6.QtGui import QTextCharFormat, QFont
from PyQt6.QtWidgets import QTableWidgetItem

from Codes.window import Window


class Attendance(Window):
    def __init__(self):
        super().__init__("Attendance", r"Designs\Attendance.ui")
        self.calendarFrom()
        self.calendarTo()
        self.form.backToMenu.clicked.connect(self.showBackToMenu)
        self.form.searchAttendance.clicked.connect(self.search)
        self.form.calendarFrom.clicked.connect(self.calendarFrom)
        self.form.calendarTo.clicked.connect(self.calendarTo)
        self.form.dateFrom.dateChanged.connect(self.dateChangedFrom)
        self.form.dateTo.dateChanged.connect(self.dateChangedTo)

    def showBackToMenu(self):
        Window.windows["Menu"]["window"].show()
        self.hide()

    def search(self):
        datefrom = self.form.dateFrom.date().startOfDay().toPyDateTime().date()
        dateto = self.form.dateTo.date().startOfDay().toPyDateTime().date()
        result = Window.db.getAttendance(datefrom, dateto)
        self.form.attendanceTable.setColumnCount(3)
        self.form.attendanceTable.setRowCount(len(result))
        for i, elem in enumerate(result):
            id = QTableWidgetItem(str(elem[0]))
            username = QTableWidgetItem(elem[1])
            last_visit = QTableWidgetItem(elem[2].strftime("%d-%m-%y"))
            self.form.attendanceTable.setItem(i, 0, id)
            if elem[1] is not None:
                self.form.attendanceTable.setItem(i, 1, username)
            self.form.attendanceTable.setItem(i, 2, last_visit)

    def calendarFrom(self):
        self.form.dateFrom.setDate(self.form.calendarFrom.selectedDate())

    def calendarTo(self):
        self.form.dateTo.setDate(self.form.calendarTo.selectedDate())

    def dateChangedFrom(self):
        self.form.calendarFrom.setSelectedDate(self.form.dateFrom.date())

    def dateChangedTo(self):
        self.form.calendarTo.setSelectedDate(self.form.dateTo.date())
