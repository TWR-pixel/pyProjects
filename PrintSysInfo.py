import math
import platform
import os

lis = [
platform.processor(),
platform.python_build(),
platform.release(),
platform.architecture(),
platform.system(),
platform.version()
]

def printLis():
    print()
    print(">CPU stepping: " + lis[0])
    print(">python: " + str(lis[1]))
    print(">Выпуск системы: " + lis[2])
    print(">Архитектура и версия ОС: " + str(lis[3]))
    print(">Имя ОС: " + lis[4])
    print(">Версия выпуска системы: " + lis[5] )
    
printLis()

a = input()
