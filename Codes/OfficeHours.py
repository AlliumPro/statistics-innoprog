import datetime

from PyQt6.QtWidgets import QTableWidgetItem

from Codes.window import Window

class OfficeHours(Window):
    def __init__(self):
        super().__init__('OfficeHours', r'Designs\OfficeHours.ui')
        self.form.backToMenu.clicked.connect(self.showBackToMenu)
        for teacher in self.db.getTeachers():
            self.form.teacherList.addItem(teacher)
        if int(self.form.yearList.itemText(0))!=datetime.datetime.now().year



    def showBackToMenu(self):
        Window.windows['Menu']['window'].show()
        self.hide()



