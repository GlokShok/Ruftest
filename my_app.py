from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)
app = QApplication([])
first_win = QWidget()
first_win.setWindowTitle("Здоровье")
first_win.resize(1200,600)
first_win.move(500,200)
label =  QLabel(txt_hello)
label1 =  QLabel(txt_instruction)
h_line  = QHBoxLayout()
h_line.addWidget(label, alignment = Qt.AlignCenter)
h_line.addWidget(label1, alignment = Qt.AlignCenter)
my_win.setLayout(h_line)
my_win.show()
app.exec_()