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
    
    :param assumed_occupancy:
    :type assumed_occupancy: int
    
    :param V_dm_table_1c:
    :type V_dm_table_1c: float
    
    :param days_in_month:
    :type days_in_month: int
    
    :param T_table_1d:
    :type T_table_1d: float #  should be list (of floats) ???
    
    :param water_storage_loss_manufacturer:
    :type water_storage_loss_manufacturer: float or None
    
    :param temperature_factor_table_2b:
    :type temperature_factor_table_2b: float
    
    :param storage_volume_litres:
    :type storage_volume_litres: int (if no tank or combi boiler enter '0'. If community heating enter '110')
    
    :param hot_water_storage_loss_table_2:
    :type hot_water_storage_loss_table_2: float
    
    :param volume_factor_table_2a:
    :type volume_factor_table_2a: float
    
    :param volume_factor_table_2a:
    :type volume_factor_table_2a: float
    
    :param Vs_appendix_G3:
    :type Vs_appendix_G3: float or None
    
    :param solar_storage_WWHRS_factor:
    :type solar_storage_WWHRS_factor: int or None
    
    :param primary_circuit_loss_table_3:
    :type primary_circuit_loss_table_3: float
    
    :param combi_loss_table_3:
    :type combi_loss_table_3: float
    
    :param solar_DHW_input_appendix_G:
    :type solar_DHW_input_appendix_G: float or None
    
    :param annual_hot_water_usage_litres_per_day: (43)
    :type annual_hot_water_usage_litres_per_day: float
    
    :param hot_water_usage_in_litres_per_day_monthly: (44)
    :type hot_water_usage_in_litres_per_day_monthly: float
    
    :param energy_content_of_water_used: (45)
    :type energy_content_of_water_used: float
    
    :param distribution_loss: (46)
    :type distribution_loss: float
    
    :param energy_lost_from_water_storage: (55)
    :type energy_lost_from_water_storage: float
    
    :param water_storage_loss_monthly: (56)
    :type water_storage_loss_monthly: float
    
    :param total_heat_required_for_water_heating: (62)
    :type total_heat_required_for_water_heating: float
    
    :param output_from_water_heater_monthly: (64)
    :type output_from_water_heater_monthly: float
    
    :param heat_gains_from_water_heating_monthly: (65)
    :type heat_gains_from_water_heating_monthly: float
    
    
    
   """
    
    
    
    annual_hot_water_usage_litres_per_day = (assumed_occupancy * 25) + 36
    
    hot_water_usage_in_litres_per_day_monthly = []
    for i in range(12):
        hot_water_usage_in_litres_per_day_monthly.append(V_dm_table_1c[i] * annual_hot_water_usage_litres_per_day)
        
    energy_content_of_water_used =[]
    for i in range(12):
        energy_content_of_water_used.append((4.18 * hot_water_usage_in_litres_per_day_monthly[i] * days_in_month[i] * T_table_1d) / 3600.0)
        
        
    distribution_loss = []
    for i in range(12):
        distribution_loss.append(energy_content_of_water_used[i] * 0.15)
        
    
    if water_storage_loss_manufacturer is None:
       energy_lost_from_water_storage = (storage_volume_litres * hot_water_storage_loss_table_2 * 
                                         volume_factor_table_2a * temperature_factor_table_2b)
       
    else:
       energy_lost_from_water_storage = water_storage_loss_manufacturer * temperature_factor_table_2b
       
       
    water_storage_loss_monthly =[]   
    if solar_storage_WWHRS_factor is None:
        for i in range(12):
            water_storage_loss_monthly.append(days_in_month[i] *  energy_lost_from_water_storage)
            
    else:
        for i in range(12):
            water_storage_loss_monthly.append(days_in_month[i] *  energy_lost_from_water_storage * 
                                      (storage_volume_litres - Vs_appendix_G3) / storage_volume_litres)
        
        
    total_heat_required_for_water_heating =[]   
    for i in range(12):
        total_heat_required_for_water_heating.append((0.85 * energy_content_of_water_used[i]) + 
                                                distribution_loss[i] + water_storage_loss_monthly[i] + 
                                                primary_circuit_loss_table_3 + combi_loss_table_3)
        
        
    output_from_water_heater_monthly =[]   
    for i in range(12):
        output_from_water_heater_monthly = total_heat_required_for_water_heating[i] + solar_DHW_input_appendix_G
        
        if output_from_water_heater_monthly < 0:
            output_from_water_heater_monthly = 0
        
    heat_gains_from_water_heating_monthly =[]
    for i in range(12):
        heat_gains_from_water_heating_monthly.append(0.25 * (0.85 * energy_content_of_water_used[i] + combi_loss_table_3 ) + (0.8 * 
                                                 (distribution_loss[i] + water_storage_loss_monthly[i] + primary_circuit_loss_table_3 )))
     
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