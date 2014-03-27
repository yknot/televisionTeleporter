

import subprocess
import re

# command to find list of torrents
transmission_list = 'transmission-remote -l'
# run process and capture output
process = subprocess.Popen(transmission_list.split(), stdout=subprocess.PIPE)
transmission_output = process.communicate()[0]

# split output into strings by line
transmission_lines = transmission_output.splitlines()
nlines=len(transmission_lines)

# directory listing command, to provide list of folders for name comparison
list_cmd= 'ls /media/storage/XBMCMedia/TV\ Shows/'
process = subprocess.Popen(list_cmd.split(), stdout=subprocess.PIPE)
list_output = process.communicate()[0]
show_dirs=list_output.splitlines()


# to be used in target directory string
dir_stem='/media/storage/XBMCMedia/TV\ Shows/'

# for each line
for i in transmission_lines:

        transmission_list=transmission_lines[i].split()
        # if one or more of the torrents are seeding
        if 'Seeding' in transmission_list:

                # store index of the seeding
                #Commenting out older code# index = transmission_list.index('Seeding')
                #ids = []

                # get torrent ID number
        `       tor_id= transmission_list[0]

                # get torrent name (for moving torrents)
                tor_name=transmission_list[len(transmission_list)-1]
                # remove torrent command with id
                remove_torrent_cmd = "transmission-remote -t " + str(tor_id) + " -r"
                process = subprocess.Popen(remove_torrent_cmd.split(), stdout=subprocess.PIPE)
                remove_torrent_output = process.communicate()[0]

                # make sure success

                # parse name
                name=tor_name.split('.')

                # Need code to find target directory, I thought about this a bit.
                # We might not even need an xml file, we can likely get away with just using bash.
                # Using ls with wildcards (taken from filenames of torrents)
                # we should be able to deduce what the target directory is.
                # This would also make it easier than figuring out where to put
                # the backslashes for spaces in folder names.
                # We could even have python figure out which directory it is, given filename 
                

                # move command (commented out until target directory is coded)
                # move_command="mv Torrents/" + str(tor_name) + " " + str(target_directory)

                
