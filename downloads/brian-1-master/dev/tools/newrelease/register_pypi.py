'''
NOTE: you need a .pypirc file to do this, you may need to set the
HOME env to where it is saved. Also note that any spaces in the
filename of HOME will cause it to not work, so use old style 8.3
equivalent name.

Also note that manifest.in may not work right with this?
'''
import os
from distutils.core import run_setup

pathname = os.path.abspath(os.path.dirname(__file__))
os.chdir(pathname)
os.chdir('../../../.') # work from Brian's root
run_setup('setup.py', ['register'])
os.environ['BRIAN_SETUP_NO_EXTENSIONS'] = '1' 
run_setup('setup.py', ['sdist', '--formats=gztar,zip',
                       'bdist_wininst', '--plat-name=win32',
                       'upload'])
del os.environ['BRIAN_SETUP_NO_EXTENSIONS']
