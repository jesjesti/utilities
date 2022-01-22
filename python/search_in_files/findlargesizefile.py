import glob
import os
dir_name = ''
# Get list of files in a directory & sub-directories
list_of_files = filter( os.path.isfile,
                        glob.glob(  dir_name + '/**/*',
                                    recursive=True) )
# Find the file with max size from the list of files
max_file = max( list_of_files,
                key =  lambda x: os.stat(x).st_size)
print('Max File: ', max_file)
print('Max File size in bytes: ', os.stat(max_file).st_size)