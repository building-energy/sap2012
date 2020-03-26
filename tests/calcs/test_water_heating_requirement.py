# -*- coding: utf-8 -*-
import unittest
from pprint import pprint
import math

from sap2012.calcs.Water_Heating_Requirement import Water_Heating_Energy_Requirement
import sap2012.tables

class TestWaterHeatingRequirement(unittest.TestCase):
    
    def test_calc1(self):
                
        result=Water_Heating_Energy_Requirement(
            assumed_occupancy=2.883,
            V_dm_table_1c=[1.1,1.06,1.02,0.98,0.94,0.9,0.9,0.94,0.98,1.02,1.06,1.1],
            days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31],
            T_table_1d=41.2,
            water_storage_loss_manufacturer=None,
            temperature_factor_table_2b=0,
            storage_volume_litres=0,
            hot_water_storage_loss_table_2=0,
            volume_factor_table_2a=0,
            Vs_appendix_G3=0,
            solar_storage_WWHRS_factor=None,
            primary_circuit_loss_table_3=0,
            combi_loss_table_3=0,
            solar_DHW_input_appendix_G=0    
            )
        
        print(result)
        
        #answer=([25.0], 10, 25.0)        
        #self.assertEqual(result,answer)
        
        
if __name__=='__main__':
    
    o=unittest.main(TestWaterHeatingRequirement())  
    

