# -*- coding: utf-8 -*-

import unittest
from pprint import pprint
import math

from sap2012.calcs.space_heating_requirement import Space_Heating_Requirement
import sap2012.tables

class TestSpaceHeatingRequirement(unittest.TestCase):
    
    def test_calc1(self):
                
        result=Space_Heating_Requirement(
            utilisation_factor_for_gains_table_9a =[1,1,1,1,1,1,1,1,1,1,1,1],
            total_gains_internal_and_solar=[10,10,10,10,10,10,10,10,10,10,10,10],
            monthly_external_temperature_table_U1=[1,1,1,1,1,1,1,1,1,1,1,1],
            mean_internal_temperature_whole_dwelling=[5,5,5,5,5,5,5,5,5,5,5,5],
            heat_transfer_coefficient=[4,4,4,4,4,4,4,4,4,4,4,4],
            days_in_month=[1,2,3,4,5,6,7,8,9,10,11,12],
            total_floor_area = 100
            )
        
        print(result)
        
        #answer=([25.0], 10, 25.0)        
        #self.assertEqual(result,answer)
        
        
if __name__=='__main__':
    
    o=unittest.main(TestSpaceHeatingRequirement())  