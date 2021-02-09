# -*- coding: utf-8 -*-

from .overall_dwelling_dimensions import overall_dwelling_dimensions
from .ventilation_rates import ventilation_rates
from .heat_losses_and_heat_loss_parameter import heat_losses_and_heat_loss_parameter
from .water_heating_requirement import water_heating_requirement
from ..SAP_appendices import internal_gains_appendix_L
from .internal_gains import internal_gains
from ..SAP_appendices import solar_gains_appendix_U3
from .solar_gains import solar_gains
from ..SAP_tables import utilisation_factor_for_heating_table_9a
from ..SAP_tables import temperature_reduction_when_heating_is_off_table_9b
from ..SAP_tables import heating_requirement_table_9c
from .mean_internal_temperature import mean_internal_temperature
from ..SAP_tables import utilisation_factor_for_heating_whole_house_table_9a
from .space_heating_requirement import space_heating_requirement
from .energy_requirements import energy_requirements
from .fuel_costs import fuel_costs
from .SAP_rating import SAP_rating
from .CO2_emissions import CO2_emissions


def calculate_worksheet(inputs):
    """This function runs the complete set of calculations for the SAP2012 worksheet.
    
    :param inputs: A dictionary of the SAP model inputs.
    :type inputs: dict
    
    :returns: A dictionary with the results of all the calculation sections.
    :rtype: dict
    
    .. rubric:: SAP Calculation Sections
    
    The SAP calculation sections are run as given in the order below:
        
    - `overall_dwelling_dimensions` (Section 1)
    - `ventilation_rates` (Section 2)
    - `heat_losses_and_heat_loss_parameter` (Section 3)
    - `water_heating_requirement` (Section 4)
    - `internal_gains_appendix_L` 
    - `internal_gains` (Section 5)
    - `solar_gains_appendix_U3`
    - `solar_gains` (Section 6)
    - `utilisation_factor_for_heating_table_9a`
    - `temperature_reduction_when_heating_is_off_table_9b`
    - `heating_requirement_table_9c`
    - `mean_internal_temperature` (Section 7)
    - `utilisation_factor_for_heating_whole_house_table_9a`
    - `space_heating_requirement` (Section 8)
    - `energy_requirements` (Section 9)
    - `fuel_costs` (Section 10)
    - `SAP_rating` (Section 11)
    - `CO2_emissions` (Section 12)
    
    
    .. rubric:: Inputs
    
    The 'inputs' dictionary holds all the inputs to run a complete SAP calculation.
    The dictionary is a collection of 18 individual dictionaries which contain
    the model inputs to individual calculation sections as listed above.
    
    To see definitions of the model inputs, please see the documentation for the
    individual calculation sections.
    
    For the `calculate_worksheet` function, not all inputs need to be provided
    for all calculation sections. This is because some inputs for later sections
    are calculated as outputs by earlier sections.
    
    An example of a valid 'inputs' dictionary is:
        
    .. code-block:: python
    
       {'overall_dwelling_dimensions':
            {'area':[0,63,63],
             'average_storey_height': [0,2.5,2.75]
             }
        'ventilation_rates':
            {'number_of_chimneys_main_heating': 0, 
             'number_of_chimneys_secondary_heating': 0, 
             'number_of_chimneys_other': 0, 
             'number_of_open_flues_main_heating': 0, 
             'number_of_open_flues_secondary_heating': 0, 
             'number_of_open_flues_other': 0, 
             'number_of_intermittant_fans_total': 0, 
             'number_of_passive_vents_total': 0, 
             'number_of_flueless_gas_fires_total': 0, 
             'air_permeability_value_q50': 11.78, 
             'number_of_storeys_in_the_dwelling': 2, 
             'structural_infiltration': 0, 
             'suspended_wooden_ground_floor_infiltration': 0, 
             'no_draft_lobby_infiltration': 0, 
             'percentage_of_windows_and_doors_draught_proofed': 0, 
             'number_of_sides_on_which_dwelling_is_sheltered': 2, 
             'monthly_average_wind_speed': [4.5, 4.5, 4.4, 3.9, 3.8, 3.4, 3.3, 3.3, 3.5, 3.8, 3.9, 4.1], 
             'applicable_case': 'natural ventilation or whole house positive input ventilation from loft', 
             'mechanical_ventilation_air_change_rate_through_system': 0.5, 
             'exhaust_air_heat_pump_using_Appendix_N': False, 
             'mechanical_ventilation_throughput_factor': None, 
             'efficiency_allowing_for_in_use_factor': None
             }
         'heat_losses_and_heat_loss_parameter':
             {'solid_door_net_area': 1.5, 
              'solid_door_u_value': 3, 
              'semi_glazed_door_net_area': 10.6, 
              'semi_glazed_door_u_value': 1.4, 
              'window_net_area': 23, 
              'window_u_value': 2, 
              'roof_window_net_area': 0, 
              'roof_window_u_value': None, 
              'basement_floor_net_area': 0, 
              'basement_floor_u_value': None, 
              'basement_floor_heat_capacity': None, 
              'ground_floor_net_area': 63, 
              'ground_floor_u_value': 0.63, 
              'ground_floor_heat_capacity': 20, 
              'exposed_floor_net_area': 0, 
              'exposed_floor_u_value': None, 
              'exposed_floor_heat_capacity': None, 
              'basement_wall_gross_area': 0, 
              'basement_wall_opening': 0, 
              'basement_wall_u_value': None, 
              'basement_wall_heat_capacity': None, 
              'external_wall_gross_area': 120, 
              'external_wall_opening': 35.1, 
              'external_wall_u_value': 1.5, 
              'external_wall_heat_capacity': 190, 
              'roof_gross_area': 63, 
              'roof_opening': 0, 
              'roof_u_value': 0.14, 
              'roof_heat_capacity': 9, 
              'party_wall_net_area': 47, 
              'party_wall_u_value': 0.5, 
              'party_wall_heat_capacity': 180, 
              'party_floor_net_area': 0, 
              'party_floor_heat_capacity': None, 
              'party_ceiling_net_area': 39, 
              'party_ceiling_heat_capacity': 100, 
              'internal_wall_net_area': 131, 
              'internal_wall_heat_capacity': 9, 
              'internal_floor_net_area': 63, 
              'internal_floor_heat_capacity': 18, 
              'internal_ceiling_net_area': 63, 
              'internal_ceiling_heat_capacity': 9, 
              'thermal_bridges_appendix_k': 36.9
              },
        'water_heating_requirement':
            {'assumed_occupancy': 2.88, 
             'V_dm_table_1c': [1.1, 1.06, 1.02, 0.98, 0.94, 0.9, 0.9, 0.94, 0.98, 1.02, 1.06, 1.1], 
             'days_in_month': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], 
             'T_table_1d': [41.2, 41.4, 40.1, 37.6, 36.4, 33.9, 30.4, 33.4, 33.5, 36.3, 39.4, 39.9], 
             'water_storage_loss_manufacturer': 0, 
             'temperature_factor_table_2b': 0, 
             'storage_volume_litres': 0, 
             'hot_water_storage_loss_table_2': 0, 
             'volume_factor_table_2a': 0, 
             'Vs_appendix_G3': 0, 
             'solar_storage_WWHRS_factor': 0, 
             'primary_circuit_loss_table_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             'combi_loss_table_3': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
             'solar_DHW_input_appendix_G': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
             },
         'internal_gains_appendix_L':
             {'number_of_low_energy_light_bulbs': 0, 
              'total_number_of_light_bulbs': 10, 
              'frame_factor': 0.7, 
              'window_area': 23, 
              'light_access_factor_table_6d': 0, 
              'light_transmittance_factor_table_6d': 0, 
              'month_number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
              },
         'internal_gains':
             {'pumps_and_fans_gains':[3,3,3,3,3,3,3,3,3,3,3,3]
              }
         'solar_gains_appendix_U3':
             {'solar_radiation_horizontal_plane_monthly_table_U3': [28, 55, 97, 153, 191, 208, 194, 208, 163, 69, 35, 23], 
              'solar_declination_monthly_table_U3': [-20.7, -12.8, -1.8, 9.8, 18.8, 23.1, 21.2, 13.7, 2.9, -8.7, -18.4, -23], 
              'location_latitude_table_U4': 53.4, 
              'p_tilt': 90
              },
         'solar_gains':
             {'access_factor_table_6d_north': 0.77, 
              'access_factor_table_6d_north_east': 0, 
              'access_factor_table_6d_east': 0.77, 
              'access_factor_table_6d_south_east': 0, 
              'access_factor_table_6d_south': 0.77, 
              'access_factor_table_6d_south_west': 0, 
              'access_factor_table_6d_west': 0, 
              'access_factor_table_6d_north_west': 0, 
              'access_factor_table_6d_roof_windows': 0, 
              'area_north': 10, 
              'area_north_east': 0, 
              'area_east': 4.9, 
              'area_south_east': 0, 
              'area_south': 11.9, 
              'area_south_west': 0, 
              'area_west': 0, 
              'area_north_west': 0, 
              'area_roof_windows': 0, 
              'solar_flux_roof_windows': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              'g_table_6b_north': 0.72, 
              'g_table_6b_north_east': 0, 
              'g_table_6b_east': 0.72, 
              'g_table_6b_south_east': 0, 
              'g_table_6b_south': 0.72, 
              'g_table_6b_south_west': 0, 
              'g_table_6b_west': 0, 
              'g_table_6b_north_west': 0, 
              'g_table_6b_roof_windows': 0, 
              'FF_table_6b_north': 0.72, 
              'FF_table_6b_north_east': 0, 
              'FF_table_6b_east': 0.72, 
              'FF_table_6b_south_east': 0, 
              'FF_table_6b_south': 0.72, 
              'FF_table_6b_south_west': 0, 
              'FF_table_6b_west': 0, 
              'FF_table_6b_north_west': 0, 
              'FF_table_6b_roof_windows': 0
              },
         'utilisation_factor_for_heating_table_9a':
             {'temperature_during_heating_living_room': 20, 
              'heating_controls': 2, 
              'monthly_external_temperature_table_U1': [4.3, 4.8, 6.6, 9, 11.8, 14.8, 16.6, 16.5, 14, 10.5, 7.1, 4.2]
              },
         'temperature_reduction_when_heating_is_off_table_9b':
             {'hours_heating_is_off_1_weekday_living_room': 8, 
              'hours_heating_is_off_2_weekday_living_room': 8, 
              'hours_heating_is_off_1_weekend_living_room': 8, 
              'hours_heating_is_off_2_weekend_living_room': 8, 
              'hours_heating_is_off_1_weekday_rest_of_dwelling': 8, 
              'hours_heating_is_off_2_weekday_rest_of_dwelling': 8, 
              'hours_heating_is_off_1_weekend_rest_of_dwelling': 8, 
              'hours_heating_is_off_2_weekend_rest_of_dwelling': 8, 
              'responsiveness_of_heating_system': 1
              },
         'heating_requirement_table_9c':
             {'temperature_adjustment_table_4e': 0
              },
         'mean_internal_temperature':
             {'living_room_area': 16
              },
         'energy_requirements':
             {'fraction_of_space_heat_secondary_system': 0, 
              'fraction_of_space_heat_from_main_system_2': 0, 
              'efficiency_of_main_space_heating_system_1': 88.8, 
              'efficiency_of_main_space_heating_system_2': 0, 
              'efficiency_of_secondary_space_heating_system': 0, 
              'cooling_system_energy_efficiency_ratio_table_10c': 0, 
              'water_heater_type': 'gas/oil boiler main system', 
              'efficiency_of_water_heater': 80, 
              'efficiency_of_water_heater_adjustment_table_4c': 0, 
              'space_cooling_requirement_monthly': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
              'electricity_demand_mechanical_ventilation_fans_table_4f': 0, 
              'electricity_demand_warm_air_heating_systems_fans_table_4f': 0, 
              'electricity_demand_central_heating_pump_or_water_pump_table_4f': 0, 
              'electricity_demand_oil_boiler_pump_table_4f': 0, 
              'electricity_demand_boiler_flue_fan_table_4f': 0, 
              'electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f': 0, 
              'electricity_demand_pump_for_solar_water_heating_table_4f': 0, 
              'electricity_demand_pump_for_storage_WWHRS_Table_G3': 0, 
              'electricity_generated_by_PV_appendix_M': [0], 
              'electricity_generated_by_wind_turbine_appendix_M': [0], 
              'electricity_used_or_generated_by_micro_CHP_appendix_N': [0], 
              'electricity_generated_by_hydro_electric_generator_appendix_M': [0], 
              'appendix_Q_energy_saved': [0], 'appendix_Q_energy_used': [0]
              },
         'fuel_costs':
             {'space_heating_fuel_price_main_system_1': 3.48, 
              'space_heating_fuel_price_main_system_2': 0, 
              'space_heating_fuel_price_secondary': 0, 
              'water_heating_high_rate_fraction_table_13': 0, 
              'water_heating_low_rate_fraction_table_13': 1, 
              'high_rate_fuel_price': 0, 
              'low_rate_fuel_price': 3.48, 
              'water_heating_fuel_price_other': 0, 
              'space_cooling_fuel_used': 0, 
              'space_cooling_fuel_price': 0, 
              'electricity_for_pumps_fans_electric_keep_hot': 0, 
              'fuel_price_for_pumps_fans_electric_keep_hot': 0, 
              'fuel_price_for_lighting': 13.19, 
              'additional_standing_charges_table_12': 0, 
              'energy_saving_generation_technologies': [0], 
              'energy_saving_generation_technologies_fuel_price': [0], 
              'appendix_Q_energy_used_fuel_price': [0], 
              'appendix_Q_energy_saved_fuel_price': [0]
              },
        'SAP_rating':
            {'energy_cost_deflator': 0.42
             },
        'CO2_emissions':
            {'space_heating_fuel_emission_factor_main_system_1': 0.216, 
             'space_heating_fuel_emission_factor_main_system_2': 0, 
             'space_heating_fuel_emission_factor_secondary': 0, 
             'water_heating_fuel_emission_factor': 0.216, 
             'space_cooling_fuel_emission_factor': 0, 
             'fuel_emission_factor_for_pumps_fans_electric_keep_hot': 0, 
             'fuel_emission_factor_for_lighting': 0.519, 
             'energy_saving_generation_technologies_fuel_emission_factor': [0], 
             'appendix_Q_energy_used_fuel_emission_factor': [0], 
             'appendix_Q_energy_saved_fuel_emission_factor': [0]
             }
        }
    
    .. rubric:: Outputs
    
    The `calculate_worksheet` function returns a dictionary containing
    the outputs of all SAP calculation sections.
    
    The output dictionary is a collection of dictionaries, where each
    dictiionary holds the outputs of an individual calculation section.
    
    An example of an output dictionary as returned by the `calculate_worksheet`
    function is:
        
    .. code-block:: python
    
       {
            "overall_dwelling_dimensions": {
                "volume": [
                    0,
                    157.5,
                    173.25
                ],
                "total_floor_area": 126,
                "dwelling_volume": 330.75
            },
            "ventilation_rates": {
                "number_of_chimneys_total": 0,
                "number_of_chimneys_m3_per_hour": 0.0,
                "number_of_open_flues_total": 0,
                "number_of_open_flues_m3_per_hour": 0.0,
                "number_of_intermittant_fans_m3_per_hour": 0.0,
                "number_of_passive_vents_m3_per_hour": 0.0,
                "number_of_flueless_gas_fires_m3_per_hour": 0.0,
                "infiltration_due_to_chimneys_flues_fans_PSVs": 0.0,
                "additional_infiltration": null,
                "window_infiltration": null,
                "infiltration_rate": null,
                "infiltration_rate2": 0.589,
                "shelter_factor": 0.85,
                "infiltration_rate_incorporating_shelter_factor": 0.5006499999999999,
                "wind_factor": [
                    1.125,
                    1.125,
                    1.1,
                    0.975,
                    0.95,
                    0.85,
                    0.825,
                    0.825,
                    0.875,
                    0.95,
                    0.975,
                    1.025
                ],
                "adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed": [
                    0.56323125,
                    0.56323125,
                    0.550715,
                    0.4881337499999999,
                    0.4756174999999999,
                    0.42555249999999994,
                    0.41303624999999994,
                    0.41303624999999994,
                    0.43806874999999995,
                    0.4756174999999999,
                    0.4881337499999999,
                    0.5131662499999999
                ],
                "exhaust_air_heat_pump_air_change_rate_through_system": null,
                "effective_air_change_rate": [
                    0.6586147204882813,
                    0.6586147204882813,
                    0.6516435056125,
                    0.6191372789445312,
                    0.6131060031531249,
                    0.590547465128125,
                    0.5852994719070312,
                    0.5852994719070312,
                    0.5959521148632813,
                    0.6131060031531249,
                    0.6191372789445312,
                    0.6316698000695312
                ]
            },
            "heat_losses_and_heat_loss_parameter": {
                "solid_floor_UA": 4.5,
                "semi_glazed_door_UA": 14.839999999999998,
                "window_UA": 46,
                "roof_window_UA": 0,
                "basement_floor_UA": 0,
                "basement_floor_Ak": 0,
                "ground_floor_UA": 39.69,
                "ground_floor_Ak": 1260,
                "exposed_floor_UA": 0,
                "exposed_floor_Ak": 0,
                "basement_wall_net_area": 0,
                "basement_wall_UA": 0,
                "basement_wall_Ak": 0,
                "external_wall_net_area": 84.9,
                "external_wall_UA": 127.35000000000001,
                "external_wall_Ak": 16131.000000000002,
                "roof_net_area": 63,
                "roof_UA": 8.82,
                "roof_Ak": 567,
                "total_area_of_external_elements": 246.0,
                "party_wall_UA": 23.5,
                "party_wall_Ak": 8460,
                "party_floor_Ak": 0,
                "party_ceiling_Ak": 3900,
                "internal_wall_Ak": 1179,
                "internal_floor_Ak": 1134,
                "internal_ceiling_Ak": 567,
                "fabric_heat_loss": 264.7,
                "heat_capacity": 33198.0,
                "thermal_mass_parameter": 263.4761904761905,
                "thermal_bridges": 36.9,
                "total_fabric_heat_loss": 301.59999999999997,
                "ventilation_heat_loss_calculated_monthly": [
                    71.88615020449468,
                    71.88615020449468,
                    71.12525952884035,
                    67.57728615359822,
                    66.9189874791557,
                    64.45677945007202,
                    63.8839741099727,
                    63.8839741099727,
                    65.04668345703999,
                    66.9189874791557,
                    67.57728615359822,
                    68.94517950308916
                ],
                "heat_transfer_coefficient": [
                    373.48615020449466,
                    373.48615020449466,
                    372.7252595288403,
                    369.1772861535982,
                    368.51898747915567,
                    366.056779450072,
                    365.4839741099727,
                    365.4839741099727,
                    366.64668345703996,
                    368.51898747915567,
                    369.1772861535982,
                    370.5451795030891
                ],
                "average_heat_transfer_coefficient": 369.1088914861237,
                "heat_loss_parameter": [
                    2.9641757952737673,
                    2.9641757952737673,
                    2.9581369803876214,
                    2.9299784615364937,
                    2.924753868882188,
                    2.905212535318032,
                    2.9006664611902595,
                    2.9006664611902595,
                    2.909894313151111,
                    2.924753868882188,
                    2.9299784615364937,
                    2.940834757961025
                ],
                "average_heat_loss_parameter": 0.27899387111573976
            },
            "water_heating_requirement": {
                "annual_hot_water_usage_litres_per_day": 108.0,
                "hot_water_usage_in_litres_per_day_monthly": [
                    118.80000000000001,
                    114.48,
                    110.16,
                    105.84,
                    101.52,
                    97.2,
                    97.2,
                    101.52,
                    105.84,
                    110.16,
                    114.48,
                    118.80000000000001
                ],
                "energy_content_of_water_used": [
                    176.17696800000002,
                    154.0855008,
                    159.00243479999997,
                    138.622176,
                    133.01127839999998,
                    114.77861999999999,
                    106.35926399999998,
                    122.04881039999998,
                    123.50646,
                    143.93487239999996,
                    157.116168,
                    170.617986
                ],
                "distribution_loss": [
                    26.426545200000003,
                    23.11282512,
                    23.850365219999997,
                    20.793326399999998,
                    19.951691759999996,
                    17.216793,
                    15.953889599999997,
                    18.307321559999995,
                    18.525969,
                    21.590230859999995,
                    23.5674252,
                    25.5926979
                ],
                "energy_lost_from_water_storage": 0,
                "water_storage_loss_monthly": [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0
                ],
                "total_heat_required_for_water_heating": [
                    176.17696800000002,
                    154.0855008,
                    159.00243479999997,
                    138.622176,
                    133.01127839999998,
                    114.77861999999999,
                    106.35926399999998,
                    122.04881039999997,
                    123.50646,
                    143.93487239999996,
                    157.116168,
                    170.617986
                ],
                "output_from_water_heater_monthly": [
                    176.17696800000002,
                    154.0855008,
                    159.00243479999997,
                    138.622176,
                    133.01127839999998,
                    114.77861999999999,
                    106.35926399999998,
                    122.04881039999997,
                    123.50646,
                    143.93487239999996,
                    157.116168,
                    170.617986
                ],
                "heat_gains_from_water_heating_monthly": [
                    58.57884186000001,
                    51.233429016,
                    52.868309571,
                    46.09187352,
                    44.22625006799999,
                    38.16389115,
                    35.364455279999994,
                    40.58122945799999,
                    41.06589795,
                    47.85834507299999,
                    52.24112586,
                    56.730480345000004
                ]
            },
            "internal_gains_appendix_L": {
                "G_L": 0.0,
                "C_1": 1.0,
                "C_2": 1.433,
                "E_B": 961.3129846269878,
                "initial_annual_lighting_demand": 1377.5615069704736,
                "monthly_lighting_demand": [
                    170.44004138215163,
                    136.73333404409811,
                    123.11320471364185,
                    90.19801113556179,
                    69.67153789610578,
                    56.92224382365604,
                    63.55670774707949,
                    82.61341500897964,
                    107.30665588605414,
                    140.792137622484,
                    159.02439796754066,
                    175.17709717811994
                ],
                "annual_lighting_demand": 1375.548784405473,
                "lighting_gains": [
                    194.72316555756572,
                    172.9513897879217,
                    140.65352689058545,
                    106.48376314614931,
                    79.59785915549719,
                    67.19987118070505,
                    72.61183008738921,
                    94.38360585703319,
                    126.68146875436948,
                    160.85123249880564,
                    187.7371364894577,
                    200.1351244642499
                ],
                "initial_annual_electrical_appliance_demand": 3344.397090331292,
                "monthly_electrical_appliance_demand": [
                    324.97196609445984,
                    296.56891709489645,
                    319.84634209264283,
                    292.02145229267745,
                    278.91906038248453,
                    249.1509937495433,
                    243.11740267414316,
                    239.74521055639624,
                    240.2351871057679,
                    266.3338680661697,
                    279.8422339220502,
                    310.63334189407493
                ],
                "annual_electrical_appliance_demand": 3341.3859759253064,
                "appliances_gains": [
                    436.7902770086826,
                    441.32279329597685,
                    429.9009974363479,
                    405.5853504064965,
                    374.89121019151145,
                    346.0430468743657,
                    326.77070251900966,
                    322.2381862317154,
                    333.6599820913443,
                    357.9756291211959,
                    388.66976933618076,
                    417.5179326533265
                ],
                "cooking_gains": [
                    55.16,
                    55.16,
                    55.16,
                    55.16,
                    55.16,
                    55.16,
                    55.16,
                    55.16,
                    55.16,
                    55.16,
                    55.16,
                    55.16
                ],
                "losses": [
                    -115.19999999999999,
                    -115.19999999999999,
                    -115.19999999999999,
                    -115.19999999999999,
                    -115.19999999999999,
                    -115.19999999999999,
                    -115.19999999999999,
                    -115.19999999999999,
                    -115.19999999999999,
                    -115.19999999999999,
                    -115.19999999999999,
                    -115.19999999999999
                ],
                "water_heating_gains": [
                    78.73500250000002,
                    76.24022175,
                    71.059555875,
                    64.016491,
                    59.44388449999999,
                    53.005404375,
                    47.532869999999996,
                    54.544663249999985,
                    57.035969375,
                    64.32573262499999,
                    72.55711925,
                    76.250645625
                ],
                "metabolic_gains": [
                    172.79999999999998,
                    172.79999999999998,
                    172.79999999999998,
                    172.79999999999998,
                    172.79999999999998,
                    172.79999999999998,
                    172.79999999999998,
                    172.79999999999998,
                    172.79999999999998,
                    172.79999999999998,
                    172.79999999999998,
                    172.79999999999998
                ]
            },
            "internal_gains": {
                "total_internal_gains": [
                    826.0084450662484,
                    806.2744048338986,
                    757.3740802019332,
                    691.8456045526458,
                    629.6929538470085,
                    582.0083224300707,
                    562.6754026063988,
                    586.9264553387486,
                    633.1374202207138,
                    698.9125942450014,
                    764.7240250756385,
                    809.6637027425766
                ]
            },
            "solar_gains_appendix_U3": {
                "solar_flux_north": [
                    11.436412538787879,
                    20.68106276617149,
                    34.88819996564874,
                    56.60050580088716,
                    74.37336606102218,
                    83.23769024974976,
                    76.70104638812194,
                    78.53644960579577,
                    58.8572132744309,
                    25.27636829258531,
                    13.896518711289401,
                    9.694808146066876
                ],
                "solar_flux_north_east": [
                    12.145680410782088,
                    23.390120502005598,
                    41.822541929590635,
                    69.35106310279406,
                    90.92010849368495,
                    101.33317075341961,
                    93.56166394939247,
                    96.27172344125725,
                    71.49571781748358,
                    29.345278592731244,
                    15.052394030804441,
                    10.086433192648474
                ],
                "solar_flux_east": [
                    21.134620057486963,
                    39.10325251255132,
                    63.89067906174743,
                    94.07548963233845,
                    112.45528635480359,
                    120.35576029517244,
                    113.08865238428933,
                    125.3690022999708,
                    104.24164026519922,
                    47.62774419378216,
                    25.95337911472664,
                    17.67550544600751
                ],
                "solar_flux_south_east": [
                    39.52445140930432,
                    63.67584001530772,
                    86.45248517226558,
                    108.19002478773515,
                    118.24508642072698,
                    122.75319126127208,
                    116.79405702599594,
                    138.09149868418606,
                    131.337465411037,
                    72.24114109708997,
                    46.62387627277164,
                    34.40022790846911
                ],
                "solar_flux_south": [
                    50.19978039205471,
                    77.74870204827221,
                    98.25759733263759,
                    112.15296767461275,
                    114.04561780476595,
                    114.77624296019953,
                    110.66770715027762,
                    138.64572001814557,
                    144.00160165626096,
                    86.0766956546692,
                    58.60023126922464,
                    44.116758929075765
                ],
                "solar_flux_south_west": [
                    39.52445140930432,
                    63.67584001530772,
                    86.45248517226558,
                    108.19002478773515,
                    118.24508642072698,
                    122.75319126127208,
                    116.79405702599594,
                    138.09149868418606,
                    131.337465411037,
                    72.24114109708997,
                    46.62387627277164,
                    34.40022790846911
                ],
                "solar_flux_west": [
                    21.134620057486963,
                    39.10325251255132,
                    63.89067906174743,
                    94.07548963233845,
                    112.45528635480359,
                    120.35576029517244,
                    113.08865238428933,
                    125.3690022999708,
                    104.24164026519922,
                    47.62774419378216,
                    25.95337911472664,
                    17.67550544600751
                ],
                "solar_flux_north_west": [
                    12.145680410782088,
                    23.390120502005598,
                    41.822541929590635,
                    69.35106310279406,
                    90.92010849368495,
                    101.33317075341961,
                    93.56166394939247,
                    96.27172344125725,
                    71.49571781748358,
                    29.345278592731244,
                    15.052394030804441,
                    10.086433192648474
                ]
            },
            "solar_gains": {
                "gains_north": [
                    41.085449282545916,
                    74.29696616022427,
                    125.33627703499268,
                    203.33799629575677,
                    267.187210054615,
                    299.032401074509,
                    275.5494295618847,
                    282.14313764621653,
                    211.44524497495226,
                    90.80565640753223,
                    49.923410228531715,
                    34.828714602443
                ],
                "gains_north_east": [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "gains_east": [
                    37.20392432426168,
                    68.8346629062817,
                    112.46873529656344,
                    165.60398945092524,
                    197.9585131896034,
                    211.86596143347,
                    199.07344696965018,
                    220.6909261434296,
                    183.4997783406816,
                    83.84058884905545,
                    45.68653469600037,
                    31.1147380562152
                ],
                "gains_south_east": [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "gains_south": [
                    214.60854301242728,
                    332.38264266048253,
                    420.0600010353155,
                    479.4639498259235,
                    487.55519810813206,
                    490.6786858778245,
                    473.1143284803312,
                    592.7228313674555,
                    615.6197035435115,
                    367.98555885109886,
                    250.52122050458306,
                    188.60308316603607
                ],
                "gains_south_west": [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "gains_west": [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "gains_north_west": [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "gains_roof_windows": [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "solar_gains_watts": [
                    292.8979166192349,
                    475.5142717269885,
                    657.8650133668716,
                    848.4059355726056,
                    952.7009213523504,
                    1001.5770483858034,
                    947.7372050118661,
                    1095.5568951571017,
                    1010.5647268591454,
                    542.6318041076865,
                    346.13116542911513,
                    254.54653582469427
                ],
                "total_internal_and_solar_gains": [
                    1118.9063616854833,
                    1281.788676560887,
                    1415.239093568805,
                    1540.2515401252513,
                    1582.393875199359,
                    1583.5853708158743,
                    1510.412607618265,
                    1682.4833504958503,
                    1643.702147079859,
                    1241.544398352688,
                    1110.8551905047536,
                    1064.2102385672708
                ]
            },
            "utilisation_factor_for_heating_table_9a": {
                "time_constant": [
                    24.690786155303304,
                    24.690786155303304,
                    24.741190544273064,
                    24.97896542538086,
                    25.02358624652486,
                    25.19190241612353,
                    25.23138446527864,
                    25.23138446527864,
                    25.151370741219782,
                    25.02358624652486,
                    24.97896542538086,
                    24.886753833994458
                ],
                "a": [
                    2.646052410353554,
                    2.646052410353554,
                    2.6494127029515377,
                    2.6652643616920573,
                    2.6682390831016574,
                    2.679460161074902,
                    2.6820922976852426,
                    2.6820922976852426,
                    2.6767580494146523,
                    2.6682390831016574,
                    2.6652643616920573,
                    2.659116922266297
                ],
                "heat_loss_rate_living_room": [
                    5863.732558210566,
                    5676.989483108318,
                    4994.51847768646,
                    4060.95014768958,
                    3021.855697329076,
                    1903.495253140374,
                    1242.6455119739067,
                    1279.1939093849044,
                    2199.88010074224,
                    3500.9303810519787,
                    4762.386991381417,
                    5854.613836148808
                ],
                "y_living_room": [
                    0.19081810955357412,
                    0.2257866921146858,
                    0.28335846586443425,
                    0.37928353811522547,
                    0.5236497151726959,
                    0.8319355502480427,
                    1.2154814812947081,
                    1.3152684187691812,
                    0.747178060533969,
                    0.3546327013734052,
                    0.23325596859622907,
                    0.18177291762547967
                ],
                "utilisation_factor_for_heating_living_room": [
                    0.9898710602320386,
                    0.9848424812922535,
                    0.9743732827705389,
                    0.9517679810882888,
                    0.9065144344272734,
                    0.7913072833532275,
                    0.6541059073056135,
                    0.6227782770288123,
                    0.8237698575019649,
                    0.958475204499211,
                    0.9840832115221984,
                    0.9911951081097073
                ],
                "temperature_during_heating_rest_of_dwelling": [
                    17.768019050166806,
                    17.768019050166806,
                    17.771077552507112,
                    17.78541935388582,
                    17.788094897246257,
                    17.798142454296052,
                    17.80048903206591,
                    17.80048903206591,
                    17.79572942965799,
                    17.788094897246257,
                    17.78541935388582,
                    17.77987433150828
                ],
                "heat_loss_rate_rest_of_dwelling": [
                    5030.118585927595,
                    4843.375510825348,
                    4163.742779975016,
                    3243.377274788865,
                    2206.726668462289,
                    1097.4903711521472,
                    438.7595023148832,
                    475.30789972588104,
                    1391.6916066843835,
                    2685.8013521851917,
                    3944.814118480702,
                    5031.9569717981285
                ],
                "y_rest_of_dwelling": [
                    0.22244134856298778,
                    0.26464780062912374,
                    0.3398958985591557,
                    0.4748912659954175,
                    0.7170774241388113,
                    1.442915047312373,
                    3.4424613020330477,
                    3.5397756937475053,
                    1.181082173079907,
                    0.4622621838143601,
                    0.28159886806848744,
                    0.21149032961364614
                ],
                "utilisation_factor_for_heating_rest_of_dwelling": [
                    0.9853699748581132,
                    0.9780077699256723,
                    0.9614077696920973,
                    0.9228038974306823,
                    0.8347106825562942,
                    0.5854904937196589,
                    0.2829256350308353,
                    0.2756078214168028,
                    0.6650196783967307,
                    0.9270852526727167,
                    0.9752439186346192,
                    0.9872897632890457
                ]
            },
            "temperature_reduction_when_heating_is_off_table_9b": {
                "t_c": [
                    10.172696538825825,
                    10.172696538825825,
                    10.185297636068267,
                    10.244741356345216,
                    10.255896561631214,
                    10.297975604030881,
                    10.30784611631966,
                    10.30784611631966,
                    10.287842685304945,
                    10.255896561631214,
                    10.244741356345216,
                    10.221688458498615
                ],
                "internal_temperature_without_heating_living_room": [
                    7.265499593319735,
                    8.179937756795958,
                    10.299698709041044,
                    12.970889200651463,
                    15.69250740817979,
                    18.223246632997107,
                    19.303182298260516,
                    19.366922098850182,
                    17.69301658672797,
                    13.72911318422433,
                    10.061108346609386,
                    7.046724342447828
                ],
                "internal_temperature_without_heating_rest_of_dwelling": [
                    7.252015042268464,
                    8.15648131635647,
                    10.25046861124734,
                    12.850047599244316,
                    15.384187291612122,
                    17.332869851499847,
                    17.76922895787599,
                    17.76874392216354,
                    16.98132868112836,
                    13.623360101808329,
                    10.034510896677231,
                    7.035508144874141
                ],
                "temperature_reduction_when_heating_is_off_1_weekday_living_room": [
                    1.6691084621239978,
                    1.549253232000747,
                    1.2698436036675929,
                    0.9148252168084217,
                    0.5600020847759796,
                    0.23004564978867345,
                    0.09013427815099194,
                    0.08188945184807807,
                    0.2989915357819771,
                    0.815256118349966,
                    1.2935275842416891,
                    1.6896459210425174
                ],
                "temperature_reduction_when_heating_is_off_2_weekday_living_room": [
                    1.6691084621239978,
                    1.549253232000747,
                    1.2698436036675929,
                    0.9148252168084217,
                    0.5600020847759796,
                    0.23004564978867345,
                    0.09013427815099194,
                    0.08188945184807807,
                    0.2989915357819771,
                    0.815256118349966,
                    1.2935275842416891,
                    1.6896459210425174
                ],
                "temperature_reduction_when_heating_is_off_1_weekend_living_room": [
                    1.6691084621239978,
                    1.549253232000747,
                    1.2698436036675929,
                    0.9148252168084217,
                    0.5600020847759796,
                    0.23004564978867345,
                    0.09013427815099194,
                    0.08188945184807807,
                    0.2989915357819771,
                    0.815256118349966,
                    1.2935275842416891,
                    1.6896459210425174
                ],
                "temperature_reduction_when_heating_is_off_2_weekend_living_room": [
                    1.6691084621239978,
                    1.549253232000747,
                    1.2698436036675929,
                    0.9148252168084217,
                    0.5600020847759796,
                    0.23004564978867345,
                    0.09013427815099194,
                    0.08188945184807807,
                    0.2989915357819771,
                    0.815256118349966,
                    1.2935275842416891,
                    1.6896459210425174
                ],
                "temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling": [
                    1.378330575740952,
                    1.2597823591973238,
                    0.9845052100232168,
                    0.6423291173456148,
                    0.31252364155432943,
                    0.06024130316953887,
                    0.004043531349765543,
                    0.004106271351504554,
                    0.10554862646346783,
                    0.541442641692104,
                    1.008765790188604,
                    1.4015122492084897
                ],
                "temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling": [
                    1.378330575740952,
                    1.2597823591973238,
                    0.9845052100232168,
                    0.6423291173456148,
                    0.31252364155432943,
                    0.06024130316953887,
                    0.004043531349765543,
                    0.004106271351504554,
                    0.10554862646346783,
                    0.541442641692104,
                    1.008765790188604,
                    1.4015122492084897
                ],
                "temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling": [
                    1.378330575740952,
                    1.2597823591973238,
                    0.9845052100232168,
                    0.6423291173456148,
                    0.31252364155432943,
                    0.06024130316953887,
                    0.004043531349765543,
                    0.004106271351504554,
                    0.10554862646346783,
                    0.541442641692104,
                    1.008765790188604,
                    1.4015122492084897
                ],
                "temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling": [
                    1.378330575740952,
                    1.2597823591973238,
                    0.9845052100232168,
                    0.6423291173456148,
                    0.31252364155432943,
                    0.06024130316953887,
                    0.004043531349765543,
                    0.004106271351504554,
                    0.10554862646346783,
                    0.541442641692104,
                    1.008765790188604,
                    1.4015122492084897
                ]
            },
            "heating_requirement_table_9c": {
                "T_weekday_living_room": [
                    16.661783075752005,
                    16.901493535998505,
                    17.460312792664816,
                    18.170349566383155,
                    18.879995830448042,
                    19.539908700422654,
                    19.819731443698018,
                    19.836221096303845,
                    19.402016928436044,
                    18.369487763300068,
                    17.412944831516622,
                    16.620708157914965
                ],
                "T_weekend_living_room": [
                    16.661783075752005,
                    16.901493535998505,
                    17.460312792664816,
                    18.170349566383155,
                    18.879995830448042,
                    19.539908700422654,
                    19.819731443698018,
                    19.836221096303845,
                    19.402016928436044,
                    18.369487763300068,
                    17.412944831516622,
                    16.620708157914965
                ],
                "mean_internal_temperature_living_room_T1_Table_9c": [
                    16.661783075752005,
                    16.901493535998505,
                    17.460312792664816,
                    18.170349566383155,
                    18.879995830448042,
                    19.539908700422654,
                    19.81973144369802,
                    19.83622109630384,
                    19.402016928436044,
                    18.369487763300068,
                    17.412944831516622,
                    16.620708157914965
                ],
                "T_weekday_rest_of_dwelling": [
                    15.011357898684903,
                    15.248454331772159,
                    15.802067132460678,
                    16.500761119194593,
                    17.163047614137596,
                    17.677659847956974,
                    17.79240196936638,
                    17.7922764893629,
                    17.584632176731052,
                    16.70520961386205,
                    15.767887773508614,
                    14.976849833091302
                ],
                "T_weekend_rest_of_dwelling": [
                    15.011357898684903,
                    15.248454331772159,
                    15.802067132460678,
                    16.500761119194593,
                    17.163047614137596,
                    17.677659847956974,
                    17.79240196936638,
                    17.7922764893629,
                    17.584632176731052,
                    16.70520961386205,
                    15.767887773508614,
                    14.976849833091302
                ],
                "mean_internal_temperature_rest_of_dwelling_T2_table_9c": [
                    15.011357898684903,
                    15.24845433177216,
                    15.802067132460678,
                    16.500761119194593,
                    17.163047614137596,
                    17.677659847956974,
                    17.79240196936638,
                    17.7922764893629,
                    17.584632176731052,
                    16.70520961386205,
                    15.767887773508614,
                    14.976849833091302
                ]
            },
            "mean_internal_temperature": {
                "living_area_fraction": 0.12698412698412698,
                "mean_internal_temp_whole_dwelling": [
                    15.220935698947391,
                    15.45836407199138,
                    16.01263800994692,
                    16.712772350583617,
                    17.381072784462734,
                    17.91413589271452,
                    18.049840632773574,
                    18.05182501087921,
                    17.815411192820577,
                    16.916546521727195,
                    15.976783907858838,
                    15.185593747354623
                ]
            },
            "utilisation_factor_for_heating_whole_house_table_9a": {
                "time_constant_whole_house": [
                    24.690786155303304,
                    24.690786155303304,
                    24.741190544273064,
                    24.97896542538086,
                    25.02358624652486,
                    25.19190241612353,
                    25.23138446527864,
                    25.23138446527864,
                    25.151370741219782,
                    25.02358624652486,
                    24.97896542538086,
                    24.886753833994458
                ],
                "a_whole_house": [
                    2.646052410353554,
                    2.646052410353554,
                    2.6494127029515377,
                    2.6652643616920573,
                    2.6682390831016574,
                    2.679460161074902,
                    2.6820922976852426,
                    2.6820922976852426,
                    2.6767580494146523,
                    2.6682390831016574,
                    2.6652643616920573,
                    2.659116922266297
                ],
                "heat_loss_rate_whole_house": [
                    4078.8182308306937,
                    3980.7513647259616,
                    3508.3279451084923,
                    2847.380365108968,
                    2056.731291577679,
                    1139.9505556569516,
                    529.8935162922027,
                    567.1671720993851,
                    1398.9078598725332,
                    2364.619227299804,
                    3277.1069928752577,
                    4070.6588070615326
                ],
                "y_whole_house": [
                    0.2743212122638783,
                    0.3219966682468566,
                    0.4033941854101783,
                    0.5409363494245725,
                    0.7693731707585074,
                    1.3891702258114667,
                    2.850407791714455,
                    2.966468147773947,
                    1.1749895716717405,
                    0.5250504537977673,
                    0.33897434319961434,
                    0.261434398953099
                ],
                "utilisation_factor_for_heating_whole_house": [
                    0.9761079099113684,
                    0.9656434303833015,
                    0.9441263026325147,
                    0.9002533073727103,
                    0.8145321748485704,
                    0.600728558381495,
                    0.3368108736174081,
                    0.3247811027290035,
                    0.6670380534773137,
                    0.9060274656261859,
                    0.9623032505637008,
                    0.9789958324108872
                ]
            },
            "space_heating_requirement": {
                "useful_gains": [
                    1092.1733500913508,
                    1237.7508146607272,
                    1336.1644527521073,
                    1386.6165431836682,
                    1288.9107246331912,
                    951.3049568842453,
                    508.7233898946552,
                    546.4387978972308,
                    1096.4118806846304,
                    1124.8733247018736,
                    1068.9795607282836,
                    1041.8573883663541
                ],
                "heat_loss_rate_for_mean_internal_temperature": [
                    4078.8182308306937,
                    3980.7513647259616,
                    3508.3279451084923,
                    2847.380365108968,
                    2056.731291577679,
                    1139.9505556569516,
                    529.8935162922027,
                    567.1671720993851,
                    1398.9078598725332,
                    2364.619227299804,
                    3277.1069928752577,
                    4070.6588070615326
                ],
                "space_heating_requirement_monthly": [
                    2222.0637912700713,
                    1843.2963696438374,
                    1616.0896383131505,
                    1051.749951786216,
                    571.2585018066987,
                    135.82483111634852,
                    15.750574039775303,
                    15.421910406402821,
                    217.79710501529001,
                    922.3709515328603,
                    1589.8517511458213,
                    2253.428255509213
                ],
                "space_heating_requirement_yearly": 12454.903631585687,
                "space_heating_requirement_yearly_per_m2": 98.84844152052132
            },
            "energy_requirements": {
                "fraction_of_space_heat_from_main_systems": 1,
                "fraction_of_total_space_heat_from_main_system_1": 1,
                "fraction_of_total_space_heat_from_main_system_2": 0,
                "space_heating_fuel_main_system_1": [
                    2502.3240892680983,
                    2075.7842000493665,
                    1819.9207638661605,
                    1184.403098858351,
                    643.3091236561924,
                    0,
                    0,
                    0,
                    0,
                    1038.7060265009688,
                    1790.3735936326816,
                    2537.644431879745
                ],
                "space_heating_fuel_main_system_2": [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "space_heating_fuel_secondary_system": [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0
                ],
                "efficiency_of_water_heater_table_4a": [
                    88.08818571043759,
                    88.05280057451473,
                    87.93357632302069,
                    87.67687598232241,
                    86.99272176591167,
                    84.54075372718351,
                    81.03583975422129,
                    80.89937924581712,
                    85.40059859744034,
                    87.50076184715809,
                    87.93010620821106,
                    88.11775553227744
                ],
                "fuel_for_water_heating_monthly": [
                    200.0006772521423,
                    174.99216355941462,
                    180.8210713685868,
                    158.10574275929866,
                    152.8993181267732,
                    135.76720686734745,
                    131.2496598080352,
                    150.8649529054458,
                    144.62013384962597,
                    164.49556479453074,
                    178.6830185647248,
                    193.62497940327455
                ],
                "space_cooling_fuel_monthly": [
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0
                ],
                "space_heating_fuel_used_main_system_1": 13592.465327711565,
                "space_heating_fuel_used_main_system_2": 0.0,
                "space_heating_fuel_used_secondary": 0.0,
                "water_fuel_used": 1966.1244892592,
                "space_cooling_fuel_used": 0,
                "electricity_for_pumps_fans_electric_keep_hot": 0,
                "energy_saving_generation_technologies_total": 0,
                "appendix_Q_energy_total": 0,
                "energy_for_lighting": 1375.548784405473,
                "total_energy_used": 16934.13860137624
            },
            "fuel_costs": {
                "space_heating_main_system_1_fuel_cost": 473.01779340436246,
                "space_heating_main_system_2_fuel_cost": 0.0,
                "space_heating_secondary_fuel_cost": 0.0,
                "water_heating_high_rate_fuel_cost": 0.0,
                "water_heating_low_rate_fuel_cost": 68.42113222622015,
                "water_heating_cost_other": 0.0,
                "space_cooling_cost": 0.0,
                "pumps_fan_keep_hot_cost": 0.0,
                "lighting_cost": 181.4348846630819,
                "appendix_Q_fuel_cost": 0.0,
                "energy_saving_total_fuel_cost": 0.0,
                "additional_standing_charges_table_12": 0,
                "total_fuel_cost": 722.8738102936645
            },
            "SAP_rating": {
                "energy_cost_factor": 1.7754795340546146,
                "SAP_rating_value": 75.23206049993813
            },
            "CO2_emissions": {
                "space_heating_main_system_1_emissions": 2935.972510785698,
                "space_heating_main_system_2_emissions": 0.0,
                "space_heating_secondary_emissions": 0.0,
                "water_used_emissions": 424.68288967998717,
                "space_cooling_used_emissions": 0,
                "pumps_fans_electric_keep_hot_emissions": 0,
                "lighting_emissions": 713.9098191064405,
                "appendix_Q_used_emissions": [
                    0
                ],
                "appendix_Q_saved_emissions": [
                    0
                ],
                "energy_saving_generation_technologies_emissions": [
                    0
                ],
                "space_and_water_heating_emissions": 3360.655400465685,
                "appendix_Q_total_used_emissions": 0,
                "appendix_Q_total_saved_emissions": 0,
                "energy_saving_generation_technologies_total_emissions": 0,
                "total_CO2_emissions_yearly": 4074.5652195721254,
                "dwelling_CO2_emission_rate": 32.337819202953376,
                "CF": 23.82786678112354,
                "EI_rating": 68.07065851329446
            }
        }
        
    
    """
    
    result={}
    
    # overall_dwelling_dimensions
    result['overall_dwelling_dimensions']=(
        overall_dwelling_dimensions(**inputs['overall_dwelling_dimensions'])
        )
    
    # ventilation_rates
    result['ventilation_rates']=(
        ventilation_rates(**inputs['ventilation_rates'],
            dwelling_volume=result['overall_dwelling_dimensions']['dwelling_volume']
            )
        )
    
    # heat_losses_and_heat_loss_parameter
    result['heat_losses_and_heat_loss_parameter']=(
        heat_losses_and_heat_loss_parameter(
            **inputs['heat_losses_and_heat_loss_parameter'],
            total_floor_area=result['overall_dwelling_dimensions']['total_floor_area'],
            effective_air_change_rate=result['ventilation_rates']['effective_air_change_rate'],
            dwelling_volume=result['overall_dwelling_dimensions']['dwelling_volume']
            )
        )
    
    # water_heating_requirement
    result['water_heating_requirement']=(
        water_heating_requirement(
            **inputs['water_heating_requirement'],
            )
        )
    
    # internal_gains_appendix_L
    result['internal_gains_appendix_L']=(
        internal_gains_appendix_L(
            **inputs['internal_gains_appendix_L'],
            total_floor_area=result['overall_dwelling_dimensions']['total_floor_area'],
            assumed_occupancy=inputs['water_heating_requirement']['assumed_occupancy'],
            days_in_month=inputs['water_heating_requirement']['days_in_month'],
            heat_gains_from_water_heating_monthly=result['water_heating_requirement']['heat_gains_from_water_heating_monthly']
            )
        )
    
    # internal_gains
    result['internal_gains']=(
        internal_gains(
            **inputs['internal_gains'],
            metabolic_gains=result['internal_gains_appendix_L']['metabolic_gains'],
            lighting_gains=result['internal_gains_appendix_L']['lighting_gains'],
            appliances_gains=result['internal_gains_appendix_L']['appliances_gains'],
            cooking_gains=result['internal_gains_appendix_L']['cooking_gains'],
            losses=result['internal_gains_appendix_L']['losses'],
            water_heating_gains=result['internal_gains_appendix_L']['water_heating_gains'],
            )
        )
    
    # solar_gains_appendix_U3
    result['solar_gains_appendix_U3']=(
        solar_gains_appendix_U3(
            **inputs['solar_gains_appendix_U3']
            )
        )
    
    # solar_gains
    result['solar_gains']=(
        solar_gains(
            **inputs['solar_gains'],
            solar_flux_north=result['solar_gains_appendix_U3']['solar_flux_north'],
            solar_flux_north_east=result['solar_gains_appendix_U3']['solar_flux_north_east'],
            solar_flux_east=result['solar_gains_appendix_U3']['solar_flux_east'],
            solar_flux_south_east=result['solar_gains_appendix_U3']['solar_flux_south_east'],
            solar_flux_south=result['solar_gains_appendix_U3']['solar_flux_south'],
            solar_flux_south_west=result['solar_gains_appendix_U3']['solar_flux_south_west'],
            solar_flux_west=result['solar_gains_appendix_U3']['solar_flux_west'],
            solar_flux_north_west=result['solar_gains_appendix_U3']['solar_flux_north_west'],
            total_internal_gains=result['internal_gains']['total_internal_gains']
            )
        )
    
    # utilisation_factor_for_heating_table_9a
    result['utilisation_factor_for_heating_table_9a']=(
        utilisation_factor_for_heating_table_9a(
            **inputs['utilisation_factor_for_heating_table_9a'],
            heat_transfer_coefficient=result['heat_losses_and_heat_loss_parameter']['heat_transfer_coefficient'],
            total_internal_and_solar_gains=result['solar_gains']['total_internal_and_solar_gains'],
            thermal_mass_parameter=result['heat_losses_and_heat_loss_parameter']['thermal_mass_parameter'],
            heat_loss_parameter=result['heat_losses_and_heat_loss_parameter']['heat_loss_parameter']
            )
        )
    
    # temperature_reduction_when_heating_is_off_table_9b
    result['temperature_reduction_when_heating_is_off_table_9b']=(
        temperature_reduction_when_heating_is_off_table_9b(
            **inputs['temperature_reduction_when_heating_is_off_table_9b'],
            time_constant=result['utilisation_factor_for_heating_table_9a']['time_constant'], 
            temperature_during_heating_living_room=inputs['utilisation_factor_for_heating_table_9a']['temperature_during_heating_living_room'], 
            temperature_during_heating_rest_of_dwelling=result['utilisation_factor_for_heating_table_9a']['temperature_during_heating_rest_of_dwelling'], 
            monthly_external_temperature_table_U1=inputs['utilisation_factor_for_heating_table_9a']['monthly_external_temperature_table_U1'], 
            utilisation_factor_for_heating_living_room=result['utilisation_factor_for_heating_table_9a']['utilisation_factor_for_heating_living_room'], 
            utilisation_factor_for_heating_rest_of_dwelling=result['utilisation_factor_for_heating_table_9a']['utilisation_factor_for_heating_rest_of_dwelling'], 
            heat_transfer_coefficient=result['heat_losses_and_heat_loss_parameter']['heat_transfer_coefficient'],
            total_internal_and_solar_gains=result['solar_gains']['total_internal_and_solar_gains']
            )
        )
    
    # temperature_adjustment_table_4e=0
    result['heating_requirement_table_9c']=(
        heating_requirement_table_9c(
            **inputs['heating_requirement_table_9c'],
            temperature_reduction_when_heating_is_off_1_weekday_living_room=result['temperature_reduction_when_heating_is_off_table_9b']['temperature_reduction_when_heating_is_off_1_weekday_living_room'], 
            temperature_reduction_when_heating_is_off_2_weekday_living_room=result['temperature_reduction_when_heating_is_off_table_9b']['temperature_reduction_when_heating_is_off_2_weekday_living_room'], 
            temperature_reduction_when_heating_is_off_1_weekend_living_room=result['temperature_reduction_when_heating_is_off_table_9b']['temperature_reduction_when_heating_is_off_1_weekend_living_room'], 
            temperature_reduction_when_heating_is_off_2_weekend_living_room=result['temperature_reduction_when_heating_is_off_table_9b']['temperature_reduction_when_heating_is_off_2_weekend_living_room'], 
            temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling=result['temperature_reduction_when_heating_is_off_table_9b']['temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling'], 
            temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling=result['temperature_reduction_when_heating_is_off_table_9b']['temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling'], 
            temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling=result['temperature_reduction_when_heating_is_off_table_9b']['temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling'], 
            temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling=result['temperature_reduction_when_heating_is_off_table_9b']['temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling'],
            temperature_during_heating_living_room=inputs['utilisation_factor_for_heating_table_9a']['temperature_during_heating_living_room'],
            temperature_during_heating_rest_of_dwelling=result['utilisation_factor_for_heating_table_9a']['temperature_during_heating_rest_of_dwelling'],
            )
        )
    
    # mean_internal_temperature
    result['mean_internal_temperature']=(
        mean_internal_temperature(
            **inputs['mean_internal_temperature'],
            mean_internal_temperature_living_room_T1_Table_9c=result['heating_requirement_table_9c']['mean_internal_temperature_living_room_T1_Table_9c'], 
            mean_internal_temperature_rest_of_dwelling_T2_table_9c=result['heating_requirement_table_9c']['mean_internal_temperature_rest_of_dwelling_T2_table_9c'], 
            total_floor_area=result['overall_dwelling_dimensions']['total_floor_area'], 
            temperature_adjustment_table_4e=inputs['heating_requirement_table_9c']['temperature_adjustment_table_4e'] 
            )
        )
    
    # utilisation_factor_for_heating_whole_house_table_9a
    result['utilisation_factor_for_heating_whole_house_table_9a']=(
        utilisation_factor_for_heating_whole_house_table_9a(
            heat_transfer_coefficient=result['heat_losses_and_heat_loss_parameter']['heat_transfer_coefficient'],
            total_internal_and_solar_gains=result['solar_gains']['total_internal_and_solar_gains'],
            mean_internal_temp_whole_dwelling=result['mean_internal_temperature']['mean_internal_temp_whole_dwelling'],
            monthly_external_temperature_table_U1=inputs['utilisation_factor_for_heating_table_9a']['monthly_external_temperature_table_U1'],
            thermal_mass_parameter=result['heat_losses_and_heat_loss_parameter']['thermal_mass_parameter'],
            heat_loss_parameter=result['heat_losses_and_heat_loss_parameter']['heat_loss_parameter']
            )
        )
    
    # space_heating_requirement
    result['space_heating_requirement']=(
        space_heating_requirement(
            utilisation_factor_for_heating_whole_house=result['utilisation_factor_for_heating_whole_house_table_9a']['utilisation_factor_for_heating_whole_house'],
            total_internal_and_solar_gains=result['solar_gains']['total_internal_and_solar_gains'],
            monthly_external_temperature_table_U1=inputs['utilisation_factor_for_heating_table_9a']['monthly_external_temperature_table_U1'],
            mean_internal_temp_whole_dwelling=result['mean_internal_temperature']['mean_internal_temp_whole_dwelling'],
            heat_transfer_coefficient=result['heat_losses_and_heat_loss_parameter']['heat_transfer_coefficient'],
            days_in_month=inputs['water_heating_requirement']['days_in_month'],
            total_floor_area=result['overall_dwelling_dimensions']['total_floor_area']
            )
        )
    
    # energy_requirements
    result['energy_requirements']=(
        energy_requirements(
            **inputs['energy_requirements'],
            space_heating_requirement_monthly=result['space_heating_requirement']['space_heating_requirement_monthly'],
            output_from_water_heater_monthly=result['water_heating_requirement']['output_from_water_heater_monthly'],
            annual_lighting_demand=result['internal_gains_appendix_L']['annual_lighting_demand']
            )
        )
    
    # fuel_costs
    result['fuel_costs']=(
        fuel_costs(
            **inputs['fuel_costs'],
            space_heating_fuel_used_main_system_1=result['energy_requirements']['space_heating_fuel_used_main_system_1'], 
            space_heating_fuel_used_main_system_2=result['energy_requirements']['space_heating_fuel_used_main_system_2'], 
            space_heating_fuel_used_secondary=result['energy_requirements']['space_heating_fuel_used_secondary'],
            water_fuel_used=result['energy_requirements']['water_fuel_used'],
            energy_for_lighting=result['energy_requirements']['energy_for_lighting'],
            appendix_Q_energy_used=inputs['energy_requirements']['appendix_Q_energy_used'],
            appendix_Q_energy_saved=inputs['energy_requirements']['appendix_Q_energy_saved'],
            )
        )
    
    # SAP_rating
    result['SAP_rating']=(
        SAP_rating(
            **inputs['SAP_rating'],
            total_fuel_cost=result['fuel_costs']['total_fuel_cost'],
            total_floor_area=result['overall_dwelling_dimensions']['total_floor_area']
            )
        )
    
    # CO2_emissions
    result['CO2_emissions']=(
        CO2_emissions(
            **inputs['CO2_emissions'],
            space_heating_fuel_used_main_system_1=result['energy_requirements']['space_heating_fuel_used_main_system_1'], 
            space_heating_fuel_used_main_system_2=result['energy_requirements']['space_heating_fuel_used_main_system_2'], 
            space_heating_fuel_used_secondary=result['energy_requirements']['space_heating_fuel_used_secondary'], 
            water_fuel_used=result['energy_requirements']['water_fuel_used'], 
            space_cooling_fuel_used=result['energy_requirements']['space_cooling_fuel_used'],
            electricity_for_pumps_fans_electric_keep_hot=result['energy_requirements']['electricity_for_pumps_fans_electric_keep_hot'], 
            energy_for_lighting=result['energy_requirements']['energy_for_lighting'], 
            energy_saving_generation_technologies=inputs['fuel_costs']['energy_saving_generation_technologies'], 
            appendix_Q_energy_used=inputs['energy_requirements']['appendix_Q_energy_used'],
            appendix_Q_energy_saved=inputs['energy_requirements']['appendix_Q_energy_saved'],
            total_floor_area=result['overall_dwelling_dimensions']['total_floor_area']
            )
        )
    
    return result


# def calculate_worksheet_old(
#         # overall_dwelling_dimensions inputs
#         area,
#         average_storey_height,    
    
#         # ventilation_rates inputs
#         number_of_chimneys_main_heating,
#         number_of_chimneys_secondary_heating,
#         number_of_chimneys_other,
#         number_of_open_flues_main_heating,
#         number_of_open_flues_secondary_heating,
#         number_of_open_flues_other,
#         number_of_intermittant_fans_total,
#         number_of_passive_vents_total,
#         number_of_flueless_gas_fires_total,
#         air_permeability_value_q50,
#         number_of_storeys_in_the_dwelling,
#         structural_infiltration,
#         suspended_wooden_ground_floor_infiltration,
#         no_draft_lobby_infiltration,
#         percentage_of_windows_and_doors_draught_proofed,
#         number_of_sides_on_which_dwelling_is_sheltered,
#         monthly_average_wind_speed,
#         applicable_case,
#         mechanical_ventilation_air_change_rate_through_system,
#         exhaust_air_heat_pump_using_Appendix_N,
#         mechanical_ventilation_throughput_factor,
#         efficiency_allowing_for_in_use_factor,
        
#         # heat_losses_and_heat_loss_parameter inputs
#         solid_door_net_area,
#         solid_door_u_value,
#         semi_glazed_door_net_area,
#         semi_glazed_door_u_value,
#         window_net_area,
#         window_u_value,
#         roof_window_net_area,
#         roof_window_u_value,
#         basement_floor_net_area,
#         basement_floor_u_value,
#         basement_floor_heat_capacity,
#         ground_floor_net_area,
#         ground_floor_u_value,
#         ground_floor_heat_capacity,
#         exposed_floor_net_area,
#         exposed_floor_u_value,
#         exposed_floor_heat_capacity,
#         basement_wall_gross_area,
#         basement_wall_opening,
#         basement_wall_u_value,
#         basement_wall_heat_capacity,
#         external_wall_gross_area,
#         external_wall_opening,
#         external_wall_u_value,
#         external_wall_heat_capacity,
#         roof_gross_area,
#         roof_opening,
#         roof_u_value,
#         roof_heat_capacity,
#         party_wall_net_area,
#         party_wall_u_value,
#         party_wall_heat_capacity,
#         party_floor_net_area,
#         party_floor_heat_capacity,
#         party_ceiling_net_area,
#         party_ceiling_heat_capacity,
#         internal_wall_net_area,
#         internal_wall_heat_capacity,
#         internal_floor_net_area,
#         internal_floor_heat_capacity,
#         internal_ceiling_net_area,
#         internal_ceiling_heat_capacity,
#         thermal_bridges_appendix_k,
        
#         #water heating requirement inputs
#         assumed_occupancy,
#         V_dm_table_1c,
#         days_in_month,
#         T_table_1d,
#         water_storage_loss_manufacturer,
#         temperature_factor_table_2b,
#         storage_volume_litres,
#         hot_water_storage_loss_table_2,
#         volume_factor_table_2a,
#         Vs_appendix_G3,
#         solar_storage_WWHRS_factor,
#         primary_circuit_loss_table_3,
#         combi_loss_table_3,
#         solar_DHW_input_appendix_G,
        
#         #internal gains appendix L inputs
#         number_of_low_energy_light_bulbs,
#         total_number_of_light_bulbs,
#         frame_factor,
#         window_area,
#         light_access_factor_table_6d,
#         light_transmittance_factor_table_6d,
#         month_number,
        
#         #internal gains inputs
#         pumps_and_fans_gains,
        
#         #solar gains appendix U inputs
#         solar_radiation_horizontal_plane_monthly_table_U3,
#         solar_declination_monthly_table_U3,
#         location_latitude_table_U4,
#         p_tilt,
        
#         #solar gains inputs
#         access_factor_table_6d_north,
#         access_factor_table_6d_north_east,
#         access_factor_table_6d_east,
#         access_factor_table_6d_south_east,
#         access_factor_table_6d_south,
#         access_factor_table_6d_south_west,
#         access_factor_table_6d_west,
#         access_factor_table_6d_north_west,
#         access_factor_table_6d_roof_windows,
#         area_north,
#         area_north_east,
#         area_east,
#         area_south_east,
#         area_south,
#         area_south_west,
#         area_west,
#         area_north_west,
#         area_roof_windows,
#         solar_flux_roof_windows,
#         g_table_6b_north,
#         g_table_6b_north_east,
#         g_table_6b_east,
#         g_table_6b_south_east,
#         g_table_6b_south,
#         g_table_6b_south_west,
#         g_table_6b_west,
#         g_table_6b_north_west,
#         g_table_6b_roof_windows,
#         FF_table_6b_north,
#         FF_table_6b_north_east,
#         FF_table_6b_east,
#         FF_table_6b_south_east,
#         FF_table_6b_south,
#         FF_table_6b_south_west,
#         FF_table_6b_west,
#         FF_table_6b_north_west,
#         FF_table_6b_roof_windows,
        
#         #utilisation factor inputs
#         temperature_during_heating_living_room,
#         heating_controls,
#         monthly_external_temperature_table_U1,
        
#         #temperature reduction inputs
#         hours_heating_is_off_1_weekday_living_room,
#         hours_heating_is_off_2_weekday_living_room,
#         hours_heating_is_off_1_weekend_living_room,
#         hours_heating_is_off_2_weekend_living_room,
#         hours_heating_is_off_1_weekday_rest_of_dwelling,
#         hours_heating_is_off_2_weekday_rest_of_dwelling,
#         hours_heating_is_off_1_weekend_rest_of_dwelling,
#         hours_heating_is_off_2_weekend_rest_of_dwelling,
#         responsiveness_of_heating_system,
        
#         #mean internal temperature inputs
#         living_room_area,
#         temperature_adjustment_table_4e,
        
#         #space heating requirement inputs
        
#         #energy requirements inputs
#         fraction_of_space_heat_secondary_system,
#         fraction_of_space_heat_from_main_system_2,
#         efficiency_of_main_space_heating_system_1,
#         efficiency_of_main_space_heating_system_2,
#         efficiency_of_secondary_space_heating_system,
#         cooling_system_energy_efficiency_ratio_table_10c,
#         water_heater_type,
#         efficiency_of_water_heater,
#         efficiency_of_water_heater_adjustment_table_4c,
#         space_cooling_requirement_monthly,
#         electricity_demand_mechanical_ventilation_fans_table_4f,
#         electricity_demand_warm_air_heating_systems_fans_table_4f,
#         electricity_demand_central_heating_pump_or_water_pump_table_4f,
#         electricity_demand_oil_boiler_pump_table_4f,
#         electricity_demand_boiler_flue_fan_table_4f,
#         electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f,
#         electricity_demand_pump_for_solar_water_heating_table_4f,
#         electricity_demand_pump_for_storage_WWHRS_Table_G3,
#         electricity_generated_by_PV_Appendix_M,
#         electricity_generated_by_wind_turbine_appendix_M,
#         electricity_used_or_generated_by_micro_CHP_appendix_N,
#         electricity_generated_by_hydro_electric_generator_appendix_M,
#         appendix_Q_energy_saved,
#         appendix_Q_energy_used,
        
#         #fuel cost inputs
#         space_heating_fuel_price_main_system_1,
#         space_heating_fuel_price_main_system_2,
#         space_heating_fuel_price_secondary,
#         water_heating_high_rate_fraction_table_13,
#         water_heating_low_rate_fraction_table_13,
#         high_rate_fuel_price,
#         low_rate_fuel_price,
#         water_heating_fuel_price_other,
#         space_cooling_fuel_used,
#         space_cooling_fuel_price,
#         electricity_for_pumps_fans_electric_keep_hot,
#         fuel_price_for_pumps_fans_electric_keep_hot,
#         fuel_price_for_lighting,
#         additional_standing_charges_table_12,
#         energy_saving_generation_technologies,
#         energy_saving_generation_technologies_fuel_price,
#         appendix_Q_energy_used_fuel_price,
#         appendix_Q_energy_saved_fuel_price,
        
#         #Sap rating inputs
#         energy_cost_deflator,
        
#         #CO2 emissions inputs
#         space_heating_fuel_emission_factor_main_system_1,
#         space_heating_fuel_emission_factor_main_system_2,
#         space_heating_fuel_emission_factor_secondary,
#         water_heating_fuel_emission_factor,
#         space_cooling_fuel_emission_factor,
#         fuel_emission_factor_for_pumps_fans_electric_keep_hot,
#         fuel_emission_factor_for_lighting,
#         energy_saving_generation_technologies_fuel_emission_factor,
#         appendix_Q_energy_used_fuel_emission_factor,
#         appendix_Q_energy_saved_fuel_emission_factor
#         ):
    
#     """This method runs the complete set of calculations for the SAP2012 worksheet.
    
#     Using the supplied parameters, each of the individual SAP calculation
#     sections are run in turn. 
    
#     In some cases, an output from one section is used as an input to a later section.
    
#     The SAP sections run are as the following functions:
        
#     - `overall_dwelling_dimensions` (Section 1)
#     - `ventilation_rates` (Section 2)
#     - `heat_losses_and_heat_loss_parameter` (Section 3)
#     - `water_heating_requirement` (Section 4)
#     - `Internal_gains_appendix_L` 
#     - `internal_gains` (Section 5)
#     - `Solar_gains_appendix_U3`
#     - `solar_gains` (Section 6)
#     - `Utilisation_factor_for_heating`
#     - `Temperature_reduction`
#     - `Heating_requirement`
#     - `mean_internal_temperature` (Section 7)
#     - `Utilisation_factor_for_heating_whole_house`
#     - `space_heating_requirement` (Section 8)
#     - `energy_requirements` (Section 9)
#     - `fuel_costs` (Section 10)
#     - `SAP_rating` (Section 11)
#     - `CO2_emissions` (Section 12)
    
#     :returns: A tuple with the results of all the calculation sections.
#     :rtype: tuple
    
#     """
    
#     # overall_dwelling_dimensions calculations
#     result=overall_dwelling_dimensions(
#         area,
#         average_storey_height
#         )
    
#     volume,total_floor_area,dwelling_volume=result
    
    
#     # ventilation_rates calculations
#     result=ventilation_rates(
#         number_of_chimneys_main_heating,
#         number_of_chimneys_secondary_heating,
#         number_of_chimneys_other,
#         number_of_open_flues_main_heating,
#         number_of_open_flues_secondary_heating,
#         number_of_open_flues_other,
#         number_of_intermittant_fans_total,
#         number_of_passive_vents_total,
#         number_of_flueless_gas_fires_total,
#         dwelling_volume,
#         air_permeability_value_q50,
#         number_of_storeys_in_the_dwelling,
#         structural_infiltration,
#         suspended_wooden_ground_floor_infiltration,
#         no_draft_lobby_infiltration,
#         percentage_of_windows_and_doors_draught_proofed,
#         number_of_sides_on_which_dwelling_is_sheltered,
#         monthly_average_wind_speed,
#         applicable_case,
#         mechanical_ventilation_air_change_rate_through_system,
#         exhaust_air_heat_pump_using_Appendix_N,
#         mechanical_ventilation_throughput_factor,
#         efficiency_allowing_for_in_use_factor
#         )
    
#     (number_of_chimneys_total,
#      number_of_chimneys_m3_per_hour,
#      number_of_open_flues_total,
#      number_of_open_flues_m3_per_hour,
#      number_of_intermittant_fans_m3_per_hour,
#      number_of_passive_vents_m3_per_hour,
#      number_of_flueless_gas_fires_m3_per_hour,
#      infiltration_due_to_chimneys_flues_fans_PSVs,
#      additional_infiltration,
#      window_infiltration,
#      infiltration_rate,
#      infiltration_rate2,
#      shelter_factor,
#      infiltration_rate_incorporating_shelter_factor,
#      wind_factor,
#      adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed,
#      exhaust_air_heat_pump_air_change_rate_through_system,
#      effective_air_change_rate) = result
    
     
#     # heat_losses_and_heat_loss_parameter calculations
#     result=heat_losses_and_heat_loss_parameter(
#         solid_door_net_area,
#         solid_door_u_value,
#         semi_glazed_door_net_area,
#         semi_glazed_door_u_value,
#         window_net_area,
#         window_u_value,
#         roof_window_net_area,
#         roof_window_u_value,
#         basement_floor_net_area,
#         basement_floor_u_value,
#         basement_floor_heat_capacity,
#         ground_floor_net_area,
#         ground_floor_u_value,
#         ground_floor_heat_capacity,
#         exposed_floor_net_area,
#         exposed_floor_u_value,
#         exposed_floor_heat_capacity,
#         basement_wall_gross_area,
#         basement_wall_opening,
#         basement_wall_u_value,
#         basement_wall_heat_capacity,
#         external_wall_gross_area,
#         external_wall_opening,
#         external_wall_u_value,
#         external_wall_heat_capacity,
#         roof_gross_area,
#         roof_opening,
#         roof_u_value,
#         roof_heat_capacity,
#         party_wall_net_area,
#         party_wall_u_value,
#         party_wall_heat_capacity,
#         party_floor_net_area,
#         party_floor_heat_capacity,
#         party_ceiling_net_area,
#         party_ceiling_heat_capacity,
#         internal_wall_net_area,
#         internal_wall_heat_capacity,
#         internal_floor_net_area,
#         internal_floor_heat_capacity,
#         internal_ceiling_net_area,
#         internal_ceiling_heat_capacity,
#         total_floor_area,
#         thermal_bridges_appendix_k,
#         effective_air_change_rate,
#         dwelling_volume
#         )     
    
#     (solid_floor_UA,
#      semi_glazed_door_UA,
#      window_UA,
#      roof_window_UA,
#      basement_floor_UA,
#      basement_floor_Ak,
#      ground_floor_UA,
#      ground_floor_Ak,
#      exposed_floor_UA,
#      exposed_floor_Ak,
#      basement_wall_net_area,
#      basement_wall_UA,
#      basement_wall_Ak,
#      external_wall_net_area,
#      external_wall_UA,
#      external_wall_Ak,
#      roof_net_area,
#      roof_UA,
#      roof_Ak,
#      total_area_of_external_elements,
#      party_wall_UA,
#      party_wall_Ak,
#      party_floor_Ak,
#      party_ceiling_Ak,
#      internal_wall_Ak,
#      internal_floor_Ak,
#      internal_ceiling_Ak,
#      fabric_heat_loss,
#      heat_capacity,
#      thermal_mass_parameter,
#      thermal_bridges,
#      total_fabric_heat_loss,
#      ventilation_heat_loss_calculated_monthly,
#      heat_transfer_coefficient,
#      average_heat_transfer_coefficient,
#      heat_loss_parameter,
#      average_heat_loss_parameter) = result
     
     
     
#     # Water heating requirement calculations 
#     result = water_heating_requirement(
#         assumed_occupancy,
#         V_dm_table_1c,
#         days_in_month,
#         T_table_1d,
#         water_storage_loss_manufacturer,
#         temperature_factor_table_2b,
#         storage_volume_litres,
#         hot_water_storage_loss_table_2,
#         volume_factor_table_2a,
#         Vs_appendix_G3,
#         solar_storage_WWHRS_factor,
#         primary_circuit_loss_table_3,
#         combi_loss_table_3,
#         solar_DHW_input_appendix_G
#         )
    
#     (annual_hot_water_usage_litres_per_day,
#      hot_water_usage_in_litres_per_day_monthly,
#      energy_content_of_water_used,
#      distribution_loss,
#      energy_lost_from_water_storage,
#      water_storage_loss_monthly,
#      total_heat_required_for_water_heating,
#      output_from_water_heater_monthly,
#      heat_gains_from_water_heating_monthly) = result
     
     
#     #Appendix L calculations for internal gains
#     result= Internal_gains_appendix_L(
#         total_floor_area,
#         assumed_occupancy,
#         number_of_low_energy_light_bulbs,
#         total_number_of_light_bulbs,
#         frame_factor,
#         window_area,
#         light_access_factor_table_6d,
#         light_transmittance_factor_table_6d,
#         month_number,
#         days_in_month,
#         heat_gains_from_water_heating_monthly) 
    
#     (G_L,
#      C_1,
#      C_2,
#      E_B,
#      initial_annual_lighting_demand,
#      monthly_lighting_demand,
#      annual_lighting_demand,
#      lighting_gains,
#      initial_annual_electrical_appliance_demand,
#      monthly_electrical_appliance_demand,
#      annual_electrical_appliance_demand,
#      appliances_gains,
#      cooking_gains,
#      losses,
#      water_heating_gains,
#      metabolic_gains) = result
     
#     #Internal gains inputs
#     result = internal_gains(
#         metabolic_gains,
#         lighting_gains,
#         appliances_gains,
#         cooking_gains,
#         pumps_and_fans_gains,
#         losses,
#         water_heating_gains
#         )
    
#     (total_internal_gains) = result
    
#     #solar gains appendix U calculations
#     result = Solar_gains_appendix_U3(
#         solar_radiation_horizontal_plane_monthly_table_U3,
#         solar_declination_monthly_table_U3,
#         location_latitude_table_U4,
#         p_tilt,
#         )
#     (solar_flux_north,
#      solar_flux_north_east,
#      solar_flux_east,
#      solar_flux_south_east,
#      solar_flux_south,
#      solar_flux_south_west,
#      solar_flux_west,
#      solar_flux_north_west,) = result
    
#     # Solar gains calculations
#     result = solar_gains(
#         access_factor_table_6d_north,
#         access_factor_table_6d_north_east,
#         access_factor_table_6d_east,
#         access_factor_table_6d_south_east,
#         access_factor_table_6d_south,
#         access_factor_table_6d_south_west,
#         access_factor_table_6d_west,
#         access_factor_table_6d_north_west,
#         access_factor_table_6d_roof_windows,
#         area_north,
#         area_north_east,
#         area_east,
#         area_south_east,
#         area_south,
#         area_south_west,
#         area_west,
#         area_north_west,
#         area_roof_windows,
#         solar_flux_north,
#         solar_flux_north_east,
#         solar_flux_east,
#         solar_flux_south_east,
#         solar_flux_south,
#         solar_flux_south_west,
#         solar_flux_west,
#         solar_flux_north_west,
#         solar_flux_roof_windows,
#         g_table_6b_north,
#         g_table_6b_north_east,
#         g_table_6b_east,
#         g_table_6b_south_east,
#         g_table_6b_south,
#         g_table_6b_south_west,
#         g_table_6b_west,
#         g_table_6b_north_west,
#         g_table_6b_roof_windows,
#         FF_table_6b_north,
#         FF_table_6b_north_east,
#         FF_table_6b_east,
#         FF_table_6b_south_east,
#         FF_table_6b_south,
#         FF_table_6b_south_west,
#         FF_table_6b_west,
#         FF_table_6b_north_west,
#         FF_table_6b_roof_windows,
#         total_internal_gains
#         )
    
#     (gains_north,
#      gains_north_east,
#      gains_east,
#      gains_south_east,
#      gains_south,
#      gains_south_west,
#      gains_west,
#      gains_north_west,
#      gains_roof_windows,
#      solar_gains_watts,
#      total_internal_and_solar_gains) = result
     
#     #Utilisation factor for heating table 9a
#     result = Utilisation_factor_for_heating(
#         heat_transfer_coefficient,
#         total_internal_and_solar_gains,
#         temperature_during_heating_living_room,
#         heating_controls,
#         monthly_external_temperature_table_U1,
#         thermal_mass_parameter,
#         heat_loss_parameter
#         )
    
#     (time_constant,
#      a,
#      heat_loss_rate_living_room,
#      y_living_room,
#      utilisation_factor_for_heating_living_room,
#      temperature_during_heating_rest_of_dwelling,
#      heat_loss_rate_rest_of_dwelling,
#      y_rest_of_dwelling,
#      utilisation_factor_for_heating_rest_of_dwelling
#      )=result
     
#     #Internal temperature reduction when heating is off
#     result = Temperature_reduction(
#         time_constant,
#         hours_heating_is_off_1_weekday_living_room,
#         hours_heating_is_off_2_weekday_living_room,
#         hours_heating_is_off_1_weekend_living_room,
#         hours_heating_is_off_2_weekend_living_room,
#         hours_heating_is_off_1_weekday_rest_of_dwelling,
#         hours_heating_is_off_2_weekday_rest_of_dwelling,
#         hours_heating_is_off_1_weekend_rest_of_dwelling,
#         hours_heating_is_off_2_weekend_rest_of_dwelling,
#         temperature_during_heating_living_room,
#         temperature_during_heating_rest_of_dwelling,
#         responsiveness_of_heating_system,
#         monthly_external_temperature_table_U1,
#         utilisation_factor_for_heating_living_room,
#         utilisation_factor_for_heating_rest_of_dwelling,
#         heat_transfer_coefficient,
#         total_internal_and_solar_gains
#         )

#     (t_c,
#      internal_temperature_without_heating_living_room,
#      internal_temperature_without_heating_rest_of_dwelling,
#      temperature_reduction_when_heating_is_off_1_weekday_living_room,
#      temperature_reduction_when_heating_is_off_2_weekday_living_room,
#      temperature_reduction_when_heating_is_off_1_weekend_living_room,
#      temperature_reduction_when_heating_is_off_2_weekend_living_room,
#      temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling,
#      temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling,
#      temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling,
#      temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling)=result
     
#     #Heating requirement table 9c
#     result = Heating_requirement(
#         temperature_reduction_when_heating_is_off_1_weekday_living_room,
#         temperature_reduction_when_heating_is_off_2_weekday_living_room,
#         temperature_reduction_when_heating_is_off_1_weekend_living_room,
#         temperature_reduction_when_heating_is_off_2_weekend_living_room,
#         temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling,
#         temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling,
#         temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling,
#         temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling,
#         temperature_during_heating_living_room,
#         temperature_during_heating_rest_of_dwelling,
#         temperature_adjustment_table_4e
#         )

#     (T_weekday_living_room,
#      T_weekend_living_room,
#      mean_internal_temperature_living_room_T1_Table_9c,
#      T_weekday_rest_of_dwelling,
#      T_weekend_rest_of_dwelling,
#      mean_internal_temperature_rest_of_dwelling_T2_table_9c)=result
    
#     # Mean internal temperature calculations
#     result = mean_internal_temperature(
#         mean_internal_temperature_living_room_T1_Table_9c,
#         mean_internal_temperature_rest_of_dwelling_T2_table_9c,
#         living_room_area,
#         total_floor_area,
#         temperature_adjustment_table_4e
#         )
    
#     (living_area_fraction,
#      mean_internal_temp_whole_dwelling) = result
     
     
#     # Utilisation factor for heating whole house
#     result = Utilisation_factor_for_heating_whole_house(
#         heat_transfer_coefficient,
#         total_internal_and_solar_gains,
#         mean_internal_temp_whole_dwelling,
#         monthly_external_temperature_table_U1,
#         thermal_mass_parameter,
#         heat_loss_parameter
#         )
    
#     (time_constant_whole_house,
#      a_whole_house,
#      heat_loss_rate_whole_house,
#      y_whole_house,
#      utilisation_factor_for_heating_whole_house)=result
     
#     # Space heating requirement calculations
#     result = space_heating_requirement(
#         utilisation_factor_for_heating_whole_house,
#         total_internal_and_solar_gains,
#         monthly_external_temperature_table_U1,
#         mean_internal_temp_whole_dwelling,
#         heat_transfer_coefficient,
#         days_in_month,
#         total_floor_area
#         )
    
#     (useful_gains,
#      heat_loss_rate_for_mean_internal_temperature,
#      space_heating_requirement_monthly,
#      space_heating_requirement_yearly,
#      space_heating_requirement_yearly_per_m2) = result
     
#     # Energy requirements calculations 
#     result = energy_requirements(
#         fraction_of_space_heat_secondary_system,
#         fraction_of_space_heat_from_main_system_2,
#         efficiency_of_main_space_heating_system_1,
#         efficiency_of_main_space_heating_system_2,
#         efficiency_of_secondary_space_heating_system,
#         cooling_system_energy_efficiency_ratio_table_10c,
#         space_heating_requirement_monthly,
#         output_from_water_heater_monthly,
#         water_heater_type,
#         efficiency_of_water_heater,
#         efficiency_of_water_heater_adjustment_table_4c,
#         space_cooling_requirement_monthly,
#         electricity_demand_mechanical_ventilation_fans_table_4f,
#         electricity_demand_warm_air_heating_systems_fans_table_4f,
#         electricity_demand_central_heating_pump_or_water_pump_table_4f,
#         electricity_demand_oil_boiler_pump_table_4f,
#         electricity_demand_boiler_flue_fan_table_4f,
#         electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f,
#         electricity_demand_pump_for_solar_water_heating_table_4f,
#         electricity_demand_pump_for_storage_WWHRS_Table_G3,
#         annual_lighting_demand,
#         electricity_generated_by_PV_Appendix_M,
#         electricity_generated_by_wind_turbine_appendix_M,
#         electricity_used_or_generated_by_micro_CHP_appendix_N,
#         electricity_generated_by_hydro_electric_generator_appendix_M,
#         appendix_Q_energy_saved,
#         appendix_Q_energy_used
#         )
    
#     (fraction_of_space_heat_from_main_systems,
#      fraction_of_total_space_heat_from_main_system_1,
#      fraction_of_total_space_heat_from_main_system_2,
#      space_heating_fuel_main_system_1,
#      space_heating_fuel_main_system_2,
#      space_heating_fuel_secondary_system,
#      efficiency_of_water_heater_table_4a,
#      fuel_for_water_heating_monthly,
#      space_cooling_fuel_monthly,
#      space_heating_fuel_used_main_system_1,
#      space_heating_fuel_used_main_system_2,
#      space_heating_fuel_used_secondary,
#      water_fuel_used,
#      space_cooling_fuel_used,
#      electricity_for_pumps_fans_electric_keep_hot,
#      energy_saving_generation_technologies_total,
#      appendix_Q_energy_total,
#      energy_for_lighting,
#      total_energy_used) = result
     
#      # Fuel cost calculations
#     result = fuel_costs(
#         space_heating_fuel_used_main_system_1,
#         space_heating_fuel_used_main_system_2,
#         space_heating_fuel_used_secondary,
#         space_heating_fuel_price_main_system_1,
#         space_heating_fuel_price_main_system_2,
#         space_heating_fuel_price_secondary,
#         water_heating_high_rate_fraction_table_13,
#         water_heating_low_rate_fraction_table_13,
#         high_rate_fuel_price,
#         low_rate_fuel_price,
#         water_fuel_used,
#         water_heating_fuel_price_other,
#         space_cooling_fuel_used,
#         space_cooling_fuel_price,
#         electricity_for_pumps_fans_electric_keep_hot,
#         fuel_price_for_pumps_fans_electric_keep_hot,
#         energy_for_lighting,
#         fuel_price_for_lighting,
#         additional_standing_charges_table_12,
#         energy_saving_generation_technologies,
#         energy_saving_generation_technologies_fuel_price,
#         appendix_Q_energy_used,
#         appendix_Q_energy_used_fuel_price,
#         appendix_Q_energy_saved,
#         appendix_Q_energy_saved_fuel_price
#         )
    
#     (space_heating_main_system_1_fuel_cost,
#      space_heating_main_system_2_fuel_cost,
#      space_heating_secondary_fuel_cost,
#      water_heating_high_rate_fuel_cost,
#      water_heating_low_rate_fuel_cost,
#      water_heating_cost_other,
#      space_cooling_cost,
#      pumps_fan_keep_hot_cost,
#      lighting_cost,
#      appendix_Q_fuel_cost,
#      energy_saving_total_fuel_cost,
#      additional_standing_charges_table_12,
#      total_fuel_cost) = result
     
#     # SAP rating calculations
#     result = SAP_rating(
#         energy_cost_deflator,
#         total_fuel_cost,
#         total_floor_area
#         )
     
#     (SAP_rating_value) = result
    
#     # CO2 emissions calculations
#     result = CO2_emissions(
#         space_heating_fuel_used_main_system_1,
#         space_heating_fuel_used_main_system_2,
#         space_heating_fuel_used_secondary,
#         space_heating_fuel_emission_factor_main_system_1,
#         space_heating_fuel_emission_factor_main_system_2,
#         space_heating_fuel_emission_factor_secondary,
#         water_fuel_used,
#         water_heating_fuel_emission_factor,
#         space_cooling_fuel_used,
#         space_cooling_fuel_emission_factor,
#         electricity_for_pumps_fans_electric_keep_hot,
#         fuel_emission_factor_for_pumps_fans_electric_keep_hot,
#         energy_for_lighting,
#         fuel_emission_factor_for_lighting,
#         energy_saving_generation_technologies,
#         energy_saving_generation_technologies_fuel_emission_factor,
#         appendix_Q_energy_used,
#         appendix_Q_energy_used_fuel_emission_factor,
#         appendix_Q_energy_saved,
#         appendix_Q_energy_saved_fuel_emission_factor,
#         total_floor_area
#         )
    
#     (space_heating_main_system_1_emissions,
#      space_heating_main_system_2_emissions,
#      space_heating_secondary_emissions,
#      water_used_emissions,
#      space_cooling_used_emissions,
#      pumps_fans_electric_keep_hot_emissions,
#      lighting_emissions,
#      appendix_Q_used_emissions,
#      appendix_Q_saved_emissions,
#      energy_saving_generation_technologies_emissions,
#      space_and_water_heating_emissions,
#      appendix_Q_total_used_emissions,
#      appendix_Q_total_saved_emissions,
#      energy_saving_generation_technologies_total_emissions,
#      total_CO2_emissions_yearly,
#      dwelling_CO2_emission_rate,
#      CF,
#      EI_rating) = result
    
#     return (
#         # overall_dwelling_dimensions results
#         volume,
#         total_floor_area,
#         dwelling_volume,
        
#         # ventilation_rates results
#         number_of_chimneys_total,
#         number_of_chimneys_m3_per_hour,
#         number_of_open_flues_total,
#         number_of_open_flues_m3_per_hour,
#         number_of_intermittant_fans_m3_per_hour,
#         number_of_passive_vents_m3_per_hour,
#         number_of_flueless_gas_fires_m3_per_hour,
#         infiltration_due_to_chimneys_flues_fans_PSVs,
#         additional_infiltration,
#         window_infiltration,
#         infiltration_rate,
#         infiltration_rate2,
#         shelter_factor,
#         infiltration_rate_incorporating_shelter_factor,
#         wind_factor,
#         adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed,
#         exhaust_air_heat_pump_air_change_rate_through_system,
#         effective_air_change_rate,
        
#         # heat_losses_and_heat_loss_parameter results
#         solid_floor_UA,
#         semi_glazed_door_UA,
#         window_UA,
#         roof_window_UA,
#         basement_floor_UA,
#         basement_floor_Ak,
#         ground_floor_UA,
#         ground_floor_Ak,
#         exposed_floor_UA,
#         exposed_floor_Ak,
#         basement_wall_net_area,
#         basement_wall_UA,
#         basement_wall_Ak,
#         external_wall_net_area,
#         external_wall_UA,
#         external_wall_Ak,
#         roof_net_area,
#         roof_UA,
#         roof_Ak,
#         total_area_of_external_elements,
#         party_wall_UA,
#         party_wall_Ak,
#         party_floor_Ak,
#         party_ceiling_Ak,
#         internal_wall_Ak,
#         internal_floor_Ak,
#         internal_ceiling_Ak,
#         fabric_heat_loss,
#         heat_capacity,
#         thermal_mass_parameter,
#         thermal_bridges,
#         total_fabric_heat_loss,
#         ventilation_heat_loss_calculated_monthly,
#         heat_transfer_coefficient,
#         average_heat_transfer_coefficient,
#         heat_loss_parameter,
#         average_heat_loss_parameter,
        
#         #water heating requirements results
#         annual_hot_water_usage_litres_per_day,
#         hot_water_usage_in_litres_per_day_monthly,
#         energy_content_of_water_used,
#         distribution_loss,
#         energy_lost_from_water_storage,
#         water_storage_loss_monthly,
#         total_heat_required_for_water_heating,
#         output_from_water_heater_monthly,
#         heat_gains_from_water_heating_monthly,
        
#         #internal gains results
#         G_L,
#         C_1,
#         C_2,
#         E_B,
#         initial_annual_lighting_demand,
#         monthly_lighting_demand,
#         annual_lighting_demand,
#         lighting_gains,
#         initial_annual_electrical_appliance_demand,
#         monthly_electrical_appliance_demand,
#         annual_electrical_appliance_demand,
#         appliances_gains,
#         cooking_gains,
#         losses,
#         water_heating_gains,
#         metabolic_gains,
#         total_internal_gains,
        
#         #solar gains appendix U results
#         solar_flux_north,
#         solar_flux_north_east,
#         solar_flux_east,
#         solar_flux_south_east,
#         solar_flux_south,
#         solar_flux_south_west,
#         solar_flux_west,
#         solar_flux_north_west,
        
#         #solar gains results
#         gains_north,
#         gains_north_east,
#         gains_east,
#         gains_south_east,
#         gains_south,
#         gains_south_west,
#         gains_west,
#         gains_north_west,
#         gains_roof_windows,
#         solar_gains_watts,
#         total_internal_and_solar_gains,
        
#         #utilisation factor for heating outputs
#         time_constant,
#             a,
#             heat_loss_rate_living_room,
#             y_living_room,
#             utilisation_factor_for_heating_living_room,
#             temperature_during_heating_rest_of_dwelling,
#             heat_loss_rate_rest_of_dwelling,
#             y_rest_of_dwelling,
#             utilisation_factor_for_heating_rest_of_dwelling,
        
#         #temperature reduction outputs
#         t_c,
#         internal_temperature_without_heating_living_room,
#         internal_temperature_without_heating_rest_of_dwelling,
#         temperature_reduction_when_heating_is_off_1_weekday_living_room,
#         temperature_reduction_when_heating_is_off_2_weekday_living_room,
#         temperature_reduction_when_heating_is_off_1_weekend_living_room,
#         temperature_reduction_when_heating_is_off_2_weekend_living_room,
#         temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling,
#         temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling,
#         temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling,
#         temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling,
        
#         #heating requirement outputs
#         T_weekday_living_room,
#         T_weekend_living_room,
#         mean_internal_temperature_living_room_T1_Table_9c,
#         T_weekday_rest_of_dwelling,
#         T_weekend_rest_of_dwelling,
#         mean_internal_temperature_rest_of_dwelling_T2_table_9c,
        
#         #mean internal temperature results
#         living_area_fraction,
#         mean_internal_temp_whole_dwelling,
        
#         #utilisation factor for heating whole house outputs
#         time_constant_whole_house,
#         a_whole_house,
#         heat_loss_rate_whole_house,
#         y_whole_house,
#         utilisation_factor_for_heating_whole_house,
        
#         #space heating requirements results
#         useful_gains,
#         heat_loss_rate_for_mean_internal_temperature,
#         space_heating_requirement_monthly,
#         space_heating_requirement_yearly,
#         space_heating_requirement_yearly_per_m2,
        
#         #energy requirements results
#         fraction_of_space_heat_from_main_systems,
#            fraction_of_total_space_heat_from_main_system_1,
#            fraction_of_total_space_heat_from_main_system_2,
#            space_heating_fuel_main_system_1,
#            space_heating_fuel_main_system_2,
#            space_heating_fuel_secondary_system,
#            efficiency_of_water_heater_table_4a,
#            fuel_for_water_heating_monthly,
#            space_cooling_fuel_monthly,
#            space_heating_fuel_used_main_system_1,
#            space_heating_fuel_used_main_system_2,
#            space_heating_fuel_used_secondary,
#            water_fuel_used,
#            space_cooling_fuel_used,
#            electricity_for_pumps_fans_electric_keep_hot,
#            energy_saving_generation_technologies_total,
#            appendix_Q_energy_total,
#            energy_for_lighting,
#            total_energy_used,
        
#         #fuel cost results
#         space_heating_main_system_1_fuel_cost,
#         space_heating_main_system_2_fuel_cost,
#         space_heating_secondary_fuel_cost,
#         water_heating_high_rate_fuel_cost,
#         water_heating_low_rate_fuel_cost,
#         water_heating_cost_other,
#         space_cooling_cost,
#         pumps_fan_keep_hot_cost,
#         lighting_cost,
#         appendix_Q_fuel_cost,
#         energy_saving_total_fuel_cost,
#         additional_standing_charges_table_12,
#         total_fuel_cost,
        
#         #SAP rating result
#         SAP_rating_value,
        
#         #CO2 emissions result
#         space_heating_main_system_1_emissions,
#         space_heating_main_system_2_emissions,
#         space_heating_secondary_emissions,
#         water_used_emissions,
#         space_cooling_used_emissions,
#         pumps_fans_electric_keep_hot_emissions,
#         lighting_emissions,
#         appendix_Q_used_emissions,
#         appendix_Q_saved_emissions,
#         energy_saving_generation_technologies_emissions,
#         space_and_water_heating_emissions,
#         appendix_Q_total_used_emissions,
#         appendix_Q_total_saved_emissions,
#         energy_saving_generation_technologies_total_emissions,
#         total_CO2_emissions_yearly,
#         dwelling_CO2_emission_rate,
#         CF,
#         EI_rating
#         )
    
    