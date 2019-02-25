from setuptools import setup, find_packages, Extension
from setuptools.command.build_clib import build_clib as orig_build_clib


#right path to shared-object:
import os
import sys
import platform
from distutils.util import get_platform

def get_path_to_sharedobject():
    PLAT_SPEC = "{platform}-{version[0]}.{version[1]}".format(platform=get_platform(), version=sys.version_info)
    return os.path.join("build", "lib." + PLAT_SPEC, 'commonso')

def get_shared_object_name(lib_name):
    if platform.system() == 'Windows':
        return lib_name+'.dll'
    else:
        return 'lib'+lib_name+'.so'

def get_extra_link_args():
    if platform.system() == 'Windows':
        return []
    else:
        return ["-Wl,-rpath=$ORIGIN/."]


class build_shared_clib(orig_build_clib):

    def finalize_options(self):
        super(build_shared_clib, self).finalize_options()
        self.build_clib = get_path_to_sharedobject()

    def build_libraries(self, libraries):
        for (lib_name, build_info) in libraries:
            # First, compile the source code to object files in the library
            # directory.  (This should probably change to putting object
            # files in a temporary build directory.)
            macros = build_info.get('macros')
            include_dirs = build_info.get('include_dirs')
            cflags = build_info.get('cflags')
            sources = list(build_info.get('sources'))
            objects = self.compiler.compile(
                    sources,
                    output_dir=self.build_temp,
                    macros=macros,
                    include_dirs=include_dirs,
                    extra_postargs=cflags,
                    debug=self.debug
                    )

            # Now link shared object
            language = self.compiler.detect_language(sources)
            self.compiler.link_shared_object(
                objects,                     
                get_shared_object_name(lib_name),
                output_dir=self.build_clib, 
                target_lang=language
                )


# Cython-extensions:
setter_ext = Extension(
                name='commonso.setter',
                sources = ["src/commonso/setter.pyx"],
                extra_link_args = get_extra_link_args(),
              )

getter_ext = Extension(
                name='commonso.getter',
                sources = ["src/commonso/getter.pyx"],
                extra_link_args = get_extra_link_args(),
              )

libcommon = ('common', {'sources': ['src/commonso/common.c'], 'cflags' : ['-O2']})

kwargs = {
      'name' : 'commonso',
      'ext_modules' :  [setter_ext, getter_ext],
      'setup_requires' : ["cython"],

      'libraries' : [libcommon],
      'cmdclass' : {'build_clib': build_shared_clib},

      'packages' : find_packages(where='src'),
      'package_dir' : {"": "src"},
}



setup(**kwargs)
