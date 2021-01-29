import time
import os
import random as r
import module as m
from module import hi as a, add as b
try:
    import nomodule
except ImportError:
    print('модуля nomodule Не сеществует')
a()
print(b(45, 15))
