from distutils.core import setup, Extension
from os import getenv
import sys
import os
p = sys.prefix
NUMPYPATH = '.'
if os.path.isdir(p + '/include/numpy'):
  NUMPY = 'NUMPY'
elif os.path.isdir(p + 'lib/python2.7/site-packages/numpy/core/include/numpy'):
  NUMPY = 'NUMPY'
  NUMPYPATH = p + 'lib/python2.7/site-packages/numpy/core/include/numpy'
else:
  NUMPY = 'NONUMPY'
print 'numpy: ' + NUMPY
windir = getenv('windir')
if windir == None:
  WIN32 = 'NOWIN32'
  LPSOLVE55 = '../../lpsolve55/bin/osx64'
else:
  WIN32 = 'WIN32'
  LPSOLVE55 = '../../lpsolve55/bin/osx64'
setup (name = "lpsolve55",
       version = "5.5.0.10",
       description = "Linear Program Solver, Interface to lpsolve",
       author = "Peter Notebaert",
       author_email = "lpsolve@peno.be",
       url = "http://www.peno.be/",
       py_modules=['lp_solve', 'lp_maker'],
       ext_modules = [Extension("lpsolve55",
				["lpsolve.c", "hash.c", "pythonmod.c"],
                                define_macros=[('PYTHON', '1'), (WIN32, '1'), ('NODEBUG', '1'), ('DINLINE', 'static'), (NUMPY, '1'), ('_CRT_SECURE_NO_WARNINGS', '1')],
                                include_dirs=['../..', '/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/usr/include', '/Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.13.sdk/usr/include/malloc'],
                                library_dirs=[LPSOLVE55],
				libraries = ["lpsolve55"])
		      ]
)
