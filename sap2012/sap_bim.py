# -*- coding: utf-8 -*-

from pybim import sBIM, Space

class SapBIM(sBIM):
    ""
    
    def __repr__(self):
        ""
        return "SapBIM(id='%s')" % (self._id)
    
    


    def add_space(self,
                  id=None,
                  base_polygon=None,
                  extrud=None):
        ""
        s=sBIM.add_space(self,
                         id=id,
                         base_polygon=base_polygon,
                         extrud=extrud,
                         _kls=SapSpace)
        return s
        
    
class SapSpace(Space):
    ""
    
    def __repr__(self):
        ""
        return "SapSpace(id='%s')" % (self._id)
    