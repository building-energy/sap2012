# -*- coding: utf-8 -*-

import unittest
from pprint import pprint
import math

from sap2012.calcs.SAP_rating import SAP_Rating
import sap2012.tables

class TestSAPRating(unittest.TestCase):
    
    def test_calc1(self):
                
        result=SAP_Rating(
            energy_cost_deflator=0.42,
            total_fuel_cost=1015,
            total_floor_area=126   
            )
        
        print(result)
        
        #answer=([25.0], 10, 25.0)        
        #self.assertEqual(result,answer)
        
        
if __name__=='__main__':
    
    o=unittest.main(TestSAPRating()) 

