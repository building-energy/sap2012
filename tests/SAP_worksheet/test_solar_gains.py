# -*- coding: utf-8 -*-
import unittest
from pprint import pprint
import math

from sap2012.calcs.solar_gains import Solar_gains
import sap2012.tables

class TestSolargains(unittest.TestCase):
    
    def test_calc1(self):
                
        result=Solar_gains(
            access_factor_table_6d_north=0.77,
            access_factor_table_6d_north_east=0,
            access_factor_table_6d_east=0.77,
            access_factor_table_6d_south_east=0,
            access_factor_table_6d_south=0.77,
            access_factor_table_6d_south_west=0,
            access_factor_table_6d_west=0,
            access_factor_table_6d_north_west=0,
            access_factor_table_6d_roof_windows=0,
            area_north=10,
            area_north_east=0,
            area_east=4.9,
            area_south_east=0,
            area_south=11.9,
            area_south_west=0,
            area_west=0,
            area_north_west=0,
            area_roof_windows=0,
            solar_flux_north=[11.43,20.68,34.89,56.6,74.4,83.2,76.7,61.5,43.7,25.3,13.9,9.7],
            solar_flux_north_east=[0,0,0,0,0,0,0,0,0,0,0,0],
            solar_flux_east=[21.1,39.1,63.9,94.1,112.5,120.4,113.1,98.2,77.4,47.6,25.9,17.7],
            solar_flux_south_east=[0,0,0,0,0,0,0,0,0,0,0,0],
            solar_flux_south=[50.2,77.7,98.3,112.2,114,114.8,110.7,108.7,106.9,86.1,58.6,44.1],
            solar_flux_south_west=[0,0,0,0,0,0,0,0,0,0,0,0],
            solar_flux_west=[0,0,0,0,0,0,0,0,0,0,0,0],
            solar_flux_north_west=[0,0,0,0,0,0,0,0,0,0,0,0],
            solar_flux_roof_windows=[0,0,0,0,0,0,0,0,0,0,0,0],
            g_table_6b_north=0.72,
            g_table_6b_north_east=0,
            g_table_6b_east=0.72,
            g_table_6b_south_east=0,
            g_table_6b_south=0.72,
            g_table_6b_south_west=0,
            g_table_6b_west=0,
            g_table_6b_north_west=0,
            g_table_6b_roof_windows=0,
            FF_table_6b_north=0.72,
            FF_table_6b_north_east=0,
            FF_table_6b_east=0.72,
            FF_table_6b_south_east=0,
            FF_table_6b_south=0.72,
            FF_table_6b_south_west=0,
            FF_table_6b_west=0,
            FF_table_6b_north_west=0,
            FF_table_6b_roof_windows=0
            )
        
        print(result)
        
        #answer=([25.0], 10, 25.0)        
        #self.assertEqual(result,answer)
        
        
if __name__=='__main__':
    
    o=unittest.main(TestSolargains())  
    



