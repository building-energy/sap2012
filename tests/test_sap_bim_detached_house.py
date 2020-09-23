# -*- coding: utf-8 -*-

import unittest
from pprint import pprint

from sap2012 import SapBIM, SapSpace

from crossproduct import Point3D, Vector3D, PlaneVolume3D, Polygon3D, Polygons

# ground floor

vz1=Vector3D(0,0,2.5)

v1=Vector3D(4.3,0,0)
v2=Vector3D(0,4.43,0)
v3=Vector3D(0,3.83,0)
v4=Vector3D(-3.43,0,0)
v5=Vector3D(-2.93,0,0)
v6=Vector3D(0,-2.63,0)
v7=Vector3D(0,-4.43,0)
v8=Vector3D(2.06,0,0)

P0=Point3D(2.06,0,0)
P1=P0+v1
P2=P1+v2
P3=P2-v1
P4=P2+v3
P5=P4+v4
P6=P5-v3
P7=P5+v5
P8=P7+v6
P9=P8+v7
P10=P9+v8
P11=P8-v5

# first floor

vz2=Vector3D(0,0,2.35)

v101=Vector3D(4.3,0,0)
v102=Vector3D(0,4.43,0)
v103=Vector3D(0,3.83,0)
v104=Vector3D(-3.43,0,0)
v105=Vector3D(0,-2.65,0)
v106=Vector3D(-2.28,0,0)
v107=Vector3D(-0.83,0,0)
v108=Vector3D(-2.1,0,0)
v109=Vector3D(0,-1.63,0)
v110=Vector3D(0,-3.06,0)
v111=Vector3D(0,-2.37,0)
v112=Vector3D(2.93,0,0)
v113=Vector3D(0,3.23,0)
v114=Vector3D(1,0,0)

P101=P0+vz1
P102=P101+v101
P103=P102+v102
P112=P103+v106
P108=P103+v103
P109=P108+v104
P110=P109+v105
P111=P108+v105+v106
P113=P109+v107
P114=P113+v109
P115=P113+v108
P116=P115+v109
P117=P116+v110
P118=P117+v114
P120=P117+v111
P107=P101+v102+v103+v109+v110+v111
P106=P120+v112
P105=P106+v113
P119=P120+v114+v113
P121=P109+v109



class TestSapBIM_DetachedHouse(unittest.TestCase):
        
    def test1(self):
        ""
    
        b=SapBIM()
        
        lr=b.add_space(id='living_room',
                        base_polygon=Polygon3D(P0,P1,P2,P3),
                        extrud=vz1)
        
        dr=b.add_space(id='dining_room',
                        base_polygon=Polygon3D(P2,P4,P5,P6),
                        extrud=vz1)
        
        kt=b.add_space(id='kitchen',
                        base_polygon=Polygon3D(P5,P7,P8,P11),
                        extrud=vz1)
        
        hl=b.add_space(id='hall',
                       base_polygon=Polygon3D(P8,P9,P10,P3,P6,P11),
                       extrud=vz1)
        
        br1=b.add_space(id='bedroom1',
                        base_polygon=Polygon3D(P101,P102,P103,P105,P106,P107),
                        extrud=vz2)
        
        br2=b.add_space(id='bedroom2',
                        base_polygon=Polygon3D(P103,P108,P109,P110,P111,P112),
                        extrud=vz2)
        
        wc=b.add_space(id='wc',
                        base_polygon=Polygon3D(P109,P113,P114,P121),
                        extrud=vz2)
        
        ba=b.add_space(id='bathroom',
                        base_polygon=Polygon3D(P113,P115,P116,P114),
                        extrud=vz2)
        
        la=b.add_space(id='landing',
                        base_polygon=Polygon3D(P116,P117,P118,P119,P112,P111,P110,P121), 
                        extrud=vz2)
        
        br3=b.add_space(id='bedroom3',
                        base_polygon=Polygon3D(P120,P106,P105,P119,P118,P117), 
                        extrud=vz2)
        
        b.plot()
    
        l0=b.add_level(height=0)
        l1=b.add_level(height=2.5)
        
        print(l0._spaces)
        print(l1._spaces)
        print(b._spaces)
    
        print(l1._check_space_belongs_to(br1))
        
        br1.plot(normal=True)
        
    
if __name__=='__main__':
    
    o=unittest.main(TestSapBIM_DetachedHouse())  