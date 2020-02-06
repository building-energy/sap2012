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
    
    :param number_of_chimneys_main_heating:
    :type number_of_chimneys_main_heating: int


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
            average_heat_transfer_coefficient
            heat_loss_parameter,
            average_heat_loss_parameter
            )





    """
