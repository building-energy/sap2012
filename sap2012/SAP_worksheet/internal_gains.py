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
    
    """Calculates Internal Gains, Section 5.
    
    :param metabolic_gains: Calculated using table 5. See (66), in W.
    :type metabolic_gains: list (float)
    
    :param lighting_gains: Calculated using table 5. See (67), in W.
    :type lighting_gains: list (float)
    
    :param appliances_gains: Calculated using Table 5. See (68), in W.
    :type appliances_gains: list (float)
    
    :param cooking_gains: Calculated using Table 5. See (69), in W.
    :type cooking_gains: list (float)
    
    :param pumps_and_fans_gains: Calculated using Table 5a. See (70), in W.
    :type pumps_and_fans_gains: list (float)
    
    :param losses: Calculated using Table 5. See (71), in W.
    :type losses: list (float)
    
    :param water_heating_gains: Calculated using Table 5. See (72), in W.
    :type water_heating_gains: list (float)
    
    :returns: A dictionary with keys ( total_internal_gains )
    
    - **total_internal_gains** (`list` (`float`)): Sum of all internal gains. See (73), in W.
    
    
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
        
        
    return dict(total_internal_gains=total_internal_gains)        