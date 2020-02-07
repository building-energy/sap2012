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
        effective_air_change_rate
        ):
    
    """Calculates the heat losses and the heat loss parameter, Section 3
    
    :param solid_door_net_area: see (26), in m2
    :type solid_door_net_area: float
    
    :param solid_door_u_value: see (26), in W/m2K
    :type solid_door_u_value: float
    
    :param semi_glazed_door_net_area: see (26a), in m2
    :type semi_glazed_door_net_area: float
    
    :param semi_glazed_door_u_value: see (26a), in W/m2K
    :type semi_glazed_door_u_value: float
    
    :param window_net_area: see (27), in m2
    :type window_net_area: float
    
    :param window_u_value: see (27), in W/m2K
        for windows and roof windows, use effective window U-value 
        calculated using formula 1/[(1/U-value)+0.04] as given in paragraph 3.2
    :type window_u_value:float
    
    :param roof_window_net_area: see (27a), in m2
        for windows and roof windows, use effective window U-value 
        calculated using formula 1/[(1/U-value)+0.04] as given in paragraph 3.2
    :type roof_window_net_area: float
    
    :param roof_window_u_value: see (27a), in W/m2K
    :type roof_window_u_value: float
    
    :param basement_floor_net_area:  see (28), in m2
    :type basement_floor_net_area: float
    
    :param basement_floor_u_value: see (28), in W/m2K
    :type basement_floor_u_value: float
    
    :param basement_floor_heat_capacity: see (28), in kJ/m2K
    :type basement_floor_heat_capacity: float
    
    :param ground_floor_net_area: see (28a), in m2
    :type ground_floor_net_area: float
    
    :param ground_floor_u_value: see (28a), in W/m2K
    :type ground_floor_u_value: float
    
    :param ground_floor_heat_capacity: see (28a), in kJ/m2K
    :type ground_floor_heat_capacity: float
    
    :param exposed_floor_net_area: see (28b), in m2
    :type exposed_floor_net_area: float
    
    :param exposed_floor_u_value: see (28b), in W/m2K
    :type exposed_floor_u_value: float
    
    :param exposed_floor_heat_capacity: see (28b), in kJ/m2K
    :type exposed_floor_heat_capacity: float
    
    :param basement_wall_gross_area: see (29), in m2
    :type basement_wall_gross_area: float
    
    :param basement_wall_opening: see (29), in m2
    :type basement_wall_opening: float
    
    :param basement_wall_u_value: see (29), in W/m2K
    :type basement_wall_u_value: float
    
    :param basement_wall_heat_capacity: see (29), in kJ/m2K
    :type basement_wall_heat_capacity: float
    
    :param external_wall_gross_area: see (29a), in m2
    :type external_wall_gross_area: float
    
    :param external_wall_opening: see (29a), in m2
    :type external_wall_opening: float
    
    :param external_wall_u_value: see (29a), in W/m2K
    :type external_wall_u_value: float
    
    :param external_wall_heat_capacity: see (29a), in kJ/m2K
    :type external_wall_heat_capacity: float
    
    :param roof_gross_area: see (30), in m2
    :type roof_gross_area: float
    
    :param roof_opening: see (30), in m2
    :type roof_opening: float
    
    :param roof_u_value: see (30), in W/m2K
    :type roof_u_value: float
    
    :param roof_heat_capacity: see (30), in kJ/m2K
    :type roof_heat_capacity: float
    
    :param party_wall_net_area: see (32), in m2
    :type party_wall_net_area: float
    
    :param party_wall_u_value: see (32), in W/m2K
    :type party_wall_u_value: float
    
    :param party_wall_heat_capacity: see (32), in kJ/m2K
    :type party_wall_heat_capacity: float
    
    :param party_floor_net_area: see (32a), in m2
    :type party_floor_net_area: float
    
    :param party_floor_heat_capacity: see (32a), in kJ/m2K
    :type party_floor_heat_capacity: float
    
    :param party_ceiling_net_area: see (32b), in m2
    :type party_ceiling_net_area: float
    
    :param party_ceiling_heat_capacity: see (32b), in kJ/m2K
    :type party_ceiling_heat_capacity: float
    
    :param internal_wall_net_area: see (32c), in m2
    :type internal_wall_net_area: float
    
    :param internal_wall_heat_capacity: see (32c), in kJ/m2K
    :type internal_wall_heat_capacity: float
    
    :param internal_floor_net_area: see (32d), in m2
    :type internal_floor_net_area: float
    
    :param internal_floor_heat_capacity: see (32d), in kJ/m2K
    :type internal_floor_heat_capacity: float
    
    :param internal_ceiling_net_area: see (32e), in m2
    :type internal_ceiling_net_area: float
    
    :param internal_ceiling_heat_capacity: see (32e), in kJ/m2K
    :type internal_ceiling_heat_capacity: float
    
    :param effective_air_change_rate: see (25)
    :type effective_air_change_rate: list (of floats)
    

    :return:(
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

    solid_floor_UA: (float), see (26), in W/K
    semi_glazed_door_UA: (float), see (26a), in W/K
    window_UA: (float), see (27), in W/K
    roof_window_UA: (float), see (27a), in W/K
    basement_floor_UA: (float), see (28), in W/K
    basement_floor_Ak: (float), see (28), in kJ/K
    ground_floor_UA: (float), see (28a), in W/K
    ground_floor_Ak: (float), see (28a), in kJ/K
    exposed_floor_UA: (float), see (28b), in W/K
    exposed_floor_Ak: (float), see (28b), in kJ/K
    basement_wall_net_area: (float), see (29), in m2
    basement_wall_UA: (float), see (29), in W/K
    basement_wall_Ak: (float), see (29), in kJ/K
    external_wall_net_area: (float), see (29a), in m2
    external_wall_UA: (float), see (29a), in W/K
    external_wall_Ak: (float), see (29a), in kJ/K
    roof_net_area: (float), see (30), in m2
    roof_UA: (float), see (30), in W/K
    roof_Ak: (float), see (30), in kJ/K
    total_area_of_external_elements: (float), see (31), in m2
    party_wall_UA: (float), see (32), in W/K
    party_wall_Ak: (float), see (32), in kJ/K
    party_floor_Ak: (float), see (32a), in kJ/K
    party_ceiling_Ak: (float), see (32b), in kJ/K
    internal_wall_Ak: (float), see (32c), in kJ/K
    internal_floor_Ak: (float), see (32d), in kJ/K
    internal_ceiling_Ak: (float), see (32e), in kJ/K
    fabric_heat_loss: (float), see (33), in W/K
    heat_capacity: (float), see (34), in kJ/K
    thermal_mass_parameter: (float), see (35), in kJ/m2K
    thermal_bridges: (float), see (36), in W/K
    total_fabric_heat_loss: (float), see (37), in W/K
    ventilation_heat_loss_calculated_monthly:  (list of floats), see (82), in W/K
    heat_transfer_coefficient:  (list of floats), see (39), in W/K
    average_heat_transfer_coefficient  (float), see (39), in W/K
    heat_loss_parameter: (list of floats), see (40), in W/m2K
    average_heat_loss_parameter: (float), see (40), in W/m2K


    rtype: tuple


    """

    solid_floor_UA = solid_door_net_area * solid_door_u_value    
    semi_glazed_door_UA = semi_glazed_door_net_area * semi_glazed_door_u_value
    window_UA = window_net_area * window_u_value
    roof_window_UA = roof_window_net_area * roof_window_u_value
    basement_floor_UA = basement_floor_net_area * basement_floor_u_value
    basement_floor_Ak = basement_floor_net_area * basement_floor_heat_capacity
    ground_floor_UA = ground_floor_net_area * ground_floor_u_value
    ground_floor_Ak = ground_floor_net_area * ground_floor_heat_capacity
    exposed_floor_UA = exposed_floor_net_area * exposed_floor_u_value
    exposed_floor_Ak = exposed_floor_net_area * exposed_floor_heat_capacity
    basement_wall_net_area = basement_wall_gross_area - basement_wall_opening
    basement_wall_UA = basement_wall_net_area * basement_wall_u_value
    basement_wall_Ak= basement_wall_net_area * basement_wall_heat_capacity
    external_wall_net_area = external_wall_gross_area - external_wall_opening
    external_wall_UA = external_wall_net_area * external_wall_u_value
    external_wall_Ak = external_wall_net_area * external_wall_heat_capacity
    roof_net_area = roof_gross_area - roof_opening
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
    party_wall_UA = party_wall_net_area * party_wall_u_value
    party_wall_Ak = party_wall_net_area * party_wall_heat_capacity
    party_floor_Ak = party_floor_net_area * party_floor_heat_capacity
    party_ceiling_Ak = party_ceiling_net_area * party_ceiling_heat_capacity
    internal_wall_Ak = internal_wall_net_area * internal_wall_net_area
    internal_floor_Ak = internal_floor_net_area * internal_floor_heat_capacity
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
    
    


    return (
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









