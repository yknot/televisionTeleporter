televisionTeleporter
====================

A continously running media management script

Update 3/25/2014:
Made changes to split by line, then split each line by whitespace. Now gets ID number and torrent name.

Update 3/27/14
Added some foundation for finding target directory for moving the files.  May not require XML file at all,
if we are clever/a bit janky with our use of both python and bash.  I figure if we split the filenames by 
periods, we can see if the resultant strings match up with any of our directory names (which we could do 
either with creative ls commands, or having python compare the separate strings of the filenames with the 
names of our directories, or some form of both).  Once we have a reliable way of finding the target directory,
this part of the teleporter is good to go.

Update 3/27/14 (2)
Target directory code completed, script should be smart enough to automatically move things now!