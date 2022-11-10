import os
import json
import shutil
import pathlib
import re
from textblob import TextBlob
import textblob
import pprint
from textparse import parstrings

pp = pprint.PrettyPrinter(indent=4)

notedic = {}
sents = []
sourcedir = 'data'
outdir = 'data'
notelist = {}
cleanlist = {}
bigdict = {}

thisdir = os.getcwd()
spath = os.path.join(thisdir, sourcedir)
dpath = os.path.join(thisdir, outdir)
notefilename = 'data.json'
notefile = os.path.join(spath, notefilename)
print('Souce: ' + sourcedir + ' path: ' + str(spath))
print('Destination: ' + outdir + ' path: ' + str(dpath))
print('Current Working: ' + thisdir)
with open(notefile) as json_file:
    notelist = json.load(json_file)
    json_file.close()
    #print(notelist)
parser = parstrings(notelist).keywordcheck()

for entry in parser:
  
    print('==============================================================')
    print(entry + ' found')
    print(parser[entry])



# for item in notelist:
#     temptext = notelist[item]
#     tblob = TextBlob(temptext)
#     tblob = tblob.sentences
#     notelist[item] = tblob
#     for sent in range(len(tblob)):
#         sents.append(tblob[sent])    
#     cleanlist[item]= {'Sentences': str(sents)}
#     print(cleanlist[item])

# with open(os.path.join(dpath,'fulldata.json'), 'w') as fp:
#     newdata = json.dumps(cleanlist, indent = 4)
#     #print(newdata)
#     json.dump(newdata, fp)
#     newdict = json.loads(newdata)
    


# print('notelist data type = ' + str(type(notelist)))
# print('newdict data type = ' + str(type(newdict)))
# keylist = notelist.keys()
# print(keylist)
# for key in keylist:
#     print('')
#     print(key)
#     print(newdict[key])

# for item in keylist:
#     print('============================================ ' + item + ' ===============================')
#     bigdict[item] = newdict[item]
#     pp.pprint(bigdict[item])








