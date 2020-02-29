from PyQt5 import QtWidgets,uic

app=QtWidgets.QApplication([])
dlg=uic.loadUi("acra.ui")
dlg.show()
app.exec()
