# -*- coding: utf-8 -*-
import unittest
from pprint import pprint
import math

from sap2012.calcs.CO2_emissions import CO2_emissions
import sap2012.tables

class TestCO2emissions(unittest.TestCase):
    
    def test_calc1(self):
                
        result=CO2_emissions(
                space_heating_fuel_main_system_1=19203,
                space_heating_fuel_main_system_2=0,
                space_heating_fuel_secondary_system=0,
                space_heating_fuel_emission_factor_main_system_1=0.216,
                space_heating_fuel_emission_factor_main_system_2=0,
                space_heating_fuel_emission_factor_secondary=0,
                water_fuel_used=2358,
                water_heating_fuel_emission_factor=0.216,
                space_cooling_fuel_used=0,
                space_cooling_fuel_emission_factor=0,
                electricity_for_pumps_fans_electric_keep_hot=0,
                fuel_emission_factor_for_pumps_fans_electric_keep_hot=0,
                electricity_for_lighting=2008,
                fuel_emission_factor_for_lighting=0.519,
                energy_saving_generation_technologies=[0],
                energy_saving_generation_technologies_fuel_emission_factor=[0],
                appendix_Q_energy_used=[0],
                appendix_Q_energy_used_fuel_emission_factor=[0],
                appendix_Q_energy_saved=[0],
                appendix_Q_energy_saved_fuel_emission_factor=[0],
                total_floor_area=126   
                                )
        
        print(result)
        
        #answer=([25.0], 10, 25.0)        
        #self.assertEqual(result,answer)
        
        
if __name__=='__main__':
    
    o=unittest.main(TestCO2emissions()) 

