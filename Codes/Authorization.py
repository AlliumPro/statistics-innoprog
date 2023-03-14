from PyQt6.QtWidgets import QMessageBox

from Codes.window import Window


class Authorization(Window):

    def __init__(self):
        super().__init__('Authorization', r'Designs\Authorization.ui')
        self.form.pushLogin.clicked.connect(self.login)
        self.form.pushAccess.clicked.connect(self.callForAccess)

    def login(self):
            user=self.db.getAuthorizationInfo(self.form.textLogin.text(), self.form.textPassword.text())
            if user is not None:
                Window.windows['Menu']['window'].show()
                self.hide()
                f = open(r'C:\Users\фвьшт\PycharmProjects\Statistics\authorizationInfo.txt', 'w', encoding = 'UTF-8')
                f.write(f'{user[0]}\n{user[1]}\n{user[2]}')
                f.close()
            else:

                dlg = QMessageBox()
                dlg.setWindowTitle("Error")
                dlg.setText("Access denied")
                dlg.setStandardButtons(QMessageBox.StandardButton.Close)
                dlg.setIcon(QMessageBox.Icon.Warning)
                dlg.exec()

    def callForAccess(self):
        if len(self.form.textPassword.text()) < 6:
            dlg = QMessageBox()
            dlg.setWindowTitle("Error")
            dlg.setText("Your password must be at least 6 symbols")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Critical)
            dlg.exec()
        else:
            dlg = QMessageBox()
            dlg.setWindowTitle("Success")
            dlg.setText("Your data was sent for a check")
            dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
            dlg.setIcon(QMessageBox.Icon.Information)
            dlg.exec()

        Authorization.database[self.form.textLogin.text()] = self.form.textPassword.text()
