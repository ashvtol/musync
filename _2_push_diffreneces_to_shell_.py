import os
import glob
import sys
name = sys.argv[1];
phone_storage = sys.argv[2];
#####################################################
## Parse Path
def parsepath(oldpath):
    path = "";
    for i in range(len(oldpath)):
        if(not((oldpath[i].isalnum()) or (oldpath[i]=='/') or (oldpath[i]=="."))):
        ##        print(str[i], end='');
            path = path +"\\"+oldpath[i] 
        else:
            path = path + oldpath[i];
    return path;
        
#####################################################


#####################################################
## Map the old entries
ct = 0
with open('./olog',"r", encoding="utf-8") as f:
    array = {}
    for line in f:
        line = line.strip();
        array.update({line:1})
f.close();
#####################################################
##if(array['04 Jhalla Wallah.mp3']==1):
##    print("True");
#####################################################


#####################################################
##Remap Process
flag = 0
updatedct = 0
lp = 0
olog = open('./olog','ab')
shell = open('./push.sh','wb')
shell.write(('\n').encode('utf-8'))
for filename in glob.glob('/Users/'+name+'/Music/iTunes/iTunes Media/Music/**/*.mp3', recursive=True):
    name = filename
    path = parsepath(filename)
    ct = ct+1
    lp = lp+1;
##    if(lp>14):
##        break;       
    name = name.split('/')
##    print(array[name[-1]+'\n'])
    try:
       array[name[-1]]
        
    except KeyError:
        ## if key not found, update olog and push it to the device
        print(name[-1])
        name = (name[-1] + '\n').encode('utf-8')
        olog.write(name)
        shell.write(('adb push ' + path + ' /'+phone_storage+'\n').encode('utf-8'))
        flag = 1;
        updatedct = updatedct + 1;
        
        
    else:
##        if(array[name[-1]+'\n']):
##            lp = lp+1;
##            print(lp,".",sep='', end='')
##            print(name[-1], "True");
        continue;
#####################################################

#####################################################
#File Close
olog.close()
shell.write(("\necho '**********************AZ**********************' \n").encode('utf-8'))
shell.write(("  echo '*             File Transfer Complete         *'\n").encode('utf-8'))
shell.write(("echo   '**********************************************' \n").encode('utf-8'))
shell.close()
print("Total Files Updated = ", updatedct)
#####################################################


