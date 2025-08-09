from PySide6.QtWidgets import QApplication
from labui import *

app = QApplication([])

window = LabMonWindow()
window.show()

app.exec()
