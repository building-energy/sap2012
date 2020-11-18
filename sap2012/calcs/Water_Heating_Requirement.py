# -*- coding: utf-8 -*-


def water_heating_requirement (
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
        ):
    
    """Calculates water heating requirement, section 4
    
    :param assumed_occupancy: see (42)
        calculate using equation from (42) if TFA > 13.9, N = 1 + 1.76 * [1 - exp(-0.000349 * (TFA -13.9)2)] + 0.0013 * (TFA -13.9), if TFA =< 13.9, N = 1
        TFA = Total Floor Area
    :type assumed_occupancy: float
    
    :param V_dm_table_1c: see table 1c
    :type V_dm_table_1c: list of floats
    
    :param days_in_month: list of the number of days in each month of the calendar year
    :type days_in_month: list of int
    
    :param T_table_1d: see table 1d
    :type T_table_1d: list (of floats)
    
    :param storage_volume_litres: see (47)
        value is 0 if no tank in dwelling
    :type storage_volume_litres: int (if no tank or combi boiler enter '0'. If community heating enter '110')
    
    :param water_storage_loss_manufacturer: see (48)
        value is None if unknown or no tank in dwelling
    :type water_storage_loss_manufacturer: float or None
    
    :param temperature_factor_table_2b: see (49/53)
        value is 0 if no tank in dwelling
    :type temperature_factor_table_2b: float
    
    :param hot_water_storage_loss_table_2: see (51)
        value is 0 if no tank in dwelling
    :type hot_water_storage_loss_table_2: float
    
    :param volume_factor_table_2a: see (52)
        value is 0 if no tank in dwelling
    :type volume_factor_table_2a: float
    
    :param Vs_appendix_G3: see appendix G3
        only applies where solar storage is within dwelling
    :type Vs_appendix_G3: float or None
    
    :param solar_storage_WWHRS_factor:
        Applies to dwellings with solar storage
    :type solar_storage_WWHRS_factor: int or None
    
    :param primary_circuit_loss_table_3: see (59)
        values found in table 3
    :type primary_circuit_loss_table_3: float
    
    :param combi_loss_table_3: see (61)
        values found in table 3
    :type combi_loss_table_3: float
    
    :param solar_DHW_input_appendix_G: see appendix G
    :type solar_DHW_input_appendix_G: float or None
    
    return (
            annual_hot_water_usage_litres_per_day,
            hot_water_usage_in_litres_per_day_monthly,
            energy_content_of_water_used,
            distribution_loss,
            energy_lost_from_water_storage,
            water_storage_loss_monthly,
            total_heat_required_for_water_heating,
            output_from_water_heater_monthly,
            heat_gains_from_water_heating_monthly
            )
    
    :param annual_hot_water_usage_litres_per_day: (43) in L
    :type annual_hot_water_usage_litres_per_day: float
    
    :param hot_water_usage_in_litres_per_day_monthly: (44) in L
    :type hot_water_usage_in_litres_per_day_monthly: list of floats
    
    :param energy_content_of_water_used: (45) in kWh/month
    :type energy_content_of_water_used: list of floats
    
    :param distribution_loss: (46) in kWh/month
    :type distribution_loss: list of floats
    
    :param energy_lost_from_water_storage: (50/55) in kWh/month
    :type energy_lost_from_water_storage: list of floats
    
    :param water_storage_loss_monthly: (56) in kWh/month
    :type water_storage_loss_monthly: list of floats
    
    :param total_heat_required_for_water_heating: (62) in kWh/month
    :type total_heat_required_for_water_heating: list of floats
    
    :param output_from_water_heater_monthly: (64) in kWh/month
    :type output_from_water_heater_monthly: list of floats
    
    :param heat_gains_from_water_heating_monthly: (65) in kWh/month
    :type heat_gains_from_water_heating_monthly: list of floats
    
    
    
   """
    
    
    
    annual_hot_water_usage_litres_per_day = (assumed_occupancy * 25) + 36
    
    hot_water_usage_in_litres_per_day_monthly = []
    for i in range(12):
        hot_water_usage_in_litres_per_day_monthly.append(V_dm_table_1c[i] * annual_hot_water_usage_litres_per_day)
        
    energy_content_of_water_used =[]
    for i in range(12):
        energy_content_of_water_used.append((4.18 * hot_water_usage_in_litres_per_day_monthly[i] * days_in_month[i] * T_table_1d[i]) / 3600)
        
        
    distribution_loss = []
    for i in range(12):
        distribution_loss.append(energy_content_of_water_used[i] * 0.15)
        
    
    if water_storage_loss_manufacturer ==0:
       energy_lost_from_water_storage = (storage_volume_litres * hot_water_storage_loss_table_2 * 
                                         volume_factor_table_2a * temperature_factor_table_2b)
       
    else:
       energy_lost_from_water_storage = water_storage_loss_manufacturer * temperature_factor_table_2b
       
       
    water_storage_loss_monthly =[]   
    if solar_storage_WWHRS_factor ==0:
        for i in range(12):
            water_storage_loss_monthly.append(days_in_month[i] *  energy_lost_from_water_storage)
            
    else:
        for i in range(12):
            if storage_volume_litres == 0:
                water_storage_loss_monthly.append(days_in_month[i] * 0)
            else:
                water_storage_loss_monthly.append(days_in_month[i] *  energy_lost_from_water_storage * 
                                      (storage_volume_litres - Vs_appendix_G3) / storage_volume_litres)
        
        
    total_heat_required_for_water_heating =[]   
    for i in range(12):
        total_heat_required_for_water_heating.append((0.85 * energy_content_of_water_used[i]) + 
                                                distribution_loss[i] + water_storage_loss_monthly[i] + 
                                                primary_circuit_loss_table_3[i] + combi_loss_table_3[i])
        
        
    output_from_water_heater_monthly =[]   
    for i in range(12):
        output_from_water_heater_monthly.append(total_heat_required_for_water_heating[i] + solar_DHW_input_appendix_G[i])
        
        
    heat_gains_from_water_heating_monthly =[]
    for i in range(12):
        heat_gains_from_water_heating_monthly.append(0.25 * (0.85 * energy_content_of_water_used[i] + combi_loss_table_3[i] ) + (0.8 * 
                                                 (distribution_loss[i] + water_storage_loss_monthly[i] + primary_circuit_loss_table_3[i] )))
     
    return (
            annual_hot_water_usage_litres_per_day,
            hot_water_usage_in_litres_per_day_monthly,
            energy_content_of_water_used,
            distribution_loss,
            energy_lost_from_water_storage,
            water_storage_loss_monthly,
            total_heat_required_for_water_heating,
            output_from_water_heater_monthly,
            heat_gains_from_water_heating_monthly
            )