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
        
        #print(params)
        et.execute(*params)
        #metadata = et.get_metadata(targetPath)
        #print(metadata)
        
def parseDateTime(name,prefix):
    
    #name is required, prefix is optional
    #future task: change prefix to list of things to remove, iterate through
    
    #lot of crap to get rid of, I need to tidy this up
    s = name.replace(prefix,'')
    s = s.replace('_','')
    s = s.replace('.','')
    s = s.replace('jpg','')
    #print(s)
    
    if(s.isnumeric() == True):
        
        formattedDate = ''.join(['20', s[4:6], ':', s[0:2], ':', s[2:4], ' ', s[6:8], ':', s[8:10], ':', s[10:12]])
        
        return (formattedDate)
        

screenshotDir = 'E:\\ProgFiles WoW\\World of Warcraft\\test\\'
dirPath = Path(screenshotDir)
filePrefix = 'WoWScrnShot_'

if(dirPath.exists()):
    print('Now converting...')
    for file in dirPath.iterdir():
        strFile = str(file)
        fileName = strFile.replace(screenshotDir,'')
        
        dateTime = parseDateTime(fileName,filePrefix)
        dateTime = str(dateTime)
        writeExif(dateTime,strFile)


