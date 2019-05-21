import os

try:
    os.mkdir("./all/ana")
except OSError:
    pass

os.system("rm -rf ./all/ana")