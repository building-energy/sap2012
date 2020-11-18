# -*- coding: utf-8 -*-


def internal_gains (
        metabolic_gains,
        lighting_gains,
        appliances_gains,
        cooking_gains,
        pumps_and_fans_gains,
        losses,
        water_heating_gains
        ):
    
    """ Calculates Internal Gains, section 5
    
    :param metabolic_gains: Calculated using table 5 see (66), in W
    :type metabolic_gains: list of floats
    
    :param lighting_gains: Calculated using table 5 see (67), in W
    :type lighting_gains: list of floats
    
    :param appliances_gains: Calculated using table 5 see (68), in W
    :type appliances_gains: list of floats
    
    :param cooking_gains:Calculated using table 5 see (69), in W
    :type cooking_gains: list of floats
    
    :param pumps_and_fans_gains: Calculated using table 5a see (70), in W
    :type pumps_and_fans_gains: list of floats
    
    :param losses: Calculated using table 5 see (71), in W
    :type losses: list of floats
    
    :param water_heating_gains: Calculated using table 5 see (72), in W
    :type water_heating_gains: list of floats
    
    return (total_internal_gains) 
    
    :param total_internal_gains: Sum of all internal gains see (73), in W
    :type total_internal_gains: list of floats
    
    """
    
    total_internal_gains =[]
    for i in range(12):
        total_internal_gains.append(metabolic_gains[i] + 
                                lighting_gains[i] +
                                appliances_gains[i] +
                                cooking_gains[i] +
                                pumps_and_fans_gains[i] +
                                losses[i] +
                                water_heating_gains[i])
        
        
    return (total_internal_gains)        