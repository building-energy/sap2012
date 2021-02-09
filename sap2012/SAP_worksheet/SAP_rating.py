# -*- coding: utf-8 -*-
import math

def SAP_rating (
        energy_cost_deflator,
        total_fuel_cost,
        total_floor_area
        ):
    
    """Calculates SAP rating, Section 11.
    
    :param energy_cost_deflator: See (256).
        Found in Table 12.
    :type energy_cost_deflator: float
    
    :param total_energy_cost: See (255) in £.
    :type total_energy_cost: float
    
    :param total_floor_area: in m2.
    :type total_floor_area: float
    
    :returns: A dictionary with keys of ( energy_cost_factor,
                                         SAP_rating_value )    
    
    - **energy_cost_factor** (`float`): See (257)
    
    - **SAP_rating_value** (`float`): See (258)
    
    :rtype: dict
    
    """
    
    
    energy_cost_factor = (total_fuel_cost * energy_cost_deflator) / (total_floor_area + 45)
    
    if energy_cost_factor < 3.5:
        SAP_rating_value = 100 - 13.95 * energy_cost_factor
        
    else:
        SAP_rating_value = 117 - 121 * math.log10(energy_cost_factor)
        
    return dict(energy_cost_factor=energy_cost_factor,
                SAP_rating_value=SAP_rating_value
                )    
        
        
        
        
        