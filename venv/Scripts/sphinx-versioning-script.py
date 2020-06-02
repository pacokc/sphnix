#!c:\users\pacok\desktop\pp\pythonprojects\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'sphinxcontrib-versioning==2.2.1','console_scripts','sphinx-versioning'
__requires__ = 'sphinxcontrib-versioning==2.2.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('sphinxcontrib-versioning==2.2.1', 'console_scripts', 'sphinx-versioning')()
    )
