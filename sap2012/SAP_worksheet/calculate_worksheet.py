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
#from sap2012.tables.temperature_reduction_when_heating_is_off import Temperature_reduction
#from sap2012.tables.Heating_Requirement_table_9c import Heating_requirement
#from sap2012.tables.Utilisation_factor_for_heating_whole_house import Utilisation_factor_for_heating_whole_house 


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
    - `utilisation_factor_for_heating_whole_house`
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
    
    
    return result


def calculate_worksheet_old(
        # overall_dwelling_dimensions inputs
        area,
        average_storey_height,    
    
        # ventilation_rates inputs
        number_of_chimneys_main_heating,
        number_of_chimneys_secondary_heating,
        number_of_chimneys_other,
        number_of_open_flues_main_heating,
        number_of_open_flues_secondary_heating,
        number_of_open_flues_other,
        number_of_intermittant_fans_total,
        number_of_passive_vents_total,
        number_of_flueless_gas_fires_total,
        air_permeability_value_q50,
        number_of_storeys_in_the_dwelling,
        structural_infiltration,
        suspended_wooden_ground_floor_infiltration,
        no_draft_lobby_infiltration,
        percentage_of_windows_and_doors_draught_proofed,
        number_of_sides_on_which_dwelling_is_sheltered,
        monthly_average_wind_speed,
        applicable_case,
        mechanical_ventilation_air_change_rate_through_system,
        exhaust_air_heat_pump_using_Appendix_N,
        mechanical_ventilation_throughput_factor,
        efficiency_allowing_for_in_use_factor,
        
        # heat_losses_and_heat_loss_parameter inputs
        solid_door_net_area,
        solid_door_u_value,
        semi_glazed_door_net_area,
        semi_glazed_door_u_value,
        window_net_area,
        window_u_value,
        roof_window_net_area,
        roof_window_u_value,
        basement_floor_net_area,
        basement_floor_u_value,
        basement_floor_heat_capacity,
        ground_floor_net_area,
        ground_floor_u_value,
        ground_floor_heat_capacity,
        exposed_floor_net_area,
        exposed_floor_u_value,
        exposed_floor_heat_capacity,
        basement_wall_gross_area,
        basement_wall_opening,
        basement_wall_u_value,
        basement_wall_heat_capacity,
        external_wall_gross_area,
        external_wall_opening,
        external_wall_u_value,
        external_wall_heat_capacity,
        roof_gross_area,
        roof_opening,
        roof_u_value,
        roof_heat_capacity,
        party_wall_net_area,
        party_wall_u_value,
        party_wall_heat_capacity,
        party_floor_net_area,
        party_floor_heat_capacity,
        party_ceiling_net_area,
        party_ceiling_heat_capacity,
        internal_wall_net_area,
        internal_wall_heat_capacity,
        internal_floor_net_area,
        internal_floor_heat_capacity,
        internal_ceiling_net_area,
        internal_ceiling_heat_capacity,
        thermal_bridges_appendix_k,
        
        #water heating requirement inputs
        assumed_occupancy,
        V_dm_table_1c,
        days_in_month,
        T_table_1d,
        water_storage_loss_manufacturer,
        temperature_factor_table_2b,
        storage_volume_litres,
        hot_water_storage_loss_table_2,
        volume_factor_table_2a,
        Vs_appendix_G3,
        solar_storage_WWHRS_factor,
        primary_circuit_loss_table_3,
        combi_loss_table_3,
        solar_DHW_input_appendix_G,
        
        #internal gains appendix L inputs
        number_of_low_energy_light_bulbs,
        total_number_of_light_bulbs,
        frame_factor,
        window_area,
        light_access_factor_table_6d,
        light_transmittance_factor_table_6d,
        month_number,
        
        #internal gains inputs
        pumps_and_fans_gains,
        
        #solar gains appendix U inputs
        solar_radiation_horizontal_plane_monthly_table_U3,
        solar_declination_monthly_table_U3,
        location_latitude_table_U4,
        p_tilt,
        
        #solar gains inputs
        access_factor_table_6d_north,
        access_factor_table_6d_north_east,
        access_factor_table_6d_east,
        access_factor_table_6d_south_east,
        access_factor_table_6d_south,
        access_factor_table_6d_south_west,
        access_factor_table_6d_west,
        access_factor_table_6d_north_west,
        access_factor_table_6d_roof_windows,
        area_north,
        area_north_east,
        area_east,
        area_south_east,
        area_south,
        area_south_west,
        area_west,
        area_north_west,
        area_roof_windows,
        solar_flux_roof_windows,
        g_table_6b_north,
        g_table_6b_north_east,
        g_table_6b_east,
        g_table_6b_south_east,
        g_table_6b_south,
        g_table_6b_south_west,
        g_table_6b_west,
        g_table_6b_north_west,
        g_table_6b_roof_windows,
        FF_table_6b_north,
        FF_table_6b_north_east,
        FF_table_6b_east,
        FF_table_6b_south_east,
        FF_table_6b_south,
        FF_table_6b_south_west,
        FF_table_6b_west,
        FF_table_6b_north_west,
        FF_table_6b_roof_windows,
        
        #utilisation factor inputs
        temperature_during_heating_living_room,
        heating_controls,
        monthly_external_temperature_table_U1,
        
        #temperature reduction inputs
        hours_heating_is_off_1_weekday_living_room,
        hours_heating_is_off_2_weekday_living_room,
        hours_heating_is_off_1_weekend_living_room,
        hours_heating_is_off_2_weekend_living_room,
        hours_heating_is_off_1_weekday_rest_of_dwelling,
        hours_heating_is_off_2_weekday_rest_of_dwelling,
        hours_heating_is_off_1_weekend_rest_of_dwelling,
        hours_heating_is_off_2_weekend_rest_of_dwelling,
        responsiveness_of_heating_system,
        
        #mean internal temperature inputs
        living_room_area,
        temperature_adjustment_table_4e,
        
        #space heating requirement inputs
        
        #energy requirements inputs
        fraction_of_space_heat_secondary_system,
        fraction_of_space_heat_from_main_system_2,
        efficiency_of_main_space_heating_system_1,
        efficiency_of_main_space_heating_system_2,
        efficiency_of_secondary_space_heating_system,
        cooling_system_energy_efficiency_ratio_table_10c,
        water_heater_type,
        efficiency_of_water_heater,
        efficiency_of_water_heater_adjustment_table_4c,
        space_cooling_requirement_monthly,
        electricity_demand_mechanical_ventilation_fans_table_4f,
        electricity_demand_warm_air_heating_systems_fans_table_4f,
        electricity_demand_central_heating_pump_or_water_pump_table_4f,
        electricity_demand_oil_boiler_pump_table_4f,
        electricity_demand_boiler_flue_fan_table_4f,
        electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f,
        electricity_demand_pump_for_solar_water_heating_table_4f,
        electricity_demand_pump_for_storage_WWHRS_Table_G3,
        electricity_generated_by_PV_Appendix_M,
        electricity_generated_by_wind_turbine_appendix_M,
        electricity_used_or_generated_by_micro_CHP_appendix_N,
        electricity_generated_by_hydro_electric_generator_appendix_M,
        appendix_Q_energy_saved,
        appendix_Q_energy_used,
        
        #fuel cost inputs
        space_heating_fuel_price_main_system_1,
        space_heating_fuel_price_main_system_2,
        space_heating_fuel_price_secondary,
        water_heating_high_rate_fraction_table_13,
        water_heating_low_rate_fraction_table_13,
        high_rate_fuel_price,
        low_rate_fuel_price,
        water_heating_fuel_price_other,
        space_cooling_fuel_used,
        space_cooling_fuel_price,
        electricity_for_pumps_fans_electric_keep_hot,
        fuel_price_for_pumps_fans_electric_keep_hot,
        fuel_price_for_lighting,
        additional_standing_charges_table_12,
        energy_saving_generation_technologies,
        energy_saving_generation_technologies_fuel_price,
        appendix_Q_energy_used_fuel_price,
        appendix_Q_energy_saved_fuel_price,
        
        #Sap rating inputs
        energy_cost_deflator,
        
        #CO2 emissions inputs
        space_heating_fuel_emission_factor_main_system_1,
        space_heating_fuel_emission_factor_main_system_2,
        space_heating_fuel_emission_factor_secondary,
        water_heating_fuel_emission_factor,
        space_cooling_fuel_emission_factor,
        fuel_emission_factor_for_pumps_fans_electric_keep_hot,
        fuel_emission_factor_for_lighting,
        energy_saving_generation_technologies_fuel_emission_factor,
        appendix_Q_energy_used_fuel_emission_factor,
        appendix_Q_energy_saved_fuel_emission_factor
        ):
    
    """This method runs the complete set of calculations for the SAP2012 worksheet.
    
    Using the supplied parameters, each of the individual SAP calculation
    sections are run in turn. 
    
    In some cases, an output from one section is used as an input to a later section.
    
    The SAP sections run are as the following functions:
        
    - `overall_dwelling_dimensions` (Section 1)
    - `ventilation_rates` (Section 2)
    - `heat_losses_and_heat_loss_parameter` (Section 3)
    - `water_heating_requirement` (Section 4)
    - `Internal_gains_appendix_L` 
    - `internal_gains` (Section 5)
    - `Solar_gains_appendix_U3`
    - `solar_gains` (Section 6)
    - `Utilisation_factor_for_heating`
    - `Temperature_reduction`
    - `Heating_requirement`
    - `mean_internal_temperature` (Section 7)
    - `Utilisation_factor_for_heating_whole_house`
    - `space_heating_requirement` (Section 8)
    - `energy_requirements` (Section 9)
    - `fuel_costs` (Section 10)
    - `SAP_rating` (Section 11)
    - `CO2_emissions` (Section 12)
    
    :returns: A tuple with the results of all the calculation sections.
    :rtype: tuple
    
    """
    
    # overall_dwelling_dimensions calculations
    result=overall_dwelling_dimensions(
        area,
        average_storey_height
        )
    
    volume,total_floor_area,dwelling_volume=result
    
    
    # ventilation_rates calculations
    result=ventilation_rates(
        number_of_chimneys_main_heating,
        number_of_chimneys_secondary_heating,
        number_of_chimneys_other,
        number_of_open_flues_main_heating,
        number_of_open_flues_secondary_heating,
        number_of_open_flues_other,
        number_of_intermittant_fans_total,
        number_of_passive_vents_total,
        number_of_flueless_gas_fires_total,
        dwelling_volume,
        air_permeability_value_q50,
        number_of_storeys_in_the_dwelling,
        structural_infiltration,
        suspended_wooden_ground_floor_infiltration,
        no_draft_lobby_infiltration,
        percentage_of_windows_and_doors_draught_proofed,
        number_of_sides_on_which_dwelling_is_sheltered,
        monthly_average_wind_speed,
        applicable_case,
        mechanical_ventilation_air_change_rate_through_system,
        exhaust_air_heat_pump_using_Appendix_N,
        mechanical_ventilation_throughput_factor,
        efficiency_allowing_for_in_use_factor
        )
    
    (number_of_chimneys_total,
     number_of_chimneys_m3_per_hour,
     number_of_open_flues_total,
     number_of_open_flues_m3_per_hour,
     number_of_intermittant_fans_m3_per_hour,
     number_of_passive_vents_m3_per_hour,
     number_of_flueless_gas_fires_m3_per_hour,
     infiltration_due_to_chimneys_flues_fans_PSVs,
     additional_infiltration,
     window_infiltration,
     infiltration_rate,
     infiltration_rate2,
     shelter_factor,
     infiltration_rate_incorporating_shelter_factor,
     wind_factor,
     adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed,
     exhaust_air_heat_pump_air_change_rate_through_system,
     effective_air_change_rate) = result
    
     
    # heat_losses_and_heat_loss_parameter calculations
    result=heat_losses_and_heat_loss_parameter(
        solid_door_net_area,
        solid_door_u_value,
        semi_glazed_door_net_area,
        semi_glazed_door_u_value,
        window_net_area,
        window_u_value,
        roof_window_net_area,
        roof_window_u_value,
        basement_floor_net_area,
        basement_floor_u_value,
        basement_floor_heat_capacity,
        ground_floor_net_area,
        ground_floor_u_value,
        ground_floor_heat_capacity,
        exposed_floor_net_area,
        exposed_floor_u_value,
        exposed_floor_heat_capacity,
        basement_wall_gross_area,
        basement_wall_opening,
        basement_wall_u_value,
        basement_wall_heat_capacity,
        external_wall_gross_area,
        external_wall_opening,
        external_wall_u_value,
        external_wall_heat_capacity,
        roof_gross_area,
        roof_opening,
        roof_u_value,
        roof_heat_capacity,
        party_wall_net_area,
        party_wall_u_value,
        party_wall_heat_capacity,
        party_floor_net_area,
        party_floor_heat_capacity,
        party_ceiling_net_area,
        party_ceiling_heat_capacity,
        internal_wall_net_area,
        internal_wall_heat_capacity,
        internal_floor_net_area,
        internal_floor_heat_capacity,
        internal_ceiling_net_area,
        internal_ceiling_heat_capacity,
        total_floor_area,
        thermal_bridges_appendix_k,
        effective_air_change_rate,
        dwelling_volume
        )     
    
    (solid_floor_UA,
     semi_glazed_door_UA,
     window_UA,
     roof_window_UA,
     basement_floor_UA,
     basement_floor_Ak,
     ground_floor_UA,
     ground_floor_Ak,
     exposed_floor_UA,
     exposed_floor_Ak,
     basement_wall_net_area,
     basement_wall_UA,
     basement_wall_Ak,
     external_wall_net_area,
     external_wall_UA,
     external_wall_Ak,
     roof_net_area,
     roof_UA,
     roof_Ak,
     total_area_of_external_elements,
     party_wall_UA,
     party_wall_Ak,
     party_floor_Ak,
     party_ceiling_Ak,
     internal_wall_Ak,
     internal_floor_Ak,
     internal_ceiling_Ak,
     fabric_heat_loss,
     heat_capacity,
     thermal_mass_parameter,
     thermal_bridges,
     total_fabric_heat_loss,
     ventilation_heat_loss_calculated_monthly,
     heat_transfer_coefficient,
     average_heat_transfer_coefficient,
     heat_loss_parameter,
     average_heat_loss_parameter) = result
     
     
     
    # Water heating requirement calculations 
    result = water_heating_requirement(
        assumed_occupancy,
        V_dm_table_1c,
        days_in_month,
        T_table_1d,
        water_storage_loss_manufacturer,
        temperature_factor_table_2b,
        storage_volume_litres,
        hot_water_storage_loss_table_2,
        volume_factor_table_2a,
        Vs_appendix_G3,
        solar_storage_WWHRS_factor,
        primary_circuit_loss_table_3,
        combi_loss_table_3,
        solar_DHW_input_appendix_G
        )
    
    (annual_hot_water_usage_litres_per_day,
     hot_water_usage_in_litres_per_day_monthly,
     energy_content_of_water_used,
     distribution_loss,
     energy_lost_from_water_storage,
     water_storage_loss_monthly,
     total_heat_required_for_water_heating,
     output_from_water_heater_monthly,
     heat_gains_from_water_heating_monthly) = result
     
     
    #Appendix L calculations for internal gains
    result= Internal_gains_appendix_L(
        total_floor_area,
        assumed_occupancy,
        number_of_low_energy_light_bulbs,
        total_number_of_light_bulbs,
        frame_factor,
        window_area,
        light_access_factor_table_6d,
        light_transmittance_factor_table_6d,
        month_number,
        days_in_month,
        heat_gains_from_water_heating_monthly) 
    
    (G_L,
     C_1,
     C_2,
     E_B,
     initial_annual_lighting_demand,
     monthly_lighting_demand,
     annual_lighting_demand,
     lighting_gains,
     initial_annual_electrical_appliance_demand,
     monthly_electrical_appliance_demand,
     annual_electrical_appliance_demand,
     appliances_gains,
     cooking_gains,
     losses,
     water_heating_gains,
     metabolic_gains) = result
     
    #Internal gains inputs
    result = internal_gains(
        metabolic_gains,
        lighting_gains,
        appliances_gains,
        cooking_gains,
        pumps_and_fans_gains,
        losses,
        water_heating_gains
        )
    
    (total_internal_gains) = result
    
    #solar gains appendix U calculations
    result = Solar_gains_appendix_U3(
        solar_radiation_horizontal_plane_monthly_table_U3,
        solar_declination_monthly_table_U3,
        location_latitude_table_U4,
        p_tilt,
        )
    (solar_flux_north,
     solar_flux_north_east,
     solar_flux_east,
     solar_flux_south_east,
     solar_flux_south,
     solar_flux_south_west,
     solar_flux_west,
     solar_flux_north_west,) = result
    
    # Solar gains calculations
    result = solar_gains(
        access_factor_table_6d_north,
        access_factor_table_6d_north_east,
        access_factor_table_6d_east,
        access_factor_table_6d_south_east,
        access_factor_table_6d_south,
        access_factor_table_6d_south_west,
        access_factor_table_6d_west,
        access_factor_table_6d_north_west,
        access_factor_table_6d_roof_windows,
        area_north,
        area_north_east,
        area_east,
        area_south_east,
        area_south,
        area_south_west,
        area_west,
        area_north_west,
        area_roof_windows,
        solar_flux_north,
        solar_flux_north_east,
        solar_flux_east,
        solar_flux_south_east,
        solar_flux_south,
        solar_flux_south_west,
        solar_flux_west,
        solar_flux_north_west,
        solar_flux_roof_windows,
        g_table_6b_north,
        g_table_6b_north_east,
        g_table_6b_east,
        g_table_6b_south_east,
        g_table_6b_south,
        g_table_6b_south_west,
        g_table_6b_west,
        g_table_6b_north_west,
        g_table_6b_roof_windows,
        FF_table_6b_north,
        FF_table_6b_north_east,
        FF_table_6b_east,
        FF_table_6b_south_east,
        FF_table_6b_south,
        FF_table_6b_south_west,
        FF_table_6b_west,
        FF_table_6b_north_west,
        FF_table_6b_roof_windows,
        total_internal_gains
        )
    
    (gains_north,
     gains_north_east,
     gains_east,
     gains_south_east,
     gains_south,
     gains_south_west,
     gains_west,
     gains_north_west,
     gains_roof_windows,
     solar_gains_watts,
     total_internal_and_solar_gains) = result
     
    #Utilisation factor for heating table 9a
    result = Utilisation_factor_for_heating(
        heat_transfer_coefficient,
        total_internal_and_solar_gains,
        temperature_during_heating_living_room,
        heating_controls,
        monthly_external_temperature_table_U1,
        thermal_mass_parameter,
        heat_loss_parameter
        )
    
    (time_constant,
     a,
     heat_loss_rate_living_room,
     y_living_room,
     utilisation_factor_for_heating_living_room,
     temperature_during_heating_rest_of_dwelling,
     heat_loss_rate_rest_of_dwelling,
     y_rest_of_dwelling,
     utilisation_factor_for_heating_rest_of_dwelling
     )=result
     
    #Internal temperature reduction when heating is off
    result = Temperature_reduction(
        time_constant,
        hours_heating_is_off_1_weekday_living_room,
        hours_heating_is_off_2_weekday_living_room,
        hours_heating_is_off_1_weekend_living_room,
        hours_heating_is_off_2_weekend_living_room,
        hours_heating_is_off_1_weekday_rest_of_dwelling,
        hours_heating_is_off_2_weekday_rest_of_dwelling,
        hours_heating_is_off_1_weekend_rest_of_dwelling,
        hours_heating_is_off_2_weekend_rest_of_dwelling,
        temperature_during_heating_living_room,
        temperature_during_heating_rest_of_dwelling,
        responsiveness_of_heating_system,
        monthly_external_temperature_table_U1,
        utilisation_factor_for_heating_living_room,
        utilisation_factor_for_heating_rest_of_dwelling,
        heat_transfer_coefficient,
        total_internal_and_solar_gains
        )

    (t_c,
     internal_temperature_without_heating_living_room,
     internal_temperature_without_heating_rest_of_dwelling,
     temperature_reduction_when_heating_is_off_1_weekday_living_room,
     temperature_reduction_when_heating_is_off_2_weekday_living_room,
     temperature_reduction_when_heating_is_off_1_weekend_living_room,
     temperature_reduction_when_heating_is_off_2_weekend_living_room,
     temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling,
     temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling,
     temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling,
     temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling)=result
     
    #Heating requirement table 9c
    result = Heating_requirement(
        temperature_reduction_when_heating_is_off_1_weekday_living_room,
        temperature_reduction_when_heating_is_off_2_weekday_living_room,
        temperature_reduction_when_heating_is_off_1_weekend_living_room,
        temperature_reduction_when_heating_is_off_2_weekend_living_room,
        temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling,
        temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling,
        temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling,
        temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling,
        temperature_during_heating_living_room,
        temperature_during_heating_rest_of_dwelling,
        temperature_adjustment_table_4e
        )

    (T_weekday_living_room,
     T_weekend_living_room,
     mean_internal_temperature_living_room_T1_Table_9c,
     T_weekday_rest_of_dwelling,
     T_weekend_rest_of_dwelling,
     mean_internal_temperature_rest_of_dwelling_T2_table_9c)=result
    
    # Mean internal temperature calculations
    result = mean_internal_temperature(
        mean_internal_temperature_living_room_T1_Table_9c,
        mean_internal_temperature_rest_of_dwelling_T2_table_9c,
        living_room_area,
        total_floor_area,
        temperature_adjustment_table_4e
        )
    
    (living_area_fraction,
     mean_internal_temp_whole_dwelling) = result
     
     
    # Utilisation factor for heating whole house
    result = Utilisation_factor_for_heating_whole_house(
        heat_transfer_coefficient,
        total_internal_and_solar_gains,
        mean_internal_temp_whole_dwelling,
        monthly_external_temperature_table_U1,
        thermal_mass_parameter,
        heat_loss_parameter
        )
    
    (time_constant_whole_house,
     a_whole_house,
     heat_loss_rate_whole_house,
     y_whole_house,
     utilisation_factor_for_heating_whole_house)=result
     
    # Space heating requirement calculations
    result = space_heating_requirement(
        utilisation_factor_for_heating_whole_house,
        total_internal_and_solar_gains,
        monthly_external_temperature_table_U1,
        mean_internal_temp_whole_dwelling,
        heat_transfer_coefficient,
        days_in_month,
        total_floor_area
        )
    
    (useful_gains,
     heat_loss_rate_for_mean_internal_temperature,
     space_heating_requirement_monthly,
     space_heating_requirement_yearly,
     space_heating_requirement_yearly_per_m2) = result
     
    # Energy requirements calculations 
    result = energy_requirements(
        fraction_of_space_heat_secondary_system,
        fraction_of_space_heat_from_main_system_2,
        efficiency_of_main_space_heating_system_1,
        efficiency_of_main_space_heating_system_2,
        efficiency_of_secondary_space_heating_system,
        cooling_system_energy_efficiency_ratio_table_10c,
        space_heating_requirement_monthly,
        output_from_water_heater_monthly,
        water_heater_type,
        efficiency_of_water_heater,
        efficiency_of_water_heater_adjustment_table_4c,
        space_cooling_requirement_monthly,
        electricity_demand_mechanical_ventilation_fans_table_4f,
        electricity_demand_warm_air_heating_systems_fans_table_4f,
        electricity_demand_central_heating_pump_or_water_pump_table_4f,
        electricity_demand_oil_boiler_pump_table_4f,
        electricity_demand_boiler_flue_fan_table_4f,
        electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f,
        electricity_demand_pump_for_solar_water_heating_table_4f,
        electricity_demand_pump_for_storage_WWHRS_Table_G3,
        annual_lighting_demand,
        electricity_generated_by_PV_Appendix_M,
        electricity_generated_by_wind_turbine_appendix_M,
        electricity_used_or_generated_by_micro_CHP_appendix_N,
        electricity_generated_by_hydro_electric_generator_appendix_M,
        appendix_Q_energy_saved,
        appendix_Q_energy_used
        )
    
    (fraction_of_space_heat_from_main_systems,
     fraction_of_total_space_heat_from_main_system_1,
     fraction_of_total_space_heat_from_main_system_2,
     space_heating_fuel_main_system_1,
     space_heating_fuel_main_system_2,
     space_heating_fuel_secondary_system,
     efficiency_of_water_heater_table_4a,
     fuel_for_water_heating_monthly,
     space_cooling_fuel_monthly,
     space_heating_fuel_used_main_system_1,
     space_heating_fuel_used_main_system_2,
     space_heating_fuel_used_secondary,
     water_fuel_used,
     space_cooling_fuel_used,
     electricity_for_pumps_fans_electric_keep_hot,
     energy_saving_generation_technologies_total,
     appendix_Q_energy_total,
     energy_for_lighting,
     total_energy_used) = result
     
     # Fuel cost calculations
    result = fuel_costs(
        space_heating_fuel_used_main_system_1,
        space_heating_fuel_used_main_system_2,
        space_heating_fuel_used_secondary,
        space_heating_fuel_price_main_system_1,
        space_heating_fuel_price_main_system_2,
        space_heating_fuel_price_secondary,
        water_heating_high_rate_fraction_table_13,
        water_heating_low_rate_fraction_table_13,
        high_rate_fuel_price,
        low_rate_fuel_price,
        water_fuel_used,
        water_heating_fuel_price_other,
        space_cooling_fuel_used,
        space_cooling_fuel_price,
        electricity_for_pumps_fans_electric_keep_hot,
        fuel_price_for_pumps_fans_electric_keep_hot,
        energy_for_lighting,
        fuel_price_for_lighting,
        additional_standing_charges_table_12,
        energy_saving_generation_technologies,
        energy_saving_generation_technologies_fuel_price,
        appendix_Q_energy_used,
        appendix_Q_energy_used_fuel_price,
        appendix_Q_energy_saved,
        appendix_Q_energy_saved_fuel_price
        )
    
    (space_heating_main_system_1_fuel_cost,
     space_heating_main_system_2_fuel_cost,
     space_heating_secondary_fuel_cost,
     water_heating_high_rate_fuel_cost,
     water_heating_low_rate_fuel_cost,
     water_heating_cost_other,
     space_cooling_cost,
     pumps_fan_keep_hot_cost,
     lighting_cost,
     appendix_Q_fuel_cost,
     energy_saving_total_fuel_cost,
     additional_standing_charges_table_12,
     total_fuel_cost) = result
     
    # SAP rating calculations
    result = SAP_rating(
        energy_cost_deflator,
        total_fuel_cost,
        total_floor_area
        )
     
    (SAP_rating_value) = result
    
    # CO2 emissions calculations
    result = CO2_emissions(
        space_heating_fuel_used_main_system_1,
        space_heating_fuel_used_main_system_2,
        space_heating_fuel_used_secondary,
        space_heating_fuel_emission_factor_main_system_1,
        space_heating_fuel_emission_factor_main_system_2,
        space_heating_fuel_emission_factor_secondary,
        water_fuel_used,
        water_heating_fuel_emission_factor,
        space_cooling_fuel_used,
        space_cooling_fuel_emission_factor,
        electricity_for_pumps_fans_electric_keep_hot,
        fuel_emission_factor_for_pumps_fans_electric_keep_hot,
        energy_for_lighting,
        fuel_emission_factor_for_lighting,
        energy_saving_generation_technologies,
        energy_saving_generation_technologies_fuel_emission_factor,
        appendix_Q_energy_used,
        appendix_Q_energy_used_fuel_emission_factor,
        appendix_Q_energy_saved,
        appendix_Q_energy_saved_fuel_emission_factor,
        total_floor_area
        )
    
    (space_heating_main_system_1_emissions,
     space_heating_main_system_2_emissions,
     space_heating_secondary_emissions,
     water_used_emissions,
     space_cooling_used_emissions,
     pumps_fans_electric_keep_hot_emissions,
     lighting_emissions,
     appendix_Q_used_emissions,
     appendix_Q_saved_emissions,
     energy_saving_generation_technologies_emissions,
     space_and_water_heating_emissions,
     appendix_Q_total_used_emissions,
     appendix_Q_total_saved_emissions,
     energy_saving_generation_technologies_total_emissions,
     total_CO2_emissions_yearly,
     dwelling_CO2_emission_rate,
     CF,
     EI_rating) = result
    
    return (
        # overall_dwelling_dimensions results
        volume,
        total_floor_area,
        dwelling_volume,
        
        # ventilation_rates results
        number_of_chimneys_total,
        number_of_chimneys_m3_per_hour,
        number_of_open_flues_total,
        number_of_open_flues_m3_per_hour,
        number_of_intermittant_fans_m3_per_hour,
        number_of_passive_vents_m3_per_hour,
        number_of_flueless_gas_fires_m3_per_hour,
        infiltration_due_to_chimneys_flues_fans_PSVs,
        additional_infiltration,
        window_infiltration,
        infiltration_rate,
        infiltration_rate2,
        shelter_factor,
        infiltration_rate_incorporating_shelter_factor,
        wind_factor,
        adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed,
        exhaust_air_heat_pump_air_change_rate_through_system,
        effective_air_change_rate,
        
        # heat_losses_and_heat_loss_parameter results
        solid_floor_UA,
        semi_glazed_door_UA,
        window_UA,
        roof_window_UA,
        basement_floor_UA,
        basement_floor_Ak,
        ground_floor_UA,
        ground_floor_Ak,
        exposed_floor_UA,
        exposed_floor_Ak,
        basement_wall_net_area,
        basement_wall_UA,
        basement_wall_Ak,
        external_wall_net_area,
        external_wall_UA,
        external_wall_Ak,
        roof_net_area,
        roof_UA,
        roof_Ak,
        total_area_of_external_elements,
        party_wall_UA,
        party_wall_Ak,
        party_floor_Ak,
        party_ceiling_Ak,
        internal_wall_Ak,
        internal_floor_Ak,
        internal_ceiling_Ak,
        fabric_heat_loss,
        heat_capacity,
        thermal_mass_parameter,
        thermal_bridges,
        total_fabric_heat_loss,
        ventilation_heat_loss_calculated_monthly,
        heat_transfer_coefficient,
        average_heat_transfer_coefficient,
        heat_loss_parameter,
        average_heat_loss_parameter,
        
        #water heating requirements results
        annual_hot_water_usage_litres_per_day,
        hot_water_usage_in_litres_per_day_monthly,
        energy_content_of_water_used,
        distribution_loss,
        energy_lost_from_water_storage,
        water_storage_loss_monthly,
        total_heat_required_for_water_heating,
        output_from_water_heater_monthly,
        heat_gains_from_water_heating_monthly,
        
        #internal gains results
        G_L,
        C_1,
        C_2,
        E_B,
        initial_annual_lighting_demand,
        monthly_lighting_demand,
        annual_lighting_demand,
        lighting_gains,
        initial_annual_electrical_appliance_demand,
        monthly_electrical_appliance_demand,
        annual_electrical_appliance_demand,
        appliances_gains,
        cooking_gains,
        losses,
        water_heating_gains,
        metabolic_gains,
        total_internal_gains,
        
        #solar gains appendix U results
        solar_flux_north,
        solar_flux_north_east,
        solar_flux_east,
        solar_flux_south_east,
        solar_flux_south,
        solar_flux_south_west,
        solar_flux_west,
        solar_flux_north_west,
        
        #solar gains results
        gains_north,
        gains_north_east,
        gains_east,
        gains_south_east,
        gains_south,
        gains_south_west,
        gains_west,
        gains_north_west,
        gains_roof_windows,
        solar_gains_watts,
        total_internal_and_solar_gains,
        
        #utilisation factor for heating outputs
        time_constant,
            a,
            heat_loss_rate_living_room,
            y_living_room,
            utilisation_factor_for_heating_living_room,
            temperature_during_heating_rest_of_dwelling,
            heat_loss_rate_rest_of_dwelling,
            y_rest_of_dwelling,
            utilisation_factor_for_heating_rest_of_dwelling,
        
        #temperature reduction outputs
        t_c,
        internal_temperature_without_heating_living_room,
        internal_temperature_without_heating_rest_of_dwelling,
        temperature_reduction_when_heating_is_off_1_weekday_living_room,
        temperature_reduction_when_heating_is_off_2_weekday_living_room,
        temperature_reduction_when_heating_is_off_1_weekend_living_room,
        temperature_reduction_when_heating_is_off_2_weekend_living_room,
        temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling,
        temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling,
        temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling,
        temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling,
        
        #heating requirement outputs
        T_weekday_living_room,
        T_weekend_living_room,
        mean_internal_temperature_living_room_T1_Table_9c,
        T_weekday_rest_of_dwelling,
        T_weekend_rest_of_dwelling,
        mean_internal_temperature_rest_of_dwelling_T2_table_9c,
        
        #mean internal temperature results
        living_area_fraction,
        mean_internal_temp_whole_dwelling,
        
        #utilisation factor for heating whole house outputs
        time_constant_whole_house,
        a_whole_house,
        heat_loss_rate_whole_house,
        y_whole_house,
        utilisation_factor_for_heating_whole_house,
        
        #space heating requirements results
        useful_gains,
        heat_loss_rate_for_mean_internal_temperature,
        space_heating_requirement_monthly,
        space_heating_requirement_yearly,
        space_heating_requirement_yearly_per_m2,
        
        #energy requirements results
        fraction_of_space_heat_from_main_systems,
           fraction_of_total_space_heat_from_main_system_1,
           fraction_of_total_space_heat_from_main_system_2,
           space_heating_fuel_main_system_1,
           space_heating_fuel_main_system_2,
           space_heating_fuel_secondary_system,
           efficiency_of_water_heater_table_4a,
           fuel_for_water_heating_monthly,
           space_cooling_fuel_monthly,
           space_heating_fuel_used_main_system_1,
           space_heating_fuel_used_main_system_2,
           space_heating_fuel_used_secondary,
           water_fuel_used,
           space_cooling_fuel_used,
           electricity_for_pumps_fans_electric_keep_hot,
           energy_saving_generation_technologies_total,
           appendix_Q_energy_total,
           energy_for_lighting,
           total_energy_used,
        
        #fuel cost results
        space_heating_main_system_1_fuel_cost,
        space_heating_main_system_2_fuel_cost,
        space_heating_secondary_fuel_cost,
        water_heating_high_rate_fuel_cost,
        water_heating_low_rate_fuel_cost,
        water_heating_cost_other,
        space_cooling_cost,
        pumps_fan_keep_hot_cost,
        lighting_cost,
        appendix_Q_fuel_cost,
        energy_saving_total_fuel_cost,
        additional_standing_charges_table_12,
        total_fuel_cost,
        
        #SAP rating result
        SAP_rating_value,
        
        #CO2 emissions result
        space_heating_main_system_1_emissions,
        space_heating_main_system_2_emissions,
        space_heating_secondary_emissions,
        water_used_emissions,
        space_cooling_used_emissions,
        pumps_fans_electric_keep_hot_emissions,
        lighting_emissions,
        appendix_Q_used_emissions,
        appendix_Q_saved_emissions,
        energy_saving_generation_technologies_emissions,
        space_and_water_heating_emissions,
        appendix_Q_total_used_emissions,
        appendix_Q_total_saved_emissions,
        energy_saving_generation_technologies_total_emissions,
        total_CO2_emissions_yearly,
        dwelling_CO2_emission_rate,
        CF,
        EI_rating
        )
    
    