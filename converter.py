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
        
        if(et.get_tag('CreateDate',targetPath) == None):
            et.execute(*params)
            return True
        else: 
            return False
            
                    
def parseDateTime(name,strip):    
    
    for chars in strip:
        name = name.replace(chars,'')
    
    if(name.isnumeric() == True):
        formattedDate = ''.join(['20', name[4:6], ':', name[0:2], ':', name[2:4], ' ', name[6:8], ':', name[8:10], ':', name[10:12]])
        return (formattedDate)
    else: return ''


def introText():
    print("WoWStamper 1.1.1 by Louis Mitas\n" +
          "To begin, fill in the following information:\n")
    


introText()

screenshotDir = ''
print("TARGET FOLDER PATH:\n"
      "*All* image files in the target folder will be processed\n")
while(screenshotDir == ''): screenshotDir = input("Path? ")

procLimit = input("\nCONVERSION LIMIT:\n"
                  "Set limit to number of files to process this batch (must be an integer)\n"
                  "Or press return for no limit\n"
                  "\nLimit? ")

dirPath = Path(screenshotDir)
nameStrip = [screenshotDir,'\\','WoWScrnShot','_','.','jpg','tif']

if(dirPath.exists()):

    fileList = []
    for file in dirPath.iterdir(): fileList.append(file)

    print('\nNow processing...')
    
    if (procLimit.isdigit() == False):
        procLimit = len(fileList)
        allFiles = True
    else:
        procLimit = int(procLimit)
        allFiles = False
        
    i = 0
    skipped = 0
    iOffset = 0
    procLimitOffset = 0
    
    while (i < procLimit):
        strFile = str(fileList[i])
        dateTime = parseDateTime(strFile,nameStrip)
        dateTime = str(dateTime)
        exifSuccess = False
        
        if (dateTime != ''): exifSuccess = writeExif(dateTime,strFile)
        if (exifSuccess == False):
                skipped += 1
                if(skipped > 1): fileWord = ' files'
                else: fileWord = ' file'
                skipMsg = ', skipped ' + str(skipped) + fileWord + ' because of reasons'
                # Our skipped file should not be counted towards the total
                iOffset += 1
                # If processing all files, skipped file must be accounted for
                procLimitOffset += 1
                if(allFiles == False): procLimit += 1
        
        i += 1
        
        if(procLimit > procLimitOffset):
            percentProc = '(' + str(int(100*(i-iOffset)/(procLimit-procLimitOffset))) + '%)'
        else: percentProc = '(0%)'
        
        print('\r' + str(i-iOffset) + ' of ' + str(procLimit-procLimitOffset) + ' files processed ' + percentProc + skipMsg + ' ',end='')
        
    
    input ('\nProcessing complete. Press enter to exit.')