# Loop through all the files in the dataset

import os  # importing built-in library "os" which means operating system

# Considering whole data-set
# Remember to take "\\" as python considers "\" as escape character
rootdir = "F:\\enron_mail_20150507\\maildir"

# Using os.walk to traverse the directory tree i.e., loops through our directory & gives folders,sub-folders & filenames
for directory, subdirectory, filenames in os.walk(rootdir):
    print('directory:',directory, ' subdirectory:',subdirectory, ' No. of files:',len(filenames))