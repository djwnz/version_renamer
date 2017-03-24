import subprocess
import os
import time

exit = False
######################### Requires py2exe Installed ########################
try:
    # Does py2exe exist?
    import py2exe
except ImportError, e:
    print '**** this build requires \'py2exe\' ****'
    exit = True
# end

if exit:
    sys.exit()
# end

# install setup.py
inst = subprocess.Popen(['python', 'setup.py', 'install'], cwd=os.getcwd())
inst.wait()
print '\n## Setup.py installed\n'

# build the .exe file
exe = subprocess.Popen(['python', 'setup.py', 'py2exe'], cwd=os.getcwd())
exe.wait()
time.sleep(1)
print '\n## .exe created\n'
time.sleep(2)