import os
if 'DOCROOT' in os.environ:
    os.chdir(os.environ['DOCROOT'])
else:
    os.chdir('../../../')

os.chdir('docs_sphinx') # work from docs_sphinx/ directory until we make the big change
# if this doesn't work, run build_html_clean.py instead
os.system('sphinx-build -b html . ../docs')
