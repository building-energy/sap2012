# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:34:55 2022

@author: cvskf
"""

import unittest
from sap2012.SAP_appendices import Appendix_S_RdSAP

rdsap_inputs={
    'whole_dwelling':{
        'country':'England & Wales',
        'region':'Midlands',
        'transaction_type':'none of the above',
        'tenure':'owner-occupied',
        'dwelling_type':'house',
        'built_form_and_detachment':'detached',
        'number_of_habitable_rooms':8,
        'number_of_heated_habitable_rooms':6,
        'dimension_type':'measured_internally',
        'conservatory':'no conservatory',
        'number_of_extensions':0,
        
        
        
        
        
        
        
        },
    'main_dwelling':{
        'age_band':'I',
        'below_the_building_part':'',
        'above_the_building_part':'',
        'dimensions_area':[64,64],
        'dimensions_average_room_height':[2.5,2.5],
        'dimensions_exposed_perimeter':[32,32],
        'dimensions_party_wall_length':[0,0],
        'floor_construction':'',
        'floor_insulation':'',
        'floor_insulation_thickness':'',
        'floor_u_value':None,
        'wall_construction':None,
        'wall_thickness':None,
        'wall_insulation_type':'',
        },
    'extension_1':{},
    'extension_2':{},
    'extension_3':{},
    'extension_4':{}
        
        
    
    }


class TestSAPAppendices(unittest.TestCase):
    ""
    
    def test_validate_inputs(self):
        ""
        
        
        Appendix_S_RdSAP.validate_inputs(
            rdsap_inputs
            )
        
        
    def test_infer_inputs(self):
        ""
        
        
        result=Appendix_S_RdSAP.infer_inputs(
            rdsap_inputs
            )
        
        
        print(result)
        
    
    def test_infer_overall_dwelling_dimensions(self):
        ""
        
        
        
        result=Appendix_S_RdSAP.infer_overall_dwelling_dimensions(
            dimensions_area=[64,64],
            dimensions_average_room_height=[2.5,2.5],
            dimension_type='measured_internally',
            below_the_building_part='ground floor'
            )
        
        #print(result)
        
        self.assertEqual(
            result,
            {'area': [64, 64], 
             'average_storey_height': [2.75, 2.5]}
            )
        
        
        
        
        
        
    
    
        
        
if __name__=='__main__':
    
    unittest.main()