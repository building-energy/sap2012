# -*- coding: utf-8 -*-

def fuel_costs (
        space_heating_fuel_main_system_1,
        space_heating_fuel_main_system_2,
        space_heating_fuel_secondary_system,
        space_heating_fuel_price_main_system_1,
        space_heating_fuel_price_main_system_2,
        space_heating_fuel_price_secondary,
        water_heating_high_rate_fraction_table_13,
        water_heating_low_rate_fraction_table_13,
        high_rate_fuel_price,
        low_rate_fuel_price,
        water_fuel_used,
        water_heating_fuel_price_other,
        space_cooling_fuel_used,
        space_cooling_fuel_price,
        electricity_for_pumps_fans_electric_keep_hot,
        fuel_price_for_pumps_fans_electric_keep_hot,
        electricity_for_lighting,
        fuel_price_for_lighting,
        additional_standing_charges_table_12,
        energy_saving_generation_technologies,
        energy_saving_generation_technologies_fuel_price,
        appendix_Q_energy_used,
        appendix_Q_energy_used_fuel_price,
        appendix_Q_energy_saved,
        appendix_Q_energy_saved_fuel_price
        ):
    
    """ Calculates Fuel Costs, section 10
    
    :param space_heating_fuel_main_system_1:
    :type space_heating_fuel_main_system_1: float
    
    :param space_heating_fuel_main_system_2:
    :type space_heating_fuel_main_system_2: float
    
    :param space_heating_fuel_secondary:
    :type space_heating_fuel_secondary: float
    
    :param space_heating_fuel_price_main_system_1:
    :type space_heating_fuel_price_main_system_1: float
    
    :param space_heating_fuel_price_main_system_2:
    :type space_heating_fuel_price_main_system_2: float
    
    :param space_heating_fuel_price_secondary:
    :type space_heating_fuel_price_secondary: float
    
    :param water_heating_high_rate_fraction_table_13:
    :type water_heating_high_rate_fraction_table_13: float
    
    :param water_heating_low_rate_fraction_table_13:
    :type water_heating_low_rate_fraction_table_13: float
    
    :param high_rate_fuel_price:
    :type high_rate_fuel_price: float
    
    :param low_rate_fuel_price:
    :type low_rate_fuel_price: float
    
    :param water_fuel_used:
    :type water_fuel_used: float
    
    :param water_heating_fuel_price_other:
    :type water_heating_fuel_price_other: float
    
    :param space_cooling_fuel_used:
    :type space_cooling_fuel_used: float
    
    :param space_cooling_fuel_price:
    :type space_cooling_fuel_price: float
    
    :param electricity_for_pumps_fans_electric_keep_hot:
    :type electricity_for_pumps_fans_electric_keep_hot: float
    
    :param fuel_price_for_pumps_fans_electric_keep_hot:
    :type fuel_price_for_pumps_fans_electric_keep_hot: float
    
    :param energy_for_lighting:
    :type energy_for_lighting: float
    
    :param fuel_price_for_lighting:
    :type fuel_price_for_lighting: float
    
    :param additional_standing_charges_table_12:
    :type additional_standing_charges_table_12: float
    
    :param energy_saving_generation_technologies:
    :type energy_saving_generation_technologies: float
    
    :param energy_saving_generation_technologies_fuel_price:
    :type energy_saving_generation_technologies_fuel_price: float
    
    :param appendix_Q_energy_used:
    :type appendix_Q_energy_used: float
    
    :param appendix_Q_energy_used_fuel_price:
    :type appendix_Q_energy_used_fuel_price: float
    
    :param appendix_Q_energy_saved:
    :type appendix_Q_energy_saved: float
    
    :param appendix_Q_energy_saved_fuel_price:
    :type appendix_Q_energy_saved_fuel_price: float
    
    :param space_heating_main_system_1_fuel_cost:
    :type space_heating_main_system_1_fuel_cost: float
    
    :param space_heating_main_system_2_fuel_cost:
    :type space_heating_main_system_2_fuel_cost: float
    
    :param space_heating_secondary_fuel_cost:
    :type space_heating_secondary_fuel_cost: float
    
    :param water_heating_high_rate_fuel_cost:
    :type water_heating_high_rate_fuel_cost: float
    
    :param water_heating_low_rate_fuel_cost:
    :type water_heating_low_rate_fuel_cost: float
    
    :param water_heating_cost_other:
    :type water_heating_cost_other: float
    
    :param space_cooling_cost:
    :type space_cooling_cost: float
    
    :param pumps_fan_keep_hot_cost:
    :type pumps_fan_keep_hot_cost: float
    
    :param lighting_cost:
    :type lighting_cost: float
    
    :param appendix_Q_used_fuel_cost:
    :type appendix_Q_used_fuel_cost: float
    
    :param appendix_Q_saved_fuel_cost:
    :type appendix_Q_saved_fuel_cost: float
    
    :param energy_saving_generation_technologies_fuel_cost:
    :type energy_saving_generation_technologies_fuel_cost: float
    
    :param appendix_Q_fuel_cost:
    :type appendix_Q_fuel_cost: float
    
    :param energy_saving_total_fuel_cost:
    :type energy_saving_total_fuel_cost: float
    
    :param total_fuel_cost:
    :type total_fuel_cost: float
    
    """
    
    space_heating_main_system_1_fuel_cost = (space_heating_fuel_main_system_1 * 
                                             space_heating_fuel_price_main_system_1 * 
                                             0.01)
    
    space_heating_main_system_2_fuel_cost = (space_heating_fuel_main_system_2 * 
                                             space_heating_fuel_price_main_system_2 * 
                                             0.01)
    
    space_heating_secondary_fuel_cost = (space_heating_fuel_secondary_system * 
                                         space_heating_fuel_price_secondary * 
                                         0.01)
    
    water_heating_high_rate_fuel_cost = (water_fuel_used * 
                                         water_heating_high_rate_fraction_table_13 * 
                                         high_rate_fuel_price * 
                                         0.01)
    
    water_heating_low_rate_fuel_cost = (water_fuel_used * 
                                        water_heating_low_rate_fraction_table_13 * 
                                        low_rate_fuel_price * 
                                        0.01)
    
    water_heating_cost_other = (water_fuel_used * 
                                water_heating_fuel_price_other * 
                                0.01)
    
    space_cooling_cost = (space_cooling_fuel_used * 
                          space_cooling_fuel_price * 
                          0.01)
    
    pumps_fan_keep_hot_cost = (electricity_for_pumps_fans_electric_keep_hot * 
                               fuel_price_for_pumps_fans_electric_keep_hot * 
                               0.01)
    
    lighting_cost = (electricity_for_lighting * 
                     fuel_price_for_lighting * 
                     0.01)
    
    
    appendix_Q_used_fuel_cost =[]
    for i in range(len(appendix_Q_energy_used)):
        appendix_Q_used_fuel_cost.append(appendix_Q_energy_used[i] * 
                                         appendix_Q_energy_used_fuel_price[i] * 
                                         0.01)
        
        
        
    appendix_Q_saved_fuel_cost =[]
    for i in range(len(appendix_Q_energy_saved)):
        appendix_Q_saved_fuel_cost.append(appendix_Q_energy_saved[i] * 
                                          appendix_Q_energy_saved_fuel_price[i] * 
                                          0.01)
        
        
        
    energy_saving_generation_technologies_fuel_cost =[]
    for i in range(len(energy_saving_generation_technologies)):
        energy_saving_generation_technologies_fuel_cost.append(energy_saving_generation_technologies[i] * 
                                                               energy_saving_generation_technologies_fuel_price[i] * 
                                                               0.01)
    
    appendix_Q_fuel_cost = (sum(appendix_Q_used_fuel_cost) + 
                            sum(appendix_Q_saved_fuel_cost))
    
    energy_saving_total_fuel_cost = sum(energy_saving_generation_technologies_fuel_cost)
    
    
    total_fuel_cost = (space_heating_main_system_1_fuel_cost +
                       space_heating_main_system_2_fuel_cost +
                       space_heating_secondary_fuel_cost +
                       water_heating_high_rate_fuel_cost +
                       water_heating_low_rate_fuel_cost +
                       water_heating_cost_other +
                       space_cooling_cost +
                       pumps_fan_keep_hot_cost +
                       lighting_cost +
                       appendix_Q_fuel_cost +
                       energy_saving_total_fuel_cost +
                       additional_standing_charges_table_12
                       )
    
    
    return(space_heating_main_system_1_fuel_cost,
           space_heating_main_system_2_fuel_cost,
           space_heating_secondary_fuel_cost,
           water_heating_high_rate_fuel_cost,
           water_heating_low_rate_fuel_cost,
           water_heating_cost_other,
           space_cooling_cost,
           pumps_fan_keep_hot_cost,
           lighting_cost,
           appendix_Q_fuel_cost,
           energy_saving_total_fuel_cost,
           additional_standing_charges_table_12,
           total_fuel_cost
            )
    
    
    
    