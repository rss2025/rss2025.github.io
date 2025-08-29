import os
import sys
folder = "_site"
keyword = "BLAH"


def isDir(path):
	return os.path.isdir(path)


def replace(root, file, key, rep):
	fname = root+os.sep+file
	print("Replacing "+fname)
	fin = open(fname, "rt")
	data = fin.read()
	data = data.replace(key, rep)
	fin.close()
	fin = open(fname, "wt")
	fin.write(data)
	fin.close()



for root, dirs, files in os.walk(folder):
    path = root.split(os.sep)
    print(os.path.basename(root))
    for file in files:
    	if "html" not in file:
    		continue
    	prefix = ""
    	if (len(path) -1) == 0:
    		prefix = "."
    	else:
    		prefix = str((len(path) -1) * '../')
    		prefix = prefix[:-1]
    	print(prefix,root,os.sep,file)
    	replace(root,file,keyword,prefix)
        
