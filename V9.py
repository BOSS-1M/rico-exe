import os, sys, platform
try:os.system('git pull')
except:pass
try:os.system('xdg-open https://t.me/ricoexedz')
except:pass
bit = platform.architecture()[0]
try:
    if bit == '64bit':
        import v8
        v8._Exception()
    else:
        import v832
        v832._Exception()
except Exception as e:
    exit(str(e))
