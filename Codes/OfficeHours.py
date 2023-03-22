import datetime

from PyQt6.QtWidgets import QTableWidgetItem

from Codes.window import Window

class OfficeHours(Window):
    def __init__(self):
        super().__init__('OfficeHours', r'Designs\OfficeHours.ui')
        self.form.backToMenu.clicked.connect(self.showBackToMenu)
        self.form.byMonthButton.toggled.connect(self.byMonthPressed)
        self.form.allButton.toggled.connect(self.allPressed)
        for teacher in self.db.getTeachers():
            self.form.teacherList.addItem(teacher)
        for i in reversed(range(2022, datetime.datetime.now().year+1)):
            self.form.yearList.addItem(str(i))
        self.form.monthList.hide()
        self.form.yearList.hide()



    def byMonthPressed(self):
        self.form.monthList.show()
        self.form.yearList.show()
    def allPressed(self):
        self.form.monthList.hide()
        self.form.yearList.hide()







    def showBackToMenu(self):
        Window.windows['Menu']['window'].show()
        self.hide()



