# -*- coding: utf-8 -*-


def Utilisation_factor_for_heating(
        heat_transfer_coefficient,
        total_internal_and_solar_gains,
        internal_temperature,
        external_temperature,
        thermal_mass_parameter,
        heat_loss_parameter
        ):
    
    time_constant = []
    for i in range(12):
        time_constant.append(thermal_mass_parameter/
                             (3.6 * heat_loss_parameter[i]))

    a = []
    for i in range(12):
        a.append(1 + time_constant[i]/15)
        
    heat_loss_rate = []
    for i in range(12):
        heat_loss_rate.append(heat_transfer_coefficient[i] * 
                              (internal_temperature - external_temperature[i]))
        
    y = []
    for i in range(12):
        if heat_loss_rate[i] == 0:
            y.append(10^6)
            
        else:
            y.append(total_internal_and_solar_gains[i] / heat_loss_rate[i])
            
            
    utilisation_factor_for_heating = []
    for i in range(12):
        if y[i] ==1:
            utilisation_factor_for_heating.append(a[i] / 
                                                  (a[i] + 1))
            
        if y[i] > 0:
            utilisation_factor_for_heating.append((1-y[i]^a[i]) / (1 - y[i]^(a[i] + 1)))
                
        else:
            utilisation_factor_for_heating.append(1)
            
    
    
    return(
            time_constant,
            a,
            heat_loss_rate,
            y,
            utilisation_factor_for_heating
            )
            
            
            
            
            
            
            