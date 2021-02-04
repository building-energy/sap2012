# -*- coding: utf-8 -*-

import unittest

from sap2012.SAP_worksheet.overall_dwelling_dimensions import overall_dwelling_dimensions

class TestOverallDwellingDimensions(unittest.TestCase):
    
    def test_calc1(self):
        
        area=[10]
        average_storey_height=[2.5]
        
        result=overall_dwelling_dimensions(area,
                                           average_storey_height)
        print(result)
        
        answer=([25.0], 10, 25.0)        
        self.assertEqual(result,answer)
        
        
if __name__=='__main__':
    
    o=unittest.main(TestOverallDwellingDimensions())  
    
    