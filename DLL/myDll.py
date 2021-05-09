from System import IO
from System.IO.Path import Combine

def walk(folder):
  for file in IO.Directory.GetFiles(folder):
    yield file
  for folder in IO.Directory.GetDirectories(folder):
    for file in walk(folder): yield file

folder = IO.Path.GetDirectoryName(__file__)
all_files = list(walk(Combine(folder, 'moduleName')))

import clr
clr.CompileModules(Combine(folder, "myDll.dll"), *all_files)
