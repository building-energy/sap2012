# -*- coding: utf-8 -*-

import unittest
from pprint import pprint
import math

from sap2012.calcs.space_heating_requirement import Space_Heating_Requirement
import sap2012.tables

class TestSpaceHeatingRequirement(unittest.TestCase):
    
    def test_calc1(self):
                
        result=Space_Heating_Requirement(
            utilisation_factor_for_gains_table_9a =[0.98,0.97,0.94,0.84,0.58,-0.55,-3.06,-2.15,0.36,0.88,0.97,0.99],
            total_gains_internal_and_solar=[968,1130,1260,1290,948,-918,-4963,-3309,516,1082,1001,932],
            monthly_external_temperature_table_U1=[4.3,4.8,6.6,9,11.8,14.8,16.6,16.5,14,10.5,7.1,4.2],
            mean_internal_temperature_whole_dwelling=[17.7,17.9,18.5,19.2,19.7,19.7,18.5,19.1,20.0,19.4,18.5,17.7],
            heat_transfer_coefficient=[363,363,361,355,353,348,347,347,349,354,355,358],
            days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31],
            total_floor_area = 126
            )
        
        print(result)
        
        #answer=([25.0], 10, 25.0)        
        #self.assertEqual(result,answer)
        
        
if __name__=='__main__':
    
    o=unittest.main(TestSpaceHeatingRequirement())  