# -*- coding: utf-8 -*-


def Heating_requirement (
        temperature_reduction_when_heating_is_off_1_weekday_living_room,
        temperature_reduction_when_heating_is_off_2_weekday_living_room,
        temperature_reduction_when_heating_is_off_1_weekend_living_room,
        temperature_reduction_when_heating_is_off_2_weekend_living_room,
        temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling,
        temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling,
        temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling,
        temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling,
        temperature_during_heating_living_room,
        temperature_during_heating_rest_of_dwelling,
        temperature_adjustment_table_4e
        ):
    
    
    
    T_weekday_living_room = [] 
    for i in range(12):
        T_weekday_living_room.append(temperature_during_heating_living_room - 
                                     (temperature_reduction_when_heating_is_off_1_weekday_living_room[i] + 
                                      temperature_reduction_when_heating_is_off_2_weekday_living_room[i]))
    
    T_weekend_living_room = [] 
    for i in range(12):
        T_weekend_living_room.append(temperature_during_heating_living_room - 
                                     (temperature_reduction_when_heating_is_off_1_weekend_living_room[i] + 
                                      temperature_reduction_when_heating_is_off_2_weekend_living_room[i]))
        
        
        
    mean_internal_temperature_living_room_T1_Table_9c = []
    for i in range(12):
        mean_internal_temperature_living_room_T1_Table_9c.append((5 * T_weekday_living_room[i] + 
                                             2 * T_weekend_living_room[i] ) / 7)
        
        
        
        
    T_weekday_rest_of_dwelling = []
    for i in range(12):
        T_weekday_rest_of_dwelling.append(temperature_during_heating_rest_of_dwelling[i] - 
                                          (temperature_reduction_when_heating_is_off_1_weekday_rest_of_dwelling[i] + 
                                           temperature_reduction_when_heating_is_off_2_weekday_rest_of_dwelling[i]))
    
    T_weekend_rest_of_dwelling = [] 
    for i in range(12):
        T_weekend_rest_of_dwelling.append(temperature_during_heating_rest_of_dwelling[i] - 
                                          (temperature_reduction_when_heating_is_off_1_weekend_rest_of_dwelling[i] + 
                                           temperature_reduction_when_heating_is_off_2_weekend_rest_of_dwelling[i]))
        
        
    mean_internal_temperature_rest_of_dwelling_T2_table_9c = []
    for i in range(12):
        mean_internal_temperature_rest_of_dwelling_T2_table_9c.append(((5 * T_weekday_rest_of_dwelling[i] + 
                                             2 * T_weekend_rest_of_dwelling[i]) / 7) + temperature_adjustment_table_4e)
        

        
    
    return(
            T_weekday_living_room,
            T_weekend_living_room,
            mean_internal_temperature_living_room_T1_Table_9c,
            T_weekday_rest_of_dwelling,
            T_weekend_rest_of_dwelling,
            mean_internal_temperature_rest_of_dwelling_T2_table_9c
            )
        
        
        
    
    
    
    