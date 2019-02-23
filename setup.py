from setuptools import setup, find_packages, Extension


#right path to shared-object:
import os
import sys
from distutils.util import get_platform

def get_path_to_sharedobject():
    PLAT_SPEC = "{platform}-{version[0]}.{version[1]}".format(platform=get_platform(), version=sys.version_info)
    return os.path.join("build", "lib." + PLAT_SPEC, 'commonso')


# Cython-extensions:
setter_ext = Extension(
                name='commonso.setter',
                sources = ["src/commonso/setter.pyx"],
                extra_link_args=["-Wl,-rpath=$ORIGIN/."],
                libraries = ['common'],
                library_dirs=[get_path_to_sharedobject()],
              )

getter_ext = Extension(
                name='commonso.getter',
                sources = ["src/commonso/getter.pyx"],
                extra_link_args=["-Wl,-rpath=$ORIGIN/."],
                libraries = ['common'],
                library_dirs=[get_path_to_sharedobject()],
              )

kwargs = {
      'name' : 'commonso',
      'ext_modules' :  [setter_ext, getter_ext],
      'setup_requires' : ["cython"],

      'packages' : find_packages(where='src'),
      'package_dir' : {"": "src"},
      'package_data' : { 'commonso': ['*.so']},
      'include_package_data' : True,
      'zip_safe' : False  #needed because setuptools are used
}



setup(**kwargs)
