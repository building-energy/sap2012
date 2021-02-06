# -*- coding: utf-8 -*-

import csv
import ast
import json
from .SAP_worksheet.calculate_worksheet import calculate_worksheet


class Sap2012():
    """A class representing the SAP2012 calculation procedure.
    
    .. rubric:: Code Example
    
    .. code-block:: python

       >>> from sap2012 import Sap2012
       >>> s=Sap2012()
       >>> s.read_input_csv('my_input_file.csv')
       >>> s.run()
       >>> print(s.outputs['total_energy_used'])
       16499.45199251753
        
    """
    
    def __init__(self):
        """
        """
        self._inputs={    
            'area':None,
            'average_storey_height':None,
            
            # ventilation_rates inputs
            'number_of_chimneys_main_heating':None,
            'number_of_chimneys_secondary_heating':None,
            'number_of_chimneys_other':None,
            'number_of_open_flues_main_heating':None,
            'number_of_open_flues_secondary_heating':None,
            'number_of_open_flues_other':None,
            'number_of_intermittant_fans_total':None,
            'number_of_passive_vents_total':None,
            'number_of_flueless_gas_fires_total':None,
            #### note that 'dwelling_volume' isn't needed as an input here because it is calculated in 'overall_dwelling_dimenstions' #### 
            'air_permeability_value_q50':None,
            'number_of_storeys_in_the_dwelling':None,
            'structural_infiltration':None,
            'suspended_wooden_ground_floor_infiltration':None,
            'no_draft_lobby_infiltration':None,
            'percentage_of_windows_and_doors_draught_proofed':None,
            'number_of_sides_on_which_dwelling_is_sheltered':None,
            'monthly_average_wind_speed':None,
            'applicable_case':None,
            'mechanical_ventilation_air_change_rate_through_system':None,
            'exhaust_air_heat_pump_using_Appendix_N':None,
            'mechanical_ventilation_throughput_factor':None,
            'efficiency_allowing_for_in_use_factor':None,
            
            # heat_losses_and_heat_loss_parameter inputs
            'solid_door_net_area':None,
            'solid_door_u_value':None,
            'semi_glazed_door_net_area':None,
            'semi_glazed_door_u_value':None,
            'window_net_area':None,
            'window_u_value':None,
            'roof_window_net_area':None,
            'roof_window_u_value':None,
            'basement_floor_net_area':None,
            'basement_floor_u_value':None,
            'basement_floor_heat_capacity':None,
            'ground_floor_net_area':None,
            'ground_floor_u_value':None,
            'ground_floor_heat_capacity':None,
            'exposed_floor_net_area':None,
            'exposed_floor_u_value':None,
            'exposed_floor_heat_capacity':None,
            'basement_wall_gross_area':None,
            'basement_wall_opening':None,
            'basement_wall_u_value':None,
            'basement_wall_heat_capacity':None,
            'external_wall_gross_area':None,
            'external_wall_opening':None,
            'external_wall_u_value':None,
            'external_wall_heat_capacity':None,
            'roof_gross_area':None,
            'roof_opening':None,
            'roof_u_value':None,
            'roof_heat_capacity':None,
            'party_wall_net_area':None,
            'party_wall_u_value':None,
            'party_wall_heat_capacity':None,
            'party_floor_net_area':None,
            'party_floor_heat_capacity':None,
            'party_ceiling_net_area':None,
            'party_ceiling_heat_capacity':None,
            'internal_wall_net_area':None,
            'internal_wall_heat_capacity':None,
            'internal_floor_net_area':None,
            'internal_floor_heat_capacity':None,
            'internal_ceiling_net_area':None,
            'internal_ceiling_heat_capacity':None,
            'thermal_bridges_appendix_k':None,
            
            #water heating requirement inputs
            'assumed_occupancy':None,
            'V_dm_table_1c':None,
            'days_in_month':None,
            'T_table_1d':None,
            'water_storage_loss_manufacturer':None,
            'temperature_factor_table_2b':None,
            'storage_volume_litres':None,
            'hot_water_storage_loss_table_2':None,
            'volume_factor_table_2a':None,
            'Vs_appendix_G3':None,
            'solar_storage_WWHRS_factor':None,
            'primary_circuit_loss_table_3':None,
            'combi_loss_table_3':None,
            'solar_DHW_input_appendix_G':None,
            
            #internal gains inputs
            'number_of_low_energy_light_bulbs':None,
            'total_number_of_light_bulbs':None,
            'frame_factor':None,
            'window_area':None,
            'pumps_and_fans_gains':None,
            'light_access_factor_table_6d':None,
            'light_transmittance_factor_table_6d':None,
            'month_number':None,
            
            #solar gains appendix U inputs
            'solar_radiation_horizontal_plane_monthly_table_U3':None,
            'solar_declination_monthly_table_U3':None,
            'location_latitude_table_U4':None,
            'p_tilt':None,
            
            #solar gains inputs
            'access_factor_table_6d_north':None,
            'access_factor_table_6d_north_east':None,
            'access_factor_table_6d_east':None,
            'access_factor_table_6d_south_east':None,
            'access_factor_table_6d_south':None,
            'access_factor_table_6d_south_west':None,
            'access_factor_table_6d_west':None,
            'access_factor_table_6d_north_west':None,
            'access_factor_table_6d_roof_windows':None,
            'area_north':None,
            'area_north_east':None,
            'area_east':None,
            'area_south_east':None,
            'area_south':None,
            'area_south_west':None,
            'area_west':None,
            'area_north_west':None,
            'area_roof_windows':None,
            'solar_flux_roof_windows':None,
            'g_table_6b_north':None,
            'g_table_6b_north_east':None,
            'g_table_6b_east':None,
            'g_table_6b_south_east':None,
            'g_table_6b_south':None,
            'g_table_6b_south_west':None,
            'g_table_6b_west':None,
            'g_table_6b_north_west':None,
            'g_table_6b_roof_windows':None,
            'FF_table_6b_north':None,
            'FF_table_6b_north_east':None,
            'FF_table_6b_east':None,
            'FF_table_6b_south_east':None,
            'FF_table_6b_south':None,
            'FF_table_6b_south_west':None,
            'FF_table_6b_west':None,
            'FF_table_6b_north_west':None,
            'FF_table_6b_roof_windows':None,
            
            #utilisation factor for heating inputs
            'temperature_during_heating_living_room':None,
            'heating_controls':None,
            'monthly_external_temperature_table_U1':None,
            
            #temperature reduction inputs
            'hours_heating_is_off_1_weekday_living_room':None,
            'hours_heating_is_off_2_weekday_living_room':None,
            'hours_heating_is_off_1_weekend_living_room':None,
            'hours_heating_is_off_2_weekend_living_room':None,
            'hours_heating_is_off_1_weekday_rest_of_dwelling':None,
            'hours_heating_is_off_2_weekday_rest_of_dwelling':None,
            'hours_heating_is_off_1_weekend_rest_of_dwelling':None,
            'hours_heating_is_off_2_weekend_rest_of_dwelling':None,
            'responsiveness_of_heating_system':None,
            
            #mean internal temperature inputs
            'living_room_area':None,
            'temperature_adjustment_table_4e':None,
            
            #space heating requirement inputs
            
            #energy requirements inputs
            'fraction_of_space_heat_secondary_system':None,
            'fraction_of_space_heat_from_main_system_2':None,
            'efficiency_of_main_space_heating_system_1':None,
            'efficiency_of_main_space_heating_system_2':None,
            'efficiency_of_secondary_space_heating_system':None,
            'cooling_system_energy_efficiency_ratio_table_10c':None,
            'water_heater_type':None,
            'efficiency_of_water_heater':None,
            'efficiency_of_water_heater_adjustment_table_4c':None,
            'space_cooling_requirement_monthly':None,
            'electricity_demand_mechanical_ventilation_fans_table_4f':None,
            'electricity_demand_warm_air_heating_systems_fans_table_4f':None,
            'electricity_demand_central_heating_pump_or_water_pump_table_4f':None,
            'electricity_demand_oil_boiler_pump_table_4f':None,
            'electricity_demand_boiler_flue_fan_table_4f':None,
            'electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f':None,
            'electricity_demand_pump_for_solar_water_heating_table_4f':None,
            'electricity_demand_pump_for_storage_WWHRS_Table_G3':None,
            'electricity_generated_by_PV_Appendix_M':None,
            'electricity_generated_by_wind_turbine_appendix_M':None,
            'electricity_used_or_generated_by_micro_CHP_appendix_N':None,
            'electricity_generated_by_hydro_electric_generator_appendix_M':None,
            'appendix_Q_energy_saved':None,
            'appendix_Q_energy_used':None,
            
            #fuel cost inputs
            'space_heating_fuel_price_main_system_1':None,
            'space_heating_fuel_price_main_system_2':None,
            'space_heating_fuel_price_secondary':None,
            'water_heating_high_rate_fraction_table_13':None,
            'water_heating_low_rate_fraction_table_13':None,
            'high_rate_fuel_price':None,
            'low_rate_fuel_price':None,
            'water_heating_fuel_price_other':None,
            'space_cooling_fuel_used':None,
            'space_cooling_fuel_price':None,
            'electricity_for_pumps_fans_electric_keep_hot':None,
            'fuel_price_for_pumps_fans_electric_keep_hot':None,
            'fuel_price_for_lighting':None,
            'additional_standing_charges_table_12':None,
            'energy_saving_generation_technologies':None,
            'energy_saving_generation_technologies_fuel_price':None,
            'appendix_Q_energy_used_fuel_price':None,
            'appendix_Q_energy_saved_fuel_price':None,
            
            #Sap rating inputs
            'energy_cost_deflator':None,
            
            #CO2 emissions inputs
            'space_heating_fuel_emission_factor_main_system_1':None,
            'space_heating_fuel_emission_factor_main_system_2':None,
            'space_heating_fuel_emission_factor_secondary':None,
            'water_heating_fuel_emission_factor':None,
            'space_cooling_fuel_emission_factor':None,
            'fuel_emission_factor_for_pumps_fans_electric_keep_hot':None,
            'fuel_emission_factor_for_lighting':None,
            'energy_saving_generation_technologies_fuel_emission_factor':None,
            'appendix_Q_energy_used_fuel_emission_factor':None,
            'appendix_Q_energy_saved_fuel_emission_factor':None,
        }
        
        self._outputs={
            # overall_dwelling_dimensions results
            'volume':None,
            'total_floor_area':None,
            'dwelling_volume':None,
            
            # ventilation_rates results
            'number_of_chimneys_total':None,
            'number_of_chimneys_m3_per_hour':None,
            'number_of_open_flues_total':None,
            'number_of_open_flues_m3_per_hour':None,
            'number_of_intermittant_fans_m3_per_hour':None,
            'number_of_passive_vents_m3_per_hour':None,
            'number_of_flueless_gas_fires_m3_per_hour':None,
            'infiltration_due_to_chimneys_flues_fans_PSVs':None,
            'additional_infiltration':None,
            'window_infiltration':None,
            'infiltration_rate':None,
            'infiltration_rate2':None,
            'shelter_factor':None,
            'infiltration_rate_incorporating_shelter_factor':None,
            'wind_factor':None,
            'adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed':None,
            'exhaust_air_heat_pump_air_change_rate_through_system':None,
            'effective_air_change_rate':None,
            
            # heat_losses_and_heat_loss_parameter results
            'solid_floor_UA':None,
            'semi_glazed_door_UA':None,
            'window_UA':None,
            'roof_window_UA':None,
            'basement_floor_UA':None,
            'basement_floor_Ak':None,
            'ground_floor_UA':None,
            'ground_floor_Ak':None,
            'exposed_floor_UA':None,
            'exposed_floor_Ak':None,
            'basement_wall_net_area':None,
            'basement_wall_UA':None,
            'basement_wall_Ak':None,
            'external_wall_net_area':None,
            'external_wall_UA':None,
            'external_wall_Ak':None,
            'roof_net_area':None,
            'roof_UA':None,
            'roof_Ak':None,
            'total_area_of_external_elements':None,
            'party_wall_UA':None,
            'party_wall_Ak':None,
            'party_floor_Ak':None,
            'party_ceiling_Ak':None,
            'internal_wall_Ak':None,
            'internal_floor_Ak':None,
            'internal_ceiling_Ak':None,
            'fabric_heat_loss':None,
            'heat_capacity':None,
            'thermal_mass_parameter':None,
            'thermal_bridges':None,
            'total_fabric_heat_loss':None,
            'ventilation_heat_loss_calculated_monthly':None,
            'heat_transfer_coefficient':None,
            'average_heat_transfer_coefficient':None,
            'heat_loss_parameter':None,
            'average_heat_loss_parameter':None,
           
            #water heating requirements results
            'annual_hot_water_usage_litres_per_day':None,
            'hot_water_usage_in_litres_per_day_monthly':None,
            'energy_content_of_water_used':None,
            'distribution_loss':None,
            'energy_lost_from_water_storage':None,
            'water_storage_loss_monthly':None,
            'total_heat_required_for_water_heating':None,
            'output_from_water_heater_monthly':None,
            'heat_gains_from_water_heating_monthly':None,
            
            #internal gains results
            'G_L':None,
            'C_1':None,
            'C_2':None,
            'E_B':None,
            'initial_annual_lighting_demand':None,
            'monthly_lighting_demand':None,
            'annual_lighting_demand':None,
            'lighting_gains':None,
            'initial_annual_electrical_appliance_demand':None,
            'monthly_electrical_appliance_demand':None,
            'annual_electrical_appliance_demand':None,
            'appliances_gains':None,
            'cooking_gains':None,
            'losses':None,
            'water_heating_gains':None,
            'metabolic_gains':None,
            'total_internal_gains':None,
            
            #solar gains appendix U results
            'solar_flux_north':None,
            'solar_flux_north_east':None,
            'solar_flux_east':None,
            'solar_flux_south_east':None,
            'solar_flux_south':None,
            'solar_flux_south_west':None,
            'solar_flux_west':None,
            'solar_flux_north_west':None,
            
            #solar gains results
            'gains_north':None,
            'gains_north_east':None,
            'gains_east':None,
            'gains_south_east':None,
            'gains_south':None,
            'gains_south_west':None,
            'gains_west':None,
            'gains_north_west':None,
            'gains_roof_windows':None,
            'solar_gains_watts':None,
            'total_internal_and_solar_gains':None,
            
            
            #utilisation factor for heating outputs
            'time_constant':None,
            'a':None,
            'heat_loss_rate_living_room':None,
            'y_living_room':None,
            'utilisation_factor_for_heating_living_room':None,
            'temperature_during_heating_rest_of_dwelling':None,
            'heat_loss_rate_rest_of_dwelling':None,
            'y_rest_of_dwelling':None,
            'utilisation_factor_for_heating_rest_of_dwelling':None,
            
            
            #temperature reduction outputs
            't_c':None,
            'internal_temperature_without_heating_living_room':None,
            'internal_temperature_without_heating_rest_of_dwelling':None,
            'temperature_reduction_when_heating_is_off_1_weekday_living_room':None,
            'temperature_reduction_when_heating_is_off_2_weekday_living_room':None,
            'temperature_reduction_when_heating_is_off_1_weekend_living_room':None,
            'temperature_reduction_when_heating_is_off_2_weekend_living_room':None,
            'temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling':None,
            'temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling':None,
            'temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling':None,
            'temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling':None,
            
            #heating requirement results
            'T_weekday_living_room':None,
            'T_weekend_living_room':None,
            'mean_internal_temperature_living_room_T1_Table_9c':None,
            'T_weekday_rest_of_dwelling':None,
            'T_weekend_rest_of_dwelling':None,
            'mean_internal_temperature_rest_of_dwelling_T2_table_9c':None,
            
            #mean internal temperature results
            'living_area_fraction':None,
            'mean_internal_temp_whole_dwelling':None,
            
            #utilisation factor whole house results
            'time_constant_whole_house':None,
            'a_whole_house':None,
            'heat_loss_rate_whole_house':None,
            'y_whole_house':None,
            'utilisation_factor_for_heating_whole_house':None,
            
            #space heating requirements results
            'useful_gains':None,
            'heat_loss_rate_for_mean_internal_temperature':None,
            'space_heating_requirement_monthly':None,
            'space_heating_requirement_yearly':None,
            'space_heating_requirement_yearly_per_m2':None,
            
            #energy requirements results
            'fraction_of_space_heat_from_main_systems':None,
            'fraction_of_total_space_heat_from_main_system_1':None,
            'fraction_of_total_space_heat_from_main_system_2':None,
            'space_heating_fuel_main_system_1':None,
            'space_heating_fuel_main_system_2':None,
            'space_heating_fuel_secondary_system':None,
            'efficiency_of_water_heater_table_4a':None,
            'fuel_for_water_heating_monthly':None,
            'space_cooling_fuel_monthly':None,
            'space_heating_fuel_used_main_system_1':None,
            'space_heating_fuel_used_main_system_2':None,
            'space_heating_fuel_used_secondary':None,
            'water_fuel_used':None,
            'space_cooling_fuel_used':None,
            'electricity_for_pumps_fans_electric_keep_hot':None,
            'energy_saving_generation_technologies':None,
            'appendix_Q_energy_total':None,
            'energy_for_lighting':None,
            'total_energy_used':None,
            
            #fuel cost results
            'space_heating_main_system_1_fuel_cost':None,
            'space_heating_main_system_2_fuel_cost':None,
            'space_heating_secondary_fuel_cost':None,
            'water_heating_high_rate_fuel_cost':None,
            'water_heating_low_rate_fuel_cost':None,
            'water_heating_cost_other':None,
            'space_cooling_cost':None,
            'pumps_fan_keep_hot_cost':None,
            'lighting_cost':None,
            'appendix_Q_fuel_cost':None,
            'energy_saving_total_fuel_cost':None,
            'additional_standing_charges_table_12':None,
            'total_fuel_cost':None,
            
            #SAP rating result
            'SAP_rating':None,
            
            #CO2 emissions result
            'space_heating_main_system_1_emissions':None,
            'space_heating_main_system_2_emissions':None,
            'space_heating_secondary_emissions':None,
            'water_used_emissions':None,
            'space_cooling_used_emissions':None,
            'pumps_fans_electric_keep_hot_emissions':None,
            'lighting_emissions':None,
            'appendix_Q_used_emissions':None,
            'appendix_Q_saved_emissions':None,
            'energy_saving_generation_technologies_emissions':None,
            'space_and_water_heating_emissions':None,
            'appendix_Q_total_used_emissions':None,
            'appendix_Q_total_saved_emissions':None,
            'energy_saving_generation_technologies_total_emissions':None,
            'total_CO2_emissions_yearly':None,
            'dwelling_CO2_emission_rate':None,
            'CF':None,
            'EI_rating':None,
        }
    
    @property
    def inputs(self):
        """A dictionary of the inputs needed for the SAP calculation.
            
        This dictionary has 197 items and is in the form {model_input_paramater:value}.
        Upon instance creation, all dictionary values are set to `None`. 
        These values need to be updated with the input values for the SAP calculation to run.
    
        :rtype: dict
        """
        return self._inputs
    
    
    @property
    def outputs(self):
        """A dictionary of the outputs generated by a successful SAP calculation run.
        
        This dictionary has 192 items and is in the form {model_output_paramater:value}.
        Upon instance creation, all dictionary values are set to `None`. 
        These values are generated by running a SAP calcuation.
        
        :rtype: dict
        """
        return self._outputs
    
    
    def read_input_csv(self,fp):
        """Reads an input csv file and places the values in the `inputs` dictionary.
        
        An input csv file is formatted as:
            
        - the first row contains the input keys.
        - the second row contains the input values.
        
        :param fp: The filepath of the csv file.
        :type fp: str
        
        """
        with open(fp,'r') as csvfile:
            
            csvreader = csv.reader(csvfile, delimiter=',')
            
            keys=next(csvreader)
            values=next(csvreader)
            l=zip(keys,values)
            
            input_keys=self.inputs.keys()
            
            for i,(k,v) in enumerate(l):
                if k in input_keys:
                    try:
                        v1=float(v)
                    except ValueError:
                        try:
                            v1=ast.literal_eval(v)
                        except SyntaxError:
                            v1=v
                    self.inputs[k]=v1
                else:
                    raise Exception('column %s key %s not in self.inputs dictionary ' % (i,k))
    
    
    def read_input_json(self,fp):
        """Reads an inputs json file and places the values in the `inputs` dictionary.
        
        An input json file is formatted as a dictionary-like object matching the 
        format of the `inputs` dictionary.
        
        :param fp: The filepath of the json file.
        :type fp: str
        
        """
        with open(fp,'r') as f:
            d=json.load(f)
            
        input_keys=self.inputs.keys()
        
        for k,v in d.items():
               if k in input_keys:
                   self.inputs[k]=v
               else:
                   raise Exception('key %s not in self.inputs dictionary ' % (k))
    
    
    def run(self):
        """Runs the SAP2012 model calculations and places the results in `outputs`.
        
        The SAP calcuations are run using the `calculate_worksheet` function.
        The function runs each of the individual SAP calculation sections in turn.
        
        """
        output_values=calculate_worksheet(**self.inputs)
        output_keys=self.outputs.keys()
        l=zip(output_keys,output_values)
        for k,v in l:
            self.outputs[k]=v
            
    
    def write_input_csv(self,fp):
        """Writes the inputs stored in the `inputs` dictionary as a csv file.
        
        An input csv file is formatted as:
            
        - the first row contains the input keys.
        - the second row contains the input values.
        
        :param fp: The filepath of the csv file.
        :type fp: str
        
        """
        with open(fp,'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.inputs.keys())
            csvwriter.writerow(self.inputs.values())
    
    
    def write_input_json(self,fp):
        """Writes the inputs stored in the `inputs` dictionary as a json file.
        
        An input json file is formatted as a dictionary-like object matching the 
        format of the `inputs` dictionary.
        
        :param fp: The filepath of the json file.
        :type fp: str
        
        """
        with open(fp,'w') as f:
            json.dump(self.inputs,f,indent=4, sort_keys=True)
    
    
    def write_output_csv(self,fp):
        """Writes the outputs stored in the `outputs` dictionary as a csv file.
        
        An output csv file is formatted as:
            
        - the first row contains the output keys.
        - the second row contains the output values.
        
        :param fp: The filepath of the csv file.
        :type fp: str
        
        """
        with open(fp,'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.outputs.keys())
            csvwriter.writerow(self.outputs.values())
    
    
    def write_output_json(self,fp):
        """Writes the outputs stored in the `outputs` dictionary as a json file.
        
        An output json file is formatted as a dictionary-like object matching the 
        format of the `outputs` dictionary.
        
        :param fp: The filepath of the json file.
        :type fp: str
        
        """
        with open(fp,'w') as f:
            json.dump(self.outputs,f,indent=4, sort_keys=True)
    

            
    
    
    
    
        
    
    
        
        
        