# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 09:38:33 2024

@author: george.alves
"""

import sys
from streamlit.web import cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "files/app.py"]
    sys.exit(stcli.main())