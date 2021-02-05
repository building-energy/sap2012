# -*- coding: utf-8 -*-

import pandas as pd
import importlib.resources
import sap2012.SAP_tables as t

class U2():
    """
    :property df: a pandas dataframe of the table
    :type df: pandas.DataFrame
    """
    
    # df
    with importlib.resources.open_text(t, 'U2.csv') as f:
        df=pd.read_csv(f)
        df.set_index(df.columns[0],inplace=True)
    
    @classmethod        
    def get_regions(kls):
        """
        :return: list of the regions (the dataframe index)
        :rtype: list (of str)
        """
        return list(kls.df.index)
    
    @classmethod
    def get_windspeed_by_region(kls,region):
        """
        :param region str: a region in the table index
        :return: the monthly windspeeds of the region
        :rtype: pandas series with an index of the months
        """
        return kls.df.loc[region]
        
        
if __name__=="__main__":
    #c=U2()
    #print(c.df.head(1))
    #print(c.get_windspeed_by_region('Thames').values)
    
    print(U2)
    print(U2.df.head(1))
    print(U2.get_regions())
    print(U2.get_windspeed_by_region('Thames'))