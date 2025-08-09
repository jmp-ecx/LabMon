from PySide6.QtWidgets import *

from labui.tile import ComponentTile
from labui.layouts import FlowLayout

# TODO - scripting for serial ports and processing proprietary analog stuff.
#      - Use built in exec / globals stuff.

class LabMonWindow(QMainWindow):
  def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

    self.tiles: list[ComponentTile] = []

    self.setWindowTitle('LabMon')
    self.setMinimumSize(800, 600)

    with open('res/style.qss') as f:
      self.setStyleSheet(f.read())

    # region Menu Bar
    self.toolbar = QToolBar()
    self.toolbar.setMovable(False)

    self.add = QToolButton()
    self.add.setText('Add Listener')
    self.add.clicked.connect(self.add_listener)
    self.toolbar.addWidget(self.add)

    self.addToolBar(self.toolbar)
    # endregion

    # region App Window
    self.container = QWidget()
    self.layout = QVBoxLayout()

    # region Tile View
    self.tile_view = QFrame()
    self.tile_layout = FlowLayout()

    self.tile_view.setLayout(self.tile_layout)
    self.layout.addWidget(self.tile_view)
    # endregion

    self.container.setLayout(self.layout)
    self.setCentralWidget(self.container)
    # endregion

  def add_listener(self) -> None:
    self.tile_layout.addWidget(ComponentTile(None, 'Test'))
