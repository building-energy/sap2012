# -*- coding: utf-8 -*-
import math

def internal_gains_appendix_L (
        total_floor_area,
        assumed_occupancy,
        number_of_low_energy_light_bulbs,
        total_number_of_light_bulbs,
        frame_factor,
        window_area,
        light_access_factor_table_6d,
        light_transmittance_factor_table_6d,
        month_number,
        days_in_month,
        heat_gains_from_water_heating_monthly
        ):
    """Internal gain calculations as given in Appendix L.
    
    
    
    
    :rtype: dict
    
    """
    
    G_L = ((0.9 * window_area * 
            light_transmittance_factor_table_6d * 
            frame_factor * 
            light_access_factor_table_6d) / 
            total_floor_area)
    
    
    C_1 = (1 - 0.5 * 
           (number_of_low_energy_light_bulbs / 
            total_number_of_light_bulbs))
    
    
    if G_L > 0.095:
        C_2 = 0.96
        
    else:
        C_2 = (52.2 * (G_L)**2 - 
               9.94 * G_L + 1.433)
        
        
    E_B = 59.73 * (total_floor_area * assumed_occupancy)**0.4714
    
    
    initial_annual_lighting_demand = E_B * C_1 * C_2
    
    
    monthly_lighting_demand = []
    for i in range(12):
        monthly_lighting_demand.append(initial_annual_lighting_demand * (1 + 0.5 * math.cos(2*math.pi * (month_number[i] - 0.2) / 12)) * days_in_month[i] / 365)
        
    
    annual_lighting_demand = sum(monthly_lighting_demand)
    
    lighting_gains = []
    for i in range(12):
        lighting_gains.append(monthly_lighting_demand[i] * 
                                                0.85 * 1000 / 
                                                (24 * days_in_month[i]))
        
        
    initial_annual_electrical_appliance_demand = 207.8 * (total_floor_area * assumed_occupancy)**0.4714
    
    monthly_electrical_appliance_demand = []
    for i in range(12):
        monthly_electrical_appliance_demand.append(initial_annual_electrical_appliance_demand * (1 + 0.157 * math.cos(2*math.pi * (month_number[i] - 1.78) / 12)) * days_in_month[i] / 365)
        
        
    annual_electrical_appliance_demand = sum(monthly_electrical_appliance_demand)
    
    appliances_gains = []
    for i in range(12):
        appliances_gains.append(monthly_electrical_appliance_demand[i] * 1000 / (24 * days_in_month[i]))
        
    
    
    
    cooking_gains = []
    for i in range(12):
        cooking_gains.append(35 + 7 * assumed_occupancy)
        
    losses= []  
    for i in range(12):
        losses.append(assumed_occupancy * -40)
    
    water_heating_gains = []
    for i in range(12):
        water_heating_gains.append((heat_gains_from_water_heating_monthly[i] * 1000) / 
                                   (days_in_month[i] * 24))
        
    metabolic_gains = []
    for i in range(12):
        metabolic_gains.append(60 * assumed_occupancy)
    
        
        
        
    return dict(
        G_L=G_L,
        C_1=C_1,
        C_2=C_2,
        E_B=E_B,
        initial_annual_lighting_demand=initial_annual_lighting_demand,
        monthly_lighting_demand=monthly_lighting_demand,
        annual_lighting_demand=annual_lighting_demand,
        lighting_gains=lighting_gains,
        initial_annual_electrical_appliance_demand=initial_annual_electrical_appliance_demand,
        monthly_electrical_appliance_demand=monthly_electrical_appliance_demand,
        annual_electrical_appliance_demand=annual_electrical_appliance_demand,
        appliances_gains=appliances_gains,
        cooking_gains=cooking_gains,
        losses=losses,
        water_heating_gains=water_heating_gains,
        metabolic_gains=metabolic_gains
        )
    
    

