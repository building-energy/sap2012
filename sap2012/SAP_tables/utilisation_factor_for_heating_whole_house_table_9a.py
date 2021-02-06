# -*- coding: utf-8 -*-

def utilisation_factor_for_heating_whole_house_table_9a(
        heat_transfer_coefficient,
        total_internal_and_solar_gains,
        mean_internal_temp_whole_dwelling,
        monthly_external_temperature_table_U1,
        thermal_mass_parameter,
        heat_loss_parameter
        ):
    """
    
    :rtype: dict
    
    """
    
    
    time_constant_whole_house = []
    for i in range(12):
        time_constant_whole_house.append(thermal_mass_parameter/
                             (3.6 * heat_loss_parameter[i]))

    a_whole_house = []
    for i in range(12):
        a_whole_house.append(1 + time_constant_whole_house[i]/15)
        
    heat_loss_rate_whole_house = []
    for i in range(12):
        heat_loss_rate_whole_house.append(heat_transfer_coefficient[i] * 
                              (mean_internal_temp_whole_dwelling[i] - monthly_external_temperature_table_U1[i]))
        
    y_whole_house = []
    for i in range(12):
        if heat_loss_rate_whole_house[i] == 0:
            y_whole_house.append(10^6)
            
        else:
            y_whole_house.append(total_internal_and_solar_gains[i] / heat_loss_rate_whole_house[i])
            
            
    utilisation_factor_for_heating_whole_house = []
    for i in range(12):
        if y_whole_house[i] ==1:
            utilisation_factor_for_heating_whole_house.append(a_whole_house[i] / 
                                                  (a_whole_house[i] + 1))
            
        if y_whole_house[i] > 0:
            utilisation_factor_for_heating_whole_house.append((1-y_whole_house[i]**a_whole_house[i]) / (1 - y_whole_house[i]**(a_whole_house[i] + 1)))
                
        else:
            utilisation_factor_for_heating_whole_house.append(1)
            
    
    
    return dict(time_constant_whole_house=time_constant_whole_house,
                a_whole_house=a_whole_house,
                heat_loss_rate_whole_house=heat_loss_rate_whole_house,
                y_whole_house=y_whole_house,
                utilisation_factor_for_heating_whole_house=utilisation_factor_for_heating_whole_house
                )

