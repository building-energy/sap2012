# -*- coding: utf-8 -*-

import math

def Solar_gains_appendix_U3 (
        solar_radiation_horizontal_plane_monthly_table_U3,
        solar_declination_monthly_table_U3,
        location_latitude_table_U4,
        p_tilt,
        ):

    solar_declination_radians = []
    for i in range(12):
        solar_declination_radians.append(solar_declination_monthly_table_U3[i] * (math.pi/180))
    
    p_radians = p_tilt * (math.pi / 180)
    
    latitude_radians = location_latitude_table_U4 * (math.pi/ 180)
    
    
    k_N_table_U5 = [26.3, -38.5, 14.8, -16.5, 27.3, -11.9, -1.06, 0.0872, -0.191]
    k_NE_NW_table_U5 = [0.165,-3.68,3,6.38,-4.53,-0.405,-4.38,4.89,-1.99]
    k_E_W_table_U5 = [1.44,-2.36,1.07,-0.514,1.89,-1.64,-0.542,-0.757,0.604]
    k_SE_SW_table_U5 = [-2.95,2.89,1.17,5.67,-3.54,-4.28,-2.72,-0.25,3.07]
    k_S_table_U5 = [-0.66,-0.106,2.93,3.63,-0.374,-7.4,-2.71,-0.991,4.59]
    
    A_N =k_N_table_U5[0] * math.sin(p_radians/2)**3 + k_N_table_U5[1] * math.sin(p_radians/2)**2 + k_N_table_U5[2] * math.sin(p_radians/2)
    
    A_NE =k_NE_NW_table_U5[0] * math.sin(p_radians/2)**3 + k_NE_NW_table_U5[1] * math.sin(p_radians/2)**2 + k_NE_NW_table_U5[2] * math.sin(p_radians/2) 
    
    A_NW =k_NE_NW_table_U5[0] * math.sin(p_radians/2)**3 + k_NE_NW_table_U5[1] * math.sin(p_radians/2)**2 + k_NE_NW_table_U5[2] * math.sin(p_radians/2)
    
    A_E =k_E_W_table_U5[0] * math.sin(p_radians/2)**3 + k_E_W_table_U5[1] * math.sin(p_radians/2)**2 + k_E_W_table_U5[2] * math.sin(p_radians/2)
     
    A_SE =k_SE_SW_table_U5[0] * math.sin(p_radians/2)**3 + k_SE_SW_table_U5[1] * math.sin(p_radians/2)**2 + k_SE_SW_table_U5[2] * math.sin(p_radians/2)
    
    A_S =k_S_table_U5[0] * math.sin(p_radians/2)**3 + k_S_table_U5[1] * math.sin(p_radians/2)**2 + k_S_table_U5[2] * math.sin(p_radians/2)
    
    A_SW =k_SE_SW_table_U5[0] * math.sin(p_radians/2)**3 + k_SE_SW_table_U5[1] * math.sin(p_radians/2)**2 + k_SE_SW_table_U5[2] * math.sin(p_radians/2)
    
    A_W =k_E_W_table_U5[0] * math.sin(p_radians/2)**3 + k_E_W_table_U5[1] * math.sin(p_radians/2)**2 + k_E_W_table_U5[2] * math.sin(p_radians/2)
    
    
    
    B_N =k_N_table_U5[3] * math.sin(p_radians/2)**3 + k_N_table_U5[4] * math.sin(p_radians/2)**2 + k_N_table_U5[5] * math.sin(p_radians/2)
    
    B_NE =k_NE_NW_table_U5[3] * math.sin(p_radians/2)**3 + k_NE_NW_table_U5[4] * math.sin(p_radians/2)**2 + k_NE_NW_table_U5[5] * math.sin(p_radians/2) 
    
    B_NW =k_NE_NW_table_U5[3] * math.sin(p_radians/2)**3 + k_NE_NW_table_U5[4] * math.sin(p_radians/2)**2 + k_NE_NW_table_U5[5] * math.sin(p_radians/2)
    
    B_E =k_E_W_table_U5[3] * math.sin(p_radians/2)**3 + k_E_W_table_U5[4] * math.sin(p_radians/2)**2 + k_E_W_table_U5[5] * math.sin(p_radians/2)
     
    B_SE =k_SE_SW_table_U5[3] * math.sin(p_radians/2)**3 + k_SE_SW_table_U5[4] * math.sin(p_radians/2)**2 + k_SE_SW_table_U5[5] * math.sin(p_radians/2)
    
    B_S =k_S_table_U5[3] * math.sin(p_radians/2)**3 + k_S_table_U5[4] * math.sin(p_radians/2)**2 + k_S_table_U5[5] * math.sin(p_radians/2)
    
    B_SW =k_SE_SW_table_U5[3] * math.sin(p_radians/2)**3 + k_SE_SW_table_U5[4] * math.sin(p_radians/2)**2 + k_SE_SW_table_U5[5] * math.sin(p_radians/2)
    
    B_W =k_E_W_table_U5[3] * math.sin(p_radians/2)**3 + k_E_W_table_U5[4] * math.sin(p_radians/2)**2 + k_E_W_table_U5[5] * math.sin(p_radians/2)
    
    
    C_N =k_N_table_U5[6] * math.sin(p_radians/2)**3 + k_N_table_U5[7] * math.sin(p_radians/2)**2 + k_N_table_U5[8] * math.sin(p_radians/2) + 1
    
    C_NE =k_NE_NW_table_U5[6] * math.sin(p_radians/2)**3 + k_NE_NW_table_U5[7] * math.sin(p_radians/2)**2 + k_NE_NW_table_U5[8] * math.sin(p_radians/2) + 1
    
    C_NW =k_NE_NW_table_U5[6] * math.sin(p_radians/2)**3 + k_NE_NW_table_U5[7] * math.sin(p_radians/2)**2 + k_NE_NW_table_U5[8] * math.sin(p_radians/2) + 1
    
    C_E =k_E_W_table_U5[6] * math.sin(p_radians/2)**3 + k_E_W_table_U5[7] * math.sin(p_radians/2)**2 + k_E_W_table_U5[8] * math.sin(p_radians/2) + 1
     
    C_SE =k_SE_SW_table_U5[6] * math.sin(p_radians/2)**3 + k_SE_SW_table_U5[7] * math.sin(p_radians/2)**2 + k_SE_SW_table_U5[8] * math.sin(p_radians/2) + 1
    
    C_S =k_S_table_U5[6] * math.sin(p_radians/2)**3 + k_S_table_U5[7] * math.sin(p_radians/2)**2 + k_S_table_U5[8] * math.sin(p_radians/2) + 1
    
    C_SW =k_SE_SW_table_U5[6] * math.sin(p_radians/2)**3 + k_SE_SW_table_U5[7] * math.sin(p_radians/2)**2 + k_SE_SW_table_U5[8] * math.sin(p_radians/2) + 1
    
    C_W =k_E_W_table_U5[6] * math.sin(p_radians/2)**3 + k_E_W_table_U5[7] * math.sin(p_radians/2)**2 + k_E_W_table_U5[8] * math.sin(p_radians/2) + 1
    
    R_N = []
    for i in range(12):
        R_N.append(A_N * math.cos(latitude_radians - solar_declination_radians[i])**2 + B_N * math.cos(latitude_radians - solar_declination_radians[i]) + C_N)
    
    R_NE = []
    for i in range(12):
        R_NE.append(A_NE * math.cos(latitude_radians - solar_declination_radians[i])**2 + B_NE * math.cos(latitude_radians - solar_declination_radians[i]) + C_NE)
        
    R_E = []
    for i in range(12):
        R_E.append(A_E * math.cos(latitude_radians - solar_declination_radians[i])**2 + B_E * math.cos(latitude_radians - solar_declination_radians[i]) + C_E)
        
    R_SE = []
    for i in range(12):
        R_SE.append(A_SE * math.cos(latitude_radians - solar_declination_radians[i])**2 + B_SE * math.cos(latitude_radians - solar_declination_radians[i]) + C_SE)
        
    R_S = []
    for i in range(12):
        R_S.append(A_S * math.cos(latitude_radians - solar_declination_radians[i])**2 + B_S * math.cos(latitude_radians - solar_declination_radians[i]) + C_S)
        
    R_SW = []
    for i in range(12):
        R_SW.append(A_SW * math.cos(latitude_radians - solar_declination_radians[i])**2 + B_SW * math.cos(latitude_radians - solar_declination_radians[i]) + C_SW)
        
    R_W = []
    for i in range(12):
        R_W.append(A_W * math.cos(latitude_radians - solar_declination_radians[i])**2 + B_W * math.cos(latitude_radians - solar_declination_radians[i]) + C_W)
     
    R_NW = []
    for i in range(12):
        R_NW.append(A_NW * math.cos(latitude_radians - solar_declination_radians[i])**2 + B_NW * math.cos(latitude_radians - solar_declination_radians[i]) + C_NW)
        
    
    solar_flux_north = []
    for i in range(12):
        solar_flux_north.append(R_N[i] * solar_radiation_horizontal_plane_monthly_table_U3[i])
        
    solar_flux_north_east = []
    for i in range(12):
        solar_flux_north_east.append(R_NE[i] * solar_radiation_horizontal_plane_monthly_table_U3[i])
        
    solar_flux_east = []
    for i in range(12):
        solar_flux_east.append(R_E[i] * solar_radiation_horizontal_plane_monthly_table_U3[i])
        
    solar_flux_south_east = []
    for i in range(12):
        solar_flux_south_east.append(R_SE[i] * solar_radiation_horizontal_plane_monthly_table_U3[i])
        
    solar_flux_south = []
    for i in range(12):
        solar_flux_south.append(R_S[i] * solar_radiation_horizontal_plane_monthly_table_U3[i])
        
    solar_flux_south_west = []
    for i in range(12):
        solar_flux_south_west.append(R_SW[i] * solar_radiation_horizontal_plane_monthly_table_U3[i])
        
    solar_flux_west = []
    for i in range(12):
        solar_flux_west.append(R_W[i] * solar_radiation_horizontal_plane_monthly_table_U3[i])
        
    solar_flux_north_west = []
    for i in range(12):
        solar_flux_north_west.append(R_NW[i] * solar_radiation_horizontal_plane_monthly_table_U3[i])
        
    return(
            solar_flux_north,
            solar_flux_north_east,
            solar_flux_east,
            solar_flux_south_east,
            solar_flux_south,
            solar_flux_south_west,
            solar_flux_west,
            solar_flux_north_west,
            
            )
    