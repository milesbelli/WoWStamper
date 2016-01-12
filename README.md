# WoWStamper

Script to batch add exif data to WoW screenshots.

Primarily, this project will be focused on:

* Parsing Timestamp from screenshot filename
* Writing the "Date Taken" exif data to the file

As of now the idea is to run this once, but in the future this script could be modified to track which files have already been converted, and only update new files. This could even be set to run with the Windows Task Scheduler so that new screenshots are timestamped periodically.

In the even further future, it may be possible to add additional exif data, possibly using OCR, to add tags based on text we know will be in certain areas on screen (such as zone name beneath minimap).


* Some Disclaimers*

This was written on Windows (sorry). As a result, you should be able to run it without issue on your machine, but with file IO being an integral part of this, I have no idea if any of it will work in other OSes.

The script works, but it's very rudimentary, and right now the code needs to be modified to point at the appropriate directory, and it is specifically tailored for WoW screenshots.