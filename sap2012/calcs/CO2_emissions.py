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
    
    Table 12 is used for fuel emission factors
    
    :param space_heating_fuel_main_system_1: see (211) in kWh/year
    :type space_heating_fuel_main_system_1: float
    
    :param space_heating_fuel_main_system_2: see (212) in kWh/year
    :type space_heating_fuel_main_system_2: float
    
    :param space_heating_fuel_secondary: see (213) in kWh/year
    :type space_heating_fuel_secondary: float
    
    
    :param space_heating_fuel_emission_factor_main_system_1: see (261) in kg CO2/kWh
    :type space_heating_fuel_emission_factor_main_system_1: float
    
    :param space_heating_fuel_emission_factor_main_system_2: see (262) in kg CO2/kWh
    :type space_heating_fuel_emission_factor_main_system_2: float
    
    :param space_heating_fuel_emission_factor_secondary: see (263) in kg CO2/kWh
    :type space_heating_fuel_emission_factor_secondary: float
    
    :param water_fuel_used: in kWh/year
    :type water_fuel_used: float
    
    :param water_heating_fuel_emission_factor: see (264) in kg CO2/kWh
    :type water_heating_fuel_emission_factor: float
    
    :param space_cooling_fuel_used: in kWh/year
    :type space_cooling_fuel_used: float
    
    :param space_cooling_fuel_emission_factor: see (266) in kg CO2/kWh
    :type space_cooling_fuel_emission_factor: float
    
    :param electricity_for_pumps_fans_electric_keep_hot:  in kWh/year   
    :type electricity_for_pumps_fans_electric_keep_hot: float
    
    :param fuel_emission_factor_for_pumps_fans_electric_keep_hot: see (267) in kg CO2/kWh
    :type fuel_emission_factor_for_pumps_fans_electric_keep_hot: float
    
    :param energy_for_lighting: in kWh/year
    :type energy_for_lighting: float
    
    :param fuel_emission_factor_for_lighting: see (268) in kg CO2/kWh
    :type fuel_emission_factor_for_lighting: float
    
    :param space_cooling_fuel_used: in kWh/year
    :type space_cooling_fuel_used: float
    
    :param energy_saving_generation_technologies: in kWh/year
    :type energy_saving_generation_technologies: float
    
    :param energy_saving_generation_technologies_fuel_emission_factor: see (269) in kg CO2/kWh
    :type energy_saving_generation_technologies_fuel_emission_factor: float
 
    :param appendix_Q_energy_used:  in kWh/year   
    :type appendix_Q_energy_used: float
    
    :param appendix_Q_energy_used_fuel_emission_factor: see (270) in kg CO2/kWh
    :type appendix_Q_energy_used_fuel_emission_factor: float
    
    :param appendix_Q_energy_saved:  in kWh/year   
    :type appendix_Q_energy_saved: float
    
    :param appendix_Q_energy_saved_fuel_emission_factor: see (271) in kg CO2/kWh
    :type appendix_Q_energy_saved_fuel_emission_factor: float
    
    :param total_floor_area: in m2
    :type total_floor_area: float
    
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
    
    :param space_heating_main_system_1_emissions: see (261) in kg CO2/yr
    :type space_heating_main_system_1_emissions: float
    
    :param space_heating_main_system_2_emissions: see (262) in kg CO2/yr
    :type space_heating_main_system_2_emissions: float
    
    :param space_heating_secondary_emissions: see (263) in kg CO2/yr
    :type space_heating_secondary_emissions: float
    
    :param water_used_emissions: see (264) in kg CO2/yr
    :type water_used_emissions: float
    
    :param space_cooling_used_emissions: see (266) in kg CO2/yr
    :type space_cooling_used_emissions: float
    
    :param pumps_fans_electric_keep_hot_emissions: see (267)  in kg CO2/yr
    :type pumps_fans_electric_keep_hot_emissions: float
    
    :param lighting_emissions: see (268) in kg CO2/yr
    :type lighting_emissions: float
    
    :param appendix_Q_used_emissions: see (270) in kg CO2/yr
    :type appendix_Q_used_emissions: float
    
    :param appendix_Q_saved_emissions: see (271) in kg CO2/yr
    :type appendix_Q_saved_emissions: float
    
    :param energy_saving_generation_technologies_emissions: see (269) in kg CO2/yr
    :type energy_saving_generation_technologies_emissions: float
    
    :param space_and_water_heating_emissions: see (265) in kg CO2/yr
    :type space_and_water_heating_emissions: float
    
    :param appendix_Q_total_used_emissions:  in kg CO2/yr
    :type appendix_Q_total_used_emissions: float
    
    :param appendix_Q_total_saved_emissions: in kg CO2/yr
    :type appendix_Q_total_saved_emissions: float
    
    :param energy_saving_generation_technologies_total_emissions: in kg CO2/yr
    :type energy_saving_generation_technologies_total_emissions: float
    
    :param total_CO2_emissions_yearly: see (272) in kg CO2/yr
    :type total_CO2_emissions_yearly: float
    
    :param dwelling_CO2_emission_rate: see (273) in kg CO2/m2/yr
    :type dwelling_CO2_emission_rate: float
    
    :param CF:
    :type CF: float
    
    :param EI_rating: see (274)
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
    
    
    
    
    
    