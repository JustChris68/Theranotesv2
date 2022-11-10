import os
import json
import shutil
import pathlib
import re


# reads text files into a ditionary indexed by filename and saved as json

notedic = {}
sourcedir = 'output'
outdir = 'data'
thisdir = os.getcwd()
spath = os.path.join(thisdir, sourcedir)
dpath = os.path.join(thisdir, outdir)
notelist = os.listdir(spath)
filecount = 0
print(notelist)
print('Souce: ' + sourcedir + ' path: ' + str(spath))
print('Destination: ' + outdir + ' path: ' + str(dpath))
print('Current Working: ' + thisdir)
for file in notelist:
    print(file)
    f =  open(os.path.join(spath, file), 'r')
    notetext = f.read()
    notetext = re.sub(r'\n', ' ', notetext)
    notetext = re.sub(r'•', ' ', notetext)
    notetext = re.sub(r'start time, end time,', ' ', notetext)

    notedic[file] = notetext
    filecount += 1
with open(os.path.join(dpath,'data.json'), 'w') as fp:
    #notedic = json.dumps(notedic, indent = 4)
    json.dump(notedic, fp)
print(notedic)
print('Files Processed In: ' + str(filecount))