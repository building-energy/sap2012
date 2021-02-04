# -*- coding: utf-8 -*-
import unittest
from pprint import pprint
import math

from sap2012.calcs.mean_internal_temperature import Mean_Internal_Temperature
import sap2012.tables

class TestMeanInternalTemperature(unittest.TestCase):
    
    def test_calc1(self):
                
        result=Mean_Internal_Temperature(
            temperature_during_heating_periods_living_room =21,
            utilisation_factor_for_gains_living_room_table_9a=[0.99,0.98,0.97,0.92,0.77,0.11,-1.45,-0.9,0.64,0.93,0.98,0.99],
            mean_internal_temperature_living_room_T1_Table_9c=[17.8,18,18.5,19.2,19.7,19.8,18.6,19.2,20,19.4,18.50,17.8],
            temperature_during_heating_periods_rest_of_dwelling=21,
            utilisation_factor_for_gains_rest_of_dwelling_table_9a=[0.99,0.98,0.97,0.92,0.77,0.11,-1.45,-0.9,0.64,0.93,0.98,0.99],
            mean_internal_temperature_rest_of_dwelling_T2_table_9c=[17.7,17.9,18.5,19.2,19.7,19.7,18.5,19.1,20,19.3,18.5,17.7],
            living_room_area=30,
            total_floor_area=126,
            temperature_adjustment_table_4e=0
            )
        
        print(result)
        
        #answer=([25.0], 10, 25.0)        
        #self.assertEqual(result,answer)
        
        
if __name__=='__main__':
    
    o=unittest.main(TestMeanInternalTemperature())  

