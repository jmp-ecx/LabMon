from typing import Self, Callable

class Context:
  def __init__(self) -> None:
    self.locals  = {}
    self.globals = {}
    self.globals.update(globals())

  def add_loc(self, name: str, value: any) -> Self:
    self.locals[name] = value
    return self

  def add_glob(self, name: str, value: any) -> Self:
    self.globals[name] = value
    return self

  def add_func(self, func: Callable) -> Self:
    self.globals[func.__name__] = func
    return self

  def add_class(self, cls: object) -> Self:
    self.globals[cls.__name__] = cls
    return self

class Script:
  def __init__(self, path: str, dynamic: bool = False) -> None:
    self.dynamic = dynamic
    self.path = path

    self.file = ''

    with open(self.path, 'r', encoding='UTF-8') as f:
      self.file = f.read()

  def exec(self, ctx: Context) -> None:
    if self.dynamic:
      with open(self.path, 'r', encoding='UTF-8') as f:
        self.file = f.read()
    exec(self.file, ctx.globals, ctx.locals)
