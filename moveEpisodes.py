
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
list_cmd= '/media/storage/XBMCMedia/TV Shows/'
process = subprocess.Popen(['ls', list_cmd], stdout=subprocess.PIPE)
list_output = process.communicate()[0]
show_dirs=list_output.splitlines()


# to be used in target directory string
dir_stem='/media/storage/XBMCMedia/TV Shows/'

# for each line
for i in xrange(len(transmission_lines)):

        transmission_list=transmission_lines[i].split()
        # if one or more of the torrents are seeding
        if '100%' in transmission_list:

                # get torrent ID number
                tor_id= transmission_list[0]


                # get torrent name (for moving torrents)
                tor_name=transmission_list[len(transmission_list)-1]
                 
                # make sure success

                target_dir = ''

                # parse name
                for j in xrange(len(show_dirs)):
                        
                        # convert directory name eztv format
                        temp=show_dirs[j].lower()
                        temp=temp.replace(" ", ".")
                        dummy_tor_name=tor_name.lower()

                        if temp in dummy_tor_name:
                             # find season number
                             reg_s=re.search("[s,S][0-9][0-9]",tor_name)
                             season=reg_s.group()
                             season_int=str(int(season[1:]))
                             season_str=season[1:]
                             

                             # create path to show directory
                             show_path=dir_stem + str(show_dirs[j]) + "/"
                             


                             # list directories in show's directory (season folders)
                             process2 = subprocess.Popen(['ls', show_path], stdout=subprocess.PIPE)
                             s_output = process2.communicate()[0]
                             season_dirs=s_output.splitlines()

                             create_dir=True
                             # find correct season directory, or create new
                             for k in xrange(len(season_dirs)):
                                     if season_str in season_dirs[k]:
                                             create_dir=False
                                             target_dir=show_path + str(season_dirs[k]) + "/"
                                             # move command
                                             tor_path= "/home/xbmc/Torrents/" + str(tor_name)
                                             process4 = subprocess.Popen(['mv', tor_path, target_dir], stdout=subprocess.PIPE)
                                             
                                             # remove torrent command with id
                                             remove_torrent_cmd = "transmission-remote -t " + str(tor_id) + " -r"
                                             process = subprocess.Popen(remove_torrent_cmd.split(), stdout=subprocess.PIPE)
                                             remove_torrent_output = process.communicate()[0]
                                             break
                                     elif season_int in season_dirs[k]:
                                             create_dir=False
                                             target_dir=show_path + str(season_dirs[k]) + "/"
                                             # move command
                                             tor_path= "/home/xbmc/Torrents/" + str(tor_name)
                                             process4 = subprocess.Popen(['mv', tor_path, target_dir], stdout=subprocess.PIPE)
                                        
                                             # remove torrent command with id
                                             remove_torrent_cmd = "transmission-remote -t " + str(tor_id) + " -r"
                                             process = subprocess.Popen(remove_torrent_cmd.split(), stdout=subprocess.PIPE)
                                             remove_torrent_output = process.communicate()[0]
                                             break
                             if create_dir:
                                     new_dir=show_path+"Season "+season_str+"/"
                                     process3 = subprocess.Popen(['mkdir', new_dir], stdout=subprocess.PIPE)
                                     target_dir=new_dir
                                     # move command
                                     tor_path= "/home/xbmc/Torrents/" + str(tor_name)
                                     process4 = subprocess.Popen(['mv', tor_path, target_dir], stdout=subprocess.PIPE)
                                
                                     # remove torrent command with id
                                     remove_torrent_cmd = "transmission-remote -t " + str(tor_id) + " -r"
                                     process = subprocess.Popen(remove_torrent_cmd.split(), stdout=subprocess.PIPE)
                                     remove_torrent_output = process.communicate()[0]
                                     print target_dir                        
