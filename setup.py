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
      'ext_modules' :  [setter_ext, getter_ext],
      'setup_requires' : ["cython"],

      'packages' : find_packages(where='src'),
      'package_dir' : {"": "src"},
}



setup(**kwargs)
