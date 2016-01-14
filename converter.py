# Must have pyexiftool (and exiftool) installed for this to work.
# Instructions to accomplish this can be found here:
# http://smarnach.github.io/pyexiftool/

import exiftool
from pathlib import Path

def writeExif(dateTime,targetPath):
    with exiftool.ExifTool() as et:
        
        # For reference, EXIF:CreateDate format is: 2014:09:02 10:58:53
        
        addDate = '-CreateDate=' + dateTime
        params = [bytearray(addDate, 'utf-8'),bytearray(targetPath, 'utf-8')]

        et.execute(*params)

        
def parseDateTime(name,strip):    
    
    for chars in strip:
        name = name.replace(chars,'')
    
    print(name)
    
    if(name.isnumeric() == True):
        
        formattedDate = ''.join(['20', name[4:6], ':', name[0:2], ':', name[2:4], ' ', name[6:8], ':', name[8:10], ':', name[10:12]])
        
        return (formattedDate)

def introText():
    print("WoWStamper 0.0.2 by Louis Mitas\n" +
          "To begin, fill in the following information:\n")

introText()
screenshotDir = input("TARGET FOLDER PATH:\n" +
                      "*All* image files in the target folder will be converted\n" +
                      "Path >")

dirPath = Path(screenshotDir)
nameStrip = ['WoWScrnShot','_','.','jpg']

if(dirPath.exists()):
    print('Now converting...')
    for file in dirPath.iterdir():
        strFile = str(file)
        fileName = strFile.replace(screenshotDir,'')
        
        dateTime = parseDateTime(fileName,nameStrip)
        dateTime = str(dateTime)
        writeExif(dateTime,strFile)


