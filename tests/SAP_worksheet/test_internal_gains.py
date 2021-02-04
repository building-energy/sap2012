# -*- coding: utf-8 -*-
import unittest
from pprint import pprint
import math

from sap2012.calcs.internal_gains import Internal_Gains
import sap2012.tables

class TestInternalGains(unittest.TestCase):
    
    def test_calc1(self):
                
        result=Internal_Gains(
                metabolic_gains=[173,173,173,173,173,173,173,173,173,173,173,173],
                lighting_gains=[195,195,195,195,195,195,195,195,195,195,195,195],
                appliances_gains=[293,293,293,293,293,293,293,293,293,293,293,293],
                cooking_gains=[55,55,55,55,55,55,55,55,55,55,55,55],
                pumps_and_fans_gains=[3,3,3,3,3,3,3,3,3,3,3,3],
                losses=[-115,-115,-115,-115,-115,-115,-115,-115,-115,-115,-115,-115],
                water_heating_gains=[88,85,81,78,75,72,72,75,78,81,85,88]   
                                                )
        
        print(result)
        
        #answer=([25.0], 10, 25.0)        
        #self.assertEqual(result,answer)
        
        
if __name__=='__main__':
    
    o=unittest.main(TestInternalGains())  
    


