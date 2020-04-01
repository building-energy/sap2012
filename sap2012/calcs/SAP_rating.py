# -*- coding: utf-8 -*-


def SAP_rating (
        energy_cost_deflator,
        total_fuel_cost,
        total_floor_area
        ):
    
    """ Calculates SAP rating, section 11
    
    :param energy_cost_deflator:
    :type energy_cost_deflator: float
    
    :param total_energy_cost:
    :type total_energy_cost: float
    
    :param total_floor_area:
    :type total_floor_area: float
    
    :param SAP_rating:
    :type SAP_rating: float
    
    """
    
    
    energy_cost_factor = (total_energy_cost * energy_cost_deflator) / (total_floor_area + 45)
    
    if energy_cost_factor < 3.5:
        SAP_rating = 100 - 13.95 * energy_cost_factor
        
    else:
        SAP_rating = 171 - 121 * math.log10(energy_cost_factor)
        
    return(
            SAP_rating
            )    
        
        
        
        
        