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
    
    :param metabolic_gains:
    :type metabolic_gains: float
    
    :param lighting_gains:
    :type lighting_gains: float
    
    :param appliances_gains:
    :type appliances_gains: float
    
    :param cooking_gains:
    :type cooking_gains: float
    
    :param pumps_and_fans_gains:
    :type pumps_and_fans_gains: float
    
    :param losses:
    :type losses: float
    
    :param water_heating_gains:
    :type water_heating_gains: float
    
    :param total_internal_gains:
    :type total_internal_gains: float
    
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
        
        
    return (
            total_internal_gains)        