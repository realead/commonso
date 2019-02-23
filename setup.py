import sys
from setuptools import setup, find_packages, Extension


setter_ext = Extension(
                name='commonso.setter',
                sources = ["src/commonso/setter.pyx", "src/commonso/common.c"]
              )

getter_ext = Extension(
                name='commonso.getter',
                sources = ["src/commonso/getter.pyx", "src/commonso/common.c"]
              )


kwargs = {
      'name' : 'commonso',
      'version' : '0.1.0',
      'description' : 'example how to install cython modules',
      'author' : 'Egor Dranischnikow',
      'url' : 'https://github.com/realead/commonso',
      'packages' : find_packages(where='src'),
      'package_dir' : {"": "src"},
      'license' : 'Unlicense',
      'ext_modules' :  [setter_ext, getter_ext],
      'setup_requires' : ["cython"],

       #ensure pxd-files:
      'package_data' : { 'commonso': ['*.pxd','*.pxi']},
      'include_package_data' : True,
      'zip_safe' : False  #needed because setuptools are used
}



setup(**kwargs)
