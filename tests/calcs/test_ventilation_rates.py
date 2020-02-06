# -*- coding: utf-8 -*-

import unittest
from pprint import pprint

from sap2012.calcs.ventilation_rates import ventilation_rates
import sap2012.tables

class TestVentilationRates(unittest.TestCase):
    
    def test_calc1(self):
                
        result=ventilation_rates(
            number_of_chimneys_main_heating=1,
            number_of_chimneys_secondary_heating=0,
            number_of_chimneys_other=0,
            number_of_open_flues_main_heating=0,
            number_of_open_flues_secondary_heating=0,
            number_of_open_flues_other=0,
            number_of_intermittant_fans_total=2,
            number_of_passive_vents_total=1,
            number_of_flueless_gas_fires_total=0,
            dwelling_volume=1000,
            air_permeability_value_q50=None,
            number_of_storeys_in_the_dwelling=2,
            structural_infiltration=0.25,
            suspended_wooden_ground_floor_infiltration=0.1,
            no_draft_lobby_infiltration=0.05,
            percentage_of_windows_and_doors_draught_proofed=80,
            number_of_sides_on_which_dwelling_is_sheltered=0,
            #monthly_average_wind_speed=[4]*12,
            monthly_average_wind_speed=sap2012.tables.U2.get_windspeed_by_region('Thames'),
            applicable_case='natural ventilation or whole house positive input ventilation from loft',
            mechanical_ventilation_air_change_rate_through_system=0.5,
            exhaust_air_heat_pump_using_Appendix_N=False,
            mechanical_ventilation_throughput_factor=None,
            efficiency_allowing_for_in_use_factor=None,
            )
        
        print(result)
        
        #answer=([25.0], 10, 25.0)        
        #self.assertEqual(result,answer)
        
        
if __name__=='__main__':
    
    o=unittest.main(TestVentilationRates())  
    