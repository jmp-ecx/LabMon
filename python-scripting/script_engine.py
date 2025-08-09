# from __future__ import annotations
from typing import Self, Callable
import threading

class Script:
    """ A file script """
    def __init__(self, path: str) -> None:
        """
        :param path: The path to the script.
        """
        self.path = path
        self.code = ""
        
    def update_path(self, np: str) -> None:
        """Update the script's path
        
        :param np: The new path.
        """
        self.path = np
        
    def load(self) -> Self:
        """ Read the contents of the script. """
        with open(self.path, "r", encoding="UTF-8") as f:
            self.code = f.read()
        return self
        
    def __str__(self) -> str:
        return f"SCRIPT: {self.path}"
        
    def __repr__(self) -> str:
        return f"SCRIPT: {self.path}"

class Context:
    """ The global context for one or more scripts. """
    def __init__(self) -> None:
        self.locals  = {}
        self.globals = {}
        
    def add_loc(self, name: str, value: any) -> Self:
        """ Add local to the context.
        
        :param name: The local's name
        :param value: The local's value
        """
        self.locals[name] = value
        return self
        
    def add_glob(self, name: str, value: any) -> Self:
        """ Add a global to the context.
        
        :param name: The globals name
        :param value: The globals value
        """
        self.globals[name] = value
        return self
        
    def add_func(self, func: Callable) -> Self:
        """ Add a global function to the context.
        
        :param func: The function to add. Name is gotten by func.__name__.
        """
        self.globals[func.__name__] = func
        return self

    def add_class(self, cls: object) -> Self:
        """ Add a class to the context.

        :param cls: The class to add. Name is gotten by func.__name__.
        """
        self.globals[cls.__name__] = cls
        return self

    def __eq__(self, other) -> None:
        return self.locals == other.locals and self.globals == other.locals
        
    def __ne__(self, other) -> None:
        return self.locals != other.locals or self.globals != other.locals
        
    def __str__(self) -> str:
        return f"LOCALS  :: {self.locals}\n" \
               f"GLOBALS :: {self.globals}"
        
    def __repr__(self) -> str:
        return f"LOCALS  :: {self.locals}\n" \
               f"GLOBALS :: {self.globals}"

def run(script: Script, ctx: Context) -> None:
    """ Execute a script under a context.
    
    :param script: The script to run. make sure to .load() it first!
    :param ctx: The script context.
    """
    exec(script.code, ctx.globals, ctx.locals)
    
def run_threaded(script: Script, ctx: Context) -> None:
    threading.Thread(target=exec, 
                     args=[script.code, ctx.globals, ctx.locals], 
                     daemon=False).start() # TODO - daemon.
    