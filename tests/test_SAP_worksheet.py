# -*- coding: utf-8 -*-

import unittest

from sap2012 import SAP_worksheet, SAP_appendices
import sap2012

class Test_SAP_worksheet(unittest.TestCase):
    "Test for the SAP_worksheet subpackage"
    
    def test_overall_dwelling_dimensions(self):
        ""
        result=SAP_worksheet.overall_dwelling_dimensions(area=[10],
                                                         average_storey_height=[2.5])
        #print(result)
        self.assertEqual(result,
                         {'volume': [25.0], 
                          'total_floor_area': 10, 
                          'dwelling_volume': 25.0})
    
        
    def test_ventilation_rates(self):
                
        result=SAP_worksheet.ventilation_rates(
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
            monthly_average_wind_speed=sap2012.tables.U2.get_windspeed_by_region('Thames'),
            applicable_case='natural ventilation or whole house positive input ventilation from loft',
            mechanical_ventilation_air_change_rate_through_system=0.5,
            exhaust_air_heat_pump_using_Appendix_N=False,
            mechanical_ventilation_throughput_factor=None,
            efficiency_allowing_for_in_use_factor=None,
            )
        
        self.assertEqual(result,
                         {'number_of_chimneys_total': 1, 
                          'number_of_chimneys_m3_per_hour': 40.0, 
                          'number_of_open_flues_total': 0, 
                          'number_of_open_flues_m3_per_hour': 0.0, 
                          'number_of_intermittant_fans_m3_per_hour': 20.0, 
                          'number_of_passive_vents_m3_per_hour': 10.0, 
                          'number_of_flueless_gas_fires_m3_per_hour': 0.0, 
                          'infiltration_due_to_chimneys_flues_fans_PSVs': 0.07, 
                          'additional_infiltration': 0.1, 
                          'window_infiltration': 0.09, 
                          'infiltration_rate': 0.66, 
                          'infiltration_rate2': 0.66, 
                          'shelter_factor': 1.0, 
                          'infiltration_rate_incorporating_shelter_factor': 0.66, 
                          'wind_factor': [1.05, 1.0, 1.0, 0.925, 0.925, 0.825, 0.85, 0.8, 0.825, 0.875, 0.875, 0.95], 
                          'adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed': [0.6930000000000001, 0.66, 0.66, 0.6105, 0.6105, 0.5445, 0.561, 0.528, 0.5445, 0.5775, 0.5775, 0.627], 
                          'exhaust_air_heat_pump_air_change_rate_through_system': None, 
                          'effective_air_change_rate': [0.7401245000000001, 0.7178, 0.7178, 0.6863551250000001, 0.6863551250000001, 0.6482401250000001, 0.6573605, 0.639392, 0.6482401250000001, 0.6667531250000001, 0.6667531250000001, 0.6965645]
                          }
                         )
    
    
    def test_heat_losses_and_heat_loss_parameter(self):
        
        result=SAP_worksheet.heat_losses_and_heat_loss_parameter(
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
        
        self.assertEqual(result,
                         {'solid_floor_UA': 4, 
                          'semi_glazed_door_UA': 0, 
                          'window_UA': 20.0, 
                          'roof_window_UA': 0, 
                          'basement_floor_UA': 0, 
                          'basement_floor_Ak': 0, 
                          'ground_floor_UA': 80.0, 
                          'ground_floor_Ak': 100, 
                          'exposed_floor_UA': 0, 
                          'exposed_floor_Ak': 0, 
                          'basement_wall_net_area': 0, 
                          'basement_wall_UA': 0, 
                          'basement_wall_Ak': 0, 
                          'external_wall_net_area': 0, 
                          'external_wall_UA': 0, 
                          'external_wall_Ak': 0, 
                          'roof_net_area': 50, 
                          'roof_UA': 60.0, 
                          'roof_Ak': 2.5, 
                          'total_area_of_external_elements': 174, 
                          'party_wall_UA': 0, 
                          'party_wall_Ak': 0, 
                          'party_floor_Ak': 0, 
                          'party_ceiling_Ak': 0, 
                          'internal_wall_Ak': 2.5, 
                          'internal_floor_Ak': 5.0, 
                          'internal_ceiling_Ak': 5.0, 
                          'fabric_heat_loss': 164.0, 
                          'heat_capacity': 115.0, 
                          'thermal_mass_parameter': 1.15, 
                          'thermal_bridges': 26.099999999999998, 
                          'total_fabric_heat_loss': 190.1, 
                          'ventilation_heat_loss_calculated_monthly': [165.0, 165.0, 165.0, 165.0, 165.0, 165.0, 165.0, 165.0, 165.0, 165.0, 165.0, 165.0], 
                          'heat_transfer_coefficient': [355.1, 355.1, 355.1, 355.1, 355.1, 355.1, 355.1, 355.1, 355.1, 355.1, 355.1, 355.1], 
                          'average_heat_transfer_coefficient': 355.09999999999997, 
                          'heat_loss_parameter': [3.551, 3.551, 3.551, 3.551, 3.551, 3.551, 3.551, 3.551, 3.551, 3.551, 3.551, 3.551], 
                          'average_heat_loss_parameter': 0.42612000000000017
                          }
                         )
    
    
    def test_water_heating_requirement(self):
                
        result=SAP_worksheet.water_heating_requirement(
            assumed_occupancy=2.883,
            V_dm_table_1c=[1.1,1.06,1.02,0.98,0.94,0.9,0.9,0.94,0.98,1.02,1.06,1.1],
            days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31],
            T_table_1d=[41.2,41.2,41.2,41.2,41.2,41.2,41.2,41.2,41.2,41.2,41.2,41.2],
            water_storage_loss_manufacturer=0,
            temperature_factor_table_2b=0,
            storage_volume_litres=0,
            hot_water_storage_loss_table_2=0,
            volume_factor_table_2a=0,
            Vs_appendix_G3=0,
            solar_storage_WWHRS_factor=0,
            primary_circuit_loss_table_3=[0,0,0,0,0,0,0,0,0,0,0,0],
            combi_loss_table_3=[0,0,0,0,0,0,0,0,0,0,0,0],
            solar_DHW_input_appendix_G=[0,0,0,0,0,0,0,0,0,0,0,0]    
            )
        
        self.assertEqual(result,
                         {'annual_hot_water_usage_litres_per_day': 108.075, 
                          'hot_water_usage_in_litres_per_day_monthly': [118.88250000000001, 114.55950000000001, 110.2365, 105.9135, 101.59049999999999, 97.2675, 97.2675, 101.59049999999999, 105.9135, 110.2365, 114.55950000000001, 118.88250000000001], 
                          'energy_content_of_water_used': [176.29931311666667, 153.44761329333338, 163.47754489000002, 151.9999943, 150.65577666333334, 139.59183149999998, 144.24489255, 150.65577666333334, 151.9999943, 163.47754489000002, 164.4081571, 176.29931311666667], 
                          'distribution_loss': [26.4448969675, 23.017141994000006, 24.5216317335, 22.799999144999997, 22.5983664995, 20.938774725, 21.6367338825, 22.5983664995, 22.799999144999997, 24.5216317335, 24.661223565, 26.4448969675], 
                          'energy_lost_from_water_storage': 0, 
                          'water_storage_loss_monthly': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                          'total_heat_required_for_water_heating': [176.29931311666667, 153.44761329333338, 163.47754489, 151.99999429999997, 150.65577666333334, 139.59183149999998, 144.24489255, 150.65577666333334, 151.99999429999997, 163.47754489, 164.4081571, 176.29931311666667], 
                          'output_from_water_heater_monthly': [176.29931311666667, 153.44761329333338, 163.47754489, 151.99999429999997, 150.65577666333334, 139.59183149999998, 144.24489255, 150.65577666333334, 151.99999429999997, 163.47754489, 164.4081571, 176.29931311666667], 
                          'heat_gains_from_water_heating_monthly': [58.61952161129167, 51.02133142003335, 54.356283675925, 50.53999810475, 50.09304574055834, 46.414283973749995, 47.961426772875, 50.09304574055834, 50.53999810475, 54.356283675925, 54.66571223575001, 58.61952161129167]
                          }
                         )
    
    
    def test_internal_gains_appendix_L(self):
        ""
        result=SAP_appendices.internal_gains_appendix_L(total_floor_area=100, 
                                                        assumed_occupancy=3, 
                                                        number_of_low_energy_light_bulbs=5, 
                                                        total_number_of_light_bulbs=5, 
                                                        frame_factor=0.8, 
                                                        window_area=20, 
                                                        light_access_factor_table_6d=0.5, 
                                                        light_transmittance_factor_table_6d=0.5, 
                                                        month_number=[1,2,3,4,5,6,7,8,9,10,11,12], 
                                                        days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31], 
                                                        heat_gains_from_water_heating_monthly=[58.61952161129167, 51.02133142003335, 54.356283675925, 50.53999810475, 50.09304574055834, 46.414283973749995, 47.961426772875, 50.09304574055834, 50.53999810475, 54.356283675925, 54.66571223575001, 58.61952161129167]
                                                        )
        self.assertEqual(result,
                         {'G_L': 0.036000000000000004, 
                          'C_1': 0.5, 
                          'C_2': 1.1428112000000001, 
                          'E_B': 878.8352623699882, 
                          'initial_annual_lighting_demand': 502.1713903956806, 
                          'monthly_lighting_demand': [62.131608735352785, 49.84428508122761, 44.87925139769654, 32.880463364922534, 25.397815545264574, 20.750233060903884, 23.16873703048885, 30.11560156876821, 39.11718809820493, 51.32386695542169, 57.97019053604232, 63.85843826957429], 
                          'annual_lighting_demand': 501.43767964386825, 
                          'lighting_gains': [70.98369277560465, 63.04708678429088, 51.273338290379115, 38.817213694700214, 29.01632152348775, 24.496802919122636, 26.46965924182194, 34.40626523313572, 46.18001372704748, 58.636138322726396, 68.43703049393885, 72.95654909830395], 
                          'initial_annual_electrical_appliance_demand': 3057.4580197636624, 
                          'monthly_electrical_appliance_demand': [297.0903625069975, 271.12420848763344, 292.4045014123461, 266.9669022965315, 254.98865565239944, 227.77459834955408, 222.25867098710407, 219.17580266850737, 219.6237407242794, 243.48323445435238, 255.83262371777624, 283.9819485328957], 
                          'annual_electrical_appliance_demand': 3054.7052497903774, 
                          'appliances_gains': [399.3150033696203, 403.4586435827879, 393.01680297358354, 370.78736430073815, 342.72668770483796, 316.35360881882514, 298.7347728321291, 294.5911326189615, 305.0329732281658, 327.26241190101126, 355.32308849691145, 381.6961673829243], 
                          'cooking_gains': [56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56, 56], 
                          'losses': [-120, -120, -120, -120, -120, -120, -120, -120, -120, -120, -120, -120], 
                          'water_heating_gains': [78.78967958506945, 75.92460032743058, 73.05952106979167, 70.19444181215277, 67.32936255451389, 64.464283296875, 64.464283296875, 67.32936255451389, 70.19444181215277, 73.05952106979167, 75.92460032743057, 78.78967958506945], 
                          'metabolic_gains': [180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]
                          }
                         )
        
    
    
    def test_internal_gains(self):
        ""        
        result=SAP_worksheet.internal_gains(
                metabolic_gains=[173,173,173,173,173,173,173,173,173,173,173,173],
                lighting_gains=[195,195,195,195,195,195,195,195,195,195,195,195],
                appliances_gains=[293,293,293,293,293,293,293,293,293,293,293,293],
                cooking_gains=[55,55,55,55,55,55,55,55,55,55,55,55],
                pumps_and_fans_gains=[3,3,3,3,3,3,3,3,3,3,3,3],
                losses=[-115,-115,-115,-115,-115,-115,-115,-115,-115,-115,-115,-115],
                water_heating_gains=[88,85,81,78,75,72,72,75,78,81,85,88]   
                )
                
        self.assertEqual(result,
                         {'total_internal_gains': [692, 689, 685, 682, 679, 676, 676, 679, 682, 685, 689, 692]
                          }
                         )
        
    
    
    def test_solar_gains(self):
                
        result=SAP_worksheet.solar_gains(
            access_factor_table_6d_north=0.77,
            access_factor_table_6d_north_east=0,
            access_factor_table_6d_east=0.77,
            access_factor_table_6d_south_east=0,
            access_factor_table_6d_south=0.77,
            access_factor_table_6d_south_west=0,
            access_factor_table_6d_west=0,
            access_factor_table_6d_north_west=0,
            access_factor_table_6d_roof_windows=0,
            area_north=10,
            area_north_east=0,
            area_east=4.9,
            area_south_east=0,
            area_south=11.9,
            area_south_west=0,
            area_west=0,
            area_north_west=0,
            area_roof_windows=0,
            solar_flux_north=[11.43,20.68,34.89,56.6,74.4,83.2,76.7,61.5,43.7,25.3,13.9,9.7],
            solar_flux_north_east=[0,0,0,0,0,0,0,0,0,0,0,0],
            solar_flux_east=[21.1,39.1,63.9,94.1,112.5,120.4,113.1,98.2,77.4,47.6,25.9,17.7],
            solar_flux_south_east=[0,0,0,0,0,0,0,0,0,0,0,0],
            solar_flux_south=[50.2,77.7,98.3,112.2,114,114.8,110.7,108.7,106.9,86.1,58.6,44.1],
            solar_flux_south_west=[0,0,0,0,0,0,0,0,0,0,0,0],
            solar_flux_west=[0,0,0,0,0,0,0,0,0,0,0,0],
            solar_flux_north_west=[0,0,0,0,0,0,0,0,0,0,0,0],
            solar_flux_roof_windows=[0,0,0,0,0,0,0,0,0,0,0,0],
            g_table_6b_north=0.72,
            g_table_6b_north_east=0,
            g_table_6b_east=0.72,
            g_table_6b_south_east=0,
            g_table_6b_south=0.72,
            g_table_6b_south_west=0,
            g_table_6b_west=0,
            g_table_6b_north_west=0,
            g_table_6b_roof_windows=0,
            FF_table_6b_north=0.72,
            FF_table_6b_north_east=0,
            FF_table_6b_east=0.72,
            FF_table_6b_south_east=0,
            FF_table_6b_south=0.72,
            FF_table_6b_south_west=0,
            FF_table_6b_west=0,
            FF_table_6b_north_west=0,
            FF_table_6b_roof_windows=0,
            total_internal_gains=[692, 689, 685, 682, 679, 676, 676, 679, 682, 685, 689, 692]
            )
        
        self.assertEqual(result,
                         {'gains_north': [41.06241216, 74.29314816, 125.34274368000001, 203.3361792, 267.28289280000007, 298.8969984, 275.5456704, 220.93948799999998, 156.9927744, 90.89055359999999, 49.9359168, 34.8473664], 
                          'gains_north_east': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                          'gains_east': [37.14298156800001, 68.82893740800002, 112.48514323200001, 165.647135808, 198.037224, 211.94383795200002, 199.09342252800002, 172.86449241600002, 136.24961011200006, 83.79174988800001, 45.592569792, 31.157856576000004], 
                          'gains_south_east': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                          'gains_south': [214.60948185599997, 332.174437056, 420.24127622399993, 479.665017216, 487.36017792, 490.7802493439999, 473.25238329599995, 464.702204736, 457.00704403200007, 368.085187008, 250.52023180800003, 188.53143724800003], 
                          'gains_south_west': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                          'gains_west': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                          'gains_north_west': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                          'gains_roof_windows': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 
                          'solar_gains_watts': [292.814875584, 475.296522624, 658.0691631359999, 848.648332224, 952.6802947200001, 1001.6210856959999, 947.8914762239999, 858.506185152, 750.2494285440001, 542.7674904959999, 346.04871840000004, 254.53666022400003], 
                          'total_internal_and_solar_gains': [984.814875584, 1164.2965226239999, 1343.069163136, 1530.6483322240001, 1631.6802947200001, 1677.621085696, 1623.891476224, 1537.506185152, 1432.2494285440002, 1227.767490496, 1035.0487184, 946.536660224]
                          }
                         )
    
    def _test_mean_internal_temperature(self):
                
        result=SAP_worksheet.mean_internal_temperature(
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
        
        
    def test_calculate_worksheet(self):
        ""
        inputs={
            'overall_dwelling_dimensions':{'area':[0,63,63],
                                           "average_storey_height": [0,2.3,2.3]
                                           },
            'ventilation_rates':dict(number_of_chimneys_main_heating=0,
                                     number_of_chimneys_secondary_heating=0,
                                     number_of_chimneys_other=0,
                                     number_of_open_flues_main_heating=0,
                                     number_of_open_flues_secondary_heating=0,
                                     number_of_open_flues_other=0,
                                     number_of_intermittant_fans_total=0,
                                     number_of_passive_vents_total=0,
                                     number_of_flueless_gas_fires_total=0,
                                     air_permeability_value_q50=11.87,
                                     number_of_storeys_in_the_dwelling=2,
                                     structural_infiltration=0,
                                     suspended_wooden_ground_floor_infiltration=0,
                                     no_draft_lobby_infiltration=0,
                                     percentage_of_windows_and_doors_draught_proofed=0,
                                     number_of_sides_on_which_dwelling_is_sheltered=2,
                                     monthly_average_wind_speed=[4.5,4.5,4.4,3.9,3.8,3.4,3.3,3.3,3.5,3.8,3.9,4.1],
                                     applicable_case='natural ventilation or whole house positive input ventilation from loft',
                                     mechanical_ventilation_air_change_rate_through_system=0.5,
                                     exhaust_air_heat_pump_using_Appendix_N=0,
                                     mechanical_ventilation_throughput_factor=0,
                                     efficiency_allowing_for_in_use_factor=0
                                     ),
            'heat_losses_and_heat_loss_parameter':dict(solid_door_net_area=1.5,
                                                       solid_door_u_value=3,
                                                       semi_glazed_door_net_area=10.6,
                                                       semi_glazed_door_u_value=1.4,
                                                       window_net_area=23,
                                                       window_u_value=2,
                                                       roof_window_net_area=0,
                                                       roof_window_u_value=0,
                                                       basement_floor_net_area=0,
                                                       basement_floor_u_value=0,
                                                       basement_floor_heat_capacity=0,
                                                       ground_floor_net_area=63,
                                                       ground_floor_u_value=0.63,
                                                       ground_floor_heat_capacity=20,
                                                       exposed_floor_net_area=0,
                                                       exposed_floor_u_value=0,
                                                       exposed_floor_heat_capacity=0,
                                                       basement_wall_gross_area=0,
                                                       basement_wall_opening=0,
                                                       basement_wall_u_value=0,
                                                       basement_wall_heat_capacity=0,
                                                       external_wall_gross_area=120,
                                                       external_wall_opening=35.1,
                                                       external_wall_u_value=1.5,
                                                       external_wall_heat_capacity=190,
                                                       roof_gross_area=63,
                                                       roof_opening=0,
                                                       roof_u_value=0.14,
                                                       roof_heat_capacity=9,
                                                       party_wall_net_area=47,
                                                       party_wall_u_value=0.5,
                                                       party_wall_heat_capacity=180,
                                                       party_floor_net_area=0,
                                                       party_floor_heat_capacity=0,
                                                       party_ceiling_net_area=39,
                                                       party_ceiling_heat_capacity=100,
                                                       internal_wall_net_area=131,
                                                       internal_wall_heat_capacity=9,
                                                       internal_floor_net_area=63,
                                                       internal_floor_heat_capacity=18,
                                                       internal_ceiling_net_area=63,
                                                       internal_ceiling_heat_capacity=9,
                                                       thermal_bridges_appendix_k=36.9
                                                       ),
            'water_heating_requirements':dict(assumed_occupancy=2.883,
                                              V_dm_table_1c=[1.1,1.06,1.02,0.98,0.94,0.9,0.9,0.94,0.98,1.02,1.06,1.1],
                                              days_in_month=[31,28,31,30,31,30,31,31,30,31,30,31],
                                              T_table_1d=[41.2,41.2,41.2,41.2,41.2,41.2,41.2,41.2,41.2,41.2,41.2,41.2],
                                              water_storage_loss_manufacturer=0,
                                              temperature_factor_table_2b=0,
                                              storage_volume_litres=0,
                                              hot_water_storage_loss_table_2=0,
                                              volume_factor_table_2a=0,
                                              Vs_appendix_G3=0,
                                              solar_storage_WWHRS_factor=0,
                                              primary_circuit_loss_table_3=[0,0,0,0,0,0,0,0,0,0,0,0],
                                              combi_loss_table_3=[0,0,0,0,0,0,0,0,0,0,0,0],
                                              solar_DHW_input_appendix_G=[0,0,0,0,0,0,0,0,0,0,0,0]
                                              ),
            'internal_gains_appendix_L':dict(number_of_low_energy_light_bulbs=0, 
                                             total_number_of_light_bulbs=10, 
                                             frame_factor=0.7,
                                             window_area=23, 
                                             light_access_factor_table_6d=0, 
                                             light_transmittance_factor_table_6d=0, 
                                             month_number=[1,2,3,4,5,6,7,8,9,10,11,12]
                                             ),
            'internal_gains':dict(pumps_and_fans_gains=[3,3,3,3,3,3,3,3,3,3,3,3]
                                  ),
            
            }
        
        
        result=SAP_worksheet.calculate_worksheet(inputs)
        print(result)
        
        
        
if __name__=='__main__':
    
    o=unittest.main(Test_SAP_worksheet())  
    
    