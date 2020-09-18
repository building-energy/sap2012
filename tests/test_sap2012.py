# -*- coding: utf-8 -*-

import unittest
from pprint import pprint

from sap2012 import Sap2012

class TestSap2012(unittest.TestCase):
    
    
    
    def test_read_input_csv(self):
        
        s=Sap2012()
        fp='input_csv_file.csv'
        s.read_input_csv(fp)
        
        result=s.inputs['area']
        answer=[0, 63, 63]
        self.assertEqual(result,answer)
        
        
    def test_write_input_csv(self):
        
        s=Sap2012()
        fp='input_csv_file.csv'
        s.read_input_csv(fp)
        s.write_input_csv('test_write_input_csv.csv')
        
        
    def test_write_input_json(self):
        
        s=Sap2012()
        fp='input_csv_file.csv'
        s.read_input_csv(fp)
        s.write_input_json('test_write_input_json.json')
        
        
    def test_read_input_json(self):
        
        s=Sap2012()
        fp='input_csv_file.csv'
        s.read_input_csv(fp)
        s.write_input_json('test_write_input_json.json')
        s.read_input_json('test_write_input_json.json')
        
        result=s.inputs['area']
        answer=[0, 63, 63]
        self.assertEqual(result,answer)
        
        
    def test_run(self):
        
        s=Sap2012()
        fp='input_csv_file.csv'
        s.read_input_csv(fp)
        s.run()
        
    def test_output(self):
        
        s=Sap2012()
        fp='input_csv_file.csv'
        s.read_input_csv(fp)
        s.run()
        outputs=s.outputs
        #print(outputs)
        print(len(s.inputs))
        print(len(s.outputs))
        print(s.inputs['external_wall_u_value'])
        print(s.outputs['total_energy_used'])

        
if __name__=='__main__':
    
    o=unittest.main(TestSap2012())  
    
    