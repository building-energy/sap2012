# -*- coding: utf-8 -*-


def space_heating_requirement (
        utilisation_factor_for_heating_whole_house,
        total_internal_and_solar_gains,
        monthly_external_temperature_table_U1,
        mean_internal_temp_whole_dwelling,
        heat_transfer_coefficient,
        days_in_month,
        total_floor_area
        ):
    
    """ Calculates Space Heating Requirement, section 8
    
    :param utilisation_factor_for_gains_table_9a: see (94)
    :type utilisation_factor_for_gains_table_9a: float
    
    :param total_gains_internal_and_solar: see (84) in W
    :type total_gains_internal_and_solar: float
    
    :param monthly_external_temperature_table_U1: see (96) in oC
    :type monthly_external_temperature_table_U1: float
    
    :param mean_internal_temperature_whole_dwelling: see (92) in oC
    :type mean_internal_temperature_whole_dwelling: float
    
    :param heat_transfer_coefficient: see (39)
    :type heat_transfer_coefficient: float
    
    :param days_in_month: 
    :type days_in_month: float
    
    :param total_floor_area: in m
    :type total_floor_area: float
    
     return(
            useful_gains,
            heat_loss_rate_for_mean_internal_temperature,
            space_heating_requirement_monthly,
            space_heating_requirement_yearly,
            space_heating_requirement_yearly_per_m2)
    
    :param useful_gains: see (95) in W
    :type useful_gains: float
    
    :param heat_loss_rate_for_mean_internal_temperature: see (97) in W
    :type heat_loss_rate_for_mean_internal_temperature: float
    
    :param space_heating_requirement_monthly: see (98) in kWh/month
    :type space_heating_requirement_monthly: float
    
    :param space_heating_requirement_yearly: see (98) in kWh
    :type space_heating_requirement_yearly: float
    
    :param space_heating_requirement_yearly_per_m2: see (99) in kWh/m2/yr
    :type space_heating_requirement_yearly_per_m2: float
    
    """
    
    useful_gains =[]
    for i in range(12):
        useful_gains.append(utilisation_factor_for_heating_whole_house[i] * 
                            total_internal_and_solar_gains[i])
        
        
    heat_loss_rate_for_mean_internal_temperature =[]
    for i in range(12):
        heat_loss_rate_for_mean_internal_temperature.append(heat_transfer_coefficient[i] * 
                                                        (mean_internal_temp_whole_dwelling[i] -
                                                         monthly_external_temperature_table_U1[i]))
        
    
    space_heating_requirement_monthly =[]    
    for i in range(12):
        space_heating_requirement_monthly.append(0.024 * (heat_loss_rate_for_mean_internal_temperature[i] - useful_gains[i]) *
                                                     days_in_month[i])
        
    
    space_heating_requirement_yearly = sum(space_heating_requirement_monthly)
    
    space_heating_requirement_yearly_per_m2 = sum(space_heating_requirement_monthly) / total_floor_area
    
    
    return(
            useful_gains,
            heat_loss_rate_for_mean_internal_temperature,
            space_heating_requirement_monthly,
            space_heating_requirement_yearly,
            space_heating_requirement_yearly_per_m2)