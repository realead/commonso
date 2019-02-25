#if defined _WIN32 || defined __CYGWIN__
  #ifdef BUILDING_DLL
      #define DLL_PUBLIC __declspec(dllexport)
  #else
      #define DLL_PUBLIC __declspec(dllimport)
  #endif
#else
    #define DLL_PUBLIC __attribute__ ((visibility ("default")))
#endif

DLL_PUBLIC extern int SINGLETON_VALUE;

