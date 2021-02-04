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
    
    """Calculates Space Heating Requirement, Section 8.
    
    :param utilisation_factor_for_gains_table_9a: See (94).
    :type utilisation_factor_for_gains_table_9a: float
    
    :param total_gains_internal_and_solar: See (84) in W.
    :type total_gains_internal_and_solar: float
    
    :param monthly_external_temperature_table_U1: See (96) in degC.
    :type monthly_external_temperature_table_U1: float
    
    :param mean_internal_temperature_whole_dwelling: See (92) in degC.
    :type mean_internal_temperature_whole_dwelling: float
    
    :param heat_transfer_coefficient: See (39).
    :type heat_transfer_coefficient: float
    
    :param days_in_month: 
    :type days_in_month: float
    
    :param total_floor_area: in m.
    :type total_floor_area: float
    
    :returns: A tuple of (
            useful_gains,
            heat_loss_rate_for_mean_internal_temperature,
            space_heating_requirement_monthly,
            space_heating_requirement_yearly,
            space_heating_requirement_yearly_per_m2 )
    
    - **useful_gains** (`float`): See (95) in W.
    
    - **heat_loss_rate_for_mean_internal_temperature** (`float`): See (97) in W.
    
    - **space_heating_requirement_monthly** (`float`): See (98) in kWh/month.
    
    - **space_heating_requirement_yearly** (`float`): See (98) in kWh.
    
    - **space_heating_requirement_yearly_per_m2** (`float`): See (99) in kWh/m2/yr.
    
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