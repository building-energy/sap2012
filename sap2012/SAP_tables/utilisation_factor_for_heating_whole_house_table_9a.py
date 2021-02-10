# -*- coding: utf-8 -*-

def utilisation_factor_for_heating_whole_house_table_9a(
        heat_transfer_coefficient,
        total_internal_and_solar_gains,
        mean_internal_temp_whole_dwelling,
        monthly_external_temperature_table_U1,
        thermal_mass_parameter,
        heat_loss_parameter
        ):
    """Utilisation factor calculations for heating from Table 9a.
    
    :param heat_transfer_coefficient: See (39), in W/K.
    :type heat_transfer_coefficient: list(float)
        
    :param total_internal_and_solar_gains: See (84) in W.
    :type total_internal_and_solar_gains: list(float)
    
    :param mean_internal_temp_whole_dwelling: See (92) in degC.
    :type mean_internal_temp_whole_dwelling: float
        
    :param monthly_external_temperature_table_U1:
    :type monthly_external_temperature_table_U1: list(float)
        
    :param thermal_mass_parameter: See (35), in kJ/m2K.
    :type thermal_mass_parameter: float
        
    :param heat_loss_parameter: See (40), in W/m2K.
    :type heat_loss_parameter: list(float)
        
    :returns: A dictionary with keys of (
        time_constant_whole_house,
        a_whole_house,
        heat_loss_rate_whole_house,
        y_whole_house,
        utilisation_factor_for_heating_whole_house
        )
    
    - **time_constant_whole_house** (`list` (`float`)) -
        
    - **a_whole_house** (`list` (`float`)) -
        
    - **heat_loss_rate_whole_house** (`list` (`float`)) -
        
    - **y_whole_house** (`list` (`float`)) -
        
    - **utilisation_factor_for_heating_whole_house** (`list` (`float`)) -
        
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

