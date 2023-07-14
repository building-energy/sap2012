# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:31:01 2022

@author: cvskf
"""

from sap2012.SAP_tables import table_u2


def infer_inputs(
        rdsap_inputs
        ):
    """Infers full SAP2012 inputs from an RdSAP input discitonary.
    
    rdsap_input (dict):
        
    returns: Full SAP2012 input dictionay which can then be used in the
        `calculate_worksheet` function.
    rtype: dict
    
    
    """
    
    
    whole_dwelling_dict=rdsap_inputs['whole_dwelling']
    
    building_parts_list=rdsap_inputs['building_parts']
    
    result=[]
    
    for i, building_part_dict in enumerate(building_parts_list):
        
        sap_inputs={}
    
        # overall dwelling dimensions
    
        sap_inputs['overall_dwelling_dimensions']=\
            infer_overall_dwelling_dimensions(
                dimensions_area=building_part_dict['dimensions_area'],
                dimensions_average_room_height=\
                    building_part_dict['dimensions_average_room_height'],
                dimension_type=whole_dwelling_dict['dimension_type'],
                below_the_building_part=\
                    building_part_dict['below_the_building_part']
                )
                
                
        # ventilation_rates
    
    
        # heat_losses_and_heat_loss_parameter
        
        
        # water_heating_requirement
        
        
        # internal_gains_appendix_L
        
        
        # internal_gains
        
        
        # solar_gains_appendix_U3
        
        
        # solar_gains
        
        
        # utilisation_factor_for_heating_table_9a
        
        
        # temperature_reduction_when_heating_is_off_table_9b
        
        
        # heating_requirement_table_9c
        
        
        # mean_internal_temperature
        
        
        # energy_requirements
        
        
        # fuel_costs
        
        
        # SAP_rating
        
        
        # CO2_emissions
        
        
        
        
    
    
    
    
    
    
    
    
        result.append(sap_inputs)
        
    return result
    
    
def infer_overall_dwelling_dimensions(
        dimensions_area,
        dimensions_average_room_height,
        dimension_type,
        below_the_building_part
        ):
    ""
    ""
    
    # S3.5 Conversion to internal dimensions
    
    # If horizontal dimensions are measured externally, they are converted 
    # to overall internal dimensions for use in SAP
    # calculations by application of the appropriate equations in Table S2, 
    # using wall thickness of the main dwelling (or
    # the appropriate wall thickness from Table S3 if thickness is unknown). 
    # The equations are applied on a storey-by-storey basis, for the whole 
    # dwelling (i.e. inclusive of any extension). 
    # This is done after any floor level adjustments (see S3.4).
    
    # Heights are always measured internally within each room and handled 
    # by software according to S3.6.
        
    area=[]
    
    for x in dimensions_area:
        
        if dimension_type=='measured_internally':
            
            area.append(x)
            
        else:  # if 'measured_externally'
            
            raise NotImplementedError  # see Table S2
    
    
    # S3.6 Heights and exposed wall areas
    
    # Heights are measured internally within each room, and 0.25 m is added 
    # by software to each room height except for the lowest storey, 
    # to obtain the storey height. 
    # For this purpose the lowest storey is considered separately for each
    # building part (main dwelling and any extension). 
    # The lowest storey of a building part is the lowest for the dwelling
    # unless it has been indicated as having the same dwelling below. 
    # Gross areas (inclusive of openings) are obtained from the product of 
    # heat loss perimeter (after conversion to internal dimensions if 
    # relevant) and storey height, summed over all storeys. 
    # Party wall area is party wall length multiplied by storey height, 
    # summed over all storeys.

    # For the main dwelling and any extension(s), window and door areas 
    # are deducted from the gross areas to obtain the net wall areas for 
    # the heat loss calculations, except for the door of a flat/maisonette 
    # to an unheated stair or corridor which is deducted from the sheltered 
    # wall area (see S3.13).
    
    # If an alternative wall is present, the area of the alternative wall 
    # is recorded net of any openings in it and the alternative wall is 
    # identified as part of the main wall or extension wall. 
    # This area is subtracted from the net wall area of the building part 
    # prior to the calculation of wall heat losses.
    
    average_storey_height=[]
    
    for i, x in enumerate(dimensions_average_room_height):
        
        if i==0 and not below_the_building_part=='same dwelling below':
            
            h = x + 0.25
            
        else:
            
            h = x
        
        average_storey_height.append(h)
        
    #
    
    return {
        'area':area,
        'average_storey_height':average_storey_height
        }
    
    
def infer_ventilation_rates(
        number_of_open_fireplaces,
        main_heating_system_flue_type,
        second_main_heating_system_flue_type,
        dwelling_type,
        age_band,
        number_of_habitable_rooms,
        floor_construction,
        floor_u_value,
        floor_insulation,
        flats_and_maisonettes_only_heat_loss_corridor,
        main_dwelling_dimensions_area,
        extension_1_dimensions_area,
        extension_2_dimensions_area,
        extension_3_dimensions_area,
        extension_4_dimensions_area,
        flats_and_maisonettes_only_floor_level_relative_to_the_lowest_level_of_the_building,
        draught_proofing,
        region,
        mechanical_ventilation,
        mechanical_ventilation_type
        ):
    """
    """
    # S4 Parameters for ventilation rate
    
    # The parameters needed for calculation of the ventilation rate are obtained from Table S5.
    
    # Table S5 : Ventilation parameters
    
    # Chimneys
    # - Number of open fireplaces
       
    number_of_chimneys_main_heating = number_of_open_fireplaces
    number_of_chimneys_secondary_heating = 0
    number_of_chimneys_other = 0
    
    # Flues
    # - Number of open flues (main and secondary heating systems). 
    #   Flue for solid fuel boiler in unheated space is not counted -- ### TO DO
    raise NotImplementedError
    
    if main_heating_system_flue_type == 'open':
        number_of_open_flues_main_heating = 1
    else:
        number_of_open_flues_main_heating = 0
        
    if second_main_heating_system_flue_type == 'open':
        number_of_open_flues_secondary_heating = 1
    else:
        number_of_open_flues_secondary_heating = 0
        
    number_of_open_flues_other = 0
        
    # Extract fans
    # - Not park home: 
    #   - Age bands A to E - all cases - 0
    #   - Age bands F to G - all cases - 1
    #   - Age bands H to L - up to 2 habitable rooms - 1 
    #                      - 3 to 5 habitable rooms - 2
    #                      - 6 to 8 habitable rooms - 3
    #                      - more than 8 habitable rooms - 4
    # - Park home: 
    #   - Age band F - all cases - 0
    #   - Age bands G, I, K - all cases - 2

    if not dwelling_type == 'park home':
        
        if age_band in ['A','B','C','D','E']:
            
            number_of_intermittant_fans_total = 0
            
        elif age_band in ['F','G']:
            
            number_of_intermittant_fans_total = 1
            
        elif age_band in ['H','I','J','K','L']:
            
            if number_of_habitable_rooms < 3:
                
                number_of_intermittant_fans_total = 1
                
            elif number_of_habitable_rooms < 6:
                
                number_of_intermittant_fans_total = 2
                
            elif number_of_habitable_rooms < 9:
                
                number_of_intermittant_fans_total = 3
                
            else:
                
                number_of_intermittant_fans_total = 4
        
        else:
            
            raise Exception
        
    elif dwelling_type == 'park home':
        
        if age_band == 'F':
            
            number_of_intermittant_fans_total = 0
            
        elif age_band in ['G','I', 'K']:
            
            number_of_intermittant_fans_total = 2
            
        else:
            
            raise Exception
        
    else:
        
        raise Exception
    

    number_of_passive_vents_total = 0
    number_of_flueless_gas_fires_total = 0
    
    
    # Wall infiltration
    # According to the largest area of wall, system build treated as masonry, 
    # and infiltration according to masonry if equal. 
    # Net wall area after deduction of openings is used for this purpose, 
    # walls of roof rooms are not included. 
    # Park home: timber frame
    
    #... from SAP worksheet
    #    Structural infiltration: 
    #    - 0.25 for steel or timber frame or 
    #    - 0.35 for maso nry construction (11)
    #    if both types of wall are present, 
    #    - use the value corresponding to the greater wall area 
    #      (after deducting areas of openings); 
    #    - if equal use 0.35
    
    
    air_permeability_value_q50 = None  
    #structural_infiltration = None ### TO DO - AFTER WALL AREA CALCS HAVE BEEN DONE
    raise NotImplementedError
    
    
    # Floor infiltration (suspended timber ground floor only)
    # - Age band of main dwelling A to E: 
    #   - if floor U-value entered by assessor is < 0.5, sealed; 
    #   - if floor insulation is ‘retro-fitted’ and no U-value is 
    #     supplied, sealed; 
    #   - otherwise unsealed 
    # - Age band of main dwelling F to L: sealed 
    # (the floor infiltration for the whole dwelling is determined by 
    # the floor type of the main dwelling) 
    # - Park home: unsealed suspended timber
    
    # ... from SAP worksheek
    #     If suspended wooden ground floor, enter 0.2 (unsealed) 
    #     or 0.1 (sealed), else enter 0
    
    if floor_construction == 'suspended timber':
        
        if dwelling_type == 'park home':
            
            suspended_wooden_ground_floor_infiltration = 0.2  # unsealed
            
        else:
               
            if age_band in ['A','B','C','D','E']:
                
                if not floor_u_value is None and floor_u_value < 0.5:
                    
                    suspended_wooden_ground_floor_infiltration = 0.1  # sealed
                    
                elif floor_insulation == 'retro-fitted' and floor_u_value is None:
                    
                    suspended_wooden_ground_floor_infiltration = 0.1  # sealed
                    
                else:
                    
                    suspended_wooden_ground_floor_infiltration = 0.2  # unsealed
                
            elif age_band in ['F','G','I','J','K','L']:
                
                suspended_wooden_ground_floor_infiltration = 0.1  # sealed
                
            else:
                
                raise Exception
        
        suspended_wooden_ground_floor_infiltration = None ### TO DO
        
    else:
        
        suspended_wooden_ground_floor_infiltration = 0
            
        
    # Draught lobby 
    # - House, bungalow or park home: no
    # - Flat or maisonette: 
    #   - yes if heated or unheated corridor, 
    #   - otherwise no
    
    #... from SAP worksheet
    #    If no draught lobby, enter 0.05, else enter 0
    
    if dwelling_type in ['house','bungalow','park home']:
        
        no_draft_lobby_infiltration = 0.05  # no draught lobby
        
    elif dwelling_type in ['flat', 'maisonette']:
        
        if flats_and_maisonettes_only_heat_loss_corridor in ['heated corridor', 'unheated corridor']:
            
            no_draft_lobby_infiltration = 0  # draught lobby
            
        elif flats_and_maisonettes_only_heat_loss_corridor == 'no corridor':
            
            no_draft_lobby_infiltration = 0.05  # no draught lobby
            
        else:
            
            raise Exception
        
    else:
        
        raise Exception
    
    
    # Number of storeys 
    # Greater of the number of storeys in the main part of the dwelling 
    # and in any extension. 
    # If an extension is above another part, no account of this is
    # taken in calculating the storey count.
    
    number_of_storeys_in_the_dwelling = \
        max(
            len(main_dwelling_dimensions_area),
            len(extension_1_dimensions_area),
            len(extension_2_dimensions_area),
            len(extension_3_dimensions_area),
            len(extension_4_dimensions_area)
            )
    
    
    # percentage_of_windows_and_doors_draught_proofed
    
    percentage_of_windows_and_doors_draught_proofed = draught_proofing
    
    
    # Sheltered sides 
    # - 4 for flat/maisonette up to third storey above ground level
    # - 2 in other cases
    
    if dwelling_type in ['flat', 'maisonette']:
        
        if flats_and_maisonettes_only_floor_level_relative_to_the_lowest_level_of_the_building < 3:
    
            number_of_sides_on_which_dwelling_is_sheltered = 4
    
        else:
            
            number_of_sides_on_which_dwelling_is_sheltered = 2
            
    else:
        
        number_of_sides_on_which_dwelling_is_sheltered = 2
            
    
    # monthly_average_wind_speed
    
    monthly_average_wind_speed = table_u2[region]
    
    
    # Number of wet rooms
    # (required for an
    # exhaust air heat
    # pump)
    # 1 to 2 habitable rooms: Kitchen + 1
    # 3 to 4 habitable rooms: Kitchen + 2
    # 5 to 6 habitable rooms: Kitchen + 3
    # 7 to 8 habitable rooms: Kitchen + 4
    # 9 to 10 habitable rooms: Kitchen + 5
    # 11 or more habitable rooms: Kitchen + 6
    raise NotImplementedError
    
    
    
    # S4.1 Mechanical ventilation
    # If a mechanical ventilation system, it is treated as mechanical 
    # extract ventilation (MEV) if an extract-only system and as mechanical 
    # ventilation with heat recovery (MVHR) if a balanced system, using the 
    # default values in SAP Table 4g and the in-use factors for default data 
    # from SAP Table 4h.
    
    # applicable_case
    # One of the following options: 
    # - ‘balanced mechanical ventilation with heat recovery’; 
    # - ‘balanced mechanical ventilation without heat recovery’; 
    # - ‘whole house extract ventilation or positive input ventilation from outside’; 
    # - or ‘natural ventilation or whole house positive input ventilation from loft’.
    
    if mechanical_ventilation == 'yes':
        
        if mechanical_ventilation_type == 'extract-only':
            
            applicable_case = 'balanced mechanical ventilation without heat recovery'
            
            raise NotImplementedError
            # mechanical_ventilation_air_change_rate_through_system = 
            # exhaust_air_heat_pump_using_Appendix_N = 
            # mechanical_ventilation_throughput_factor = 
            # efficiency_allowing_for_in_use_factor = 
            
        elif mechanical_ventilation_type == 'balanced':
            
            applicable_case = 'balanced mechanical ventilation with heat recovery'
            
            raise NotImplementedError
            # mechanical_ventilation_air_change_rate_through_system = 
            # exhaust_air_heat_pump_using_Appendix_N = 
            # mechanical_ventilation_throughput_factor = 
            # efficiency_allowing_for_in_use_factor = 
            
        else:
            
            raise Exception
        
    elif mechanical_ventilation == 'no':
        
        applicable_case = 'natural ventilation or whole house positive input ventilation from loft'  ### CHECK - is this thr right option to use here
        mechanical_ventilation_air_change_rate_through_system = None
        exhaust_air_heat_pump_using_Appendix_N = None
        mechanical_ventilation_throughput_factor = None
        efficiency_allowing_for_in_use_factor = None
        
    else:
        
        raise Exception
    
    
    
    return dict(
      number_of_chimneys_main_heating = number_of_chimneys_main_heating,
      number_of_chimneys_secondary_heating = number_of_chimneys_secondary_heating,
      number_of_chimneys_other = number_of_chimneys_other,
      number_of_open_flues_main_heating = number_of_open_flues_main_heating,
      number_of_open_flues_secondary_heating = number_of_open_flues_secondary_heating,
      number_of_open_flues_other = number_of_open_flues_other,
      number_of_intermittant_fans_total = number_of_intermittant_fans_total,
      number_of_passive_vents_total = number_of_passive_vents_total,
      number_of_flueless_gas_fires_total = number_of_flueless_gas_fires_total,
      air_permeability_value_q50 = air_permeability_value_q50,
      number_of_storeys_in_the_dwelling = number_of_storeys_in_the_dwelling,
      structural_infiltration = structural_infiltration,
      suspended_wooden_ground_floor_infiltration = suspended_wooden_ground_floor_infiltration,
      no_draft_lobby_infiltration = no_draft_lobby_infiltration,
      percentage_of_windows_and_doors_draught_proofed = percentage_of_windows_and_doors_draught_proofed,
      number_of_sides_on_which_dwelling_is_sheltered = number_of_sides_on_which_dwelling_is_sheltered,
      monthly_average_wind_speed = monthly_average_wind_speed,
      applicable_case = applicable_case,
      mechanical_ventilation_air_change_rate_through_system = mechanical_ventilation_air_change_rate_through_system,
      exhaust_air_heat_pump_using_Appendix_N = exhaust_air_heat_pump_using_Appendix_N,
      mechanical_ventilation_throughput_factor = mechanical_ventilation_throughput_factor,
      efficiency_allowing_for_in_use_factor = efficiency_allowing_for_in_use_factor,
      )


    
    
def validate_inputs(
        rdsap_inputs
        ):
    """
    """
    def test_for_item_presence(item,d, i=None):
        ""
        if not item in d:
            if i is None:
                x='["whole_dwelling"]'
            else:
                x=f'["building_parts"][{i}]'
            message=f'Item "{item}" is required in the rdsap_inputs{x} dictionary.'
            raise Exception(message)
    
    def test_for_item_options(item,options,d,i=None):
        ""
        if not d[item] in options:
            if i is None:
                x='["whole_dwelling"]'
            else:
                x=f'["building_parts"][{i}]'
            message=f'Item "{item}" in the rdsap_inputs{x} dictionary '
            message+=f'with value "{d[item]}" must have one of the following values {options}.'
            raise Exception(message)
            
    def test_for_item_value_type(item,kls,d,i=None):
        ""
        if not isinstance(d[item],kls):
            if i is None:
                x='["whole_dwelling"]'
            else:
                x=f'["building_parts"][{i}]'
            message=f'Item "{item}" in the rdsap_inputs{x} dictionary '
            message+=f'with value "{d[item]}" must be of type {kls}.'
            raise Exception(message)
            
    def test_for_item_list_min_length(item, min_length, d, i=None):
        ""
        if len(d[item]) < min_length:
            if i is None:
                x='["whole_dwelling"]'
            else:
                x=f'["building_parts"][{i}]'
            message=f'Item "{item}" in rdsap_inputs{x} '
            message+=f'must be a list with length greater than or equal to {min_length}. '
            message+=f'Current length is: {len(d[item])}.'
            raise Exception(message)
        
    def test_for_item_list_max_length(item, max_length, d, i=None):
        ""
        if len(d[item]) > max_length:
            if i is None:
                x='["whole_dwelling"]'
            else:
                x=f'["building_parts"][{i}]'
            message=f'Item "{item}" in rdsap_inputs{x} '
            message+=f'must be a list with length less than or equal to {max_length}. '
            message+=f'Current length is: {len(d[item])}.'
            raise Exception(message)
            
    def test_for_item_list_values_type(item, klses, d, i=None):
        ""
        for j, a in enumerate(d[item]):
            if not any ([isinstance(a,y) for y in klses]):
                if i is None:
                    x='["whole_dwelling"]'
                else:
                    x=f'["building_parts"][{i}]'
                message=f'List item with value "{a}" at index "{j}" in item "{item}" in rdsap_inputs{x} '
                message+=f'must be of one of the following types: {klses}. '
                message+=f'Current type is: {type(d[item][j])}.'
                raise Exception(message)
            
    
    
    # ---whole dwelling---
    d=rdsap_inputs['whole_dwelling']
    
    # country
    item='country'
    test_for_item_presence(item,d)
    options=['England & Wales','Scotland','Northern Ireland']
    test_for_item_options(item,options,d)
    
    # region
    item='region'
    test_for_item_presence(item,d)
    options=['Thames',
             'South East England',
             'Southern England',
             'South West England',
             'Severn Wales / Severn England','Midlands',
             'West Pennines Wales / West Pennines England',
             'north West England / South West Scotland',
             'Borders Scotland / Borders England',
             'North East England',
             'East Pennines',
             'East Anglia',
             'Wales',
             'West Scotland',
             'East Scotland',
             'North East Scotland',
             'Highland',
             'Western Isles',
             'Orkney',
             'Shetland',
             'Northern Ireland'
             ]
    test_for_item_options(item,options,d)
    
    # transaction_type
    item='transaction_type'
    test_for_item_presence(item,d)
    options=['marketed sale',
             'non-marketed sale',
             'rental',
             'stock condition survey',
             'assessment for Green Deal',
             'following Green Deal',
             'FIT application',
             'RHI application',
             'ECO assessment',
             'none of the above'
             ]
    test_for_item_options(item,options,d)
    
    # tenure
    item='tenure'
    test_for_item_presence(item,d)
    options=['owner-occupied',
             'rented (social)',
             'rented (private)',
             'unknown'
             ]
    test_for_item_options(item,options,d)
    
    # dwelling_type
    item='dwelling_type'
    test_for_item_presence(item,d)
    options=['house',
             'bungalow',
             'flat',
             'maisonette',
             'park home'
             ]
    test_for_item_options(item,options,d)
    
    # built_form_and_detachment
    item='built_form_and_detachment'
    test_for_item_presence(item,d)
    options=['detached',
             'semi-detached',
             'mid-terrace',
             'end-terrace',
             'enclosed mid-terrace',
             'enclosed end-terrace'
             ]
    test_for_item_options(item,options,d)
    
    # number_of_habitable_rooms
    item='number_of_habitable_rooms'
    test_for_item_presence(item,d)
    test_for_item_value_type(item,int,d)
    if d[item]<0: raise Exception
    
    # number_of_heated_habitable_rooms
    item='number_of_heated_habitable_rooms'
    test_for_item_presence(item,d)
    test_for_item_value_type(item,int,d)
    if d[item]<0: raise Exception
    
    # dimension_type
    item='dimension_type'
    test_for_item_presence(item,d)
    options=['measured_internally',
             'measured_externally'
             ]
    test_for_item_options(item,options,d)
    
    # conservatory
    item='conservatory'
    test_for_item_presence(item,d)
    options=['no conservatory',
             'separated, no fixed heaters',
             'separated, fixed heaters',
             'not separated'
             ]
    test_for_item_options(item,options,d)
    
    #
    if d['conservatory']=='not separated':
    
        # non_separated_conservatory_only_floor_area
        raise NotImplementedError
        
        # non_separated_conservatory_only_glazed_perimeter
        raise NotImplementedError
        
        # non_separated_conservatory_only_double_glazed
        raise NotImplementedError
        
        # non_separated_conservatory_only_height
        raise NotImplementedError
        
    #
    if d['dwelling_type'] in ['flat','maisionette']:
        
        # flats_and_maisonettes_only_heat_loss_corridor
        item='flats_and_maisonettes_only_heat_loss_corridor'
        test_for_item_presence(item,d)
        options=['no corridor',
                 'heated corridor',
                 'unheated corridor'
                 ]
        test_for_item_options(item,options,d)
        
        # 
        if d['flats_and_maisonettes_only_heat_loss_corridor']=='unheated_corridor':
            
            # flats_and_maisonettes_only_unheated_corridor_length_of_sheltered_wall
            raise NotImplementedError
        
        # flats_and_maisonettes_only_floor_level_relative_to_the_lowest_level_of_the_building
        raise NotImplementedError
        
        # flats_and_maisonettes_only_property_position
        raise NotImplementedError
        
    # number_of_extensions
    item='number_of_extensions'
    test_for_item_presence(item,d)
    test_for_item_value_type(item,int,d)
    if d[item]<0: raise Exception
    if d[item]>4: raise Exception
    
        
    # ---building_parts---
    for i,d in enumerate(rdsap_inputs['building_parts']):
        
        # age_band
        item='age_band'
        test_for_item_presence(item,d,i)
        options=['A','B','C','D','E','F','G','H','I','J','K','L']
        test_for_item_options(item,options,d,i)
        
        
        # below_the_building_part
        
        options=['ground floor',
                 'above partially / intermittently heated space (commerical premises)',
                 'above unheated space',
                 'to external air',
                 'same dwelling below',
                 'another dwelling below'
                 ]
        
        # above the building part
        
        options=[
            'pitched roof (slates or tiles), access to loft',
            'pitched roof (slates or tiles), no access',
            'pitched roof, sloping ceiling',
            'pitched roof (thatched)',
            'flat roof',
            'same dwelling above',
            'another dwelling above'
            ]
        
        # dimensions_area
        item='dimensions_area'
        test_for_item_presence(item,d,i)
        test_for_item_value_type(item,list,d,i)
        test_for_item_list_min_length(item, 1, d, i)
        test_for_item_list_max_length(item, 7, d, i)
        test_for_item_list_values_type(item, [int,float], d, i)
        
        # dimensions_average_room_height
        item='dimensions_average_room_height'
        test_for_item_presence(item,d,i)
        test_for_item_value_type(item,list,d,i)
        test_for_item_list_min_length(item, 1, d, i)
        test_for_item_list_max_length(item, 7, d, i)
        test_for_item_list_values_type(item, [int,float], d, i)
        
        # dimensions_exposed_perimeter
        item='dimensions_exposed_perimeter'
        test_for_item_presence(item,d,i)
        test_for_item_value_type(item,list,d,i)
        test_for_item_list_min_length(item, 1, d, i)
        test_for_item_list_max_length(item, 7, d, i)
        test_for_item_list_values_type(item, [int,float], d, i)
        
        # dimensions_party_wall_length
        item='dimensions_party_wall_length'
        test_for_item_presence(item,d,i)
        test_for_item_value_type(item,list,d,i)
        test_for_item_list_min_length(item, 1, d, i)
        test_for_item_list_max_length(item, 7, d, i)
        test_for_item_list_values_type(item, [int,float], d, i)
    
        # floor_construction
        
        options=[
            'unknown',
            'solid',
            'suspended timber',
            'suspended, not timber'
            ]
    
    
        # floor_insulation
        
        options=[
            'unknown',
            'as built',
            'retrofitted'
            ]
    
    
        # floor_insulation_thickness
        
        options=[
            'unknown',
            '50mm',
            '100 mm',
            '150 mm'
            ]
        
        
        # floor_u_value
        
        
        
        # wall_construction
        
        options=[
            'stone (granite or shinstone)',
            'stone (sandstone or limestone)',
            'solid brick',
            'cob',
            'cavity',
            'timber frame',
            'park home wall',
            'system build (i.e. an other)'
            ]
    
    
        # wall_thickness
        
        
        
        # wall_insulation_type
        
        options=[
            'as built',
            'external',
            'filled cavity',
            'internal',
            'cavity plus external',
            'cavity plus internal',
            'unknown'
            ]
        
        # wall_insulation_thickness
        
        options=[
            'unknown',
            '50 mm',
            '100 mm',
            '150 mm',
            '200 mm'
            ]
    
        # wall_u_value
        
        
        # wall_dry_lined_or_path_and_plaster
        
        options=[
            'yes',
            'no'
            ]
    
    
        # alternative_wall
        
        # party_wall_construction
        
        # roof_insulation
        
        # roof_insulation_thickness
        
        # rafter_insulation_thickness
        
        # flat_roof_insulation_thickness
        
        # sloping_ceiling_insulation_thickness
        
        # roof_u_value
        
        # roof_room_age_band
        
        # roof_rooms_connected
        
        # roof_room_insulation
        
        # roof_room_insulation_thickness_on_flat_part_of_roof_of_roof_room
        
        # roof_room_insulation_thickness_toher_parts_of_roof_room
        
        # roof_room_area
        
        # roof_room_u_value
        
    # ---whole dwelling---
    d=rdsap_inputs['whole_dwelling']
    
    # number_of_external_doors
    
    # insulated_door_u_value
    
    # windows_area_dwelling_only
    
    # proportion_with_multiple_glazing
    
    # PVC_window_frames_and_glazing_gap
    
    # window_u_value
    
    # window_g_value
    
    # window_data_source
    
    #... more on windows here
    
    # draught_proofing
    
    # fireplaces
    
    #... lots on main_heating_system
    
    #... lots on second_main_heating_system
    
    # community_heating_system
    
    # main_heating_controls
    
    # secondary_heating_system
    
    # water_heating
    
    # solar_water_heating
    
    # solar_water_heating_details
    
    # solar_collector_details
    
    # solar_store_details
    
    # flue_gas_heat_recovery
    
    # PV_for_flue_gas_heat_recovery
    
    # baths_and_showers
    
    # waste_water_heat_recovery
    
    # space_cooling_system_present
    
    # mechanical_ventilation
    options=['yes','no']
    
    # mechanical_ventilation_type
    options=['extract-only','balanced']
    
    # electricity_meter
    
    # mains_gas_available
    
    # photovoltaic_array
    
    # terrain
    
    # wind_turbine
    
    # wind_turbine_details_known
    
    # lighting
    
    # swimming_pool
    
    # special_feature
    
    
    
    
    
    
    
    
    
    
    