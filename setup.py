from distutils.core import setup
import py2exe

# create the required setup configuration
setup(console=[{'script':'rename_file_version.py', # Top level file to read in
                'dest_base': 'rename_file_version'}], # base directory
      options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
      zipfile = None
      )