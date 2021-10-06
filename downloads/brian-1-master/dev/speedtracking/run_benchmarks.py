'''
Run benchmarks for all revisions of Brian in the repository, starting with
version 1.0.0 and only using every tenth revision.
To run the benchmark on your machine you need the following python packages:
* vbench: https://github.com/pydata/vbench
You have to download/clone it from the github page and use
"python setup.py install"

vbench has two more dependencies (those are available on pypi.python.org so 
you can simply use easy_install or pip) 
* sqlalchemy: http://pypi.python.org/pypi/SQLAlchemy
* pandas: http://pypi.python.org/pypi/pandas

vbench also needs the pstats module that is part of the Python standard library
but sometimes has to be installed separately, e.g. as part of the
python-profiler package on Debian/Ubuntu systems.

vbench currently only supports git repositories. As Brian uses a SVN repository,
it has to use "git svn clone" first to convert it to git -- this should be done
automatically but you obviously need a working installation of git together
with the git-svn extension.

Benchmark results are saved in a database, therefore if you add new benchmarks
or if new revisions appear, only the new things will be run. It might make sense
to delete the database and re-run all benchmarks from time to time to avoid 
treating improvements/regressions in external libraries as numpy/scipy as 
improvements /regressions in Brian.
'''

import os, sys
import tempfile
from datetime import datetime
import pstats

try:
    import sqlalchemy
except ImportError:
    raise ImportError('You need to have sqlalchemy installed: http://pypi.python.org/pypi/SQLAlchemy/')

try:
    import pandas    
except ImportError:
    raise ImportError('You need to have pandas installed: http://pypi.python.org/pypi/pandas')

try:
    from vbench.api import Benchmark, BenchmarkRunner, GitRepo
except ImportError:
    raise ImportError('You need to have vbench installed: https://github.com/pydata/vbench')

# inspired by https://github.com/wesm/pandas/blob/master/vb_suite/suite.py
modules = ['benchmark_connections',
           'benchmark_spikegenerator',
           'benchmark_stdp']

by_module = {}
benchmarks = []

# automatically adds all the benchmarks from the above modules
for modname in modules:
    ref = __import__(modname)
    by_module[modname] = [v for v in ref.__dict__.values()
                          if isinstance(v, Benchmark)]
    benchmarks.extend(by_module[modname])

if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) > 3 or not os.path.isabs(sys.argv[1]):
        sys.stderr.write('Usage: python run_benchmarks.py PATH [n]\n' +
                         'where PATH is an absolute path that will be used as the base path for saving results.\n')            
        sys.exit(1)

    # if the directory does not exist it will be created
    PATH = sys.argv[1]
    
    if len(sys.argv) == 3:
        try:
            run_option = int(sys.argv[2])
            if run_option < 1:
                raise ValueError()
        except ValueError:
            sys.stderr.write('n has to be an integer number > 0 not %r\n' % sys.argv[2])
            sys.exit(2)
    else:
        run_option = 10

    DB_PATH = os.path.join(PATH, 'benchmarks.db')
    
    SVN_URL = 'https://neuralensemble.org/svn/brian/trunk'
    REPO_PATH = os.path.join(PATH, 'brian-trunk')
    if not os.path.exists(REPO_PATH):
        # create the repository
        os.makedirs(REPO_PATH)
        os.system('git svn clone %s %s' % (SVN_URL, REPO_PATH))
    else:
        # update the repository (can only be called from the directory...) 
        os.chdir(REPO_PATH)
        os.system('git svn rebase')
        os.system('git svn fetch')

    REPO_URL = 'file://' + REPO_PATH

    TMP_DIR = tempfile.mkdtemp(suffix='vbench')

    # Those two are not really needed at the moment as no C extensions are
    # compiled by default
    # TODO: Does using sys.executable here work on Windows? 
    PREPARE = "%s setup.py clean" % sys.executable
    BUILD = "%s setup.py build_ext" % sys.executable

    START_DATE = datetime(2008, 9, 23) # Brian version 1.0.0

    repo = GitRepo(REPO_PATH)

    runner = BenchmarkRunner(benchmarks, REPO_PATH, REPO_URL, BUILD, DB_PATH,
                             TMP_DIR, PREPARE, run_option=run_option, 
                             start_date=START_DATE)
    runner.run()
