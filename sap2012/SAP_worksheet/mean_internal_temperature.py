# -*- coding: utf-8 -*-


def mean_internal_temperature (
        mean_internal_temperature_living_room_T1_Table_9c,
        mean_internal_temperature_rest_of_dwelling_T2_table_9c,
        living_room_area,
        total_floor_area,
        temperature_adjustment_table_4e
        ):
    
    """Calculates Mean Internal Temperature, Section 7.
    
    :param mean_internal_temperature_living_room_T1_Table_9c: See (87) in degC.
    :type mean_internal_temperature_living_room_T1_Table_9c: list (float)
    
    :param mean_internal_temperature_rest_of_dwelling_T2_table_9c: See (90) in degC.
    :type mean_internal_temperature_rest_of_dwelling_T2_table_9c: list (float)
    
    :param living_room_area: See (91) in m.
    :type living_room_area: float
    
    :param total_floor_area: in m.
    :type total_floor_area: float
    
    :param temperature_adjustment_table_4e: See (93) in degC.
        Adjustments found in table 4a.
    :type temperature_adjustment_table_4e: float
    
    :returns: A dictionary with keys of (
            living_area_fraction,
            mean_internal_temp_whole_dwelling
            )
    
    - **living_area_fraction** (float): 
     
    - **mean_internal_temp_whole_dwelling** (float): See (92) in degC.
    
    """
    
    living_area_fraction = living_room_area / total_floor_area
    
    mean_internal_temp_whole_dwelling =[]
    for i in range(12):
        mean_internal_temp_whole_dwelling.append(living_area_fraction * 
                                                 mean_internal_temperature_living_room_T1_Table_9c[i] + 
                                                (1 - living_area_fraction) * 
                                                mean_internal_temperature_rest_of_dwelling_T2_table_9c[i] +
                                                temperature_adjustment_table_4e)
    
    
    
    
    return dict(living_area_fraction=living_area_fraction,
                mean_internal_temp_whole_dwelling=mean_internal_temp_whole_dwelling
                )