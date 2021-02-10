# -*- coding: utf-8 -*-


def temperature_reduction_when_heating_is_off_table_9b(
        time_constant,
        hours_heating_is_off_1_weekday_living_room,
        hours_heating_is_off_2_weekday_living_room,
        hours_heating_is_off_1_weekend_living_room,
        hours_heating_is_off_2_weekend_living_room,
        hours_heating_is_off_1_weekday_rest_of_dwelling,
        hours_heating_is_off_2_weekday_rest_of_dwelling,
        hours_heating_is_off_1_weekend_rest_of_dwelling,
        hours_heating_is_off_2_weekend_rest_of_dwelling,
        temperature_during_heating_living_room,
        temperature_during_heating_rest_of_dwelling,
        responsiveness_of_heating_system,
        monthly_external_temperature_table_U1,
        utilisation_factor_for_heating_living_room,
        utilisation_factor_for_heating_rest_of_dwelling,
        heat_transfer_coefficient,
        total_internal_and_solar_gains
        ):
    """Calculates temperature reduction as given in Table 9b.
    
    :param time_constant:
    :type time_constant: list(float)
        
    :param hours_heating_is_off_1_weekday_living_room:
    :type hours_heating_is_off_1_weekday_living_room: float
        
    :param hours_heating_is_off_2_weekday_living_room:
    :type hours_heating_is_off_2_weekday_living_room: float
        
    :param hours_heating_is_off_1_weekend_living_room:
    :type hours_heating_is_off_1_weekend_living_room: float
        
    :param hours_heating_is_off_2_weekend_living_room:
    :type hours_heating_is_off_2_weekend_living_room: float
        
    :param hours_heating_is_off_1_weekday_rest_of_dwelling:
    :type hours_heating_is_off_1_weekday_rest_of_dwelling: float
        
    :param hours_heating_is_off_2_weekday_rest_of_dwelling:
    :type hours_heating_is_off_2_weekday_rest_of_dwelling: float
        
    :param hours_heating_is_off_1_weekend_rest_of_dwelling:
    :type hours_heating_is_off_1_weekend_rest_of_dwelling: float
        
    :param hours_heating_is_off_2_weekend_rest_of_dwelling:
    :type hours_heating_is_off_2_weekend_rest_of_dwelling: float
        
    :param temperature_during_heating_living_room:
    :type temperature_during_heating_living_room: float
        
    :param temperature_during_heating_rest_of_dwelling:
    :type temperature_during_heating_rest_of_dwelling: list(float)
        
    :param responsiveness_of_heating_system: 
    :type responsiveness_of_heating_system: float
        
    :param monthly_external_temperature_table_U1:
    :type monthly_external_temperature_table_U1: list(float)
        
    :param utilisation_factor_for_heating_living_room:
    :type utilisation_factor_for_heating_living_room: list(float)
        
    :param utilisation_factor_for_heating_rest_of_dwelling:
    :type utilisation_factor_for_heating_rest_of_dwelling: list(float)
        
    :param heat_transfer_coefficient: See (39), in W/K.
    :type heat_transfer_coefficient: list(float)
        
    :param total_internal_and_solar_gains: See (84) in W.
    :type total_internal_and_solar_gains: list(float)
        
    :returns: A dictionary with keys (
        t_c,
        internal_temperature_without_heating_living_room,
        internal_temperature_without_heating_rest_of_dwelling,
        temperature_reduction_when_heating_is_off_1_weekday_living_room,
        temperature_reduction_when_heating_is_off_2_weekday_living_room,
        temperature_reduction_when_heating_is_off_1_weekend_living_room,
        temperature_reduction_when_heating_is_off_2_weekend_living_room,
        temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling,
        temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling,
        temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling,
        temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling
        )
    
    - **t_c** (`list` (`float`)) -
    
    - **internal_temperature_without_heating_living_room** (`list` (`float`)) -
    
    - **internal_temperature_without_heating_rest_of_dwelling** (`list` (`float`)) -
    
    - **temperature_reduction_when_heating_is_off_1_weekday_living_room** (`list` (`float`)) -
    
    - **temperature_reduction_when_heating_is_off_2_weekday_living_room** (`list` (`float`)) -
    
    - **temperature_reduction_when_heating_is_off_1_weekend_living_room** (`list` (`float`)) -
    
    - **temperature_reduction_when_heating_is_off_2_weekend_living_room** (`list` (`float`)) -
    
    - **temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling** (`list` (`float`)) -
    
    - **temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling** (`list` (`float`)) -
    
    - **temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling** (`list` (`float`)) -
    
    - **temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling** (`list` (`float`)) -
        
    :rtype: dict
    
    """
    
    t_c = []
    for i in range(12):
        t_c.append(4 + 0.25 * time_constant[i])
        
    
    internal_temperature_without_heating_living_room = []
    for i in range(12):
        internal_temperature_without_heating_living_room.append((1 - responsiveness_of_heating_system) + 
                                                    responsiveness_of_heating_system * 
                                                    (monthly_external_temperature_table_U1[i] + 
                                                     (utilisation_factor_for_heating_living_room[i] * total_internal_and_solar_gains[i] / 
                                                      heat_transfer_coefficient[i])))
        
    
    internal_temperature_without_heating_rest_of_dwelling = []
    for i in range(12):
        internal_temperature_without_heating_rest_of_dwelling.append((1 - responsiveness_of_heating_system) + 
                                                    responsiveness_of_heating_system * 
                                                    (monthly_external_temperature_table_U1[i] + 
                                                     (utilisation_factor_for_heating_rest_of_dwelling[i] * total_internal_and_solar_gains[i] / 
                                                      heat_transfer_coefficient[i])))
        
    temperature_reduction_when_heating_is_off_1_weekday_living_room = []
    for i in range(12):
        if hours_heating_is_off_1_weekday_living_room > t_c[i]:
            temperature_reduction_when_heating_is_off_1_weekday_living_room.append((temperature_during_heating_living_room - 
                                                                internal_temperature_without_heating_living_room[i]) * 
                                                                (hours_heating_is_off_1_weekday_living_room - 0.5 * t_c[i]) / 24)
            
            
        else:
            temperature_reduction_when_heating_is_off_1_weekday_living_room.append(0.5 * hours_heating_is_off_1_weekday_living_room**2 * 
                                                               (temperature_during_heating_living_room - 
                                                                internal_temperature_without_heating_living_room[i]) / 
                                                                (24 * t_c[i]))
                                                               
                                                               
                                                               
    temperature_reduction_when_heating_is_off_2_weekday_living_room = []
    for i in range(12):
        if hours_heating_is_off_2_weekday_living_room > t_c[i]:
            temperature_reduction_when_heating_is_off_2_weekday_living_room.append((temperature_during_heating_living_room - 
                                                                internal_temperature_without_heating_living_room[i]) * 
                                                                (hours_heating_is_off_2_weekday_living_room - 0.5 * t_c[i]) / 24)
            
            
        else:
            temperature_reduction_when_heating_is_off_2_weekday_living_room.append(0.5 * hours_heating_is_off_2_weekday_living_room**2 * 
                                                               (temperature_during_heating_living_room - 
                                                                internal_temperature_without_heating_living_room[i]) / 
                                                                (24 * t_c[i]))
                                                               
                                                               
    temperature_reduction_when_heating_is_off_1_weekend_living_room = []
    for i in range(12):
        if hours_heating_is_off_1_weekend_living_room > t_c[i]:
            temperature_reduction_when_heating_is_off_1_weekend_living_room.append((temperature_during_heating_living_room - 
                                                                internal_temperature_without_heating_living_room[i]) * 
                                                                (hours_heating_is_off_1_weekend_living_room - 0.5 * t_c[i]) / 24)
            
            
        else:
            temperature_reduction_when_heating_is_off_1_weekend_living_room.append(0.5 * hours_heating_is_off_1_weekend_living_room**2 * 
                                                               (temperature_during_heating_living_room - 
                                                                internal_temperature_without_heating_living_room[i]) / 
                                                                (24 * t_c[i]))
                                                               
                                                               
                                                               
    temperature_reduction_when_heating_is_off_2_weekend_living_room = []
    for i in range(12):
        if hours_heating_is_off_2_weekend_living_room > t_c[i]:
            temperature_reduction_when_heating_is_off_2_weekend_living_room.append((temperature_during_heating_living_room - 
                                                                internal_temperature_without_heating_living_room[i]) * 
                                                                (hours_heating_is_off_2_weekend_living_room - 0.5 * t_c[i]) / 24)
            
            
        else:
            temperature_reduction_when_heating_is_off_2_weekend_living_room.append(0.5 * hours_heating_is_off_2_weekend_living_room**2 * 
                                                               (temperature_during_heating_living_room - 
                                                                internal_temperature_without_heating_living_room[i]) / 
                                                                (24 * t_c[i]))
                                                               
    

    temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling = []
    for i in range(12):
        if hours_heating_is_off_1_weekday_rest_of_dwelling > t_c[i]:
            temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling.append((temperature_during_heating_rest_of_dwelling[i] - 
                                                                internal_temperature_without_heating_rest_of_dwelling[i]) * 
                                                                (hours_heating_is_off_1_weekday_rest_of_dwelling - 0.5 * t_c[i]) / 24)
            
            
        else:
            temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling.append(0.5 * hours_heating_is_off_1_weekday_rest_of_dwelling**2 * 
                                                               (temperature_during_heating_rest_of_dwelling[i] - 
                                                                internal_temperature_without_heating_rest_of_dwelling[i]) / 
                                                                (24 * t_c[i]))
                                                               
                                                               
                                                               
    temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling = []
    for i in range(12):
        if hours_heating_is_off_2_weekday_rest_of_dwelling > t_c[i]:
            temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling.append((temperature_during_heating_rest_of_dwelling[i] - 
                                                                internal_temperature_without_heating_rest_of_dwelling[i]) * 
                                                                (hours_heating_is_off_2_weekday_rest_of_dwelling - 0.5 * t_c[i]) / 24)
            
            
        else:
            temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling.append(0.5 * hours_heating_is_off_2_weekday_rest_of_dwelling**2 * 
                                                               (temperature_during_heating_rest_of_dwelling[i] - 
                                                                internal_temperature_without_heating_rest_of_dwelling[i]) / 
                                                                (24 * t_c[i]))
                                                               
                                                               
    temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling = []
    for i in range(12):
        if hours_heating_is_off_1_weekend_rest_of_dwelling > t_c[i]:
            temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling.append((temperature_during_heating_rest_of_dwelling[i] - 
                                                                internal_temperature_without_heating_rest_of_dwelling[i]) * 
                                                                (hours_heating_is_off_1_weekend_rest_of_dwelling - 0.5 * t_c[i]) / 24)
            
            
        else:
            temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling.append(0.5 * hours_heating_is_off_1_weekend_rest_of_dwelling**2 * 
                                                               (temperature_during_heating_rest_of_dwelling[i] - 
                                                                internal_temperature_without_heating_rest_of_dwelling[i]) / 
                                                                (24 * t_c[i]))
                                                               
                                                               
                                                               
    temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling = []
    for i in range(12):
        if hours_heating_is_off_2_weekend_rest_of_dwelling > t_c[i]:
            temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling.append((temperature_during_heating_rest_of_dwelling[i] - 
                                                                internal_temperature_without_heating_rest_of_dwelling[i]) * 
                                                                (hours_heating_is_off_2_weekend_rest_of_dwelling - 0.5 * t_c[i]) / 24)
            
            
        else:
            temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling.append(0.5 * hours_heating_is_off_2_weekend_rest_of_dwelling**2 * 
                                                               (temperature_during_heating_rest_of_dwelling[i] - 
                                                                internal_temperature_without_heating_rest_of_dwelling[i]) / 
                                                                (24 * t_c[i]))                                                           
                                                               
    return dict(t_c=t_c,
                internal_temperature_without_heating_living_room=internal_temperature_without_heating_living_room,
                internal_temperature_without_heating_rest_of_dwelling=internal_temperature_without_heating_rest_of_dwelling,
                temperature_reduction_when_heating_is_off_1_weekday_living_room=temperature_reduction_when_heating_is_off_1_weekday_living_room,
                temperature_reduction_when_heating_is_off_2_weekday_living_room=temperature_reduction_when_heating_is_off_2_weekday_living_room,
                temperature_reduction_when_heating_is_off_1_weekend_living_room=temperature_reduction_when_heating_is_off_1_weekend_living_room,
                temperature_reduction_when_heating_is_off_2_weekend_living_room=temperature_reduction_when_heating_is_off_2_weekend_living_room,
                temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling=temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling,
                temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling=temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling,
                temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling=temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling,
                temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling=temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling
                )
