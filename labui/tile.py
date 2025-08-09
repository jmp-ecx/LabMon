from typing import Self

from PySide6.QtWidgets import *
from data.ports import *

class ComponentTile(QFrame):
  def __init__(self, listener: None, name: str, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)

    self.setObjectName('ComponentTile')

    self.setMinimumSize(150, 150)

    self.port: port = NULL
    self.name: str  = name

    self.listener = listener

    self.logged: bool = False

    # Needs:
    #  - Component name
    #  - Port name
    #  - Value
    #  - Set value (if needed)
    # - color if being logged?

  def EnableLogging(self) -> Self:
    self.logged = True
    # TODO - set color
    return self

  def DisableLogging(self) -> Self:
    self.logged = False
    # TODO - color
    return self
