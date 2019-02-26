# commonso

example how to share cpp-files between cython modules

## History

 1. Version building cpp in both cython-modules -> Singleton isn't singleton any longer
 2. Version with prebuilt shared-object, works only on windows
 3. Version with default `build_clib`, but it builds a static library -> as version 1, Singleton isn't singleton anymore
 4. Version with special `build_clib`, which build shared library
 5. Version works also for windows

See also `so_answer` for a more precise version.

## Test

run `sh test_instalation.sh`

### Known shortcoming:

 1.  doesn't work correct for `--build-base` and similar options.

