
'''disk is a cross-platform library for meausre actual hard disk capacity in Python. Supported platforms:

 - Linux
 - Windows
 - macOS
 - FreeBSD
 - OpenBSD
 - NetBSD
 - Sun Solaris
 - AIX

Works with Python versions 3.4+.
'''

import psutil

def main():
    total = int()
    used = int()
    free = int()
    act_size = 0

    for disk in psutil.disk_partitions():
        if disk.fstype:
            total += int(psutil.disk_usage(disk.mountpoint).total)
            used += int(psutil.disk_usage(disk.mountpoint).used)
            free += int(psutil.disk_usage(disk.mountpoint).free)

    total = round(total / (1024.0 ** 3), 2)
    if total > 20 and total < 60:
        act_size = 40
    elif total > 60 and total < 100:
        act_size = 80
    elif total > 100 and total < 130:
        act_size = 128
    elif total > 130 and total < 180:
        act_size = 160
    elif total > 180 and total < 210:
        act_size = 200
    elif total > 210 and total < 250:
        act_size = 250
    elif total > 240 and total < 260:
        act_size = 256
    elif total > 290 and total < 350:
        act_size = 320
    elif total > 450 and total < 500:
        act_size = 500
    elif total > 500 and total < 515:
        act_size = 512
    elif total > 900 and total < 1100:
        act_size = 1000
    elif total > 1500 and total < 2100:
        act_size = 2000
    elif total > 3500 and total < 4100:
        act_size = 4000

    used = round(used / (1024.0 ** 3), 2)
    free = round(free / (1024.0 ** 3), 2)

    return total, act_size, used, free

def ret():
    total, act_size, used, free = main()
    return total, act_size, used, free