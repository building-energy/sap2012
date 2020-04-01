# -*- coding: utf-8 -*-


def mean_internal_temperature (
        temperature_during_heating_periods_living_room,
        utilisation_factor_for_gains_living_room_table_9a,
        mean_internal_temperature_living_room_T1_Table_9c,
        temperature_during_heating_periods_rest_of_dwelling,
        utilisation_factor_for_gains_rest_of_dwelling_table_9a,
        mean_internal_temperature_rest_of_dwelling_T2_table_9c,
        living_room_area,
        total_floor_area,
        temperature_adjustment_table_4e
        ):
    
    """Calculates Mean Internal Temperature, section 7
    
    :param temperature_during_heating_periods_living_room:
    :type temperature_during_heating_periods_living_room: float
    
    :param utilisation_factor_for_gains_living_room_table_9a:
    :type utilisation_factor_for_gains_living_room_table_9a: float
    
    :param mean_internal_temperature_living_room_T1_Table_9c:
    :type mean_internal_temperature_living_room_T1_Table_9c: float
    
    :param temperature_during_heating_periods_rest_of_dwelling:
    :type temperature_during_heating_periods_rest_of_dwelling: float
    
    :param utilisation_factor_for_gains_rest_of_dwelling_table_9a:
    :type utilisation_factor_for_gains_rest_of_dwelling_table_9a: float
    
    :param mean_internal_temperature_rest_of_dwelling_T2_table_9c:
    :type mean_internal_temperature_rest_of_dwelling_T2_table_9c: float
    
    :param living_room_area:
    :type living_room_area: float
    
    :param total_floor_area:
    :type total_floor_area: float
    
    :param temperature_adjustment_table_4e:
    :type temperature_adjustment_table_4e: float
    
    :param mean_internal_temp_whole_dwelling:
    :type mean_internal_temp_whole_dwelling: float
    
    """
    
    living_area_fraction = living_room_area / total_floor_area
    
    mean_internal_temp_whole_dwelling =[]
    for i in range(12):
        mean_internal_temp_whole_dwelling.append(living_area_fraction * 
                                                 mean_internal_temperature_living_room_T1_Table_9c[i] + 
                                                (1 - living_area_fraction) * 
                                                mean_internal_temperature_rest_of_dwelling_T2_table_9c[i] +
                                                temperature_adjustment_table_4e)
    
    
    
    
    return (
            living_area_fraction,
            mean_internal_temp_whole_dwelling
            )