# Loop through lay-k

import os  # importing built-in library "os" which means operating system

# Taking the folder lay-k since we want information about Kenneth Lay (the CEO of Enron)
# Remember to take "\\" as python considers "\" as escape character
rootdir = "F:\\enron_mail_20150507\\maildir\\lay-k"

# Using os.walk to traverse the directory tree
for directory, subdirectory, filenames in os.walk(rootdir):
    print('directory:',directory, ' subdirectory:',subdirectory, ' No. of files:',len(filenames))
