import os, sys, platform
try:os.system('git pull')
except:pass
try:os.system('xdg-open https://t.me/ricoexedz')
except:pass
bit = platform.architecture()[0]
try:
    if bit == '64bit':
        import maya
        maya._Exception()
    else:
        import maya32
        maya32._Exception()
except Exception as e:
    exit(str(e))
