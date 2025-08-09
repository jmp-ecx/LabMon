from data import Handler
from data.ports import *
import time

handle = Handler()

handle.write_f(DAC0, 3.5)
time.sleep(0.5)
print(handle.read_f(AIN0))

del handle
