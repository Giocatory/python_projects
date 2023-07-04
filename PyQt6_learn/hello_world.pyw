from PyQt6 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("First application")
window.resize(400, 200)
label = QtWidgets.QLabel("<center>Hellow world!!!</center>")
btnQuit = QtWidgets.QPushButton("&Quit")
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(label)
vbox.addWidget(btnQuit)
window.setLayout(vbox)
btnQuit.clicked.connect(app.quit)
window.show()
sys.exit(app.exec())
