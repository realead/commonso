cimport common

def set_value(val):
  common.SINGLETON_VALUE = val

def get_value():
  return common.SINGLETON_VALUE
