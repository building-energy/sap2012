# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:40:12 2020


"""

def solar_gains (
        access_factor_table_6d_north,
        access_factor_table_6d_north_east,
        access_factor_table_6d_east,
        access_factor_table_6d_south_east,
        access_factor_table_6d_south,
        access_factor_table_6d_south_west,
        access_factor_table_6d_west,
        access_factor_table_6d_north_west,
        access_factor_table_6d_roof_windows,
        area_north,
        area_north_east,
        area_east,
        area_south_east,
        area_south,
        area_south_west,
        area_west,
        area_north_west,
        area_roof_windows,
        solar_flux_north,
        solar_flux_north_east,
        solar_flux_east,
        solar_flux_south_east,
        solar_flux_south,
        solar_flux_south_west,
        solar_flux_west,
        solar_flux_north_west,
        solar_flux_roof_windows,
        g_table_6b_north,
        g_table_6b_north_east,
        g_table_6b_east,
        g_table_6b_south_east,
        g_table_6b_south,
        g_table_6b_south_west,
        g_table_6b_west,
        g_table_6b_north_west,
        g_table_6b_roof_windows,
        FF_table_6b_north,
        FF_table_6b_north_east,
        FF_table_6b_east,
        FF_table_6b_south_east,
        FF_table_6b_south,
        FF_table_6b_south_west,
        FF_table_6b_west,
        FF_table_6b_north_west,
        FF_table_6b_roof_windows,
        total_internal_gains
        ):
    
    """Calculates Solar Gains, Section 6.
    
    Also includes U3 from appendix U to calculate solar gains. 
    This calculation is found in tables/solar_gains_appendix_U.
    
    :param access_factor_table_6d_north: See (74).
    :type access_factor_table_6d_north: float
    
    :param access_factor_table_6d_north_east:
    :type access_factor_table_6d_north_east: float
    
    :param access_factor_table_6d_east:
    :type access_factor_table_6d_east: float
    
    :param access_factor_table_6d_south_east:
    :type access_factor_table_6d_south_east: float
    
    :param access_factor_table_6d_south:
    :type access_factor_table_6d_south: float
    
    :param access_factor_table_6d_south_west:
    :type access_factor_table_6d_south_west: float
    
    :param access_factor_table_6d_west:
    :type access_factor_table_6d_west: float
    
    :param access_factor_table_6d_north_west:
    :type access_factor_table_6d_north_west: float
    
    :param access_factor_table_6d_roof_windows:
    :type access_factor_table_6d_roof_windows: float
    
    :param area_north: See (74) in m.
    :type area_north: float
    
    :param area_north_east: See (75) in m.
    :type area_north_east: float
    
    :param area_east: See (76) in m.
    :type area_east: float
    
    :param area_south_east: See (77) in m.
    :type area_south_east: float
    
    :param area_south: See (78) in m.
    :type area_south: float
    
    :param area_south_west: See (79) in m.
    :type area_south_west: float
    
    :param area_west: See (80) in m.
    :type area_west: float
    
    :param area_north_west: See (81) in m.
    :type area_north_west: float
    
    :param area_roof_windows: See (82) in m.
    :type area_roof_windows: float
    
    :param solar_flux_north:
    :type solar_flux_north: float
    
    :param solar_flux_north_east:
    :type solar_flux_north_east: float
    
    :param solar_flux_east:
    :type solar_flux_east: float
    
    :param solar_flux_south_east:
    :type solar_flux_south_east: float
    
    :param solar_flux_south:
    :type solar_flux_south: float
    
    :param solar_flux_south_west:
    :type solar_flux_south_west: float
    
    :param solar_flux_west:
    :type solar_flux_west: float
    
    :param solar_flux_north_west:
    :type solar_flux_north_west: float
    
    :param solar_flux_roof_windows:
    :type solar_flux_roof_windows: float
    
    :param g_table_6b_north: See (74).
    :type g_table_6b_north: float
    
    :param g_table_6b_north_east: See (75).
    :type g_table_6b_north_east: float
    
    :param g_table_6b_east: See (76).
    :type g_table_6b_east: float
    
    :param g_table_6b_south_east: See (77).
    :type g_table_6b_south_east: float
    
    :param g_table_6b_south: See (78).
    :type g_table_6b_south: float
    
    :param g_table_6b_south_west: See (79).
    :type g_table_6b_south_west: float
    
    :param g_table_6b_west: See (80).
    :type g_table_6b_west: float
    
    :param g_table_6b_north_west: See (81).
    :type g_table_6b_north_west: float
    
    :param g_table_6b_roof_windows: See (82).
    :type g_table_6b_roof_windows: float
    
    :param FF_table_6b_north: See (74).
    :type FF_table_6b_north: float
    
    :param FF_table_6b_north_east: See (75).
    :type FF_table_6b_north_east: float
    
    :param FF_table_6b_east: See (76).
    :type FF_table_6b_east: float
    
    :param FF_table_6b_south_east: See (77).
    :type FF_table_6b_south_east: float
    
    :param FF_table_6b_south: See (78).
    :type FF_table_6b_south: float
    
    :param FF_table_6b_south_west: See (79).
    :type FF_table_6b_south_west: float
    
    :param FF_table_6b_west: See (80).
    :type FF_table_6b_west: float
    
    :param FF_table_6b_north_west: See (81).
    :type FF_table_6b_north_west: float
    
    :param FF_table_6b_roof_windows: See (82).
    :type FF_table_6b_roof_windows: float
    
    :returns: A dictionary with keys of (
            gains_north,
            gains_north_east,
            gains_east,
            gains_south_east,
            gains_south,
            gains_south_west,
            gains_west,
            gains_north_west,
            gains_roof_windows,
            solar_gains_watts,
            total_internal_and_solar_gains)
    
    - **gains_north** (`list` (`float`)): See (74).
    
    - **gains_north_east** (`list` (`float`)): See (75).
    
    - **gains_east** (`list` (`float`)): See (76).
    
    - **gains_south_east** (`list` (`float`)): See (77).
    
    - **gains_south** (`list` (`float`)): See (78).
    
    - **gains_south_west** (`list` (`float`)): See (79).
    
    - **gains_west** (`list` (`float`)): See (80).
    
    - **gains_north_west** (`list` (`float`)): See (81).
    
    - **gains_roof_windows** (`list` (`float`)): See (82).
    
    - **solar_gains_watts** (`list` (`float`)): See (83) in W.
    
    - **total_internal_and_solar_gains** (`list` (`float`)): See (84) in W.
    
    :rtype: dict
    
    """

    gains_north=[]
    for i in range(12):
        gains_north.append(access_factor_table_6d_north * 
                       area_north * 
                       solar_flux_north[i] * 0.9 * 
                       g_table_6b_north * 
                       FF_table_6b_north)
        
        
    gains_north_east=[]     
    for i in range(12):
        gains_north_east.append(access_factor_table_6d_north_east * 
                       area_north_east * 
                       solar_flux_north_east[i] * 0.9 * 
                       g_table_6b_north_east * 
                       FF_table_6b_north_east)
        
    gains_east =[]    
    for i in range(12):
        gains_east.append(access_factor_table_6d_east * 
                       area_east * 
                       solar_flux_east[i] * 0.9 * 
                       g_table_6b_east * 
                       FF_table_6b_east)
        
    gains_south_east =[]    
    for i in range(12):
        gains_south_east.append(access_factor_table_6d_south_east * 
                       area_south_east * 
                       solar_flux_south_east[i] * 0.9 * 
                       g_table_6b_south_east * 
                       FF_table_6b_south_east)
        
    gains_south =[]    
    for i in range(12):
        gains_south.append(access_factor_table_6d_south * 
                       area_south * 
                       solar_flux_south[i] * 0.9 * 
                       g_table_6b_south * 
                       FF_table_6b_south)
        
    gains_south_west =[]    
    for i in range(12):
        gains_south_west.append(access_factor_table_6d_south_west * 
                       area_south_west * 
                       solar_flux_south_west[i] * 0.9 * 
                       g_table_6b_south_west * 
                       FF_table_6b_south_west)
        
    gains_west =[]    
    for i in range(12):
        gains_west.append(access_factor_table_6d_west * 
                       area_west * 
                       solar_flux_west[i] * 0.9 * 
                       g_table_6b_west * 
                       FF_table_6b_west)
        
    gains_north_west =[]    
    for i in range(12):
        gains_north_west.append(access_factor_table_6d_north_west * 
                       area_north_west * 
                       solar_flux_north_west[i] * 0.9 * 
                       g_table_6b_north_west * 
                       FF_table_6b_north_west)
        
    gains_roof_windows =[]    
    for i in range(12):
        gains_roof_windows.append(access_factor_table_6d_roof_windows * 
                       area_roof_windows * 
                       solar_flux_roof_windows[i] * 0.9 * 
                       g_table_6b_roof_windows * 
                       FF_table_6b_roof_windows) 
        
    solar_gains_watts =[]    
    for i in range(12):
        solar_gains_watts.append(gains_north[i] + gains_north_east[i] + 
                             gains_east[i] + gains_south_east[i] +
                             gains_south[i] + gains_south_west[i] + 
                             gains_west[i] + gains_north_west[i] + 
                             gains_roof_windows[i]) 
        
    
    total_internal_and_solar_gains = []
    for i in range(12):
        total_internal_and_solar_gains.append(total_internal_gains[i] + solar_gains_watts[i])
        
    return dict(
            gains_north=gains_north,
            gains_north_east=gains_north_east,
            gains_east=gains_east,
            gains_south_east=gains_south_east,
            gains_south=gains_south,
            gains_south_west=gains_south_west,
            gains_west=gains_west,
            gains_north_west=gains_north_west,
            gains_roof_windows=gains_roof_windows,
            solar_gains_watts=solar_gains_watts,
            total_internal_and_solar_gains=total_internal_and_solar_gains
            )
        
        