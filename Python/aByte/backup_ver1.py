#!/usr/bin/python
# Filename: backup_ver1.py

import os
import time

# 1. The files and dirs to be backed up are specified in a list.
source = ['/c/workspace/git/learning/Python/aByte', '/c/workspace/git/learning/Python/helloPy']

# 2. /the backup must be stored in a main backup dirs
target_dir = '/c/temp/'

# 3. The files are backed up into a zip file.

# 4. The name of the zip archive is the current date and time
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "tar -czvf '%s ' %s"%(target, ' '.join(source))
# run the backup_ver1

if os.system(zip_command) == 0:
    print 'Successful backup to ', target
else:
    print 'Backup FAILED'
