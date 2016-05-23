import sys
import os

f = open(sys.argv[1], 'r+')
text = f.read()
f.seek(0)
f.write('\x90'*len(text))
f.close()
os.system("rm -rf " + sys.argv[1])
