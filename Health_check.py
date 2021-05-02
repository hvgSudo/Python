from network import *
import shutil
import psutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent()
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("ERROR!")
elif check_localhost() and check_connectivity():
    print("Everything ok")
else:
    print("Not ok")
