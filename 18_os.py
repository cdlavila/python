import os
import psutil

# Architecture
print("Architecture:")
print(os.uname().machine)
print()

# Platform
print("Platform:")
print(os.uname().sysname)
print()

# CPUs
print("CPUs")
print(psutil.cpu_count(logical=False))
print()

# Function to convert from bytes to kb, mb, and gb
SIZE = 1024

def kb(b):
    return b / SIZE

def mb(b):
    return kb(b) / SIZE

def gb(b):
    return mb(b) / SIZE

# Total RAM Memory
print("Total RAM Memory:")
print(f"{psutil.virtual_memory().total} bytes")
print(f"{kb(psutil.virtual_memory().total)} kb")
print(f"{mb(psutil.virtual_memory().total)} mb")
print(f"{gb(psutil.virtual_memory().total)} gb")
print()

# Free memory we have in bytes units
print("Free memory we have in kilo bytes units")
print(f"Free RAM memory: {psutil.virtual_memory().available} bytes")
print(f"Free RAM memory: {kb(psutil.virtual_memory().available)} kb")
print(f"Free RAM memory: {mb(psutil.virtual_memory().available)} mb")
print(f"Free RAM memory: {gb(psutil.virtual_memory().available)} gb")
print()

# Directory for the user root
print("Directory for the user root")
print(os.path.expanduser("~"))
print()

# Active Network interfaces right now
print("Network Interfaces right now")
print(psutil.net_if_addrs())
print()
