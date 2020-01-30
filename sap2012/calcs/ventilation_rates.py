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
        ):
    
    """Calculates the ventilation rates, Section 2
    
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
    
    :param dwelling_volume: see (5)
    :type dwelling_volume: float
    
    :param air_permeability_value_q50: see (17). Use None if not carried out.
    :type air_permeability_value_q50: float or None
    
    :param number_of_storeys_in_the_dwelling: see (9)
    :type number_of_storeys_in_the_dwelling: int
    
    :param structural_infiltration: see (11)
    :type structural_infiltration: float
    
    :param suspended_wooden_ground_floor_infiltration: see (12)
    :type suspended_wooden_ground_floor_infiltration: float
    
    :param no_draft_lobby_infiltration: see (13)
    :type no_draft_lobby_infiltration: float
    
    :param percentage_of_windows_and_doors_draught_proofed: see (14)
    :type percentage_of_windows_and_doors_draught_proofed: float
    
    :param number_of_sides_on_which_dwelling_is_sheltered: see (19)
    :type number_of_sides_on_which_dwelling_is_sheltered: int
    
    
    
    
    :return:(
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
            )
    
        number_of_chimneys_total: (int)
        number_of_chimneys_m3_per_hour: (float), see (6a)
        number_of_open_flues_total: (int)
        number_of_open_flues_m3_per_hour: (float), see (6b)
        infiltration_due_to_chimenys_flues_fans_PSVs: (float), see (8)
        additional_infiltration: (float), see (10)
        window_infiltration: (float), see (15)
        infiltration_rate: (float), see (16)
        infiltration_rate2: (float), see (18)
        shelter_factor: (float), see (20)
        infiltration_rate_incorporating_shelter_factor: (float), see (21)

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
    
    if air_permeability_value_q50 is None:
        
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
        
        infiltration_rate2=((air_permeability_value_q50 / 20) + 
                            infiltration_due_to_chimneys_flues_fans_PSVs)
        
    # shelter_factor
    shelter_factor = 1 - (0.075 - number_of_sides_on_which_dwelling_is_sheltered)
    
    # infiltration_rate_incorporating_shelter_factor
    infiltration_rate_incorporating_shelter_factor = (infiltration_rate2 * 
                                                      shelter_factor)
    
    
    
    return