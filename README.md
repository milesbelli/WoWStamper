# WoWStamper
Script to batch add exif data to WoW screenshots.

Primarily, this project will be focused on:

* Reading Timestamp from screenshot filename
* Writing the "Date Taken" exif data to the file

As of now the idea is to run this once, but in the future this script could be modified to track which files have already been converted, and only update new files. This could even be set to run with the Windows Task Scheduler so that new screenshots are timestamped periodically.

