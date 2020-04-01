# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:40:12 2020

@author: benny
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
        FF_table_6b_roof_windows
        ):
    
    """Calculates Solar Gains, section 6
    
    :param access_factor_table_6d_north:
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
    
    :param area_north:
    :type area_north: float
    
    :param area_north_east:
    :type area_north_east: float
    
    :param area_east:
    :type area_east: float
    
    :param area_south_east:
    :type area_south_east: float
    
    :param area_south:
    :type area_south: float
    
    :param area_south_west:
    :type area_south_west: float
    
    :param area_west:
    :type area_west: float
    
    :param area_north_west:
    :type area_north_west: float
    
    :param area_roof_windows:
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
    
    :param g_table_6b_north:
    :type g_table_6b_north: float
    
    :param g_table_6b_north_east:
    :type g_table_6b_north_east: float
    
    :param g_table_6b_east:
    :type g_table_6b_east: float
    
    :param g_table_6b_south_east:
    :type g_table_6b_south_east: float
    
    :param g_table_6b_south:
    :type g_table_6b_south: float
    
    :param g_table_6b_south_west:
    :type g_table_6b_south_west: float
    
    :param g_table_6b_west:
    :type g_table_6b_west: float
    
    :param g_table_6b_north_west:
    :type g_table_6b_north_west: float
    
    :param g_table_6b_roof_windows:
    :type g_table_6b_roof_windows: float
    
    :param FF_table_6b_north:
    :type FF_table_6b_north: float
    
    :param FF_table_6b_north_east:
    :type FF_table_6b_north_east: float
    
    :param FF_table_6b_east:
    :type FF_table_6b_east: float
    
    :param FF_table_6b_south_east:
    :type FF_table_6b_south_east: float
    
    :param FF_table_6b_south:
    :type FF_table_6b_south: float
    
    :param FF_table_6b_south_west:
    :type FF_table_6b_south_west: float
    
    :param FF_table_6b_west:
    :type FF_table_6b_west: float
    
    :param FF_table_6b_north_west:
    :type FF_table_6b_north_west: float
    
    :param FF_table_6b_roof_windows:
    :type FF_table_6b_roof_windows: float
    
    :param gains_north:
    :type gains_north: float
    
    :param gains_north_east:
    :type gains_north_east: float
    
    :param gains_east:
    :type gains_east: float
    
    :param gains_south_east:
    :type gains_south_east: float
    
    :param gains_south:
    :type gains_south: float
    
    :param gains_south_west:
    :type gains_south_west: float
    
    :param gains_west:
    :type gains_west: float
    
    :param gains_north_west:
    :type gains_north_west: float
    
    :param gains_roof_windows:
    :type gains_roof_windows: float
    
    :param solar_gains_watts:
    :type solar_gains_watts: float
    
    

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
        
    return(
            gains_north,
            gains_north_east,
            gains_east,
            gains_south_east,
            gains_south,
            gains_south_west,
            gains_west,
            gains_north_west,
            gains_roof_windows,
            solar_gains_watts)
        
        