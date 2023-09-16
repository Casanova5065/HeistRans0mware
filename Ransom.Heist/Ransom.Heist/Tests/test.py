import psutil

def get_hard_drive_info():
    hard_drives = []
    for partition in psutil.disk_partitions():
        if "cdrom" not in partition.opts.lower() and "removable" not in partition.opts.lower():
            hard_drives.append(partition.mountpoint)
    return hard_drives


drives = get_hard_drive_info()
print(drives)
drives = drives[::-1][:-1]

for drive in drives:
    print(drive)

