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
    
    :param total_floor_area: See (4).
    :type total_floor_area: float    
        
    :param assumed_occupancy: See (42). Calculated using equation from (42). 
        If TFA > 13.9, N = 1 + 1.76 * [1 - exp(-0.000349 * (TFA -13.9)2)] + 0.0013 * (TFA -13.9). if TFA =< 13.9, N = 1. Where TFA is the Total Floor Area.
    :type assumed_occupancy: float
    
    :param number_of_low_energy_light_bulbs:
    :type number_of_low_energy_light_bulbs: int
        
    :param total_number_of_light_bulbs:
    :type total_number_of_light_bulbs: int
        
    :param frame_factor:
    :type frame_factor: float
        
    :param window_area:
    :type window_area: float
        
    :param light_access_factor_table_6d:
    :type light_access_factor_table_6d: float
        
    :param light_transmittance_factor_table_6d:
    :type light_transmittance_factor_table_6d: float
        
    :param month_number:
    :type month_number: list(int)
        
    :param days_in_month: List of the number of days in each month of the calendar year.
    :type days_in_month: float(int)
    
    :param heat_gains_from_water_heating_monthly: (65) in kWh/month.
    :type heat_gains_from_water_heating_monthly: list(float)
    
    :returns: A dictionary with keys of (
        G_L,
        C_1,
        C_2,
        E_B,
        initial_annual_lighting_demand,
        monthly_lighting_demand,
        annual_lighting_demand,
        lighting_gains,
        initial_annual_electrical_appliance_demand,
        monthly_electrical_appliance_demand,
        annual_electrical_appliance_demand,
        appliances_gains,
        cooking_gains,
        losses,
        water_heating_gains,
        metabolic_gains
        )
    
    - **G_L** (`float`)-
    
    - **C_1** (`float`)-
    
    - **C_2** (`float`)-
    
    - **E_B** (`float`)-
    
    - **initial_annual_lighting_demand** (`float`)-
    
    - **monthly_lighting_demand** (`list` (`float`))-
    
    - **annual_lighting_demand** (`float`)-
    
    - **lighting_gains** (`list` (`float`))-
    
    - **initial_annual_electrical_appliance_demand** (`float`)-
    
    - **monthly_electrical_appliance_demand** (`list` (`float`))-
    
    - **annual_electrical_appliance_demand** (`float`)-
    
    - **appliances_gains** (`list` (`float`))-
    
    - **cooking_gains** (`list` (`float`))-
    
    - **losses** (`list` (`float`))-
    
    - **water_heating_gains** (`list` (`float`))-
    
    - **metabolic_gains** (`list` (`float`))-

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
    
    

