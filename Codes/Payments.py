from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox

from Codes.window import Window


class Payments(Window):
    def __init__(self):
        super().__init__("Payments", r"Designs\Payments.ui")
        self.form.backToMenu.clicked.connect(self.showBackToMenu)
        self.form.enterid.textChanged.connect(self.search)
        self.form.addButton.clicked.connect(self.addUser)
        self.form.removeButton.clicked.connect(self.removeUser)

    def showBackToMenu(self):
        Window.windows["Menu"]["window"].show()
        self.hide()

    def search(self):
        if self.form.enterid.text() == "":
            self.form.searchTable.setColumnCount(2)
            users = Window.db.getUsers()
            self.form.searchTable.setRowCount(len(users))
        else:
            self.form.searchTable.setColumnCount(2)
            users = Window.db.getUsers(self.form.enterid.text())
            self.form.searchTable.setRowCount(len(users))
        for i, elem in enumerate(users):
            id = QTableWidgetItem(str(elem[0]))
            username = QTableWidgetItem(elem[1])
            self.form.searchTable.setItem(i, 0, id)
            if elem[1] is not None:
                self.form.searchTable.setItem(i, 1, username)

    def addUser(self):
        try:
            profit = float(self.form.resultProfit.text().split(" ")[0])
            if self.form.searchTable.currentItem() is None:
                raise Exception("Select id")

            if self.form.searchTable.currentColumn() == 1:
                id, username, payment = Window.db.getPaymentInfo(
                    username=self.form.searchTable.currentItem().text()
                )
            elif self.form.searchTable.currentColumn() == 0:
                id, username, payment = Window.db.getPaymentInfo(
                    id=self.form.searchTable.currentItem().text()
                )
            else:
                raise Exception("Select user first")
            row_count = self.form.resultTable.rowCount()
            for i in range(row_count):
                if id == int(self.form.resultTable.item(i, 0).text()):
                    raise Exception("User already in list")

            self.form.resultTable.setRowCount(row_count + 1)
            self.form.resultTable.setItem(row_count, 0, QTableWidgetItem(str(id)))
            if username is not None:
                self.form.resultTable.setItem(row_count, 1, QTableWidgetItem(username))
            self.form.resultTable.setItem(row_count, 2, QTableWidgetItem(str(payment)))
            profit += payment
            self.form.resultProfit.setText(str(profit) + " р")

        except Exception as e:
            dlg = QMessageBox()
            dlg.setWindowTitle("Error")
            dlg.setText(str(e))
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()

    def removeUser(self):
        try:
            profit = float(self.form.resultProfit.text().split(" ")[0])
            if self.form.resultTable.currentItem() is None:
                raise Exception("Select id")

            if self.form.resultTable.currentColumn() == 1:
                id, username, payment = Window.db.getPaymentInfo(
                    username=self.form.resultTable.currentItem().text()
                )
            elif self.form.resultTable.currentColumn() == 0:
                id, username, payment = Window.db.getPaymentInfo(
                    id=self.form.resultTable.currentItem().text()
                )
            elif self.form.resultTable.currentColumn() == 2:
                raise Exception("Select user, not the payment value")
            else:
                raise Exception("Select user first")

            row_count = self.form.resultTable.rowCount()
            for row in range(row_count):
                if id == int(self.form.resultTable.item(row, 0).text()):
                    self.form.resultTable.removeRow(row)
                    break

            profit -= payment
            self.form.resultProfit.setText(str(profit) + " р")

        except Exception as e:
            dlg = QMessageBox()
            dlg.setWindowTitle("Error")
            dlg.setText(str(e))
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()
