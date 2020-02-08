# -*- coding: utf-8 -*-

import unittest
from pprint import pprint

from sap2012.calcs.heat_losses_and_heat_loss_parameter import heat_losses_and_heat_loss_parameter

class TestHeatLossesAndHeatLossParameter(unittest.TestCase):
    
    def test_calc1(self):
        
        result=heat_losses_and_heat_loss_parameter(
                solid_door_net_area = 4,
                solid_door_u_value = 1,
                semi_glazed_door_net_area = 0,
                semi_glazed_door_u_value = None,
                window_net_area = 20,
                window_u_value = 1.0,
                roof_window_net_area = 0,
                roof_window_u_value = None,
                basement_floor_net_area = 0,
                basement_floor_u_value = None,
                basement_floor_heat_capacity = None,
                ground_floor_net_area = 100,
                ground_floor_u_value = 0.8,
                ground_floor_heat_capacity = 1,
                exposed_floor_net_area = 0,
                exposed_floor_u_value = None,
                exposed_floor_heat_capacity = None,
                basement_wall_gross_area = 0,
                basement_wall_opening = 0,
                basement_wall_u_value = None,
                basement_wall_heat_capacity = None,
                external_wall_gross_area = 0,
                external_wall_opening = 0,
                external_wall_u_value = None,
                external_wall_heat_capacity = None,
                roof_gross_area = 50,
                roof_opening = 0,
                roof_u_value = 1.2,
                roof_heat_capacity = 0.05,
                party_wall_net_area = 0,
                party_wall_u_value = None,
                party_wall_heat_capacity = None,
                party_floor_net_area = 0,
                party_floor_heat_capacity = None,
                party_ceiling_net_area = 0,
                party_ceiling_heat_capacity = None,
                internal_wall_net_area = 50,
                internal_wall_heat_capacity = 0.05,
                internal_floor_net_area = 100,
                internal_floor_heat_capacity = 0.05,
                internal_ceiling_net_area = 100,
                internal_ceiling_heat_capacity = 0.05,
                total_floor_area = 100,
                thermal_bridges_appendix_k = None,
                effective_air_change_rate = [0.5]*12,
                dwelling_volume = 1000
                )
        
        print(result)
        
        #answer=([25.0], 10, 25.0)        
        #self.assertEqual(result,answer)
        
        
if __name__=='__main__':
    
    o=unittest.main(TestHeatLossesAndHeatLossParameter())  
    