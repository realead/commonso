import sys
from setuptools import setup, find_packages, Extension
#from setuptools.command.build_clib import build_clib


#right path to shared-object:
import os
import sys
import sysconfig

def path_to_lib_folder():
    """Returns the name of a distutils build directory"""
    f = "{dirname}.{platform}-{version[0]}.{version[1]}"
    dir_name = f.format(dirname='lib',
                    platform=sysconfig.get_platform(),
                    version=sys.version_info)
    return os.path.join('build', dir_name, 'commonso')


# Cython-extensions:
setter_ext = Extension(
                name='commonso.setter',
                sources = ["src/commonso/setter.pyx"],
                #extra_link_args=["-Wl,-rpath=$ORIGIN/."],
                #libraries=['common'], 
                #library_dirs=[path_to_lib_folder()],
              )

getter_ext = Extension(
                name='commonso.getter',
                sources = ["src/commonso/getter.pyx"],
                #extra_link_args=["-Wl,-rpath=$ORIGIN/."],
                #libraries=['common'], 
                #library_dirs=[path_to_lib_folder()],
              )

#clibraries:
libcommon = ('common', {'sources': ['src/commonso/common.c']})

kwargs = {
      'name' : 'commonso',
      'version' : '0.2.0',
      'description' : 'example how to install cython modules',
      'author' : 'Egor Dranischnikow',
      'url' : 'https://github.com/realead/commonso',
      'packages' : find_packages(where='src'),
      'package_dir' : {"": "src"},
      'license' : 'Unlicense',
      'ext_modules' :  [setter_ext, getter_ext],
      'setup_requires' : ["cython"],

       'libraries' : [libcommon],
       #'cmdclass' : {'build_clib': build_clib},

       #ensure pxd-files:
      'package_data' : { 'commonso': ['*.pxd','*.pxi']},
      'include_package_data' : True,
      'zip_safe' : False  #needed because setuptools are used
}



setup(**kwargs)
