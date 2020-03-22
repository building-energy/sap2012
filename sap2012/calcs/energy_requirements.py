# -*- coding: utf-8 -*-


def Energy_Requirements(
        fraction_of_space_heat_secondary_system,
        fraction_of_space_heat_from_main_system_2,
        efficiency_of_main_space_heating_system_1,
        efficiency_of_main_space_heating_system_2,
        efficiency_of_secondary_space_heating_system,
        cooling_system_energy_efficiency_ratio_table_10c,
        space_heating_requirement_monthly,
        output_from_water_heater_monthly,
        efficiency_of_water_heater_table_4a,
        space_cooling_requirement_monthly,
        electricity_demand_mechanical_ventilation_fans_table_4f,
        electricity_demand_warm_air_heating_systems_fans_table_4f,
        electricity_demand_central_heating_pump_or_water_pump_table_4f,
        electricity_demand_oil_boiler_pump_table_4f,
        electricity_demand_boiler_flue_fan_table_4f,
        electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f,
        electricity_demand_pump_for_solar_water_heating_table_4f,
        electricity_demand_pump_for_storage_WWHRS_Table_G3,
        electricity_for_lighting,
        electricity_generated_by_PV_Appendix_M,
        electricity_generated_by_wind_turbine_appendix_M,
        electricity_used_or_generated_by_micro_CHP_appendix_N,
        electricity_generated_by_hydro_electric_generator_appendix_M,
        appendix_Q_energy_saved,
        appendix_Q_energy_used
        ):
    
    """ Calculates Energy Requirements, section 9
    
    :param fraction_of_space_heat_secondary_system:
    :type fraction_of_space_heat_secondary_system: float
    
    :param fraction_of_space_heat_from_main_system_2:
    :type fraction_of_space_heat_from_main_system_2: float
    
    :param efficiency_of_main_space_heating_system_1:
    :type efficiency_of_main_space_heating_system_1: float
    
    :param efficiency_of_main_space_heating_system_2:
    :type efficiency_of_main_space_heating_system_2: float
    
    :param efficiency_of_secondary_space_heating_system:
    :type efficiency_of_secondary_space_heating_system: float
    
    :param cooling_system_energy_efficiency_ratio_table_10c:
    :type cooling_system_energy_efficiency_ratio_table_10c: float
    
    :param space_heating_requirement_monthly:
    :type space_heating_requirement_monthly: float
    
    :param output_from_water_heater_monthly:
    :type output_from_water_heater_monthly: float
    
    :param efficiency_of_water_heater_table_4a:
    :type efficiency_of_water_heater_table_4a: float
    
    :param space_cooling_requirement_monthly:
    :type space_cooling_requirement_monthly: float
    
    :param electricity_demand_mechanical_ventilation_fans_table_4f:
    :type electricity_demand_mechanical_ventilation_fans_table_4f: float
    
    :param electricity_demand_warm_air_heating_systems_fans_table_4f:
    :type electricity_demand_warm_air_heating_systems_fans_table_4f: float
    
    :param electricity_demand_central_heating_pump_or_water_pump_table_4f:
    :type electricity_demand_central_heating_pump_or_water_pump_table_4f: float
    
    :param electricity_demand_oil_boiler_pump_table_4f:
    :type electricity_demand_oil_boiler_pump_table_4f: float
    
    :param electricity_demand_boiler_flue_fan_table_4f:
    :type electricity_demand_boiler_flue_fan_table_4f: float
    
    :param electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f:
    :type electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f: float
    
    :param electricity_demand_pump_for_solar_water_heating_table_4f:
    :type electricity_demand_pump_for_solar_water_heating_table_4f: float
    
    :param electricity_demand_pump_for_storage_WWHRS_Table_G3:
    :type electricity_demand_pump_for_storage_WWHRS_Table_G3: float
    
    :param electricity_for_lighting:
    :type electricity_for_lighting: float
    
    :param electricity_generated_by_PV_Appendix_M:
    :type electricity_generated_by_PV_Appendix_M: float
    
    :param electricity_generated_by_wind_turbine_appendix_M:
    :type electricity_generated_by_wind_turbine_appendix_M: float
    
    :param electricity_used_or_generated_by_micro_CHP_appendix_N:
    :type electricity_used_or_generated_by_micro_CHP_appendix_N: float
    
    :param electricity_generated_by_hydro_electric_generator,appendix_M:
    :type electricity_generated_by_hydro_electric_generator,appendix_M: float
    
    :param appendix_Q_energy_saved:
    :type appendix_Q_energy_saved: float
    
    :param appendix_Q_energy_used:
    :type appendix_Q_energy_used: float
    
    :param fraction_of_space_heat_from_main_systems:
    :type fraction_of_space_heat_from_main_systems: float
    
    :param fraction_of_total_space_heat_from_main_system_1:
    :type fraction_of_total_space_heat_from_main_system_1: float
    
    :param fraction_of_total_space_heat_from_main_system_2:
    :type fraction_of_total_space_heat_from_main_system_2: float
    
    :param space_heating_fuel_main_system_1:
    :type space_heating_fuel_main_system_1: float
    
    :param space_heating_fuel_main_system_2:
    :type space_heating_fuel_main_system_2: float
    
    :param space_heating_fuel_main_system_secondary_system:
    :type space_heating_fuel_main_system_secondary_system: float
    
    :param fuel_for_water_heating_monthly:
    :type fuel_for_water_heating_monthly: float
    
    :param space_cooling_fuel_monthly:
    :type space_cooling_fuel_monthly: float
    
    :param space_heating_fuel_used_main_system_1:
    :type space_heating_fuel_used_main_system_1: float
    
    :param space_heating_fuel_used_main_system_2:
    :type space_heating_fuel_used_main_system_2: float
    
    :param space_heating_fuel_used_secondary:
    :type space_heating_fuel_used_secondary: float
    
    :param water_fuel_used:
    :type water_fuel_used: float
    
    :param space_cooling_fuel_used:
    :type space_cooling_fuel_used: float
    
    :param electricity_for_pumps_fans_electric_keep_hot:
    :type electricity_for_pumps_fans_electric_keep_hot: float
    
    :param energy_saving_generation_technologies:
    :type energy_saving_generation_technologies: float
    
    :param appendix_Q_energy:
    :type appendix_Q_energy: float
    
    :param total_energy_used:
    :type total_energy_used: float
    
    
    
    """
    
    fraction_of_space_heat_from_main_systems = 1 - fraction_of_space_heat_secondary_system
    
    
    fraction_of_total_space_heat_from_main_system_1 = (fraction_of_space_heat_from_main_systems * 
                                                       (1- fraction_of_space_heat_from_main_system_2))
    
    fraction_of_total_space_heat_from_main_system_2 = (fraction_of_space_heat_from_main_systems * 
                                                       fraction_of_space_heat_from_main_system_2)
    
    space_heating_fuel_main_system_1 =[]
    for i in range(12):
        space_heating_fuel_main_system_1.append(space_heating_requirement_monthly[i] * 
                                             fraction_of_total_space_heat_from_main_system_1 * 100 /
                                             efficiency_of_main_space_heating_system_1)
        
    
        
    space_heating_fuel_main_system_2 =[]    
    for i in range(12):
        if fraction_of_total_space_heat_from_main_system_2 ==0:
            space_heating_fuel_main_system_2.append(space_heating_requirement_monthly[i] * 0)
        else:
            
            space_heating_fuel_main_system_2.append(space_heating_requirement_monthly[i] * 
                                             fraction_of_total_space_heat_from_main_system_2 * 100 /
                                             efficiency_of_main_space_heating_system_2)
        
        
    space_heating_fuel_secondary_system =[]
    for i in range(12):
        if fraction_of_space_heat_secondary_system ==0:
            space_heating_fuel_secondary_system.append(space_heating_requirement_monthly[i] * 0)
        else:
            space_heating_fuel_secondary_system.append(space_heating_requirement_monthly[i] * 
                                             fraction_of_space_heat_secondary_system * 100 /
                                             efficiency_of_secondary_space_heating_system)
    
    fuel_for_water_heating_monthly =[]
    for i in range(12):
        fuel_for_water_heating_monthly.append(output_from_water_heater_monthly[i] * 100 / 
                                              efficiency_of_water_heater_table_4a)
        
        
        
    space_cooling_fuel_monthly =[]    
    for i in range(12):
        if cooling_system_energy_efficiency_ratio_table_10c ==0:
            space_cooling_fuel_monthly.append(space_cooling_requirement_monthly[i] * 0)
        else:
             space_cooling_fuel_monthly.append(space_cooling_requirement_monthly[i] / 
                                      cooling_system_energy_efficiency_ratio_table_10c)
        
        
    space_heating_fuel_used_main_system_1 = sum(space_heating_fuel_main_system_1)
    
    space_heating_fuel_used_main_system_2 = sum(space_heating_fuel_main_system_2)
    
    space_heating_fuel_used_secondary = sum(space_heating_fuel_secondary_system)
    
    water_fuel_used = sum(fuel_for_water_heating_monthly)
    
    space_cooling_fuel_used = sum(space_cooling_fuel_monthly)
    
    electricity_for_pumps_fans_electric_keep_hot = (electricity_demand_mechanical_ventilation_fans_table_4f +
                                                    electricity_demand_warm_air_heating_systems_fans_table_4f +
                                                    electricity_demand_central_heating_pump_or_water_pump_table_4f +
                                                    electricity_demand_oil_boiler_pump_table_4f +
                                                    electricity_demand_boiler_flue_fan_table_4f +
                                                    electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f +
                                                    electricity_demand_pump_for_solar_water_heating_table_4f +
                                                    electricity_demand_pump_for_storage_WWHRS_Table_G3 
                                                    )
    
    
    
    
    energy_saving_generation_technologies = (electricity_generated_by_PV_Appendix_M +
                                             electricity_generated_by_wind_turbine_appendix_M +
                                             electricity_used_or_generated_by_micro_CHP_appendix_N +
                                             electricity_generated_by_hydro_electric_generator_appendix_M)
    
    """appendix_Q_energy_saved_total =[]
    for i in range(len(appendix_Q_energy_saved)):
        appendix_Q_energy_saved_total.append(sum(appendix_Q_energy_saved[i]) """
                                 
    appendix_Q_energy_total = sum(appendix_Q_energy_saved) + sum(appendix_Q_energy_used)   
        
    
    
    
    total_energy_used = (space_heating_fuel_used_main_system_1 + 
                         space_heating_fuel_used_main_system_2 +
                         space_heating_fuel_used_secondary + 
                         water_fuel_used +
                         space_cooling_fuel_used + 
                         electricity_for_pumps_fans_electric_keep_hot +
                         energy_saving_generation_technologies +
                         appendix_Q_energy_total +
                         electricity_for_lighting
                         )
    
    
    return(fraction_of_space_heat_from_main_systems,
           fraction_of_total_space_heat_from_main_system_1,
           fraction_of_total_space_heat_from_main_system_2,
           space_heating_fuel_main_system_1,
           space_heating_fuel_main_system_2,
           space_heating_fuel_secondary_system,
           fuel_for_water_heating_monthly,
           space_cooling_fuel_monthly,
           space_heating_fuel_used_main_system_1,
           space_heating_fuel_used_main_system_2,
           space_heating_fuel_used_secondary,
           water_fuel_used,
           space_cooling_fuel_used,
           electricity_for_pumps_fans_electric_keep_hot,
           energy_saving_generation_technologies,
           appendix_Q_energy_total,
           total_energy_used
            )
    
    