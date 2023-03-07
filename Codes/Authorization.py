from PyQt6.QtWidgets import QMessageBox

from Codes.window import Window

class Authorization(Window):
    database = {"Allium": 'Allium', '':''}

    def __init__(self):
        super().__init__('Authorization', r'Designs\Authorization.ui')
        self.form.pushLogin.clicked.connect(self.login)
        self.form.pushAccess.clicked.connect(self.callForAccess)

    def login(self):
        try:
            self.form.textPassword.text() == Authorization.database[self.form.textLogin.text()]
            self.form.textAnswer.setText('Access granted. Proceeding to the database')
            Window.windows['Menu']['window'].show()
            self.hide()
        except KeyError:
            dlg = QMessageBox()
            dlg.setWindowTitle("Error")
            dlg.setText("Access denied")
            dlg.setStandardButtons(QMessageBox.StandardButton.Close)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()

    def callForAccess(self):
        if len(self.form.textPassword.text())<6:
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
