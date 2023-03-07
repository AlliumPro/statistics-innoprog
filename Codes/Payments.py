from PyQt6.QtWidgets import QTableWidgetItem

from Codes.window import Window


class Payments(Window):
    def __init__(self):
        super().__init__('Payments', r'Designs\Payments.ui')
        self.form.backToMenu.clicked.connect(self.showBackToMenu)
        self.form.enterid.textChanged.connect(self.search)

    def showBackToMenu(self):
        Window.windows['Menu']['window'].show()
        self.hide()
    def search(self):
        if self.form.enterid.text() =='':
            self.form.searchTable.setColumnCount(2)
            users=Window.db.getUsers()
            self.form.searchTable.setRowCount(len(users))
        else:
            self.form.searchTable.setColumnCount(2)
            users=Window.db.getUsers(self.form.enterid.text())
            self.form.searchTable.setRowCount(len(users))
        for i, elem in enumerate(users):
            id = QTableWidgetItem(str(elem[0]))
            username = QTableWidgetItem(elem[1])
            self.form.searchTable.setItem(i, 0, id)
            if elem[1] is not None:
                self.form.searchTable.setItem(i, 1, username)

    def addUser(self):



