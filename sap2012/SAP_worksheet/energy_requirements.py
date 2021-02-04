# -*- coding: utf-8 -*-


def energy_requirements(
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
        ):
    
    """Calculates Energy Requirements, Section 9.
    
    :param fraction_of_space_heat_secondary_system: See (201).
    :type fraction_of_space_heat_secondary_system: float
    
    :param fraction_of_space_heat_from_main_system_2: See (202).
    :type fraction_of_space_heat_from_main_system_2: float
    
    :param efficiency_of_main_space_heating_system_1: See (206).
    :type efficiency_of_main_space_heating_system_1: float
    
    :param efficiency_of_main_space_heating_system_2: See (207).
    :type efficiency_of_main_space_heating_system_2: float
    
    :param efficiency_of_secondary_space_heating_system: See (208).
    :type efficiency_of_secondary_space_heating_system: float
    
    :param cooling_system_energy_efficiency_ratio_table_10c: See (209).
    :type cooling_system_energy_efficiency_ratio_table_10c: list of floats
    
    :param space_heating_requirement_monthly: See (211).
    :type space_heating_requirement_monthly: list of floats
    
    :param output_from_water_heater_monthly: See (216).
    :type output_from_water_heater_monthly: list of floats
    
    :param efficiency_of_water_heater_table_4a: See (216).
    :type efficiency_of_water_heater_table_4a: float
    
    :param space_cooling_requirement_monthly: See (219).
    :type space_cooling_requirement_monthly: list of floats
    
    :param electricity_demand_mechanical_ventilation_fans_table_4f: See (230) in kWh/yr.
    :type electricity_demand_mechanical_ventilation_fans_table_4f: float
    
    :param electricity_demand_warm_air_heating_systems_fans_table_4f: See (230) in kWh/yr.
    :type electricity_demand_warm_air_heating_systems_fans_table_4f: float
    
    :param electricity_demand_central_heating_pump_or_water_pump_table_4f: See (230) in kWh/yr.
    :type electricity_demand_central_heating_pump_or_water_pump_table_4f: float
    
    :param electricity_demand_oil_boiler_pump_table_4f: See (230) in kWh/yr.
    :type electricity_demand_oil_boiler_pump_table_4f: float
    
    :param electricity_demand_boiler_flue_fan_table_4f: See (230) in kWh/yr.
    :type electricity_demand_boiler_flue_fan_table_4f: float
    
    :param electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f: See (230) in kWh/yr.
    :type electricity_demand_keep_hot_facility_gas_combi_boiler_table_4f: float
    
    :param electricity_demand_pump_for_solar_water_heating_table_4f: See (230) in kWh/yr.
    :type electricity_demand_pump_for_solar_water_heating_table_4f: float
    
    :param electricity_demand_pump_for_storage_WWHRS_Table_G3: See (230) in kWh/yr.
    :type electricity_demand_pump_for_storage_WWHRS_Table_G3: float
    
    :param electricity_for_lighting: See (232) in kWh/yr.
    :type electricity_for_lighting: float
    
    :param electricity_generated_by_PV_Appendix_M: See (233) in kWh/yr.
    :type electricity_generated_by_PV_Appendix_M: float
    
    :param electricity_generated_by_wind_turbine_appendix_M: See (234) in kWh/yr.
    :type electricity_generated_by_wind_turbine_appendix_M: float
    
    :param electricity_used_or_generated_by_micro_CHP_appendix_N: See (235) in kWh/yr.
    :type electricity_used_or_generated_by_micro_CHP_appendix_N: float
    
    :param electricity_generated_by_hydro_electric_generator,appendix_M: See (235) in kWh/yr.
    :type electricity_generated_by_hydro_electric_generator,appendix_M: float
    
    :param appendix_Q_energy_saved: See (236) in kWh/yr.
    :type appendix_Q_energy_saved: float
    
    :param appendix_Q_energy_used: See (237) in kWh/yr.
    :type appendix_Q_energy_used: float
    
    :returns: A tuple of (
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
        total_energy_used
        )
    
    - **fraction_of_space_heat_from_main_systems** (`float`): 
    
    - **fraction_of_total_space_heat_from_main_system_1** (`float`):
    
    - **fraction_of_total_space_heat_from_main_system_2** (`float`):
    
    - **space_heating_fuel_main_system_1** (`list` (`float`)): See (211) in kWh/month.
    
    - **space_heating_fuel_main_system_2** (`list` (`float`)): See (213) in kWh/month.
    
    - **space_heating_fuel_main_system_secondary_system** (`list` (`float`)): See (214) in kWh/month.
    
    - **fuel_for_water_heating_monthly** (`list` (`float`)): See (219) in kWh/month.
    
    - **space_cooling_fuel_monthly** (`list` (`float`)): See (221) in kWh/month.
    
    - **space_heating_fuel_used_main_system_1** (`float`): See (211) in kWh/yr.
    
    - **space_heating_fuel_used_main_system_2** (`float`): See (213) in kWh/yr.
    
    - **space_heating_fuel_used_secondary** (`float`): See (215) in kWh/yr.
    
    - **water_fuel_used** (`float`): See (219) in kWh/yr.
    
    - **space_cooling_fuel_used** (`float`): See (221) in kWh/yr.
    
    - **electricity_for_pumps_fans_electric_keep_hot** (`float`): See (230) in kWh/yr.
    
    - **energy_saving_generation_technologies** (`float`): See (230) in kWh/yr.
    
    - **appendix_Q_energy** (`float`): See (237) in kWh/yr.
    
    - **total_energy_used** ()`float`: See (237) in kWh/yr.
    
    """
    
    fraction_of_space_heat_from_main_systems = 1 - fraction_of_space_heat_secondary_system
    
    
    fraction_of_total_space_heat_from_main_system_1 = (fraction_of_space_heat_from_main_systems * 
                                                       (1- fraction_of_space_heat_from_main_system_2))
    
    fraction_of_total_space_heat_from_main_system_2 = (fraction_of_space_heat_from_main_systems * 
                                                       fraction_of_space_heat_from_main_system_2)
    
    space_heating_fuel_main_system_1 =[]
    for i in range(12):
        if i == 5 or i == 6 or i == 7 or i == 8:
            space_heating_fuel_main_system_1.append(0)
        else:
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
    
    
    efficiency_of_water_heater_table_4a = []
    if water_heater_type in ['hot water only boiler'
                             'seperate hot water only heater']:
        for i in range(12):
            efficiency_of_water_heater_table_4a.append(efficiency_of_water_heater + efficiency_of_water_heater_adjustment_table_4c)
            
    elif water_heater_type == 'gas/oil boiler main system':
        for i in range(12):
            efficiency_of_water_heater_table_4a.append((space_heating_requirement_monthly[i] + output_from_water_heater_monthly[i]) / 
                                                       (space_heating_requirement_monthly[i] / efficiency_of_main_space_heating_system_1 + 
                                                        output_from_water_heater_monthly[i] / efficiency_of_water_heater))
    
    elif water_heater_type == 'other':
        for i in range(12):
            efficiency_of_water_heater_table_4a.append(efficiency_of_water_heater)
            
    
    fuel_for_water_heating_monthly =[]
    for i in range(12):
        fuel_for_water_heating_monthly.append(output_from_water_heater_monthly[i] * 100 / efficiency_of_water_heater_table_4a[i])
        
        
        
    space_cooling_fuel_monthly =[]    
    for i in range(12):
        if cooling_system_energy_efficiency_ratio_table_10c ==0:
            space_cooling_fuel_monthly.append(0)
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
    
    
    
    
    energy_saving_generation_technologies_total = (sum(electricity_generated_by_PV_Appendix_M) +
                                             sum(electricity_generated_by_wind_turbine_appendix_M) +
                                             sum(electricity_used_or_generated_by_micro_CHP_appendix_N) +
                                             sum(electricity_generated_by_hydro_electric_generator_appendix_M))
    
    """appendix_Q_energy_saved_total =[]
    for i in range(len(appendix_Q_energy_saved)):
        appendix_Q_energy_saved_total.append(sum(appendix_Q_energy_saved[i]) """
                                 
    appendix_Q_energy_total = sum(appendix_Q_energy_saved) + sum(appendix_Q_energy_used)   
        
    energy_for_lighting = annual_lighting_demand
    
    
    total_energy_used = (space_heating_fuel_used_main_system_1 + 
                         space_heating_fuel_used_main_system_2 +
                         space_heating_fuel_used_secondary + 
                         water_fuel_used +
                         space_cooling_fuel_used + 
                         electricity_for_pumps_fans_electric_keep_hot +
                         energy_saving_generation_technologies_total +
                         appendix_Q_energy_total +
                         energy_for_lighting
                         ) 

    
    return(fraction_of_space_heat_from_main_systems,
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
           total_energy_used
            )
    
    