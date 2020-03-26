# -*- coding: utf-8 -*-

import unittest
from pprint import pprint
import math

from sap2012.calcs.fuel_cost import Fuel_Costs
import sap2012.tables

class TestFuelCosts(unittest.TestCase):
    
    def test_calc1(self):
                
        result=Fuel_Costs(
            space_heating_fuel_main_system_1=19203,
            space_heating_fuel_main_system_2=0,
            space_heating_fuel_secondary_system=0,
            space_heating_fuel_price_main_system_1=3.48,
            space_heating_fuel_price_main_system_2=0,
            space_heating_fuel_price_secondary=0,
            water_heating_high_rate_fraction_table_13=0,
            water_heating_low_rate_fraction_table_13=1,
            high_rate_fuel_price=0,
            low_rate_fuel_price=3.48,
            water_fuel_used=2358,
            water_heating_fuel_price_other=0,
            space_cooling_fuel_used=0,
            space_cooling_fuel_price=0,
            electricity_for_pumps_fans_electric_keep_hot=0,
            fuel_price_for_pumps_fans_electric_keep_hot=0,
            electricity_for_lighting=2008,
            fuel_price_for_lighting=13.19,
            additional_standing_charges_table_12=0,
            energy_saving_generation_technologies=[0],
            energy_saving_generation_technologies_fuel_price=[0],
            appendix_Q_energy_used=[0],
            appendix_Q_energy_used_fuel_price=[0],
            appendix_Q_energy_saved=[0],
            appendix_Q_energy_saved_fuel_price=[0]
            )
        
        print(result)
        
        #answer=([25.0], 10, 25.0)        
        #self.assertEqual(result,answer)
        
        
if __name__=='__main__':
    
    o=unittest.main(TestFuelCosts())  
    

