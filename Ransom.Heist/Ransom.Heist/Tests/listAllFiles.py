# Status - OK
# Type - Module
import os
import psutil

def find_files_by_extension(root_dir, extensions):
    found_files = []

    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            for ext in extensions:
                if filename.endswith(ext):
                    full_path = os.path.join(dirpath, filename)
                    found_files.append(full_path)
                    # break
    return found_files


def get_hard_drive_info():
    hard_drives = []
    for partition in psutil.disk_partitions():
        if "cdrom" not in partition.opts.lower() and "removable" not in partition.opts.lower():
            hard_drives.append(partition.mountpoint)
    return hard_drives

if __name__=='__main__':

    ext =  [
    ".docx",".doc",".xlsx",".xls",".pptx",".ppt",".pdf",".txt",".jpg",
    ".jpeg",".png",".gif",".mp3",".wav",".avi",".mp4",".zip",".rar",
    ".7z",".tar",".gz",".sql",".accdb",".mdb",".dbf",".odb",".pst",".ost",
    ".msg",".eml",".pem",".pfx",".key",".crt",".csr",".p12",".der",
    ".sln",".suo",".cs",".c",".cpp",".pas",".h",".asm",".js",".cmd",
    ".bat",".ps1",".vbs",".vb",".pl",".dip",".dch",".sch",".brd",".jsp",
    ".php",".asp",".rb",".java",".jar",".class",".svg",".ai",".psd",
    ".nef",".tiff",".tif",".cgm",".raw",".djvu",".hwp",".snt",".onetoc2",
    ".dwg",".sxi",".sti",".vsdx",".vsd",".edb",".pot",".potx",".ppam",
    ".ppsx",".ppsm",".pps",".dot",".dotx",".dotm",".sxc",".stc",".dif",
    ".slk",".wb2",".odp",".otp",".sxd",".std",".uop",".odg",".otg",".sxm",
    ".mml",".lay",".lay6",
]
    drives = get_hard_drive_info()
    totalFiles = []
    for drive in drives:
        files = find_files_by_extension(drive, ext)
        for file in files:
            print(file)
            totalFiles.append(file)

    print("[+] Total files :", len(totalFiles))
