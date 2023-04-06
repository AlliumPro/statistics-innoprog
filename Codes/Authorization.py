from PyQt6.QtWidgets import QMessageBox
from googletrans import Translator, constants
from Codes.path import resource_path
from Codes.window import Window


class Authorization(Window):

    translator = Translator()
    def __init__(self):
        super().__init__("Authorization", r"Designs\Authorization.ui")
        self.form.pushLogin.clicked.connect(self.login)

    def login(self):
        user = self.db.getAuthorizationInfo(
            self.form.textLogin.text(), self.form.textPassword.text()
        )
        if user is not None:
            Window.windows["Menu"]["window"].show()
            self.hide()
            f = open(resource_path("authorizationInfo.txt"), "w", encoding="UTF-8")
            f.write(f"{user[0]}\n{user[1]}\n{user[2]}")
            f.close()
            Window.windows["Menu"]["form"].helloMessage.setText(
                f'Hello, {Authorization.translator.translate(user[2], dest="en").text.replace("Venediktov Rafael Vladimirovich","Venediktov Rafail Vladimirovich")}'
            )
        else:
            dlg = QMessageBox()
            dlg.setWindowTitle("Error")
            dlg.setText("Access denied")
            dlg.setStandardButtons(QMessageBox.StandardButton.Close)
            dlg.setIcon(QMessageBox.Icon.Warning)
            dlg.exec()

    # def callForAccess(self):
    #     if len(self.form.textPassword.text()) < 6:
    #         dlg = QMessageBox()
    #         dlg.setWindowTitle("Error")
    #         dlg.setText("Your password must be at least 6 symbols")
    #         dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
    #         dlg.setIcon(QMessageBox.Icon.Critical)
    #         dlg.exec()
    #     else:
    #         dlg = QMessageBox()
    #         dlg.setWindowTitle("Success")
    #         dlg.setText("Your data was sent for a check")
    #         dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
    #         dlg.setIcon(QMessageBox.Icon.Information)
    #         dlg.exec()

        # Authorization.database[
        #     self.form.textLogin.text()
        # ] = self.form.textPassword.text()
