# -*- coding: utf-8 -*-

def ventilation_rates(
        number_of_chimneys_main_heating,
        number_of_chimneys_secondary_heating,
        number_of_chimneys_other,
        number_of_open_flues_main_heating,
        number_of_open_flues_secondary_heating,
        number_of_open_flues_other,
        number_of_intermittant_fans_total,
        number_of_passive_vents_total,
        number_of_flueless_gas_fires_total,
        dwelling_volume,
        air_permeability_value_q50,
        number_of_storeys_in_the_dwelling,
        structural_infiltration,
        suspended_wooden_ground_floor_infiltration,
        no_draft_lobby_infiltration,
        percentage_of_windows_and_doors_draught_proofed,
        number_of_sides_on_which_dwelling_is_sheltered,
        monthly_average_wind_speed,
        applicable_case,
        mechanical_ventilation_air_change_rate_through_system,
        exhaust_air_heat_pump_using_Appendix_N,
        mechanical_ventilation_throughput_factor,
        efficiency_allowing_for_in_use_factor,
        ):
    
    """Calculates the ventilation rates, Section 2.
    
    :param number_of_chimneys_main_heating:
    :type number_of_chimneys_main_heating: int

    :param number_of_chimneys_secondary_heating:
    :type number_of_chimneys_secondary_heating: int
    
    :param number_of_chimneys_other:
    :type number_of_chimneys_other: int
    
    :param number_of_open_flues_main_heating:
    :type number_of_open_flues_main_heating: int

    :param number_of_open_flues_secondary_heating:
    :type number_of_open_flues_secondary_heating: int
    
    :param number_of_open_flues_other:
    :type number_of_open_flues_other: int
    
    :param number_of_intermittant_fans_total:
    :type number_of_intermittant_fans_total: int
    
    :param number_of_passive_vents_total:
    :type number_of_passive_vents_total: int
    
    :param number_of_flueless_gas_fires_total:
    :type number_of_flueless_gas_fires_total: int
    
    :param dwelling_volume: See (5).
    :type dwelling_volume: float
    
    :param air_permeability_value_q50: See (17). Use None if not carried out.
    :type air_permeability_value_q50: float or None
    
    :param number_of_storeys_in_the_dwelling: See (9).
    :type number_of_storeys_in_the_dwelling: int
    
    :param structural_infiltration: See (11).
    :type structural_infiltration: float
    
    :param suspended_wooden_ground_floor_infiltration: See (12).
    :type suspended_wooden_ground_floor_infiltration: float
    
    :param no_draft_lobby_infiltration: See (13).
    :type no_draft_lobby_infiltration: float
    
    :param percentage_of_windows_and_doors_draught_proofed: See (14).
    :type percentage_of_windows_and_doors_draught_proofed: float
    
    :param number_of_sides_on_which_dwelling_is_sheltered: See (19).
    :type number_of_sides_on_which_dwelling_is_sheltered: int
    
    :param monthly_average_wind_speed: A list of the monthly wind speeds.
        12 items, from Jan to Dec, see (22).
    :type monthly_average_wind_speed: list (float)
    
    :param applicable_case: One of the following options:  
        'balanced mechanical ventilation with heat recovery';
        'balanced mechanical ventilation without heat recovery';
        'whole house extract ventilation or positive input ventilation from outside';
        or 'natural ventilation or whole house positive input ventilation from loft'.
    :type applicable_case: str
    
    :param mechanical_ventilation_air_change_rate_through_system: See (23a).
    :type mechanical_ventilation_air_change_rate_through_system: float
    
    :param exhaust_air_heat_pump_using_Appendix_N: 
        True if exhaust air heat pump using Appendix N, otherwise False.
    :type exhaust_air_heat_pump_using_Appendix_N: bool
    
    :param mechanical_ventilation_throughput_factor: F_mv, see Equation N4.
    :type mechanical_ventilation_throughput_factor: float
    
    :param efficiency_allowing_for_in_use_factor: In %, see (23c).
    :type efficiency_allowing_for_in_use_factor: float
    
    
    :returns: A tuple of (
            number_of_chimneys_total,
            number_of_chimneys_m3_per_hour,
            number_of_open_flues_total,
            number_of_open_flues_m3_per_hour,
            number_of_intermittant_fans_m3_per_hour,
            number_of_passive_vents_m3_per_hour,
            number_of_flueless_gas_fires_m3_per_hour,
            infiltration_due_to_chimnneys_flues_fans_PSVs,
            additional_infiltration,
            window_infiltration,
            infiltration_rate,
            infiltration_rate2,
            shelter_factor,
            infiltration_rate_incorporating_shelter_factor,
            wind_factor,
            adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed,
            exhaust_air_heat_pump_air_change_rate_through_system,
            effective_air_change_rate
            )
    
    - **number_of_chimneys_total** (`int`) -
    
    - **number_of_chimneys_m3_per_hour** (`float`) - See (6a).
    
    - **number_of_open_flues_total** (`int`) -
    
    - **number_of_open_flues_m3_per_hour** (`float`) - See (6b).
    
    - **infiltration_due_to_chimenys_flues_fans_PSVs** (`float`) - See (8).
    
    - **additional_infiltration** (`float`) - See (10).
    
    - **window_infiltration** (`float`) - See (15).
    
    - **infiltration_rate** (`float`) - See (16).
    
    - **infiltration_rate2** (`float`) - See (18).
    
    - **shelter_factor** (`float`) - See (20).
    
    - **infiltration_rate_incorporating_shelter_factor** (`float`) - See (21).
    
    - **wind_factor** list (`float`) - See (22a).
    
    - **adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed**: list (`float`) - See (22b).
    
    - **exhaust_air_heat_pump_air_change_rate_through_system** (`float`) - See (23b).
    
    - **effective_air_change_rate** list (`float`) - See (25).

    :rtype: tuple

    """
    
    # number_of_chimneys
    number_of_chimneys_total=(number_of_chimneys_main_heating +
                              number_of_chimneys_secondary_heating + 
                              number_of_chimneys_other)
    
    number_of_chimneys_m3_per_hour=number_of_chimneys_total * 40.0
    
    # number_of_open_flues
    number_of_open_flues_total=(number_of_open_flues_main_heating +
                              number_of_open_flues_secondary_heating + 
                              number_of_open_flues_other)
    
    number_of_open_flues_m3_per_hour=number_of_open_flues_total * 20.0
    
    # number_of_intermittant_fans
    number_of_intermittant_fans_m3_per_hour=number_of_intermittant_fans_total * 10.0
    
    # number_of_passive_vents
    number_of_passive_vents_m3_per_hour=number_of_passive_vents_total * 10.0
    
    # number_of_flueless_gas_fires
    number_of_flueless_gas_fires_m3_per_hour=number_of_flueless_gas_fires_total * 40.0
    
    # infiltration_due_to_chimenys_flues_fans_PSVs
    infiltration_due_to_chimneys_flues_fans_PSVs=((number_of_chimneys_m3_per_hour +
                                                   number_of_open_flues_m3_per_hour +
                                                   number_of_intermittant_fans_m3_per_hour +
                                                   number_of_passive_vents_m3_per_hour +
                                                   number_of_flueless_gas_fires_m3_per_hour) /
                                                  dwelling_volume)
    
    if air_permeability_value_q50 == 0:
        
        additional_infiltration=(number_of_storeys_in_the_dwelling-1)*0.1
        
        window_infiltration=0.25 - (0.2 * percentage_of_windows_and_doors_draught_proofed / 100.0)    
    
        infiltration_rate=(infiltration_due_to_chimneys_flues_fans_PSVs + 
                           additional_infiltration + 
                           structural_infiltration + 
                           suspended_wooden_ground_floor_infiltration + 
                           no_draft_lobby_infiltration + 
                           window_infiltration
                           )
    
        infiltration_rate2=infiltration_rate
    
    else:
        
        additional_infiltration=None
        window_infiltration=None
        
        infiltration_rate=None
        infiltration_rate2=((air_permeability_value_q50 / 20) + 
                            infiltration_due_to_chimneys_flues_fans_PSVs)
        
    # shelter_factor
    shelter_factor = 1 - (0.075 * number_of_sides_on_which_dwelling_is_sheltered)
    
    # infiltration_rate_incorporating_shelter_factor
    infiltration_rate_incorporating_shelter_factor = (infiltration_rate2 * 
                                                      shelter_factor)
    
    # wind_factor
    wind_factor=[None]*12
    for i in range(12):
        wind_factor[i]=monthly_average_wind_speed[i] / 4.0
        
    # adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed
    adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed=[None]*12
    for i in range(12):
        adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed[i] = (
            infiltration_rate_incorporating_shelter_factor * 
            wind_factor[i]
            )
    
    # exhaust_air_heat_pump_air_change_rate_through_system
    if applicable_case in ['balanced mechanical ventilation with heat recovery',
                           'balanced mechanical ventilation without heat recovery',
                           'whole house extract ventilation or positive input ventilation from outside']:
        if exhaust_air_heat_pump_using_Appendix_N:
            exhaust_air_heat_pump_air_change_rate_through_system = (
                    mechanical_ventilation_air_change_rate_through_system * 
                    mechanical_ventilation_throughput_factor)
        else:
            exhaust_air_heat_pump_air_change_rate_through_system = \
                    mechanical_ventilation_air_change_rate_through_system
    else:
        exhaust_air_heat_pump_air_change_rate_through_system = None
        
    # effective_air_change_rate
    effective_air_change_rate=[None]*12
    
    if applicable_case=='balanced mechanical ventilation with heat recovery':
        for i in range(12):
            effective_air_change_rate[i]=(
                adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed[i] + 
                exhaust_air_heat_pump_air_change_rate_through_system * 
                (1.0 - efficiency_allowing_for_in_use_factor / 100.0)
                )
            
    elif applicable_case=='balanced mechanical ventilation without heat recovery':
        for i in range(12):
            effective_air_change_rate[i]=(
                adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed[i] + 
                exhaust_air_heat_pump_air_change_rate_through_system)
            
    elif applicable_case=='whole house extract ventilation or positive input ventilation from outside':
        for i in range(12):
            if (adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed[i] 
                < 0.5 * exhaust_air_heat_pump_air_change_rate_through_system):
                effective_air_change_rate[i]=exhaust_air_heat_pump_air_change_rate_through_system
            else:
                effective_air_change_rate[i]=(
                    adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed[i] + 
                    0.5 * exhaust_air_heat_pump_air_change_rate_through_system)
        
    elif applicable_case=='natural ventilation or whole house positive input ventilation from loft':
        for i in range(12):
            if adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed[i]>1:
                effective_air_change_rate[i]=adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed[i]
            else:
                effective_air_change_rate[i]=0.5 + (adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed[i]**2 * 0.5)
                
    
    return (
            number_of_chimneys_total,
            number_of_chimneys_m3_per_hour,
            number_of_open_flues_total,
            number_of_open_flues_m3_per_hour,
            number_of_intermittant_fans_m3_per_hour,
            number_of_passive_vents_m3_per_hour,
            number_of_flueless_gas_fires_m3_per_hour,
            infiltration_due_to_chimneys_flues_fans_PSVs,
            additional_infiltration,
            window_infiltration,
            infiltration_rate,
            infiltration_rate2,
            shelter_factor,
            infiltration_rate_incorporating_shelter_factor,
            wind_factor,
            adjusted_infiltration_rate_allowing_for_shelter_and_wind_speed,
            exhaust_air_heat_pump_air_change_rate_through_system,
            effective_air_change_rate
            )