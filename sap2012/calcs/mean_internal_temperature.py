# -*- coding: utf-8 -*-


def mean_internal_temperature (
        mean_internal_temperature_living_room_T1_Table_9c,
        mean_internal_temperature_rest_of_dwelling_T2_table_9c,
        living_room_area,
        total_floor_area,
        temperature_adjustment_table_4e
        ):
    
    """Calculates Mean Internal Temperature, section 7
    
    :param utilisation_factor_for_gains_living_room_table_9a: see (86)
    :type utilisation_factor_for_gains_living_room_table_9a: list of floats
    
    :param mean_internal_temperature_living_room_T1_Table_9c: see (87) in oC
    :type mean_internal_temperature_living_room_T1_Table_9c: list of floats
    
    
    :param utilisation_factor_for_gains_rest_of_dwelling_table_9a: see (89)
    :type utilisation_factor_for_gains_rest_of_dwelling_table_9a: list of floats
    
    :param mean_internal_temperature_rest_of_dwelling_T2_table_9c: see (90) in oC
    :type mean_internal_temperature_rest_of_dwelling_T2_table_9c: list of floats
    
     return (
            living_area_fraction,
            mean_internal_temp_whole_dwelling
            )
    
    :param living_room_area: see (91) in m
    :type living_room_area: float
    
    :param total_floor_area: in m
    :type total_floor_area: float
    
    :param temperature_adjustment_table_4e: see (93) in oC
        adjustments founf in table 4a
    :type temperature_adjustment_table_4e: float
    
    :param mean_internal_temp_whole_dwelling: see (92) in oC
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