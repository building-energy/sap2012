# -*- coding: utf-8 -*-
import math

def CO2_emissions(
        space_heating_fuel_used_main_system_1,
        space_heating_fuel_used_main_system_2,
        space_heating_fuel_used_secondary,
        space_heating_fuel_emission_factor_main_system_1,
        space_heating_fuel_emission_factor_main_system_2,
        space_heating_fuel_emission_factor_secondary,
        water_fuel_used,
        water_heating_fuel_emission_factor,
        space_cooling_fuel_used,
        space_cooling_fuel_emission_factor,
        electricity_for_pumps_fans_electric_keep_hot,
        fuel_emission_factor_for_pumps_fans_electric_keep_hot,
        energy_for_lighting,
        fuel_emission_factor_for_lighting,
        energy_saving_generation_technologies,
        energy_saving_generation_technologies_fuel_emission_factor,
        appendix_Q_energy_used,
        appendix_Q_energy_used_fuel_emission_factor,
        appendix_Q_energy_saved,
        appendix_Q_energy_saved_fuel_emission_factor,
        total_floor_area
        ):
    
    """ Calculates CO2 emissions, section 12
    
    :param space_heating_fuel_main_system_1:
    :type space_heating_fuel_main_system_1: float
    
    :param space_heating_fuel_main_system_2:
    :type space_heating_fuel_main_system_2: float
    
    :param space_heating_fuel_secondary:
    :type space_heating_fuel_secondary: float
    
    :param space_heating_fuel_emission_factor_main_system_1:
    :type space_heating_fuel_emission_factor_main_system_1: float
    
    :param space_heating_fuel_emission_factor_main_system_2:
    :type space_heating_fuel_emission_factor_main_system_2: float
    
    :param space_heating_fuel_emission_factor_secondary:
    :type space_heating_fuel_emission_factor_secondary: float
    
    :param water_fuel_used:
    :type water_fuel_used: float
    
    :param water_heating_fuel_emission_factor:
    :type water_heating_fuel_emission_factor: float
    
    :param space_cooling_fuel_used:
    :type space_cooling_fuel_used: float
    
    :param space_cooling_fuel_emission_factor:
    :type space_cooling_fuel_emission_factor: float
    
    :param electricity_for_pumps_fans_electric_keep_hot:
    :type electricity_for_pumps_fans_electric_keep_hot: float
    
    :param fuel_emission_factor_for_pumps_fans_electric_keep_hot:
    :type fuel_emission_factor_for_pumps_fans_electric_keep_hot: float
    
    :param energy_for_lighting:
    :type energy_for_lighting: float
    
    :param fuel_emission_factor_for_lighting:
    :type fuel_emission_factor_for_lighting: float
    
    :param space_cooling_fuel_used:
    :type space_cooling_fuel_used: float
    
    :param energy_saving_generation_technologies:
    :type energy_saving_generation_technologies: float
    
    :param energy_saving_generation_technologies_fuel_emission_factor:
    :type energy_saving_generation_technologies_fuel_emission_factor: float
    
    :param appendix_Q_energy_used:
    :type appendix_Q_energy_used: float
    
    :param appendix_Q_energy_used_fuel_emission_factor:
    :type appendix_Q_energy_used_fuel_emission_factor: float
    
    :param appendix_Q_energy_saved:
    :type appendix_Q_energy_saved: float
    
    :param appendix_Q_energy_saved_fuel_emission_factor:
    :type appendix_Q_energy_saved_fuel_emission_factor: float
    
    :param total_floor_area:
    :type total_floor_area: float
    
    :param space_heating_main_system_1_emissions:
    :type space_heating_main_system_1_emissions: float
    
    :param space_heating_main_system_2_emissions:
    :type space_heating_main_system_2_emissions: float
    
    :param space_heating_secondary_emissions:
    :type space_heating_secondary_emissions: float
    
    :param water_used_emissions:
    :type water_used_emissions: float
    
    :param space_cooling_used_emissions:
    :type space_cooling_used_emissions: float
    
    :param pumps_fans_electric_keep_hot_emissions:
    :type pumps_fans_electric_keep_hot_emissions: float
    
    :param lighting_emissions:
    :type lighting_emissions: float
    
    :param appendix_Q_used_emissions:
    :type appendix_Q_used_emissions: float
    
    :param appendix_Q_saved_emissions:
    :type appendix_Q_saved_emissions: float
    
    :param energy_saving_generation_technologies_emissions:
    :type energy_saving_generation_technologies_emissions: float
    
    :param space_and_water_heating_emissions:
    :type space_and_water_heating_emissions: float
    
    :param appendix_Q_total_used_emissions:
    :type appendix_Q_total_used_emissions: float
    
    :param appendix_Q_total_saved_emissions:
    :type appendix_Q_total_saved_emissions: float
    
    :param energy_saving_generation_technologies_total_emissions:
    :type energy_saving_generation_technologies_total_emissions: float
    
    :param total_CO2_emissions_yearly:
    :type total_CO2_emissions_yearly: float
    
    :param dwelling_CO2_emission_rate:
    :type dwelling_CO2_emission_rate: float
    
    :param CF:
    :type CF: float
    
    :param EI_rating:
    :type EI_rating: float
    
    
    """
    
    space_heating_main_system_1_emissions = (space_heating_fuel_used_main_system_1 * 
                                             space_heating_fuel_emission_factor_main_system_1)
    
    
    
    space_heating_main_system_2_emissions = (space_heating_fuel_used_main_system_2 * 
                                             space_heating_fuel_emission_factor_main_system_2)
    
    
    
    space_heating_secondary_emissions = (space_heating_fuel_used_secondary * 
                                         space_heating_fuel_emission_factor_secondary)
    
    
    
    water_used_emissions =  (water_fuel_used * 
                             water_heating_fuel_emission_factor)
    
    
    
    space_cooling_used_emissions = (space_cooling_fuel_used * 
                                    space_cooling_fuel_emission_factor)
    
    
    
    pumps_fans_electric_keep_hot_emissions = (electricity_for_pumps_fans_electric_keep_hot * 
                                              fuel_emission_factor_for_pumps_fans_electric_keep_hot)
    
    
    
    lighting_emissions = (energy_for_lighting * 
                          fuel_emission_factor_for_lighting)
    
    
    appendix_Q_used_emissions =[]
    for i in range(len(appendix_Q_energy_used)):
        appendix_Q_used_emissions.append(appendix_Q_energy_used[i] * 
                                     appendix_Q_energy_used_fuel_emission_factor[i])
    
    
    appendix_Q_saved_emissions =[]
    for i in range(len(appendix_Q_energy_saved)):
        appendix_Q_saved_emissions.append(appendix_Q_energy_saved[i] * 
                                      appendix_Q_energy_saved_fuel_emission_factor[i])
        
        
    energy_saving_generation_technologies_emissions =[]
    for i in range(len(energy_saving_generation_technologies)):
        energy_saving_generation_technologies_emissions.append(energy_saving_generation_technologies[i] * 
                                                           energy_saving_generation_technologies_fuel_emission_factor[i])
    
   
    
    space_and_water_heating_emissions = (space_heating_main_system_1_emissions + space_heating_main_system_2_emissions +
                                         space_heating_secondary_emissions + water_used_emissions)
    
    
    
    
    appendix_Q_total_used_emissions = sum(appendix_Q_used_emissions)
    
    
    appendix_Q_total_saved_emissions = sum(appendix_Q_saved_emissions)
    
    
    energy_saving_generation_technologies_total_emissions = sum(energy_saving_generation_technologies_emissions)
    
    
    
    total_CO2_emissions_yearly = (space_and_water_heating_emissions + space_cooling_used_emissions + pumps_fans_electric_keep_hot_emissions + 
                                  lighting_emissions + appendix_Q_total_used_emissions + appendix_Q_total_saved_emissions + 
                                  energy_saving_generation_technologies_total_emissions)  
    
    
    dwelling_CO2_emission_rate = total_CO2_emissions_yearly / total_floor_area
    
    
    
    CF = total_CO2_emissions_yearly / (total_floor_area + 45)
    
    
    if CF < 28.3:
        EI_rating = 100 - 1.34 * CF
        
    else:
        EI_rating = 200 - 95 * math.log10(CF)
        
        
        
    return(space_heating_main_system_1_emissions,
           space_heating_main_system_2_emissions,
           space_heating_secondary_emissions,
           water_used_emissions,
           space_cooling_used_emissions,
           pumps_fans_electric_keep_hot_emissions,
           lighting_emissions,
           appendix_Q_used_emissions,
           appendix_Q_saved_emissions,
           energy_saving_generation_technologies_emissions,
           space_and_water_heating_emissions,
           appendix_Q_total_used_emissions,
           appendix_Q_total_saved_emissions,
           energy_saving_generation_technologies_total_emissions,
           total_CO2_emissions_yearly,
           dwelling_CO2_emission_rate,
           CF,
           EI_rating
            )
    
    
    
    
    
    