# -*- coding: utf-8 -*-,

import unittest
from pprint import pprint
import math

from sap2012.calcs.energy_requirements import Energy_Requirements
import sap2012.tables

class TestEnergyRequirements(unittest.TestCase):
    
    def test_calc1(self):
                
        result=Energy_Requirements(
            fraction_of_space_heat_secondary_system=0,
            fraction_of_space_heat_from_main_system_2=0,
            efficiency_of_main_space_heating_system_1=90,
            efficiency_of_main_space_heating_system_2=0,
            efficiency_of_secondary_space_heating_system=0,
            cooling_system_energy_efficiency_ratio_table_10c=0,
            space_heating_requirement_monthly=[2905,2448,2260,1669,1378,1900,4188,3136,1143,1524,2188,2909],
            output_from_water_heater_monthly=[176,153,164,152,151,140,144,151,152,164,164,176],
            efficiency_of_water_heater_table_4a=80,
            space_cooling_requirement_monthly=[0,0,0,0,0,0,0,0,0,0,0,0],
            electricity_demand_mechanical_ventilation_fans_table_4f=0,
            electricity_demand_warm_air_heating_systems_fans_table_4f=0,
            electricity_demand_central_heating_pump_or_water_pump_table_4f=0,
            electricity_demand_oil_boiler_pump_table_4f=0,
            electricity_demand_boiler_flue_fan_table_4f=0,
            electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f=0,
            electricity_demand_pump_for_solar_water_heating_table_4f=0,
            electricity_demand_pump_for_storage_WWHRS_Table_G3=0,
            electricity_for_lighting=2008,
            electricity_generated_by_PV_Appendix_M=0,
            electricity_generated_by_wind_turbine_appendix_M=0,
            electricity_used_or_generated_by_micro_CHP_appendix_N=0,
            electricity_generated_by_hydro_electric_generator_appendix_M=0,
            appendix_Q_energy_saved=[0],
            appendix_Q_energy_used=[0]  
            )
        
        print(result)
        
        #answer=([25.0], 10, 25.0)        
        #self.assertEqual(result,answer)
        
        
if __name__=='__main__':
    
    o=unittest.main(TestEnergyRequirements())  
    
