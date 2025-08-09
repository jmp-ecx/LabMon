from __future__ import annotations
from data import ports

from labjack import ljm as lj

class Handler:
  def __init__(self) -> None:
    self.handle = lj.openS('ANY')

  def write_i(self, port: ports.port, value: int) -> None:
    lj.eWriteAddress(int(self), port, lj.constants.INT32, value)

  def write_f(self, port: ports.port, value: float) -> None:
    lj.eWriteAddress(int(self), port, lj.constants.FLOAT32, value)

  def write_b(self, port: ports.port, value: bool) -> None:
    lj.eWriteAddress(int(self), port, lj.constants.INT32, int(value))

  def read_i(self, port: ports.port) -> int:
    return int(lj.eReadAddress(int(self), port, lj.constants.INT32))

  def read_f(self, port: ports.port) -> float:
    return float(lj.eReadAddress(int(self), port, lj.constants.FLOAT32))

  def read_b(self, port: ports.port) -> bool:
    return bool(lj.eReadAddress(int(self), port, lj.constants.INT32))

  def __del__(self) -> None:
    lj.close(self.handle)

  def __int__(self) -> int:
    return self.handle
