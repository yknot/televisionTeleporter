

import subprocess
import re

# command to find list of torrents
transmission_list = 'transmission-remote -l'
# run process and capture output
process = subprocess.Popen(transmission_list.split(), stdout=subprocess.PIPE)
transmission_output = process.communicate()[0]

# split output into strings
transmission_lines = transmission_output.splitlines()
nlines=len(transmission_lines)

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

                # Old code comments, to keep in case I broke something
                # loop through and get id indexes 
                # for x in transmission_list:
                
                        # if only numbers without . (trying to find ints)
                #        if re.match("^[0-9]*$", x):
                #                ids.append(transmission_list.index(x))

                # for each id
                # for y in ids:

                #        # if the index of seeding is the appropriate distance away such that it is an id
                #        if index - y > 4 and index - y < 10:

                                

