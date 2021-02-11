# -*- coding: utf-8 -*-

def fuel_costs (
        space_heating_fuel_used_main_system_1,
        space_heating_fuel_used_main_system_2,
        space_heating_fuel_used_secondary,
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
        energy_for_lighting,
        fuel_price_for_lighting,
        additional_standing_charges_table_12,
        energy_saving_generation_technologies,
        energy_saving_generation_technologies_fuel_price,
        appendix_Q_energy_used,
        appendix_Q_energy_used_fuel_price,
        appendix_Q_energy_saved,
        appendix_Q_energy_saved_fuel_price
        ):
    
    """Calculates Fuel Costs, Section 10.
    
    Table 12 is used for fuel price factors.
    
    :param space_heating_fuel_main_system_1: See (211) in kWh/year.
    :type space_heating_fuel_main_system_1: float
    
    :param space_heating_fuel_main_system_2: See (212) in kWh/year.
    :type space_heating_fuel_main_system_2: float
    
    :param space_heating_fuel_secondary: See (213) in kWh/year.
    :type space_heating_fuel_secondary: float
    
    :param space_heating_fuel_price_main_system_1: See (240) in £/kWh.
    :type space_heating_fuel_price_main_system_1: float
    
    :param space_heating_fuel_price_main_system_2: See (241) in £/kWh.
    :type space_heating_fuel_price_main_system_2: float
    
    :param space_heating_fuel_price_secondary: See (242) in £/kWh.
    :type space_heating_fuel_price_secondary: float
    
    :param water_heating_high_rate_fraction_table_13: See (243) in £/kWh.
    :type water_heating_high_rate_fraction_table_13: float
    
    :param water_heating_low_rate_fraction_table_13: See (244) in £/kWh.
    :type water_heating_low_rate_fraction_table_13: float
    
    :param high_rate_fuel_price: See (245) in £/kWh.
    :type high_rate_fuel_price: float
    
    :param low_rate_fuel_price: See (246) in £/kWh.
    :type low_rate_fuel_price: float
    
    :param water_fuel_used: See (219) in kWh/year.
    :type water_fuel_used: float
    
    :param water_heating_fuel_price_other: See (247) in £/kWh.
    :type water_heating_fuel_price_other: float
    
    :param space_cooling_fuel_used: See (248) in kWh/year.
    :type space_cooling_fuel_used: float
    
    :param space_cooling_fuel_price: See (248) in £/kWh.
    :type space_cooling_fuel_price: float
    
    :param electricity_for_pumps_fans_electric_keep_hot: See (249) in kWh/year.
    :type electricity_for_pumps_fans_electric_keep_hot: float
    
    :param fuel_price_for_pumps_fans_electric_keep_hot: See (249) in £/kWh.
    :type fuel_price_for_pumps_fans_electric_keep_hot: float
    
    :param energy_for_lighting: See (231) in kWh/year.
    :type energy_for_lighting: float
    
    :param fuel_price_for_lighting: See (250) in £/kWh.
    :type fuel_price_for_lighting: float
    
    :param additional_standing_charges_table_12: See (251) in £/kWh.
    :type additional_standing_charges_table_12: float
    
    :param energy_saving_generation_technologies: See (252) in kWh/year.
    :type energy_saving_generation_technologies: float
    
    :param energy_saving_generation_technologies_fuel_price: See (252) in £/kWh.
    :type energy_saving_generation_technologies_fuel_price: float
    
    :param appendix_Q_energy_used: See (253) in kWh/year.
    :type appendix_Q_energy_used: float
    
    :param appendix_Q_energy_used_fuel_price: See (253) in £/kWh.
    :type appendix_Q_energy_used_fuel_price: float
    
    :param appendix_Q_energy_saved: See (254) in kWh/year.
    :type appendix_Q_energy_saved: float
    
    :param appendix_Q_energy_saved_fuel_price: See (254) in £/kWh.
    :type appendix_Q_energy_saved_fuel_price: float
    
    :returns: A dictionary with keys of (
        space_heating_main_system_1_fuel_cost,
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
    
    - **space_heating_main_system_1_fuel_cost** (`float`): See (240) in £/year.
    
    - **space_heating_main_system_2_fuel_cost** (`float`): See (241) in £/year.
    
    - **space_heating_secondary_fuel_cost** (`float`): See (242) in £/year.
    
    - **water_heating_high_rate_fuel_cost** (`float`): See (245) in £/year.
    
    - **water_heating_low_rate_fuel_cost** (`float`): See (246) in £/year.
    
    - **water_heating_cost_other** (`float`): See (247) in £/year.
    
    - **space_cooling_cost** (`float`): See (248) in £/year.
    
    - **pumps_fan_keep_hot_cost** (`float`): See (249) in £/year.
    
    - **lighting_cost** (`float`): See (250) in £/year.
    
    - **appendix_Q_used_fuel_cost** (`float`): See (253) in £/year.
    
    - **appendix_Q_saved_fuel_cost** (`float`): See (254) in £/year.
    
    - **energy_saving_generation_technologies_fuel_cost** (`float`): See (252) in £/year.
    
    - **appendix_Q_fuel_cost** (`float`): in £/year.
    
    - **energy_saving_total_fuel_cost** (`float`): in £/year.
    
    - **total_fuel_cost** (`float`): See (255) in £/year.
    
    :rtype: dict
    
    """
    
    space_heating_main_system_1_fuel_cost = (space_heating_fuel_used_main_system_1 * 
                                             space_heating_fuel_price_main_system_1 * 
                                             0.01)
    
    space_heating_main_system_2_fuel_cost = (space_heating_fuel_used_main_system_2 * 
                                             space_heating_fuel_price_main_system_2 * 
                                             0.01)
    
    space_heating_secondary_fuel_cost = (space_heating_fuel_used_secondary * 
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
    
    lighting_cost = (energy_for_lighting * 
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
    for i in range(len(energy_saving_generation_technologies_fuel_price)):
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
    
    
    return dict(space_heating_main_system_1_fuel_cost=space_heating_main_system_1_fuel_cost,
                space_heating_main_system_2_fuel_cost=space_heating_main_system_2_fuel_cost,
                space_heating_secondary_fuel_cost=space_heating_secondary_fuel_cost,
                water_heating_high_rate_fuel_cost=water_heating_high_rate_fuel_cost,
                water_heating_low_rate_fuel_cost=water_heating_low_rate_fuel_cost,
                water_heating_cost_other=water_heating_cost_other,
                space_cooling_cost=space_cooling_cost,
                pumps_fan_keep_hot_cost=pumps_fan_keep_hot_cost,
                lighting_cost=lighting_cost,
                appendix_Q_fuel_cost=appendix_Q_fuel_cost,
                energy_saving_total_fuel_cost=energy_saving_total_fuel_cost,
                additional_standing_charges_table_12=additional_standing_charges_table_12,
                total_fuel_cost=total_fuel_cost
                )
    
    
    
    