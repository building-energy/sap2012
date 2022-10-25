# -*- coding: utf-8 -*-


def heat_losses_and_heat_loss_parameter(
        solid_door_net_area,
        solid_door_u_value,
        semi_glazed_door_net_area,
        semi_glazed_door_u_value,
        window_net_area,
        window_u_value,
        roof_window_net_area,
        roof_window_u_value,
        basement_floor_net_area,
        basement_floor_u_value,
        basement_floor_heat_capacity,
        ground_floor_net_area,
        ground_floor_u_value,
        ground_floor_heat_capacity,
        exposed_floor_net_area,
        exposed_floor_u_value,
        exposed_floor_heat_capacity,
        basement_wall_gross_area,
        basement_wall_opening,
        basement_wall_u_value,
        basement_wall_heat_capacity,
        external_wall_gross_area,
        external_wall_opening,
        external_wall_u_value,
        external_wall_heat_capacity,
        roof_gross_area,
        roof_opening,
        roof_u_value,
        roof_heat_capacity,
        party_wall_net_area,
        party_wall_u_value,
        party_wall_heat_capacity,
        party_floor_net_area,
        party_floor_heat_capacity,
        party_ceiling_net_area,
        party_ceiling_heat_capacity,
        internal_wall_net_area,
        internal_wall_heat_capacity,
        internal_floor_net_area,
        internal_floor_heat_capacity,
        internal_ceiling_net_area,
        internal_ceiling_heat_capacity,
        total_floor_area,
        thermal_bridges_appendix_k,
        effective_air_change_rate,
        dwelling_volume
        ):
    
    """Calculates the heat losses and the heat loss parameter, Section 3.
    
    :param solid_door_net_area: See (26), in m2.
    :type solid_door_net_area: float
    
    :param solid_door_u_value: See (26), in W/m2K.
    :type solid_door_u_value: float or None
    
    :param semi_glazed_door_net_area: See (26a), in m2.
    :type semi_glazed_door_net_area: float
    
    :param semi_glazed_door_u_value: See (26a), in W/m2K.
    :type semi_glazed_door_u_value: float or None
    
    :param window_net_area: See (27), in m2.
    :type window_net_area: float
    
    :param window_u_value: See (27), in W/m2K.
        For windows and roof windows, use effective window U-value. 
        Calculated using formula 1/[(1/U-value)+0.04] as given in paragraph 3.2.
    :type window_u_value: float or None
    
    :param roof_window_net_area: See (27a), in m2.
        For windows and roof windows, use effective window U-value. 
        Calculated using formula 1/[(1/U-value)+0.04] as given in paragraph 3.2.
    :type roof_window_net_area: float
    
    :param roof_window_u_value: See (27a), in W/m2K.
    :type roof_window_u_value: float or None
    
    :param basement_floor_net_area:  See (28), in m2.
    :type basement_floor_net_area: float
    
    :param basement_floor_u_value: See (28), in W/m2K.
    :type basement_floor_u_value: float or None
    
    :param basement_floor_heat_capacity: See (28), in kJ/m2K.
    :type basement_floor_heat_capacity: float or None
    
    :param ground_floor_net_area: See (28a), in m2.
    :type ground_floor_net_area: float
    
    :param ground_floor_u_value: See (28a), in W/m2K.
    :type ground_floor_u_value: float or None
    
    :param ground_floor_heat_capacity: See (28a), in kJ/m2K.
    :type ground_floor_heat_capacity: float or None
    
    :param exposed_floor_net_area: See (28b), in m2.
    :type exposed_floor_net_area: float
    
    :param exposed_floor_u_value: See (28b), in W/m2K.
    :type exposed_floor_u_value: float or None
    
    :param exposed_floor_heat_capacity: See (28b), in kJ/m2K.
    :type exposed_floor_heat_capacity: float or None
    
    :param basement_wall_gross_area: See (29), in m2.
    :type basement_wall_gross_area: float
    
    :param basement_wall_opening: See (29), in m2.
    :type basement_wall_opening: float
    
    :param basement_wall_u_value: See (29), in W/m2K.
    :type basement_wall_u_value: float or None
    
    :param basement_wall_heat_capacity: See (29), in kJ/m2K.
    :type basement_wall_heat_capacity: float or None
    
    :param external_wall_gross_area: See (29a), in m2.
    :type external_wall_gross_area: float
    
    :param external_wall_opening: See (29a), in m2.
    :type external_wall_opening: float
    
    :param external_wall_u_value: See (29a), in W/m2K.
    :type external_wall_u_value: float or None
    
    :param external_wall_heat_capacity: See (29a), in kJ/m2K.
    :type external_wall_heat_capacity: float or None
    
    :param roof_gross_area: See (30), in m2.
    :type roof_gross_area: float
    
    :param roof_opening: See (30), in m2.
    :type roof_opening: float
    
    :param roof_u_value: See (30), in W/m2K.
    :type roof_u_value: float or None
    
    :param roof_heat_capacity: See (30), in kJ/m2K.
    :type roof_heat_capacity: float or None
    
    :param party_wall_net_area: See (32), in m2.
    :type party_wall_net_area: float
    
    :param party_wall_u_value: See (32), in W/m2K.
    :type party_wall_u_value: float or None
    
    :param party_wall_heat_capacity: See (32), in kJ/m2K.
    :type party_wall_heat_capacity: float or None
    
    :param party_floor_net_area: See (32a), in m2.
    :type party_floor_net_area: float
    
    :param party_floor_heat_capacity: See (32a), in kJ/m2K.
    :type party_floor_heat_capacity: float or None
    
    :param party_ceiling_net_area: See (32b), in m2.
    :type party_ceiling_net_area: float
    
    :param party_ceiling_heat_capacity: See (32b), in kJ/m2K.
    :type party_ceiling_heat_capacity: float or None
    
    :param internal_wall_net_area: See (32c), in m2.
    :type internal_wall_net_area: float
    
    :param internal_wall_heat_capacity: See (32c), in kJ/m2K.
    :type internal_wall_heat_capacity: float or None
    
    :param internal_floor_net_area: See (32d), in m2.
    :type internal_floor_net_area: float
    
    :param internal_floor_heat_capacity: See (32d), in kJ/m2K.
    :type internal_floor_heat_capacity: float or None
    
    :param internal_ceiling_net_area: See (32e), in m2.
    :type internal_ceiling_net_area: float
    
    :param internal_ceiling_heat_capacity: See (32e), in kJ/m2K.
    :type internal_ceiling_heat_capacity: float or None
    
    :param total_floor_area: See (4).
    :type total_floor_area: float
    
    :param thermal_bridges_appendix_k: in W/K.
        The transmission heat loss coefficient due to non-repeating
        thermal bridges as calculated using Appendix K.
        If None, then a simplified calculation is done in this module.
    :type thermal_bridges_appendix_k: float or None
    
    :param effective_air_change_rate: See (25).
    :type effective_air_change_rate: list (of floats)
    
    :param dwelling_volume: See (5), in m3.
    :type dwelling_volume: float
    

    :return: A dictionary with keys of (
            solid_floor_UA,
            semi_glazed_door_UA,
            window_UA,
            roof_window_UA,
            basement_floor_UA,
            basement_floor_Ak,
            ground_floor_UA,
            ground_floor_Ak,
            exposed_floor_UA,
            exposed_floor_Ak,
            basement_wall_net_area,
            basement_wall_UA,
            basement_wall_Ak,
            external_wall_net_area,
            external_wall_UA,
            external_wall_Ak,
            roof_net_area,
            roof_UA,
            roof_Ak,
            total_area_of_external_elements,
            party_wall_UA,
            party_wall_Ak,
            party_floor_Ak,
            party_ceiling_Ak,
            internal_wall_Ak,
            internal_floor_Ak,
            internal_ceiling_Ak,
            fabric_heat_loss,
            heat_capacity,
            thermal_mass_parameter,
            thermal_bridges,
            total_fabric_heat_loss,
            ventilation_heat_loss_calculated_monthly,
            heat_transfer_coefficient,
            average_heat_transfer_coefficient,
            heat_loss_parameter,
            average_heat_loss_parameter
            )

    - **solid_floor_UA** (`float`): See (26), in W/K.
    
    - **semi_glazed_door_UA** (`float`): See (26a), in W/K.
    
    - **window_UA** (`float`): See (27), in W/K.
    
    - **roof_window_UA** (`float`): See (27a), in W/K.
    
    - **basement_floor_UA** (`float`): See (28), in W/K.
    
    - **basement_floor_Ak** (`float`): See (28), in kJ/K.
    
    - **ground_floor_UA** (`float`): See (28a), in W/K.
    
    - **ground_floor_Ak** (`float`): See (28a), in kJ/K.
    
    - **exposed_floor_UA** (`float`): See (28b), in W/K.
    
    - **exposed_floor_Ak** (`float`): See (28b), in kJ/K.
    
    - **basement_wall_net_area** (`float`): See (29), in m2.
    
    - **basement_wall_UA** (`float`): See (29), in W/K.
    
    - **basement_wall_Ak** (`float`): See (29), in kJ/K.
    
    - **external_wall_net_area** (`float`): See (29a), in m2.
    
    - **external_wall_UA** (`float`): See (29a), in W/K.
    
    - **external_wall_Ak** (`float`): See (29a), in kJ/K.
    
    - **roof_net_area** (`float`): See (30), in m2.
    
    - **roof_UA** (`float`): See (30), in W/K.
    
    - **roof_Ak** (`float`): See (30), in kJ/K.
    
    - **total_area_of_external_elements** (`float`): See (31), in m2.
    
    - **party_wall_UA** (`float`): See (32), in W/K.
    
    - **party_wall_Ak** (`float`): See (32), in kJ/K.
    
    - **party_floor_Ak** (`float`): See (32a), in kJ/K.
    
    - **party_ceiling_Ak** (`float`): See (32b), in kJ/K.
    
    - **internal_wall_Ak** (`float`): See (32c), in kJ/K.
    
    - **internal_floor_Ak** (`float`): See (32d), in kJ/K.
    
    - **internal_ceiling_Ak** (`float`): See (32e), in kJ/K.
    
    - **fabric_heat_loss** (`float`): See (33), in W/K.
    
    - **heat_capacity** (`float`): See (34), in kJ/K.
    
    - **thermal_mass_parameter** (`float`): See (35), in kJ/m2K.
    
    - **thermal_bridges** (`float`): See (36), in W/K.
    
    - **total_fabric_heat_loss** (`float`): See (37), in W/K.
    
    - **ventilation_heat_loss_calculated_monthly** (`list` (`float`): See (82), in W/K.
    
    - **heat_transfer_coefficient** (`list` (`float`): See (39), in W/K.
    
    - **average_heat_transfer_coefficient**  (`float`): See (39), in W/K.
    
    - **heat_loss_parameter** (`list` (`float`): See (40), in W/m2K.
    
    - **average_heat_loss_parameter** (`float`): See (40), in W/m2K.

    :rtype: dict

    """

    if solid_door_net_area==0:
        solid_floor_UA = 0
    else:
        solid_floor_UA = solid_door_net_area * solid_door_u_value    
        
    if semi_glazed_door_net_area==0:
        semi_glazed_door_UA = 0
    else:
        semi_glazed_door_UA = semi_glazed_door_net_area * semi_glazed_door_u_value
    
    if window_net_area==0:
        window_UA = 0
    else:
        window_UA = window_net_area * window_u_value
    
    if roof_window_net_area==0:
        roof_window_UA = 0
    else:
        roof_window_UA = roof_window_net_area * roof_window_u_value
    
    if basement_floor_net_area==0:
        basement_floor_UA = 0
        basement_floor_Ak = 0
    else:
        basement_floor_UA = basement_floor_net_area * basement_floor_u_value
        basement_floor_Ak = basement_floor_net_area * basement_floor_heat_capacity
    
    if ground_floor_net_area==0:
        ground_floor_UA=0
        ground_floor_Ak=0
    else:
        ground_floor_UA = ground_floor_net_area * ground_floor_u_value
        ground_floor_Ak = ground_floor_net_area * ground_floor_heat_capacity
        
    if exposed_floor_net_area==0:
        exposed_floor_UA=0
        exposed_floor_Ak=0
    else:
        exposed_floor_UA = exposed_floor_net_area * exposed_floor_u_value
        exposed_floor_Ak = exposed_floor_net_area * exposed_floor_heat_capacity
        
    basement_wall_net_area = basement_wall_gross_area - basement_wall_opening
    if basement_wall_net_area==0:
        basement_wall_UA=0
        basement_wall_Ak=0
    else:
        basement_wall_UA = basement_wall_net_area * basement_wall_u_value
        basement_wall_Ak= basement_wall_net_area * basement_wall_heat_capacity
        
    external_wall_net_area = external_wall_gross_area - external_wall_opening
    if external_wall_net_area==0:
        external_wall_UA=0
        external_wall_Ak=0
    else:
        external_wall_UA = external_wall_net_area * external_wall_u_value
        external_wall_Ak = external_wall_net_area * external_wall_heat_capacity
        
    roof_net_area = roof_gross_area - roof_opening
    if roof_net_area==0:
        roof_UA = 0
        roof_Ak = 0
    else:
        roof_UA = roof_net_area * roof_u_value
        roof_Ak = roof_net_area * roof_heat_capacity
    
    total_area_of_external_elements = (
            solid_door_net_area + 
            semi_glazed_door_net_area + 
            window_net_area + 
            roof_window_net_area + 
            basement_floor_net_area + 
            ground_floor_net_area + 
            exposed_floor_net_area + 
            basement_wall_net_area + 
            external_wall_net_area + 
            roof_net_area 
            )
    
    if party_wall_net_area==0:
        party_wall_UA = 0
    else:
        party_wall_UA = party_wall_net_area * party_wall_u_value
        
    if party_wall_net_area==0:
        party_wall_Ak = 0
    else:
        party_wall_Ak = party_wall_net_area * party_wall_heat_capacity
        
    if party_floor_net_area==0:
        party_floor_Ak = 0
    else:
        party_floor_Ak = party_floor_net_area * party_floor_heat_capacity
        
    if party_ceiling_net_area==0:
        party_ceiling_Ak = 0
    else:
        party_ceiling_Ak = party_ceiling_net_area * party_ceiling_heat_capacity
        
    if internal_wall_net_area==0:
        internal_wall_Ak = 0
    else:
        internal_wall_Ak = internal_wall_net_area * internal_wall_heat_capacity
        
    if internal_floor_net_area==0:
        internal_floor_Ak = 0
    else:
        internal_floor_Ak = internal_floor_net_area * internal_floor_heat_capacity
        
    if internal_ceiling_net_area==0:
        internal_ceiling_Ak = 0
    else:
        internal_ceiling_Ak = internal_ceiling_net_area * internal_ceiling_heat_capacity
    
    fabric_heat_loss = (
            solid_floor_UA + 
            semi_glazed_door_UA + 
            window_UA + 
            roof_window_UA + 
            basement_floor_UA + 
            ground_floor_UA + 
            exposed_floor_UA + 
            basement_wall_UA + 
            external_wall_UA + 
            roof_UA + 
            party_wall_UA
            )
    
    heat_capacity = (
            basement_floor_Ak + 
            ground_floor_Ak + 
            exposed_floor_Ak + 
            basement_wall_Ak +
            external_wall_Ak + 
            roof_Ak + 
            party_wall_Ak + 
            party_floor_Ak + 
            party_ceiling_Ak +
            internal_wall_Ak +
            internal_floor_Ak +
            internal_ceiling_Ak 
            )

    thermal_mass_parameter = heat_capacity / total_floor_area

    # thermal_bridges
    if not thermal_bridges_appendix_k is None:
        thermal_bridges = thermal_bridges_appendix_k
    else:
        thermal_bridges = 0.15 * total_area_of_external_elements
        
    total_fabric_heat_loss = fabric_heat_loss + thermal_bridges
    
    # ventilation_heat_loss_calculated_monthly
    ventilation_heat_loss_calculated_monthly = []
    for i in range(12):
        ventilation_heat_loss_calculated_monthly.append(
                0.33 * 
                effective_air_change_rate[i] * 
                dwelling_volume
                )
        
    # heat_transfer_coefficient
    heat_transfer_coefficient = []
    for i in range(12):
        heat_transfer_coefficient.append(
                total_fabric_heat_loss + 
                ventilation_heat_loss_calculated_monthly[i]
                )
    
    average_heat_transfer_coefficient = sum(heat_transfer_coefficient) / 12.0
    
    # heat_loss_parameter
    heat_loss_parameter = []
    for i in range(12):
        heat_loss_parameter.append(
                heat_transfer_coefficient[i] / 
                total_floor_area
                )

    average_heat_loss_parameter = sum(heat_loss_parameter) / 12.0

    return dict(
            solid_floor_UA=solid_floor_UA,
            semi_glazed_door_UA=semi_glazed_door_UA,
            window_UA=window_UA,
            roof_window_UA=roof_window_UA,
            basement_floor_UA=basement_floor_UA,
            basement_floor_Ak=basement_floor_Ak,
            ground_floor_UA=ground_floor_UA,
            ground_floor_Ak=ground_floor_Ak,
            exposed_floor_UA=exposed_floor_UA,
            exposed_floor_Ak=exposed_floor_Ak,
            basement_wall_net_area=basement_wall_net_area,
            basement_wall_UA=basement_wall_UA,
            basement_wall_Ak=basement_wall_Ak,
            external_wall_net_area=external_wall_net_area,
            external_wall_UA=external_wall_UA,
            external_wall_Ak=external_wall_Ak,
            roof_net_area=roof_net_area,
            roof_UA=roof_UA,
            roof_Ak=roof_Ak,
            total_area_of_external_elements=total_area_of_external_elements,
            party_wall_UA=party_wall_UA,
            party_wall_Ak=party_wall_Ak,
            party_floor_Ak=party_floor_Ak,
            party_ceiling_Ak=party_ceiling_Ak,
            internal_wall_Ak=internal_wall_Ak,
            internal_floor_Ak=internal_floor_Ak,
            internal_ceiling_Ak=internal_ceiling_Ak,
            fabric_heat_loss=fabric_heat_loss,
            heat_capacity=heat_capacity,
            thermal_mass_parameter=thermal_mass_parameter,
            thermal_bridges=thermal_bridges,
            total_fabric_heat_loss=total_fabric_heat_loss,
            ventilation_heat_loss_calculated_monthly=ventilation_heat_loss_calculated_monthly,
            heat_transfer_coefficient=heat_transfer_coefficient,
            average_heat_transfer_coefficient=average_heat_transfer_coefficient,
            heat_loss_parameter=heat_loss_parameter,
            average_heat_loss_parameter=average_heat_loss_parameter
            )









