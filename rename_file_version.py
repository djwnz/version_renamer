# Program to rename a hex file based on version numbers it extracts from other supplied files.
# David Wright
# Pumpkin Inc. 
# 2017

import sys
import os
from datetime import date
from time import sleep

# extract the commands from the command line call
commands = sys.argv

# get working directory
directory = os.getcwd()

# check to verify that there are the correct number of them
if len(commands)>4:
    print "Error: too many arguments given"
    print "Please Run as:"
    print "rename_file_version.exe module_filename supmcu_filename hex_filename"
    sys.exit()
# end if
    
if len(commands)<4:
    print "Error: not enough arguments given"
    print "Please Run as:"
    print "rename_file_version.exe module_filename supmcu_filename hex_filename"
    sys.exit()
# end if

module_filename = commands[1]
supmcu_filename = commands[2]
hex_filename = commands[3]

module_version = ''
supmcu_version = ''
hw_version = ''

def extract_version(filename, key):
    
    # read all lines from the file
    with open(filename, 'r') as f:
        content = f.readlines() 
    # end with
    
    # iterate through line in the file, backwards to get the most recent version
    for line in reversed(content):
        if key in line:
            # this is the line we want to get data from
            # data is in quote makes on this line
            version = line.split('"')[-2]
            # remove all whitespace from the version and return
            return ''.join(version.split())
        # end if
    # end for
    
    # If you get this far then no version was found
    print 'Error: no ' + key + ' was found in \n' + filename
    
    sys.exit()
# end def   


# Find the desired information from the module_file
if (module_filename[1] == ':'):
    # using absolute addressing
    if not os.path.isfile(module_filename):
        # the requested module file does not exist
        print "Error: module_filename provided does not exist"
        sys.exit()
        
    else:
        # the file does exist so extract the information
        module_version = extract_version(module_filename, 'STR_MODULE_VERSION')
        hw_version = extract_version(module_filename, 'STR_HW_REVISION')
    # end if

else:
    # using relative addressing
    absolute_filename = directory + '/' + module_filename
    if not os.path.isfile(absolute_filename):
        print "Error: module_filename provided does not exist"
        sys.exit()
        
    else:
        # the file does exist so extract the information
        module_version = extract_version(absolute_filename, 'STR_MODULE_VERSION')
        #hw_version = extract_version(absolute_filename, 'STR_HW_REVISION')
    # end if   
# end if

# Find the desired information from the supmcu_file
if (supmcu_filename[1] == ':'):
    # using absolute addressing
    if not os.path.isfile(supmcu_filename):
        # the requested supmcu file does not exist
        print "Error: supmcu_filename provided does not exist"
        sys.exit()
        
    else:
        # the file does exist so extract the information
        supmcu_version = extract_version(supmcu_filename, 'STR_SUPMCU_VERSION')
    # end if

else:
    # using relative addressing
    absolute_filename = directory + '/' + supmcu_filename
    if not os.path.isfile(absolute_filename):
        print "Error: supmcu_filename provided does not exist"
        sys.exit()
        
    else:
        # the file does exist so extract the information
        supmcu_version = extract_version(absolute_filename, 'STR_SUPMCU_VERSION')
    # end if   
# end if

# Rename the hex file.
if (hex_filename[1] == ':'):
    # using absolute addressing
    full_hex_filename = hex_filename

else:
    full_hex_filename = directory + '/' + hex_filename
# end if

if not os.path.isfile(full_hex_filename):
    # the requested module file does not exist
    print "Error: hex_filename provided does not exist"
    sys.exit()
# end

# find beginning of file extension
dot_index = full_hex_filename.rfind('.')

# format today's date
today_date = date.today().timetuple()
date_format = str(today_date[0]) + str(today_date[1]) + str(today_date[2])

# join the components of the filename
joined_filename = '-'.join([full_hex_filename[0:dot_index], hw_version, module_version, supmcu_version, date_format])

# add the extension back on
new_hex_filename = joined_filename + full_hex_filename[dot_index:]
    
try:
    # attempt to change the files name to see if it is available.
    os.rename(full_hex_filename,new_hex_filename)
    print 'File Renaming Successful'
except OSError as e:
    # renaming was not possible as another program is using it.
    print 'Error: Another program is still using ' + hex_filename
# end try
     

