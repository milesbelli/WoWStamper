# Must have pyexiftool (and exiftool) installed for this to work.
# Instructions to accomplish this can be found here:
# http://smarnach.github.io/pyexiftool/

import exiftool
from pathlib import Path
import sys

def writeExif(dateTime,targetPath):
    with exiftool.ExifTool() as et:
        
        # For reference, EXIF:CreateDate format is: 2014:09:02 10:58:53
        
        addDate = '-CreateDate=' + dateTime
        params = [bytearray(addDate, 'utf-8'),bytearray(targetPath, 'utf-8')]

        et.execute(*params)

        
def parseDateTime(name,strip):    
    
    for chars in strip:
        name = name.replace(chars,'')
    
    if(name.isnumeric() == True):
        formattedDate = ''.join(['20', name[4:6], ':', name[0:2], ':', name[2:4], ' ', name[6:8], ':', name[8:10], ':', name[10:12]])
        return (formattedDate)


def introText():
    print("WoWStamper 0.0.2 by Louis Mitas\n" +
          "To begin, fill in the following information:\n")
    


introText()

screenshotDir = ''
print("TARGET FOLDER PATH:\n" +
      "*All* image files in the target folder will be converted\n")
while(screenshotDir == ''): screenshotDir = input("Path >")

procLimit = input("CONVERSION LIMIT:\n" +
                  "Set limit to number of files to convert this batch (must be an integer)\n" +
                  "Or press return for no limit\n"
                  "Limit >")

dirPath = Path(screenshotDir)
nameStrip = ['WoWScrnShot','_','.','jpg']

if(dirPath.exists()):

    fileList = []
    for file in dirPath.iterdir(): fileList.append(file)

    print('Now converting...')

    if (procLimit.isdigit() == False): procLimit = (len(fileList) - 1)
    else: procLimit = int(procLimit)
    
    i = 0
    
    while (i < procLimit):
        strFile = str(fileList[i])
        fileName = strFile.replace(screenshotDir,'')
        dateTime = parseDateTime(fileName,nameStrip)
        dateTime = str(dateTime)
        
        writeExif(dateTime,strFile)
        
        i += 1
        
        print(str(i) + ' of ' + str(procLimit) + ' files converted')
        
    
    print ('Conversion complete')
        
        



