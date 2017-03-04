import pathlib

# from time import ctime

""" Check whether the the RAW-Photos in 'newdict' already exist in 'savedict' or subfolders
based on  name and data of creation"""

newdict = pathlib.WindowsPath('C:/Users/fabha/MyStuff/Test/Card')
saveddict = pathlib.WindowsPath('C:/Users/fabha/MyStuff/Test/PC')
filetypes = ['jpg']  # Filetypes in newdict to check
secondsperday = 60 * 60 * 24

found = []
missing = []
for filetype in filetypes:
    for newphoto in newdict.rglob('*.' + filetype):  # rglob includes all subdirectories
        for savedphoto in saveddict.rglob('*.' + filetype):
            if newphoto.name != savedphoto.name:
                continue
            newdate = newphoto.stat().st_ctime
            saveddate = savedphoto.stat().st_ctime
            if saveddate - secondsperday < newdate < saveddate + secondsperday:
                found.append(newphoto.name)
                break
        if newphoto.name not in found:
            missing.append(newphoto.name)

print(found)
print(missing)
