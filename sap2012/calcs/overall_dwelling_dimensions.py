# -*- coding: utf-8 -*-

def overall_dwelling_dimensions(
        area,
        average_storey_height
        ):
    
    """Calculates the overall dwelling dimensions, Section 1
    
    :param area: a list of the areas of each floor. 
        The first item is the basement, the second the ground floor etc. 
        See (1a) to (1n)
    :type area: list of floats
    
    :param average_storey_height: a list of the average storey height of each floor. 
        The first item is the basement, the second the ground floor etc. 
        See (2a) to (2n)
    :type average_storey_height: list of floats
    
    :return: (volume,total_floor_area,dwelling_volume).
    
        volume: a list of the volumes of each floor (list of floats). 
            The first item is the basement, the second the ground floor etc. 
            See (3a) to (3n)
            
        total_floor_area: (float), see (4) 
        
        dwelling_floor_area: (float), see (5) 
        
    :rtype: tuple
    
    """
    
    # calculate volume
    volume=[]
    for i in range(len(area)):
        volume.append(area[i] * average_storey_height[i])
    
    # calculate total floor area
    total_floor_area=sum(area)
    
    # calculate dwelling volume
    dwelling_volume=sum(volume)
    
    return volume,total_floor_area,dwelling_volume
    
    
    