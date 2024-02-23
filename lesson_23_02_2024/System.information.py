print()

import platform
print("Платформа: ",platform.platform())

print("Архітектура: ",platform.machine())
from platform import processor
print("Процесор: ",processor())

print("Система: ",platform.system())

print("Версія: ",platform.version())

print(platform.python_implementation())
for atr in platform.python_version_tuple():
    print(atr, end='.')
print()
