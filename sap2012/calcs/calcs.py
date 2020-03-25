# -*- coding: utf-8 -*-

from . import overall_dwelling_dimensions
from . import ventilation_rates
from . import heat_losses_and_heat_loss_parameter

def calcs(
        
        # overall_dwelling_dimensions inputs
        area,
        average_storey_height,
        
        # ventilation_rates inputs
        number_of_chimneys_main_heating,
        number_of_chimneys_secondary_heating,
        number_of_chimneys_other,
        number_of_open_flues_main_heating,
        number_of_open_flues_secondary_heating,
        number_of_open_flues_other,
        number_of_intermittant_fans_total,
        number_of_passive_vents_total,
        number_of_flueless_gas_fires_total,
        #### note that 'dwelling_volume' isn't needed as an input here because it is calculated in 'overall_dwelling_dimenstions' #### Please delete this line once read
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
        
        # heat_losses_and_heat_loss_parameter inputs
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
        thermal_bridges_appendix_k,
        ):
    
    """This method runs the complete set of calculations for SAP2012
    
    """
    
    # overall_dwelling_dimensions calculations
    result=overall_dwelling_dimensions(
        area,
        average_storey_height)
    
    volume,total_floor_area,dwelling_volume=result
    
    
    # ventilation_rates calculations
    result=ventilation_rates(
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
        efficiency_allowing_for_in_use_factor
        )
    
    (number_of_chimneys_total,
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
        effective_air_change_rate) = result
    
     
    # heat_losses_and_heat_loss_parameter calculations
    result=heat_losses_and_heat_loss_parameter(
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
        )     
    
    (solid_floor_UA,
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
        average_heat_loss_parameter) = result
     
     
     
    ### NEED TO COMPLETE WITH THE REMAINING CALCULATION MODULES IN ORDER 
     
     
     
    return (
            
        # overall_dwelling_dimensions results
        volume,
        total_floor_area,
        dwelling_volume,
        
        # ventilation_rates results
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
        effective_air_change_rate,
        
        # heat_losses_and_heat_loss_parameter results
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
    
    
    
    
    
    
    
    
    
    
    
    