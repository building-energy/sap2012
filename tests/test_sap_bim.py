# -*- coding: utf-8 -*-

import unittest
from pprint import pprint

from sap2012 import SapBIM, SapSpace

from crossproduct import Point3D, Vector3D, PlaneVolume3D, Polygon3D, Polygons


class TestSapBIM(unittest.TestCase):
    
    def test___init__(self):
        ""
        b=SapBIM(id='my_model')
        self.assertIsInstance(b,SapBIM)
        self.assertEqual(str(b),
                         "SapBIM(id='my_model')")
        self.assertEqual(b.id,
                         "my_model")
        
        
    def test_add_space(self):
        ""
    
        b=SapBIM(id='my_model')
        s=b.add_space(id='my_space',
                      base_polygon=((0,0,3),(10,0,3),(10,10,3),(0,10,3)),
                      extrud = (0,0,3),
                      )
        self.assertIsInstance(s,SapSpace)
        self.assertEqual(str(s),
                         "SapSpace(id='my_space')")
        self.assertEqual(s.id,
                         "my_space")
    
    
    
if __name__=='__main__':
    
    o=unittest.main(TestSapBIM())  