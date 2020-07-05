import logging

import pymel.core as pmc
from pymel.core.system import Path
from pymel.core.system import versions

import os

log = logging.getLogger(__name__)

"""patha = Path()"""


class SceneFile(object):
 """This class represents a DCC software scene file"""
 def __init__(self, dir='', descriptor='main', version=1, ext="ma"):
    """Returns the DCC scene file name"""
    self._dir = Path(dir)
    self.descriptor = descriptor
    self.version = version
    self.ext = ext

 @property
 def dir(self):
     
     return Path(self._dir)


 @dir.setter
 def dir(self, val):
     
     self._dir = Path(val)

 def basename(self):

    name_pattern = "{descriptor}_{version:03d}.{ext}"
    name = name_pattern.format(descriptor=self.descriptor,
        version=self.version,
        ext=self.ext)
    return name

 def path(self):



    return Path(self.dir) / self.basename()

 def save(self):

    try:
        pmc.system.saveAs(self.path())
    except RuntimeError:
        log.warning("Missing directories. Creating directiories...")
        self.dir.makedirs_p()
        pmc.system.saveAs(self.path())

    def increment_save(self):
        CurrentVersion = self.version
        for i in self.dir.files('*.ma'):
            parts = os.path.split(i)
            Directory = parts[0]
            Name = parts[1].split('_v')
            Descriptor = Name[0]
            Split2 = Name[1].split('.')
            Version = int(Split2[0])
            Extension = Split2[1]
            if(self.descriptor == Descriptor):
                if CurrentVersion < Version:
                    CurrentVersion = Version
                CurrentVersion = CurrentVersion + 1
                Path = self.dir + "\\" + self.descriptor + '_v0' + str(CurrentVersion) + '.' + self.ext
                pmc.system.saveAs(Path)




