

import subprocess
import re

# command to find list of torrents
transmission_list = 'transmission-remote -l'
# run process and capture output
process = subprocess.Popen(transmission_list.split(), stdout=subprocess.PIPE)
transmission_output = process.communicate()[0]

# split output into strings
transmission_list = transmission_output.split()


# if one or more of the torrents are seeding
if 'Seeding' in transmission_list:

	# store index of the seeding
	index = transmission_list.index('Seeding')
	ids = []

	# loop through and get id indexes 
	for x in transmission_list:

		# if only numbers without . (trying to find ints)
		if re.match("^[0-9]*$", x):
			ids.append(transmission_list.index(x))

	# for each id
	for y in ids:

		# if the index of seeding is the appropriate distance away such that it is an id
		if index - y > 4 and index - y < 10:

			# remove torrent command with id
			remove_torrent_cmd = "transmission-remote -t " + str(transmission_list[y]) + " -r"
			process = subprocess.Popen(remove_torrent_cmd.split(), stdout=subprocess.PIPE)
			remove_torrent_output = process.communicate()[0]

			# make sure success


