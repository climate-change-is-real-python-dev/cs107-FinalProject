#!/usr/bin/env python3

import runpy
runpy.run_path(path_name='tests/gradient_tests.py')
runpy.run_path(path_name='tests/forwardAD_tests.py')
runpy.run_path(path_name='tests/forwardAD_pro_tests.py')