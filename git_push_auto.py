import os
i = 1
while (i == 3):
    if (i == 1):
        os.system('cmd /k "git add -A"')
        i = i + 1
    elif (i == 2):
        os.system('cmd /k "git commit -m "Modified"')
        i = i + 1
    elif (i == 3):
        os.system('cmd /k "git push"')
        i = i + 1